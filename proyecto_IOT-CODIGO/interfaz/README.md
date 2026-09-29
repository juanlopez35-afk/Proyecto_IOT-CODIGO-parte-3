# Interfaz en Python — Actividad 3

Estos scripts reemplazan al cliente web de HiveMQ que usé en la Actividad 2.
Aquí la interfaz es de línea de comandos y habla directo con Mosquitto.

## Instalación

```
cd interfaz
python -m venv venv
source venv/bin/activate        # en Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Escuchar telemetría y alertas

```
python subscriber.py --host localhost --port 1883
```

(Si Mosquitto está expuesto con ngrok, cambia `--host` y `--port` por los que
te dio ngrok.)

## Enviar un comando

```
python publisher.py AUTO
python publisher.py ARMAR
python publisher.py SILENCIAR
python publisher.py TEST_ERROR   # para probar COMANDO_DESCONOCIDO
```
