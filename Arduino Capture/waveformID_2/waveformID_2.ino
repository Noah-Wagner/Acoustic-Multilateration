int analogPin = 3;     // potentiometer wiper (middle terminal) connected to analog pin 3
                       // outside leads to ground and +5V
int val1 = 0;           // variable to store the value read
int val2 = 0;
int val3 = 0;
int val4 = 0;
int val5 = 0;

void setup(){ 
  Serial.begin(9600);                //  setup serial
}

void loop(){
 val1 = analogRead(analogPin);     // read the input pin1
 delayMicroseconds(500);
 val2 = analogRead(analogPin);     // read the input pin2
 delayMicroseconds(500);
 val3 = analogRead(analogPin);     // read the input pin3
 delayMicroseconds(500);
 val4 = analogRead(analogPin);     // read the input pin4
 delayMicroseconds(500);
 val5 = analogRead(analogPin);     // read the input pin5
  
 if (val2 > val1 + 200){
   Serial.println(val2);
  }
 else if (val3 > val2 + 200){
   Serial.println(val3);
  } 
 else if (val4 > val3 + 200){
   Serial.println(val4);
  } 
 else if (val5 > val4 + 200){
   Serial.println(val5);
  }
}

