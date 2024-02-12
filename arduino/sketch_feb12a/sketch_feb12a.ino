#include "Servo.h"
Servo servo;
int angle; // переменная для угла поворота микро серво

void setup() {
  servo.attach(8); // пин для подключения микро серво
}

void loop() {
  // цикл для поворота от 0 до 90 градусов
  for (angle = 0; angle <= 1000; angle++) {
    servo.write(angle); // сообщаем микро серво угол поворота
  }
}
