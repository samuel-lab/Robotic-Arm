#include <AccelStepper.h>
#include <Servo.h>
#include <math.h>

#define limitSwitch1 16
#define limitSwitch2 17
#define limitSwitch3 23
#define limitSwitch4 25

// Define the stepper motors and the pins the will use
AccelStepper stepper1(1, 54, 55); // (Type:driver, STEP, DIR)
AccelStepper stepper2(1, 60, 61);
AccelStepper stepper3(1, 46, 48);
AccelStepper stepper4(1, 26, 28);

#define EN1_PIN  38
#define EN2_PIN  56
#define EN3_PIN  62
#define EN4_PIN  24
void setup() {

  pinMode(EN1_PIN, OUTPUT);
  digitalWrite(EN1_PIN, LOW);

  pinMode(EN2_PIN, OUTPUT);
  digitalWrite(EN2_PIN, LOW);

  pinMode(EN3_PIN, OUTPUT);
  digitalWrite(EN3_PIN, LOW);

  pinMode(EN4_PIN, OUTPUT);
  digitalWrite(EN4_PIN, LOW);

  Serial.begin(115200);

  pinMode(limitSwitch1, INPUT_PULLUP);
  pinMode(limitSwitch2, INPUT_PULLUP);
  pinMode(limitSwitch3, INPUT_PULLUP);
  pinMode(limitSwitch4, INPUT_PULLUP);
}

void loop() {
 // Store the target positions in the "gotopostion" array // 800 steps - full rotation with quater-step resolution

  stepper2.moveTo(-1600);
  stepper2.run(); // Calculates the required speed for all motors
  //stepper2.runSpeedToPosition(); // Blocks until all steppers are in position

  delay(1000);

  stepper2.moveTo(1600);
  stepper2.run();
  //stepper2.runSpeedToPosition();

  delay(1000);

  }
