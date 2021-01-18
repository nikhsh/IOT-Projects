
int led = 13;
int smokeA0 = A0;

int sensorThreshold = 400;

void setup() {
  // put your setup code here, to run once:

  pinMode(led, OUTPUT);
  pinMode(smokeA0, INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

  int analogSensor = analogRead(smokeA0);

  Serial.print("Pin A0 :");
  Serial.println(analogSensor);

  if(analogSensor > sensorThreshold)
  {
    digitalWrite(led, HIGH);
    digitalWrite(led, LOW);
  }
  else
  {
    digitalWrite(led, LOW);
    digitalWrite(led, HIGH);
  }
  delay(100);
  

}
