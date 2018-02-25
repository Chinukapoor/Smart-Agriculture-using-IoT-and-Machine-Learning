#include <DHT.h>
#include <SPI.h>
#include <SD.h>
#define dht_apin A0
DHT dht(dht_apin,DHT11);
File myFile;
void setup(){
// initialize serial communication at 9600 bits per second:l;
Serial.begin(9600);
dht.begin();
Serial.println("Initializating SD Card");
if(!SD.begin(10)){
  Serial.println("SD Card Initialization Failed");
  return;
}
Serial.println("Initialization Complete");
}

void loop() {
// read the input on analog pin 0:
int sensorValue = analogRead(A2); 
//Accessing DHT11 sensor
dht.read(dht_apin);
//Serial.println("Humidity");
myFile = SD.open("wet.txt",FILE_WRITE);
if(myFile){
 float h=dht.readHumidity();
 myFile.print(h);
 float t=dht.readTemperature();
 myFile.print(",");
 myFile.print(t);
  myFile.print(",");
 myFile.print(sensorValue);
 myFile.print(",");
 myFile.println(100);
 Serial.println("humidity,temperature,soil moisture logged");
 myFile.close();
}
else{
  Serial.println("File Write Error");
}
delay(2000);
}
