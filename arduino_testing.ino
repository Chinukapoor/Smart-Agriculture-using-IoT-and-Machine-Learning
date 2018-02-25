#include <DHT.h>
#include <SPI.h>
#include <SD.h>
#define dht_apin A0
DHT dht(dht_apin,DHT11);
File myFile;
char userinput;
void setup()
{
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  
if(Serial.available()>0)
{
  userinput = Serial.read();
  if (userinput == 'g'){
      int sensorValue = analogRead(A2); 
      dht.read(dht_apin);
      float h=dht.readHumidity();
      float t=dht.readTemperature();
      Serial.print(h);
      Serial.print(",");
      Serial.print(t);
      Serial.print(",");
      Serial.print(sensorValue);
      Serial.print(",");
      Serial.println(100);
      
      }

}
}
