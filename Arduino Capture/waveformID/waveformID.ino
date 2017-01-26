const int ANALOG_PIN = 3;     // potentiometer wiper (middle terminal) connected to analog pin 3
                       // outside leads to ground and +5V

const int SAMPLE_LENGTH = 900;
int val[SAMPLE_LENGTH];           // variable to store the value read

void setup(){ 
  Serial.begin(9600);                //  setup serial

}


int i = 1; // declare a variable to index the samples


void loop(){
  while(true) {
    i = i % 900;
//    Serial.println(i);
    
  val[i] = analogRead(ANALOG_PIN);     // read the input pin
  delay(10);

//  if (val[i] > val[(i - 1) % SAMPLE_LENGTH] + 500){       //if the intensity is much greater than a previous sample
//    Serial.println("FLAG2");
//    Serial.println(val[i]);            //send that value out
//    printSomeVal(val, SAMPLE_LENGTH, i);
//  } 
//  if (i == 899){
//    i = -1;
//  }
  i++;
  }
}

//void printSomeVal(int val[], int size, int triggerI) {
//    Serial.println(triggerI);
//  for (int i = 0; i < 6; ++i) {
//    Serial.println(val[(triggerI - i) % size]);
//  }
//}

 
//  val = analogRead(analogPin);
// 
//  if (val > preVal + THRESHOLD){       //if the intensity is much greater than a previous sample
//    Serial.println(val);            //send that value out
//  }
//  preVal = val;
 

