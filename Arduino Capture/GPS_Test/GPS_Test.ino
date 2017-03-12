#include <Arduino.h>
#include "Time.h"
#include "Wire.h"

#include "TinyGPS++.h"


#define GPS_BAUD 9600
#define PC_BAUD 9600

TinyGPSPlus gps;

const int ANALOG_PIN = A0;     // potentiometer wiper (middle terminal) connected to analog pin 3
// outside leads to ground and +5V

const int SAMPLE_LENGTH = 10000;
int val[SAMPLE_LENGTH];        // variable to store the value read
float val2[SAMPLE_LENGTH];
const int THRESHOLD = 750;

int i;
void displayInfo();


void setup() {
  	Serial1.begin(GPS_BAUD);
  	Serial.begin(PC_BAUD);
  	Serial.begin(9600);          //  setup serial
  	analogReadResolution(12);
  	i = 0;
  	for (int k = 0; k < SAMPLE_LENGTH; k++) {
    	val[k] = 0;
  	}
  	bool flag = true;
  	while (flag) {
	    i = i % SAMPLE_LENGTH;

    	val[i] = analogRead(ANALOG_PIN);     // read the input pin
    	//Serial.println(val[i]);
    	if (val[i] >= 2200) {
			while (Serial1.available() && flag) {             // Can Change Serial # based on RX pin
        		if (gps.encode(Serial1.read())) {
          			displayInfo();
          			flag = false;
        		}

        //if (millis() > 5000 && gps.charsProcessed() < 10)
        //{
        //Serial.println(F("No GPS detected: check for gps connection or wiring."));
        //while (true);
        //}
      		}


    	}
    	++i;
  }
}

float convertToVoltage(int val) {
	return val * 3.3 / 4095;
}

void loop() {

  //val2[i] = convertToVoltage(val[i]);
  //  if (val[i] > ((i == 0) ? val[SAMPLE_LENGTH - 1] : val[i - 5]) + THRESHOLD )  //if the intensity is much greater than a previous sample;
  //  {
  //    val2[i] = convertToVoltage(val[i]);
  //    Serial.println(val2[i]);            //send that value out
  //
  //  }
}



void displayInfo() {
	  Serial.print("Node: 1");
	  Serial.print(" ");
	  Serial.print(F("Location: "));
	  if (gps.location.isValid())
	  {
	    Serial.print(gps.location.lat(), 6);
	    Serial.print(F(","));
	    Serial.print(gps.location.lng(), 6);
	  }
	  else
	  {
	    Serial.print(F("INVALID"));
	  }
	
	  Serial.print(F(" Time: "));
	  //    if (gps.date.isValid())
	  //    {
	  //
	  //      Serial.print(gps.date.month());
	  //      Serial.print(F("/"));
	  //      Serial.print(gps.date.day());
	  //      Serial.print(F("/"));
	  //      Serial.print(gps.date.year());
	  //    }
	  //    else
	  //    {
	  //      Serial.print(F("INVALID"));
	  //    }
	
	  Serial.print(F(" "));
	  if (gps.time.isValid())
	  {
	    if (gps.time.hour() < 10) Serial.print(F("0"));
	    Serial.print(gps.time.hour());
	    Serial.print(F(":"));
	    if (gps.time.minute() < 10) Serial.print(F("0"));
	    Serial.print(gps.time.minute());
	    Serial.print(F(":"));
	    if (gps.time.second() < 10) Serial.print(F("0"));
	    Serial.print(gps.time.second());
	    Serial.print(F("."));
	    if (gps.time.centisecond() < 10) Serial.print(F("0"));
	    Serial.print(gps.time.centisecond());
	
	  }
	  else
	  {
	    Serial.print(F("INVALID"));
	  }
	  delay(1000);
	  Serial.println();

}
