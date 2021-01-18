
const int ledPin = 12;
const int ldrPin = A0;

void setup() {
  // put your setup code here, to run once:

Serial.begin(9600);
pinMode(ledPin, OUTPUT);
pinMode(ldrPin, INPUT);



}

void loop() {
  // put your main code here, to run repeatedly:

int ldrStatus = analogRead(ldrPin);
if (ldrStatus <= 200){
  digitalWrite(ledPin,LOW);
  Serial.print("ITs a dark turn on  the led..");
  Serial.println(ldrStatus);
  }else{
    digitalWrite(ledPin,HIGH);
    Serial.print("its Bright TURN off led:");
    Serial.println(ldrStatus);
  }
}
