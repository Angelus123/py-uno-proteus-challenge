#include <GSM.h>

#define PINNUMBER ""
const int led = 6;
const int led1 = 7;
const int led2 = 5;


// initialize the library instance
GSM gsmAccess;
GSM_SMS sms;
int receivedData = 0;

void setup()
{

  pinMode(led, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  digitalWrite (led, LOW);
  digitalWrite (led1, LOW);
  digitalWrite (led2, LOW);
  Serial.begin(9600);
   while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  Serial.println("Connected Successfully");
  Serial.println("SMS Messages Sender");
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while (notConnected) {
    if (gsmAccess.begin(PINNUMBER) == GSM_READY) {
      notConnected = false;
    } else {
      Serial.println("Not connected");
  
    }
  }

  Serial.println("GSM initialized");
}


void loop(){
  receivedData = Serial.read();
  if (receivedData == 'd')
  
  {
    sms.beginSMS("0785182823");
    sms.print("Hey Doctor I am testing!");
    sms.endSMS();
    Serial.println("\nWOW!\n");
    digitalWrite (led, HIGH);
    digitalWrite (led1, LOW);
    digitalWrite (led2, LOW);
  }
  else if (receivedData == 'c')
  {
    sms.beginSMS("0781789636");
    sms.print("Hey My Cleaner,  I am testing!");
    sms.endSMS();
    digitalWrite (led, LOW);
    digitalWrite (led1, HIGH);
    digitalWrite (led2, LOW);
  }
  else if (receivedData == 'r')
  {
     sms.beginSMS("0787012307");
     sms.print("Hey lovly Restaurent, I am testing!");
     sms.endSMS();
    digitalWrite (led, LOW);
    digitalWrite (led1, LOW);
    digitalWrite (led2, HIGH);
  }
}
