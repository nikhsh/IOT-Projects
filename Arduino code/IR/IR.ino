#define led 13
#define sensor 6


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(sensor,INPUT);
  pinMode(led, OUTPUT);
  
}
v
void loop() {
  // put your main code here, to run repeatedly:

  int detect=digitalRead(sensor);
  if(detect==LOW)
  {
    digitalWrite(led,HIGH);
  }
  else{
    digitalWrite(led,LOW);
    }  
    delay(20);
}
