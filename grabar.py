#!/usr/bin/env python
# Ad maiorem Dei gloriam

import argparse
import json
from os.path import abspath

from evdev import InputDevice

parser = argparse.ArgumentParser(
    description="Graba las entradas de un control de videojuegos."
)
parser.add_argument(
    "control",
    type=str,
    help="Ubicación del descriptor del control del que quiere grabar",
)
parser.add_argument(
    "salida",
    type=argparse.FileType("w"),
    help="Archivo de salida con los eventos grabados",
)
args = parser.parse_args()

dev = InputDevice(args.control)

events = []
print("Grabando eventos... Ctrl+C para detener")

try:
    for event in dev.read_loop():
        if event.type != 0:  # ignorar SYN
            events.append(
                {
                    "sec": event.sec,
                    "usec": event.usec,
                    "type": event.type,
                    "code": event.code,
                    "value": event.value,
                }
            )
            print(event.type, event.code, event.value)
except KeyboardInterrupt:
    json.dump(events, args.salida)
    print(f"\nEventos guardados en {abspath(args.salida.name)}")
    args.salida.close()
    print("adios!")
