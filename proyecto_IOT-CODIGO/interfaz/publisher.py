"""
Interfaz (lado Python) - Actividad 3
Envia comandos remotos al ESP32 a traves del broker Mosquitto:
AUTO, ARMAR, SILENCIAR (o cualquier texto, para probar COMANDO_DESCONOCIDO).

Uso:
    python publisher.py AUTO
    python publisher.py ARMAR --host 0.tcp.ngrok.io --port 12345
    python publisher.py SILENCIAR
    python publisher.py TEST_ERROR
"""

import argparse

import paho.mqtt.client as mqtt

TEMA_BASE = "iot/c05f59af8a"
TOPIC_COMMAND = f"{TEMA_BASE}/command"


def parsear_args():
    parser = argparse.ArgumentParser(description="Interfaz de comandos - Actividad 3")
    parser.add_argument("comando", help="AUTO, ARMAR, SILENCIAR (o cualquier texto)")
    parser.add_argument("--host", default="localhost", help="Host del broker Mosquitto")
    parser.add_argument("--port", type=int, default=1883, help="Puerto del broker Mosquitto")
    return parser.parse_args()


def main():
    args = parsear_args()

    client = mqtt.Client(client_id="interfaz-python-pub")
    client.connect(args.host, args.port, keepalive=60)
    client.loop_start()

    info = client.publish(TOPIC_COMMAND, args.comando, qos=1)
    info.wait_for_publish()

    print(f"Comando '{args.comando}' publicado en {TOPIC_COMMAND}")

    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    main()
