#include <Servo.h>
Servo servo; //サーボモータ

float raw_value;
float weight; //かかる圧力

void setup() { 
  Serial.begin(9600);
  servo.attach(7,500,2400); //パルス幅を500~2400msに指定
  servo.write(111); //モータ初期角度決め
  
}

void loop() {
  raw_value = analogRead(A0);
  weight = raw_value / 1024 * 200;　//圧力が大きいほど数値が小さくなる
  Serial.println(weight);

  //圧力センサが反応したら顎動かす
  if(weight <= 180){
    servo.write(45); //口開ける
    delay(1000); //1秒間口開ける
    servo.write(111); //もとに戻す
  }
  delay(100);
}
