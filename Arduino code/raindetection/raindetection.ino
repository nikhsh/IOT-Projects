
const int sensorMin = 0;
const int sensorMax = 1024;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  int sensorReading = analogRead(A0);
  int range = map(sensorReading, sensorMin, sensorMax, 0, 3);

  // range value is put

  switch(range){
    case 0:
      Serial.println("Rain Warning...");
      break;


    case 1:
      Serial.println(" Not Raining");
      break;
      
    }

    delay(1000);
}
