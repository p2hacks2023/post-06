import requests

def control_motor():
    response = requests.post("http://192.168.11.15:8000/control_motor", json={})
    print(response.json())

# モーターを制御
control_motor()