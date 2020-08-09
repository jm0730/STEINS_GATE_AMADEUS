from playsound import playsound
import sys
import speech_recognition as sr
import time
import webbrowser
import os.path
import os

def amadeus_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('한국어로 말하세요')
        audio = r.listen(source)
    try:
        print("당신은 말했습니다." + r.recognize_google(audio, language="ko-KR"))

        if '안녕' or '좋은 아침' in r.recognize_google(audio, language="ko-KR"):
                print ("하로-")
                playsound('./aa\hello.mp3')

        elif "무엇을 할 수 있" in r.recognize_google(audio, language="ko-KR"):
                print ("무엇이든 물어봐 주세요. 가능한 범위에서 대답해드릴테니까요.")
                playsound('./aa\askmewhatever.mp3')

        elif "나무위키" in r.recognize_google(audio, language="ko-KR"):
                print ("나무위키에 접속합니다.")
                webbrowser.open('https://namu.wiki')
                playsound('./aa\you_sure.mp3')
   
        elif "크롬" or "Chrome" in r.recognize_google(audio, language="ko-KR"):
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            if os.path.isfile(chromepath):
                print("크롬을 실행합니다.")
                playsound('./aa\you_sure.mp3')
                os.startfile(chromepath)
                
            else :
                print('크롬 브라우저가 설치되지 않았거나 지정된 경로에 없습니다.')
                playsound('./aa\sorry.mp3')

        else:
             webbrowser.open("http://www.google.com/search?client=chrome&rls=en-us&q=" + r.recognize_google(audio, language="ko-KR") + "&ie=UTF-8&oe=UTF-8")
    
    except sr.UnknownValueError:
        print("질문을 이해할 수 없습니다.")
        playsound('./aa\sorry.mp3')


