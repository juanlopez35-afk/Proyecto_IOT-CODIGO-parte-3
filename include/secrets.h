#ifndef SECRETS_H
#define SECRETS_H


#define WIFI_SSID     "Wokwi-GUEST"
#define WIFI_PASSWORD ""

// Actividad 3: Mosquitto corre en mi propio computador (mosquitto/mosquitto.conf),
// pero como el ESP32 simulado no puede llegar a "localhost" de mi PC, expongo
// el puerto 1883 hacia afuera (ver mosquitto/README.md) y aquí va esa dirección
// pública, por ejemplo la que entrega ngrok:
#define MQTT_BROKER   ""   // reemplazar por el host real del tunel
#define MQTT_PORT     ""              // reemplazar por el puerto real del tunel
#define MQTT_USER     ""  // Mosquitto local corre con allow_anonymous true
#define MQTT_PASSWORD ""

#endif
