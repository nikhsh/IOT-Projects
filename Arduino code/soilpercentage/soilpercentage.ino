
#define moisture_pin A0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("measure the water level in Ardunio...!!!");
  pinMode(moisture_pin, INPUT);
  delay(1000);

}

void loop() {
  // put your main code here, to run repeatedly:

  int moisture_level = map(analogRead(moisture_pin), 0, 1023, 100, 0);

  Serial.print("Moisture Level...");
  Serial.print('%');
  Serial.println();
  delay(500);
}
