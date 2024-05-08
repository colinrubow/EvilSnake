int pin_pot_x = A0;
int pin_pot_y = A1;

void setup() {
    Serial.begin(115200);
}

void loop() {
    int x = analogRead(pin_pot_x);
    int y = analogRead(pin_pot_y);

    Serial.println(x);
    Serial.println(y);
    Serial.println();
    delay(100);
}