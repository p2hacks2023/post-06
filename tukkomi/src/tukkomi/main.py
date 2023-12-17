import voice_recognition
import gag_judegement
import control_motor

def main():
    print("-- VOICE RECOGNITION --")
    while True:
        boke = voice_recognition.speech_rec()
        if(boke != "***"):
            print(boke)
            print("-- GAG JUDEGEMENT --")
            res = gag_judegement.is_boke(boke)
            print("is boke" if res else "is not boke")

            if res:
                print("-- CONTROL MOTOR --")
                control_motor.control_motor()

if __name__ == '__main__':
    main()


    