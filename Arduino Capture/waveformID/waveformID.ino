const int ANALOG_PIN = A3;     // potentiometer wiper (middle terminal) connected to analog pin 3
                               // outside leads to ground and +5V

const int SAMPLE_LENGTH = 200;
int val[SAMPLE_LENGTH];        // variable to store the value read
const int THRESHOLD = 30;

int i;

void setup(){ 
  Serial.begin(9600);          //  setup serial
  i = 0;
}

void loop(){
  i = i % SAMPLE_LENGTH;
  val[i] = analogRead(ANALOG_PIN);     // read the input pin
  if (val[i] > ((i == 0) ? val[SAMPLE_LENGTH - 1] : val[i - 1]) + THRESHOLD ){       //if the intensity is much greater than a previous sample;
    Serial.println(val[i]);            //send that value out
//    printSomeVal(val, SAMPLE_LENGTH, i);
  } 
    i++;
}

//void printSomeVal(int val[], int size, int triggerI) {
//    Serial.println(triggerI);
//  for (int i = 0; i < 6; ++i) {
//    Serial.println(val[(triggerI - i) % size]);
//  }
//}


