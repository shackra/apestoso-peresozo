import json
from evdev import InputDevice

dev = InputDevice("/dev/input/event9")  # usa tu dispositivo real

events = []
print("Grabando eventos... Ctrl+C para detener")

try:
    for event in dev.read_loop():
        if event.type != 0:  # ignorar SYN
            events.append({
                "sec": event.sec,
                "usec": event.usec,
                "type": event.type,
                "code": event.code,
                "value": event.value
            })
except KeyboardInterrupt:
    with open("events.json", "w") as f:
        json.dump(events, f)
    print("Eventos guardados en events.json")
