#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Wokwi-GUEST";    // Rede Wi-Fi simulada no Wokwi
const char* password = "";           // Sem senha no Wokwi-GUEST
const int analogPin = 34;            // Pino ADC no ESP32

const char* server = "http://api.thingspeak.com/update";
const char* apiKey = "SUA_API_KEY";

void setup() {
  Serial.begin(115200);
  delay(1000);

  WiFi.begin(ssid, password);
  Serial.print("Conectando-se ao Wi-Fi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi conectado!");
}

void loop() {
  int analogValue = analogRead(analogPin);
  Serial.print("Valor lido do ADC: ");
  Serial.println(analogValue);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    String url=String(server)+"?api_key="+apiKey+"&field1="+ String(analogValue);
    http.begin(url);
    int httpResponseCode = http.GET();

    if (httpResponseCode > 0) {
      Serial.print("Código de resposta HTTP: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("Erro ao enviar dados: ");
      Serial.println(http.errorToString(httpResponseCode).c_str());
    }

    http.end();
  } else {
    Serial.println("WiFi desconectado. Tentando reconectar...");
    WiFi.begin(ssid, password);
  }

  delay(15000); // Intervalo de 15s (mínimo permitido pelo ThingSpeak)
}
