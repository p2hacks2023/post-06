import requests

def control_motor():
    response = requests.get("http://192.168.11.15:8000/control_motor")
    print(response.json())

# モーターを制御
control_motor()
