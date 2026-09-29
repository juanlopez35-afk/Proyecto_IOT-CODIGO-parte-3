# Diagrama de bloques

## Actividad 1: sensores y actuadores

```
[ Tag RFID / MFRC522 ] --(SPI: GPIO 18, 19, 21, 23)--> [ ESP32 DevKit ]
                                                             |
                                           +-----------------+-----------------+
                                           | (GPIO 2 - Salida)                 | (GPIO 5 - Salida)
                                           v                                   v
                                    [ LED de estado ]                  [ Buzzer sonoro ]
```

## Actividad 2: conectividad hacia la nube

```
                       [ ESP32 DevKit ]
                              |
                          (WiFi STA)
                              v
                     [ Router / Wokwi-GUEST ]
                              |
                          (MQTT / TCP)
                              v
                  [ Broker en la nube (secrets.h) ]
                    |        |        |        |
              telemetry   status    alert   command
             (cada 21 s) (conexión) (eventos) (AUTO/ARMAR/SILENCIAR)
```

## Actividad 3: broker Mosquitto local + interfaz en Python

```
[ Tag RFID ] --SPI--> [ ESP32 DevKit ] --WiFi (Wokwi-GUEST)--> [ Internet ]
                              |                                     |
                     LED / Buzzer (local)                (túnel hacia mi PC*)
                                                                     v
                                                     [ Mosquitto local :1883 ]
                                                       |      |      |      |
                                                telemetry  status  alert  command
                                                     ^                       |
                                                     |                       v
                                            [ interfaz/subscriber.py ]   [ interfaz/publisher.py ]
                                              (muestra telemetría          (envía AUTO / ARMAR /
                                               y alertas en consola)        SILENCIAR)
```

\* Wokwi simula el ESP32 en la nube, así que para que llegue a un Mosquitto
que corre en mi propio computador expongo el puerto 1883 hacia afuera (por
ejemplo con un túnel tipo ngrok o con redirección de puertos en mi router).
El detalle de cómo lo hice está en `mosquitto/README.md`.
