int input3Pin = 11;
int input2Pin = 10;
int input1Pin = 9;

void setup()
{
  Serial.begin(9600);
  pinMode(input3Pin, INPUT);
  pinMode(input2Pin, INPUT);
  pinMode(input1Pin, INPUT);
}

void loop()
{
  for(int i=9 ; i<=11 ; i++) {
    checkPush(i);
  }
}

void checkPush(int pinNumber)
{
  int pushed = digitalRead(pinNumber);  // read input value
  if (pushed == HIGH){
    
    if (pinNumber == 9) {
      Serial.println("B");
    } else if (pinNumber == 10) {
      Serial.println("P");
    } else {
      Serial.println("F");
    }
    
    delay(250);
  }
}
