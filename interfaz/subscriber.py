"""
Interfaz (lado Python) - Actividad 3
Se suscribe a telemetria, status y alert, y muestra cada mensaje en consola
con el formato JSON asignado en la ficha de insumos (3.5).

Uso:
    python subscriber.py
    python subscriber.py --host 0.tcp.ngrok.io --port 12345
"""

import argparse
import json
from datetime import datetime

import paho.mqtt.client as mqtt

TEMA_BASE = "iot/c05f59af8a"
TOPICS = [
    f"{TEMA_BASE}/telemetry",
    f"{TEMA_BASE}/status",
    f"{TEMA_BASE}/alert",
]


def parsear_args():
    parser = argparse.ArgumentParser(description="Interfaz de monitoreo - Actividad 3")
    parser.add_argument("--host", default="localhost", help="Host del broker Mosquitto")
    parser.add_argument("--port", type=int, default=1883, help="Puerto del broker Mosquitto")
    return parser.parse_args()


def al_conectar(client, userdata, flags, rc):
    if rc == 0:
        print(f"[OK] Conectado al broker. Suscribiendo a {len(TOPICS)} topicos...")
        for topic in TOPICS:
            client.subscribe(topic)
            print(f"     -> {topic}")
    else:
        print(f"[ERROR] No se pudo conectar, codigo rc={rc}")


def al_recibir_mensaje(client, userdata, msg):
    hora = datetime.now().strftime("%H:%M:%S")
    crudo = msg.payload.decode(errors="replace")

    try:
        datos = json.loads(crudo)
    except json.JSONDecodeError:
        print(f"[{hora}] {msg.topic}  (mensaje no es JSON valido): {crudo}")
        return

    if msg.topic.endswith("/telemetry"):
        print(
            f"[{hora}] TELEMETRIA  device={datos.get('device_id')}  "
            f"valor={datos.get('value')} {datos.get('unit')}  "
            f"modo={datos.get('mode')}  alarma={datos.get('alarm')}  "
            f"seq={datos.get('sequence')}"
        )
    elif msg.topic.endswith("/alert"):
        print(f"[{hora}] *** ALERTA ***  {json.dumps(datos, ensure_ascii=False)}")
    elif msg.topic.endswith("/status"):
        print(f"[{hora}] ESTADO  {json.dumps(datos, ensure_ascii=False)}")
    else:
        print(f"[{hora}] {msg.topic}  {json.dumps(datos, ensure_ascii=False)}")


def main():
    args = parsear_args()

    client = mqtt.Client(client_id="interfaz-python-sub")
    client.on_connect = al_conectar
    client.on_message = al_recibir_mensaje

    print(f"Conectando a {args.host}:{args.port} ...")
    client.connect(args.host, args.port, keepalive=60)
    client.loop_forever()


if __name__ == "__main__":
    main()
