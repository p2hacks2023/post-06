import requests
import time

def control_motor():
    start = time.time()
    response = requests.get("http://192.168.11.9:8000/control_motor")
    print(response.json())
    end = time.time()
    print("control_motor time: " + str(end - start))

# モーターを制御
if __name__ == "__main__":
    control_motor()