int outPin[] = {2,3,4,5,6,7,8,9};

void setup() 
{
  Serial.begin(2304000);
   for ( int i = 2; i <= 9; i++)
    pinMode(i, OUTPUT);
}
  void loop() 
  {
    if(Serial.available())
    {
      String serial=Serial.readString();
      //char delimitadores[] = ";";
      String outpin = (serial.substring(0,1));
      String status = (serial.substring(2,3));
  
      int a=(outpin).toInt();
      int b = (status).toInt();
      digitalWrite(a,b);
    }   
}
