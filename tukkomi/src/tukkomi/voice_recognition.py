import os

import speech_recognition as sr
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate

llm = OpenAI(model_name="gpt-4")
chat_model = ChatOpenAI()

prompt = PromptTemplate.from_template("""
あなたはお笑い界の大物です．
次に渡される言葉がダジャレかどうか判定してください． 
ダジャレだった場合は`True`、そうでない場合は`False`と答えてください．
理解できない場合も`False`と答えてください．
-------
{boke}
-------
""")



def speech_rec() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("---------------------------------------------------------------")
        print("-- RECORDING...")
        audio = r.listen(source)
    try:
        # Google Web Speech APIで音声認識
        text = r.recognize_google(audio, language="ja-JP")
    except sr.UnknownValueError:
        #print("Error:Google Web Speech APIは音声を認識できませんでした")
        return "***"
    except sr.RequestError as e:
        #print("Error:GoogleWeb Speech APIに音声認識を要求できませんでした;"
        #    " {0}".format(e))
        return "***"
    else:
        return text

def is_boke(boke: str) -> bool:
    print("---------------------------------------------------------------")
    print("boke: ", boke)
    chain = prompt | llm

    output = chain.invoke({"boke": boke})

    print("output: ", output)
    


def main():
    while True:
        question = speech_rec()
        if(question != "***"):
            print(question)


if __name__ == '__main__':
    print("-- VOICE RECOGNITION --")
    # main()
    boke1 = "布団が吹っ飛んだ"
    boke2 = "今日は暑い日だ"

    is_boke(boke1)
    is_boke(boke2)






