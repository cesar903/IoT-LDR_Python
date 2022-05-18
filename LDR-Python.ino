void setup() {
  Serial.begin(115200);
}
void loop() {
  int luz=analogRead(1); 
  Serial.println(luz);
  delay(5000); 
}
