#!/usr/bin/env python
# Ad maiorem Dei gloriam

import argparse
import json
import time

from evdev import AbsInfo, InputEvent, UInput, ecodes

parser = argparse.ArgumentParser(
    description="Reproduce las entradas grabadas de un control de videojuegos (Licencia: GPLv3+).",
    epilog="Autor: Jorge Javier Araya Navarro <jorge@esavara.cr>",
)
parser.add_argument(
    "entrada",
    type=argparse.FileType("r"),
    help="Archivo de entrada con los eventos a reproducir",
)
args = parser.parse_args()

cap = {
    ecodes.EV_KEY: [
        ecodes.BTN_A,
        ecodes.BTN_B,
        ecodes.BTN_X,
        ecodes.BTN_Y,
        ecodes.BTN_TL,
        ecodes.BTN_TR,  # LB / RB
        ecodes.BTN_SELECT,
        ecodes.BTN_START,
        ecodes.BTN_THUMBL,
        ecodes.BTN_THUMBR,  # clic en sticks
    ],
    ecodes.EV_ABS: [
        (ecodes.ABS_X, AbsInfo(0, -32768, 32767, 0, 0, 0)),  # Stick izquierdo X
        (ecodes.ABS_Y, AbsInfo(0, -32768, 32767, 0, 0, 0)),  # Stick izquierdo Y
        (ecodes.ABS_RX, AbsInfo(0, -32768, 32767, 0, 0, 0)),  # Stick derecho X
        (ecodes.ABS_RY, AbsInfo(0, -32768, 32767, 0, 0, 0)),  # Stick derecho Y
        (ecodes.ABS_Z, AbsInfo(0, 0, 255, 0, 0, 0)),  # Gatillo izquierdo
        (ecodes.ABS_RZ, AbsInfo(0, 0, 255, 0, 0, 0)),  # Gatillo derecho
        (ecodes.ABS_HAT0X, AbsInfo(0, -1, 1, 0, 0, 0)),  # D-Pad X
        (ecodes.ABS_HAT0Y, AbsInfo(0, -1, 1, 0, 0, 0)),  # D-Pad Y
    ],
}

# Cargar eventos grabados
events = json.load(args.entrada)
args.entrada.close()

ui = UInput(events=cap, name="Virtual Xbox Controller (Apestoso Perezoso)", version=0x3)
print("Control virtual listo")
print("Empezando reproducción en...")
for i in range(5, 1, -1):
    print(f"{i}...")
    time.sleep(1)

try:
    while True:
        first_ts = events[0]["sec"] + events[0]["usec"] / 1e6
        play_start = time.monotonic()
        for e in events:
            scheduled = (e["sec"] + e["usec"] / 1e6) - first_ts
            to_wait = play_start + scheduled - time.monotonic()
            if to_wait > 0:
                time.sleep(to_wait)
            ui.write(e["type"], e["code"], e["value"])
            ui.syn()
            print(e["type"], e["code"], e["value"])
        print(
            "fin -- esperando 10 segundos para comenzar de nuevo (Ctrl+C para cancelar)"
        )
        time.sleep(10)
except KeyboardInterrupt:
    print("\nejecución interrumpida por el usuario (Ctrl+C)!")
finally:
    print("Control virtual destruido")
    ui.close()
print("adios!")
