/*macro definition of Speaker pin*/
#define SPEAKER 3
#define RELAY 5
int BassTab[]={1911,1702,1516,1431,1275,1136,1012};//bass 1~7
 
void setup()
{
  pinInit();
  
}
void loop()
{
        /*sound bass 1~7*/
    
    digitalWrite(RELAY,LOW);
    for(int note_index=0;note_index<7;note_index++)
    {
        sound(note_index);
        delay(500);
    }
    digitalWrite(RELAY,HIGH);
    delay(1500);
}
void pinInit()
{
    pinMode(SPEAKER,OUTPUT);
    pinMode(RELAY, OUTPUT);
    digitalWrite(SPEAKER,LOW);
    digitalWrite(RELAY,LOW);
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
