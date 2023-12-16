#include <Servo.h>
float raw_value;
float weight;

Servo servo;
//サーボ配線　茶：GND　赤：5V　黄：pin

void setup() { 
  Serial.begin(9600);
  servo.attach(7,500,2400);
  servo.write(111); //モータ初期角度決め
  
}

void loop() {
  raw_value = analogRead(A0);
  weight = raw_value / 1024 * 200;　//かかる圧力 圧力が大きいほど数値が小さくなる
  Serial.println(weight);

  //圧力センサが反応したら顎動かす
  if(weight <= 140){
    servo.write(45); //口開ける
    delay(1000); //1秒間口開ける
    servo.write(111); //もとに戻す
  }
  delay(100);
}
