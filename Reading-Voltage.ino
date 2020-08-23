#define cellPin A0
#include <SoftwareSerial.h>
#define RN_42_Rx 0
#define RN_42_Tx 1
const float mvc=4.74; //set this variable with the 5v of your own arduino via multimeter (5v actual voltage devide by 1024)
float counts=0;
float mv=0;
SoftwareSerial mySerial(RN_42_Rx,RN_42_Tx); // RX, TX
int flag=0;

void setup() {
  // put your setup code here, to run once:  
  mySerial.begin(38400);
}

void loop() {
  // put your main code here, to run repeatedly:
  counts = analogRead(cellPin);
//  Serial.println(String(counts));
    
  mv= counts * mvc;
  if(mv>=2500 && flag==0)
  {
    flag=1;
    mySerial.println("y");
  }
  else if(mv<=2500)
  {
    flag=0;
    }
  delay(1000);  
  //Serial.println(String(mv));
}
