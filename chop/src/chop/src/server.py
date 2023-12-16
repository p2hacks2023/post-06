from fastapi import FastAPI
from lib_servo import LobotServoController
import time

app = FastAPI()

HAND_ID = 7
servoController = LobotServoController('/dev/ttyS0')  # UART通信のときのラズパイ3B+におけるシリアルポート


# モーター制御のためのエンドポイント
@app.post("/control_motor")
async def control_motor():
    # パラメータを含めずにモーターを制御
    time.sleep(2) # デバイスの初期化待機
    print("デバイスの初期化終了")
    
    servos = [{"ID": HAND_ID, "Position": 2400}]
    servoController.moveServos(servos, 300) # 0.3sec
    time.sleep(1)
    servos = [{"ID": HAND_ID, "Position": 2600}] # Position is PWM
    servoController.moveServos(servos, 1000) # 1sec
    time.sleep(2)
    
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
