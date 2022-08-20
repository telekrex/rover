/*
Rover computer service - turns COM data into action
*/


void setup() {
  Serial.begin(115200);
  Serial.setTimeout(0);
  int incomdata = -1;

}


void loop() {
  incomdata = Serial.read()

}
