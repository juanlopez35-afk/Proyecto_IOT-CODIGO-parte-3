# Mosquitto local — Actividad 3

## 1. Instalar y correr Mosquitto

macOS (Homebrew):
```
brew install mosquitto
mosquitto -c mosquitto/mosquitto.conf -v
```

Linux (apt):
```
sudo apt install mosquitto mosquitto-clients
mosquitto -c mosquitto/mosquitto.conf -v
```

Windows: instalar desde https://mosquitto.org/download/ y correr
`mosquitto.exe -c mosquitto\mosquitto.conf -v` desde la carpeta del proyecto.

Deja esa terminal abierta: ahí vas a ver en vivo cada conexión y cada mensaje
publicado por el ESP32 y por los scripts de Python.

## 2. Por qué hace falta exponer el broker

El ESP32 de esta actividad corre simulado dentro de Wokwi (en la nube), no en
mi computador. Por eso no puede alcanzar directamente `localhost:1883` de mi
máquina: necesita una dirección accesible desde internet que "apunte" hacia mi
Mosquitto local.

## 3. Cómo lo expuse (opción usada: ngrok)

```
ngrok tcp 1883
```

Eso entrega algo como `tcp://0.tcp.ngrok.io:XXXXX`. Ese host y ese puerto son
los que va el ESP32 en `include/secrets.h` (`MQTT_BROKER` y `MQTT_PORT`), y
también los que usan los scripts de `interfaz/` para conectarse desde mi propio
computador (ahí sí puedo usar `localhost` directamente si corro los scripts en
la misma máquina donde vive Mosquitto).

Alternativa sin herramientas externas: si el ESP32 y mi PC están en la misma
red, y el simulador de Wokwi se corre localmente con la extensión de VS Code +
Wokwi CLI (en vez del simulador web), sí se puede usar la IP local de la
máquina (ej. `192.168.x.x`) sin necesidad de túnel.

## 4. Verificación rápida por consola (sin Python)

```
mosquitto_sub -h localhost -t "iot/c05f59af8a/#" -v
mosquitto_pub -h localhost -t "iot/c05f59af8a/command" -m "AUTO"
```
