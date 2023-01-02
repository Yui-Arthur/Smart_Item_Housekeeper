// Arduino Code to measure distance with a Sharp GP2D12 sensor
// www.swanrobotics.com

#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX
#define SPEAKER 3
#define RELAY 5

int IR_SENSOR = A0; // 類比讀取腳設為A0Sensor is connected to the analog A0
uint16_t BassTab[100];
unsigned char serialBuffer[2];//
int intSensorResult = 0; //Sensor result
float fltSensorCalc = 0; //Calculated value

void setup()
{
  
  pinInit();
  Serial.begin(38400); 
  mySerial.begin(38400);

}
void pinInit()
{
    pinMode(SPEAKER,OUTPUT);
    pinMode(RELAY, OUTPUT);
    pinMode(IR_SENSOR, INPUT);
    digitalWrite(SPEAKER,LOW);
    digitalWrite(RELAY,HIGH);
}

void loop()
{
// read the value from the ir sensor

  intSensorResult = analogRead(IR_SENSOR); //Get sensor value
  fltSensorCalc = (6787.0 / (intSensorResult - 3.0)) - 4.0; //Calculate distance in cm

  //Serial.print(fltSensorCalc); //Send distance to computer
  //Serial.println(" cm"); //Add cm to result

  mySerial.print(fltSensorCalc);
  //mySerial.println(" cm");
  delay(1000); 

  if(mySerial.available()){
    readSoundByte();
  } 

}


void readSoundByte()
{
  int idx = 0;
  while(mySerial.available()>0){

    mySerial.readBytes(serialBuffer, 2);

    int a = serialBuffer[1] + (serialBuffer[0] << 8);
    /**
    Serial.println((int)serialBuffer[0]);
    Serial.println((int)serialBuffer[1]);
    
    Serial.println("Finished Printing Recevied Data.");
    **/
    Serial.println(a);
    BassTab[idx] = a;
    idx++;

    if(idx == 7)
      break;

  }
  int order_num;
  idx = 0;

  while(mySerial.available()>0){
    mySerial.readBytes(serialBuffer, 1);
    //Serial.println((int)serialBuffer[0]);
    order_num = serialBuffer[0];
    break;
  }

  digitalWrite(RELAY,LOW);
  Serial.println(order_num);
  //sound(1);
  while(mySerial.available()>0){

    mySerial.readBytes(serialBuffer, 1);

    int a = serialBuffer[0];

    idx++;
    Serial.println(a);
    sound(a);
    if(idx == order_num)
      break;

  }

  digitalWrite(RELAY,HIGH);
}


void sound(uint8_t note_index)
{
    for(int i=0;i<100;i++)
    {
        digitalWrite(SPEAKER,HIGH);
        delayMicroseconds(BassTab[note_index]);
        digitalWrite(SPEAKER,LOW);
        delayMicroseconds(BassTab[note_index]);
    }
}