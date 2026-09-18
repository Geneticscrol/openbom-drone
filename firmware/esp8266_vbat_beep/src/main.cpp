#include <Arduino.h>

const int PIN_BEEP = 2;
const float CELLS = 4.0;

// PACK_FULL_ADC / PACK_FULL_V: bench calibration constants, not yet measured on real
// hardware (design-stage — see firmware README for the calibration walkthrough).
// Re-derive both after flashing: charge the pack full, read the printed `adc=` value,
// and set PACK_FULL_V to the multimeter reading at that same moment.
const float PACK_FULL_ADC = 860.0;
const float PACK_FULL_V = 16.80;
const float CELL_ALARM = 3.50;

void setup() {
  pinMode(PIN_BEEP, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int adc = analogRead(A0);
  float pack = PACK_FULL_V * (adc / PACK_FULL_ADC);
  float cell = pack / CELLS;
  Serial.printf("adc=%d pack=%.2f cell=%.2f\n", adc, pack, cell);
  if (cell > 0.5 && cell < CELL_ALARM) {
    digitalWrite(PIN_BEEP, HIGH);
    delay(80);
    digitalWrite(PIN_BEEP, LOW);
  }
  delay(800);
}
