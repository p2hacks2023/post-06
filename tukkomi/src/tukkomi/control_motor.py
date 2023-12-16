import requests

def control_motor():
    response = requests.get("http://192.168.11.15:8000/control_motor")
    print(response.json())

# モーターを制御
if __name__ == "__main__":
    control_motor()