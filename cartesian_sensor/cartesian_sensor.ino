int pin_pot_x = A0;
int pin_pot_y = A1;

void setup() {
    Serial.begin(115200);
}

void loop() {
    if (Serial.available() > 0) {
      Serial.println(analogRead(pin_pot_x));
      Serial.println(analogRead(pin_pot_y));
      while (Serial.available() > 0) {
        Serial.read();
      }
    }
    delay(10);
}