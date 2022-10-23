int control = 0;
int Lmotor = 7;
int Rmotor = 8;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(0);
  pinMode(Lmotor, OUTPUT);
  pinMode(Rmotor, OUTPUT);
}

void loop() {
  control = Serial.read();
  digitalWrite(Lmotor, LOW);
  digitalWrite(Rmotor, LOW);
}
