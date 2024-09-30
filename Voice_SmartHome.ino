#include <Servo.h>

const int LED_PIN = 13; // lamp
const int MOTOR_PIN = 9; // fan
const int SERVO_PIN = 12; // door

Servo myServo;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  pinMode(MOTOR_PIN, OUTPUT);
  myServo.attach(SERVO_PIN);
  myServo.write(90);  // Set servo to middle position
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command == "LED_ON") {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("LED turned on");
    } else if (command == "LED_OFF") {
      digitalWrite(LED_PIN, LOW);
      Serial.println("LED turned off");
    } else if (command == "MOTOR_ON") {
      analogWrite(MOTOR_PIN, 255);
      Serial.println("Motor turned on");
    } else if (command == "MOTOR_OFF") {
      analogWrite(MOTOR_PIN, 0);
      Serial.println("Motor turned off");
    } else if (command == "SERVO_LEFT") {
      myServo.write(0);
      Serial.println("Servo moved left");
    } else if (command == "SERVO_RIGHT") {
      myServo.write(90);
      Serial.println("Servo moved right");
    } else {
      Serial.println("Unknown command");
    }
  }
}