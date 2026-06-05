#include <WiFi.h>

// -----------------------------
// User config
// -----------------------------
const char* WIFI_SSID = "test12";
const char* WIFI_PASSWORD = "12345678";

// IP address of the machine running LeesESP32_SQlite.py
const char* SERVER_HOST = "10.38.130.47";
const uint16_t SERVER_PORT = 5000;

const unsigned long SEND_INTERVAL_MS = 5000;

unsigned long lastSend = 0;

void connectWiFi() {
  Serial.print("Connecting to WiFi");
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print('.');
  }

  Serial.println();
  Serial.print("WiFi connected. ESP32 IP: ");
  Serial.println(WiFi.localIP());
}

void sendRandomData() {
  // Realistic random ranges for BME280-style values
  float temperature = random(180, 340) / 10.0f;  // 18.0 to 34.0 C
  float humidity = random(300, 850) / 10.0f;     // 30.0 to 85.0 %
  float pressure = random(9800, 10350) / 10.0f;  // 980.0 to 1035.0 hPa

  char payload[128];
  snprintf(
    payload,
    sizeof(payload),
    "Temperature: %.2f C, Humidity: %.2f %%, Pressure: %.2f hPa",
    temperature,
    humidity,
    pressure
  );

  WiFiClient client;
  if (!client.connect(SERVER_HOST, SERVER_PORT)) {
    Serial.println("Server connection failed");
    return;
  }

  client.print(payload);
  client.flush();
  client.stop();

  Serial.print("Sent: ");
  Serial.println(payload);
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  randomSeed(esp_random());
  connectWiFi();
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi lost. Reconnecting...");
    connectWiFi();
  }

  unsigned long now = millis();
  if (now - lastSend >= SEND_INTERVAL_MS) {
    lastSend = now;
    sendRandomData();
  }

  delay(50);
}
