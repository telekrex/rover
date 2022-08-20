/*
Rover computer service - turns COM data into action
*/


void setup() {
  Serial.begin(115200);
  Serial.setTimeout(0);

}


void loop() {
  int incomdata = Serial.read();

}
