# Interpretación de la asignación — Actividad 3

**De sensor a interfaz**
Todo arranca en el lector RFID: cada 2.6 segundos el ESP32 lo revisa y saca el UID de la tarjeta. Con ese dato decide localmente si es acceso, rechazo, bloqueo o alarma, arma un JSON con esa información y lo publica por MQTT hacia el broker Mosquitto, que ahora corre en mi propia máquina y no en una nube externa. De ahí el mensaje llega a mi script de Python, suscrito a telemetría y alertas, que solo muestra en pantalla lo que va llegando.

**De interfaz a actuador**
El camino contrario: desde Python publico un texto (AUTO, ARMAR o SILENCIAR) en el tópico de comandos. Mosquitto lo reenvía al ESP32, que está suscrito ahí, y su callback interpreta el mensaje para cambiar el modo o apagar el buzzer si toca.

**Qué se queda en el ESP32 y por qué**
Toda la decisión (comparar el UID, contar rechazos, activar bloqueo, confirmar alarma) se queda en la placa, porque tiene que seguir protegiendo el módulo aunque se caiga la red o el script no esté corriendo. Fuera de la placa solo deben enterarse de lo que pasó, no decidir en tiempo real.

**Función de Python, tópicos y JSON**
Python hace de interfaz humana: no toca el hardware, solo escucha y manda comandos por MQTT. Los tópicos ordenan la conversación (telemetry, status, alert, command) y el JSON asignado estandariza cómo se reporta cada evento para que cualquier programa lo lea igual.
