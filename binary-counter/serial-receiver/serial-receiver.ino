int outPin[] = {2,3,4,5,6,7,8,9};

void setup() 
{
  Serial.begin(2000000);
   for ( int i = 2; i <= 9; i++)
    pinMode(i, OUTPUT);
}
  void loop() 
  {
    if(Serial.available())
    {
      
      String serial=Serial.readString();
      //char delimitadores[] = ";";
      for(int i=0; i<=30; i=i+4){
      String outpin = (serial.substring(i,i+1));
      String status = (serial.substring(i+2,i+3));
      int a=(outpin).toInt();
      int b = (status).toInt();
      digitalWrite(a,b);
      }
    }   
    
}
//2,1-3,1-4,0-5,0-6,0-7,0-8,0-9,0-
