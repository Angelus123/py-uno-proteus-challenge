#include <GSM.h>


#define PINNUMBER ""
const int led = 6;
const int led1 = 7;
const int led2 = 5;


// initialize the library instance
GSM gsmAccess;
GSM_SMS sms;
GSMVoiceCall vcs;
int receivedData = 0;
String remoteNumber = "0785182823";  // the number you will call
char charbuffer[20];
String remoteNumbero = "0781917267"; 
char charbuffero[20];

String remoteNumbert = "0780837606"; 
char charbuffert[20];
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
  Serial.println("Make Voice Call");

  // connection state
  boolean notConnected = true;

  // Start GSM shield
  // If your SIM has PIN, pass it as a parameter of begin() in quotes
  while (notConnected) {
    if (gsmAccess.begin(PINNUMBER) == GSM_READY) {
      notConnected = false;
    } else {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("GSM initialized.");

}
void loop(){
  Serial.print("Calling to : ");
        
      
  while(Serial.available())
  {
    receivedData = Serial.read();
  }
  
  if (receivedData == 'd')
  
  {
    Serial.println(remoteNumber);
     Serial.println(remoteNumbero);
      Serial.println(remoteNumbert);
        Serial.println();

        // Call the remote number
        remoteNumber.toCharArray(charbuffer, 20);
        remoteNumbero.toCharArray(charbuffer, 20);
        remoteNumbert.toCharArray(charbuffer, 20);


        // Check if the receiving end has picked up the call
        if (vcs.voiceCall(charbuffer)) {
          Serial.println("Call Established. Enter line to end");
          // Wait for some input from the line
          while ((vcs.getvoiceCallStatus() == TALKING));
          // And hang up
          vcs.hangCall();
        }
        Serial.println("Call Finished");
        remoteNumber = "";
         
        Serial.println("Enter phone number to call.");
  }
  else if (receivedData == 'c')
  {
    Serial.println(remoteNumbero);
        Serial.println();

        // Call the remote number
        remoteNumbero.toCharArray(charbuffer, 20);


        // Check if the receiving end has picked up the call
        if (vcs.voiceCall(charbuffer)) {
          Serial.println("Call Established. Enter line to end");
          // Wait for some input from the line
          while ((vcs.getvoiceCallStatus() == TALKING));
          // And hang up
          vcs.hangCall();
        }
        Serial.println("Call Finished");
        remoteNumber = "";
        Serial.println("Enter phone number to call.");
  }
  else if (receivedData == 'r')
  {
     Serial.println(remoteNumbert);
        Serial.println();

        // Call the remote number
        remoteNumbert.toCharArray(charbuffer, 20);


        // Check if the receiving end has picked up the call
        if (vcs.voiceCall(charbuffer)) {
          Serial.println("Call Established. Enter line to end");
          // Wait for some input from the line
          while ((vcs.getvoiceCallStatus() == TALKING));
          // And hang up
          vcs.hangCall();
        }
        Serial.println("Call Finished");
        remoteNumber = "";
        Serial.println("Enter phone number to call.");
  }
}
