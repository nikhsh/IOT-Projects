const int pingpin = 7;
const int echoPin = 6;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

long duration, inches, cm;
pinMode(pingpin, OUTPUT);
digitalWrite(pingpin, LOW);
delayMicroseconds(10);
digitalWrite(pingpin, HIGH);
delayMicroseconds(10);
digitalWrite(pingpin, LOW);
   pinMode(echoPin, INPUT);
   duration = pulseIn(echoPin, HIGH);
   inches = microsecondsToInches(duration);
   cm = microsecondsToCentimeters(duration);
   Serial.print(inches);
   Serial.print("in, ");
   Serial.print(cm);
   Serial.print("cm");
   Serial.println();
   delay(100);


}

long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}
