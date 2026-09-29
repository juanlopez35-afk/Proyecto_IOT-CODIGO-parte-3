# Parámetros asignados — resumen para desarrollo

Extraído de `ficha_insumos_IOT-C05F59AF8A.pdf` (versión de asignación
IOT-2026-B1-v1), bloque 3 (Actividad 3 — 40 %, Mosquitto local).

## Escenario
- Contexto: módulo de préstamo de materiales.
- Variable principal: identificador RFID.
- Regla asignada: autorizar únicamente la credencial asignada y bloquear
  temporalmente tras tres rechazos.

## Componentes
- Microcontrolador: ESP32 DevKit v1 (`wokwi-esp32-devkit-v1`)
- Sensor: lector RFID MFRC522, SPI (`board-mfrc522`)
- Actuador: buzzer piezoeléctrico (`wokwi-buzzer`)
- Interfaz local: LED de estado (`wokwi-led`)

## Parámetros individuales
| Parámetro | Valor |
|---|---|
| Tiempo de bloqueo | 17 segundos |
| UID autorizado | 75 F2 DD 13 |
| Intervalo de muestreo | 2600 ms |
| Período de publicación | 21 segundos |
| Intervalo de reconexión | 4 segundos |
| Confirmación de alarma | 4 lecturas consecutivas |
| Margen de retorno | 10 unidades respecto al umbral |
| Comandos remotos | AUTO, ARMAR, SILENCIAR |
| Estado seguro | apagado, excepto ante alarma local confirmada |

## Broker y tópicos (3.4)
- Broker: Eclipse Mosquitto, entorno local.
- Tema base: `iot/c05f59af8a`
- Telemetría: `iot/c05f59af8a/telemetry`
- Estado: `iot/c05f59af8a/status`
- Comandos: `iot/c05f59af8a/command`
- Alertas: `iot/c05f59af8a/alert`

## Formato de datos asignado (3.5)
```json
{
  "device_id": "IOT-C05F59AF8A",
  "variable": "identificador RFID",
  "value": 0.0,
  "unit": "segundos de bloqueo",
  "mode": "AUTO",
  "alarm": false,
  "sequence": 1
}
```

## Condiciones de referencia (3.6)
- A: una credencial no autorizada una sola vez.
- B: tres credenciales no autorizadas consecutivas -> bloqueo tras el 3er rechazo.
- Dato no válido: lectura fuera del rango admisible o valor no numérico.
- Duración de interrupción de red: 20 segundos.
- Intervalo de reconexión: 4 segundos.
- Comandos asignados: AUTO, ARMAR, SILENCIAR.
- Comando no reconocido de referencia: `COMANDO_DESCONOCIDO`.
- Estado seguro asignado: apagado, excepto ante alarma local confirmada.
