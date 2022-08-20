/*
Rover computer service - turns COM data into action
*/


int control = 0;
int LMotor = 7;
int RMotor = 8;


void setup() {
  Serial.begin(115200);
  Serial.setTimeout(0);
  pinMode(LMotor, OUTPUT);
  pinMode(RMotor, OUTPUT);

}


void loop() {
  control = Serial.read();
  digitalWrite(LMotor, LOW);
  digitalWrite(RMotor, LOW);

}
