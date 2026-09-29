# Proyecto IoT - Control de Acceso RFID para Módulo de Préstamos

**Código del proyecto:** IOT-C05F59AF8A
**Placa usada:** ESP32 DevKit v1
**Entorno:** VS Code + PlatformIO + Wokwi + Mosquitto + Python

Prototipo de control de acceso para un módulo de préstamo de materiales. Lee
credenciales con un lector RFID MFRC522, decide localmente en el ESP32 y
reporta el estado por MQTT. Si se cae el Wi-Fi, el circuito sigue
funcionando local sin quedarse pegado.

El repositorio ya incluye las tres actividades de la materia:

- **Actividad 1:** lógica local (sensor, bloqueo, alarma, actuadores).
- **Actividad 2:** conectividad hacia un broker en la nube (HiveMQ).
- **Actividad 3:** el broker pasa a ser un Mosquitto local, y la interfaz
  para ver telemetría/alertas y enviar comandos ahora es un par de scripts
  de Python en `interfaz/`, en vez del cliente web de HiveMQ.

## ¿Cómo funciona?

* **Muestreo del sensor:** lee el RFID cada **2.6 s** con `millis()` (sin `delay()`).
* **Tarjeta autorizada:** UID `75 F2 DD 13` (en Wokwi, la Tarjeta Azul).
* **Bloqueo:** 3 rechazos consecutivos -> bloqueo de **17 s**.
* **Alarma e histéresis:** 4 rechazos consecutivos confirman la alarma;
  margen de histéresis de 1 s antes de volver a estado normal.
* **Telemetría:** cada **21 s** por MQTT, con el JSON de la sección 3.5
  (`device_id, variable, value, unit, mode, alarm, sequence`). En esta
  actividad `value` son los segundos que faltan para que termine el bloqueo.
* **Comandos remotos:** `AUTO`, `ARMAR`, `SILENCIAR` (cualquier otro texto
  dispara `COMANDO_DESCONOCIDO` sin tocar el actuador ni reiniciar la placa).

## Cómo correrlo (Actividad 3)

1. Levantar Mosquitto local: ver `mosquitto/README.md`.
2. Exponer el puerto 1883 (ngrok o similar) y poner esa dirección en
   `include/secrets.h` (copiar desde `include/secrets.example.h`).
3. Abrir el proyecto en PlatformIO y correr la simulación de Wokwi.
4. En otra terminal: `interfaz/subscriber.py` para ver telemetría/alertas.
5. Para enviar comandos: `interfaz/publisher.py AUTO` (o `ARMAR`, `SILENCIAR`).

## Conexión de componentes

Ver `docs/conexiones.md` (resumen) y `docs/arquitectura/diagrama_bloques.md`
(diagramas completos de las tres actividades).

## Estructura de carpetas

```text
proyecto_IOT-CODIGO/
├── insumos_generador/
│   ├── ficha_insumos_IOT-C05F59AF8A.pdf
│   └── parametros_asignados.md
├── include/
│   └── secrets.example.h
├── src/
│   └── main.cpp
├── mosquitto/
│   ├── mosquitto.conf
│   └── README.md
├── interfaz/
│   ├── subscriber.py
│   ├── publisher.py
│   ├── requirements.txt
│   └── README.md
├── docs/
│   ├── interpretacion_asignacion.md
│   ├── interpretacion_actividad_2.md
│   ├── interpretacion_actividad_3.md
│   ├── conexiones.md
│   ├── pruebas_actividad_2.md
│   ├── pruebas_actividad_3.md
│   ├── guia_prueba_actividad_2.md
│   └── arquitectura/
│       └── diagrama_bloques.md
├── platformio.ini
├── diagram.json
├── wokwi.toml
├── .gitignore
└── README.md
```
