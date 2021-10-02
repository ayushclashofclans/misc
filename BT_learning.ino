int t;
void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
 if(Serial.available())
 {
 t=Serial.read();
 Serial.println(t);
 }
 delay(100);
}
