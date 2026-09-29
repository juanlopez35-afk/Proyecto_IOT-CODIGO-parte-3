# Pruebas — Actividad 3

Registro de pruebas sobre el prototipo conectado al broker Mosquitto local,
según las condiciones de referencia de la ficha de insumos (3.6). Se
completa cada fila con lo observado al correr la simulación en Wokwi y los
scripts `interfaz/subscriber.py` y `interfaz/publisher.py`.

| # | Condición de referencia | Cómo se provocó | Resultado esperado | Resultado observado | Evidencia |
|---|---|---|---|---|---|
| 1 | A — una credencial no autorizada una sola vez | Acercar una tarjeta distinta a la autorizada, una vez | Acceso rechazado, sin bloqueo | | |
| 2 | B — tres credenciales no autorizadas consecutivas | Acercar 3 tarjetas distintas a la autorizada, seguidas, esperando ~3 s entre cada una | Bloqueo temporal de 17 s activado en el 3er rechazo | | |
| 2b | Confirmación de alarma (4 rechazos) | Acercar una 4ta tarjeta no autorizada mientras el sistema sigue bloqueado | Se confirma la alarma (LED fijo + buzzer intermitente), sin desactivar el bloqueo | | |
| 3 | Dato no válido | Simular un UID fuera de rango | Lectura descartada, no cuenta como rechazo | | |
| 4 | Interrupción de red de 20 s | Apagar el WiFi del simulador 20 s | El RFID y el bloqueo local siguen funcionando igual | | |
| 5 | Reconexión (4 s) | Reactivar el WiFi | El dispositivo vuelve a conectar a Mosquitto sin reiniciar | | |
| 6 | Comando AUTO | `python publisher.py AUTO` | Modo vuelve a AUTO, se apaga el silenciado | | |
| 7 | Comando ARMAR | `python publisher.py ARMAR` | Modo cambia a ARMADO | | |
| 8 | Comando SILENCIAR | `python publisher.py SILENCIAR` durante alarma | Buzzer se apaga, LED sigue indicando alarma | | |
| 9 | Comando no reconocido | `python publisher.py TEST_ERROR` | Se publica alerta `COMANDO_DESCONOCIDO`, no cambia el modo, no activa actuador ni reinicia el ESP32 | | |
| 10 | Estado seguro | Sin alarma confirmada | LED y buzzer apagados | | |
| 11 | Formato de telemetría | Dejar correr `subscriber.py` 21+ segundos | Llega JSON con `device_id, variable, value, unit, mode, alarm, sequence` y `unit = "segundos de bloqueo"` | | |

## Publicación MQTT recibida

*(Pegar aquí una captura de la consola de `interfaz/subscriber.py` mostrando
al menos un mensaje recibido en `iot/c05f59af8a/telemetry`.)*
Tarjeta detectada (UID): 11 22 33 44
-> ACCESO DENEGADO (Intento 1/3)
Tarjeta detectada (UID): 11 22 33 44
-> ACCESO DENEGADO (Intento 2/3)
Tarjeta detectada (UID): 11 22 33 44
-> ACCESO DENEGADO (Intento 3/3)
-> ALERTA: Tres rechazos consecutivos detectados.
-> SISTEMA BLOQUEADO TEMPORALMENTE POR 17 SEGUNDOS.
Alerta: {"device_id":"IOT-C05F59AF8A","evento":"bloqueo_por_rechazos","mode":"AUTO","sequence":12}
Tarjeta detectada (UID): 11 22 33 44
-> Rechazo durante el bloqueo (4) - no se concede acceso.
-> ALARMA CONFIRMADA (4 lecturas consecutivas de rechazo).
Alerta: {"device_id":"IOT-C05F59AF8A","evento":"alarma_confirmada","mode":"AUTO","sequence":12}
Telemetria publicada: {"device_id":"IOT-C05F59AF8A","variable":"identificador RFID","value":14.25500011,"unit":"segundos de bloqueo","mode":"AUTO","alarm":true,"sequence":13}
-> Bloqueo cumplido, esperando margen de histeresis...
-> SISTEMA DESBLOQUEADO Y LISTO.
Telemetria publicada: {"device_id":"IOT-C05F59AF8A","variable":"identificador RFID","value":0,"unit":"segundos de bloqueo","mode":"AUTO","alarm":true,"sequence":14}
Tarjeta detectada (UID): 75 F2 DD 13
-> ACCESO CONCEDIDO
Telemetria publicada: {"device_id":"IOT-C05F59AF8A","variable":"identificador RFID","value":0,"unit":"segundos de bloqueo","mode":"AUTO","alarm":false,"sequence":15}
[19:53:41] ESTADO  {"status": "online"}
[19:54:09] ESTADO  {"device_id": "IOT-C05F59AF8A", "comando_aplicado": "ARMAR", "modo": "ARMADO"}
[19:54:10] ESTADO  {"device_id": "IOT-C05F59AF8A", "comando_aplicado": "AUTO", "modo": "AUTO"}
[19:54:11] ESTADO  {"device_id": "IOT-C05F59AF8A", "comando_aplicado": "SILENCIAR", "modo": "AUTO"}
[19:54:13] *** ALERTA ***  {"device_id": "IOT-C05F59AF8A", "evento": "COMANDO_DESCONOCIDO", "mode": "AUTO", "sequence": 0}
