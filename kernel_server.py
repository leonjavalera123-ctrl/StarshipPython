"""
kernel_server.py  --  lets the 3D ship talk to the drill kernel.

    python kernel_server.py --port-file C:/path/to/port.txt

HOW THE TWO SIDES FIND EACH OTHER
    The server binds to port ZERO, which means "the operating system picks a
    free one", and then writes the number it was given into --port-file. The
    ship waits for that file to appear and reads the port out of it.

    That is deliberate. A hardcoded port collides the day something else on
    the machine wants it, and the failure looks like the game being broken.
    Letting the OS choose cannot collide, and THE FILE APPEARING IS ALSO THE
    READY SIGNAL -- no sleeping and hoping.

THE PROTOCOL
    One JSON object per line, in both directions. Requests look like
    {"cmd": "submit", "line": "x = 1"} and replies always carry "ok".
    Newline-delimited JSON is enough here and it is trivially debuggable: you
    can drive this server by hand with a telnet client if you ever need to.

    It listens on 127.0.0.1 only. Nothing outside this machine can reach it.

WHAT IT DELIBERATELY CANNOT DO
    There is no "solution" command. Starship Pyxis has no show-me-the-answer
    button, and the way to see an answer is to ask for hints until the ladder
    runs out. Offering a shortcut here would invent a feature the game has
    chosen not to have.
"""

import json
import os
import socket
import sys

import pyxkernel
from pyxkernel import Session


HOST = "127.0.0.1"


def read_args(argv):
    out = {"port-file": ""}
    i = 0
    while i < len(argv):
        if argv[i] == "--port-file" and i + 1 < len(argv):
            out["port-file"] = argv[i + 1]
            i += 2
        else:
            i += 1
    return out


def handle(session, msg):
    """One request in, one reply dict out. `session` is a one-item list so a
    command can replace it."""
    cmd = str(msg.get("cmd", ""))

    if cmd == "hello":
        return {"ok": True, "levels": pyxkernel.level_count()}

    if cmd == "manifest":
        return {"ok": True, "manifest": pyxkernel.manifest()}

    if cmd == "start":
        pairs = msg.get("tasks") or []
        if not pairs:
            return {"ok": False, "error": "no tasks"}
        session[0] = Session(pairs)
        return {"ok": True, "state": session[0].state()}

    if session[0] is None:
        return {"ok": False, "error": "no drill running"}

    if cmd == "submit":
        out = session[0].submit(str(msg.get("line", "")))
        return {"ok": True, "out": out, "state": session[0].state()}

    if cmd == "hint":
        text = session[0].hint()
        return {"ok": True, "hint": text, "state": session[0].state()}

    if cmd == "next":
        session[0].advance()
        return {"ok": True, "state": session[0].state()}

    if cmd == "skip":
        # Skipping exists in DRILLS ONLY. The campaign has no way past a task
        # you have not solved, and that is on purpose.
        session[0].advance(skipped=True)
        return {"ok": True, "state": session[0].state()}

    if cmd == "report":
        return {"ok": True, "report": session[0].report()}

    return {"ok": False, "error": "unknown command: " + cmd}


def serve(port_file):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, 0))                       # 0 = "you choose"
    srv.listen(1)
    port = srv.getsockname()[1]

    if port_file:
        # Write to a temporary name and rename it into place, so the ship can
        # never read a half-written port number.
        tmp = port_file + ".tmp"
        os.makedirs(os.path.dirname(os.path.abspath(port_file)), exist_ok=True)
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(str(port))
        os.replace(tmp, port_file)
    print(f"kernel listening on {HOST}:{port}", flush=True)

    conn, _ = srv.accept()
    conn.settimeout(None)
    session = [None]
    buffer = b""

    try:
        while True:
            chunk = conn.recv(65536)
            if not chunk:
                break
            buffer += chunk
            while b"\n" in buffer:
                raw, buffer = buffer.split(b"\n", 1)
                if not raw.strip():
                    continue
                try:
                    msg = json.loads(raw.decode("utf-8"))
                except Exception as e:
                    reply = {"ok": False, "error": f"bad json: {e}"}
                else:
                    if str(msg.get("cmd", "")) == "bye":
                        conn.sendall(b'{"ok":true}\n')
                        return
                    try:
                        reply = handle(session, msg)
                    except Exception as e:
                        # A crash in one command must not take the drill down.
                        reply = {"ok": False,
                                 "error": f"{type(e).__name__}: {e}"}
                conn.sendall((json.dumps(reply) + "\n").encode("utf-8"))
    finally:
        try:
            conn.close()
        except Exception:
            pass
        srv.close()
        if port_file and os.path.exists(port_file):
            try:
                os.remove(port_file)      # the file IS the ready signal
            except Exception:
                pass


if __name__ == "__main__":
    args = read_args(sys.argv[1:])
    serve(args["port-file"])
