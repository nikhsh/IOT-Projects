
int sensorPin = A1;
int sensorValue;
int limit = 300;


void setup() {
  // put your setup code here, to run once:

Serial.begin(9600);
pinMode(12, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

sensorValue = analogRead(sensorPin);
Serial.println("Analog Value : ");
Serial.println(sensorValue);


if (sensorValue<limit){
  digitalWrite(12, HIGH);
  Serial.println("Water is detacted...");
  }
  else{
    digitalWrite(12,LOW);
    Serial.println("no water is detacted.....");
    }

    delay(1000);
}
