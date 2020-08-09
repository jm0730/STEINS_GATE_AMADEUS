from amadeuslogin import amadeus_login
from command import amadeus_command
import time
import os
import sys
import webbrowser

q = input('1 실행\n2 최신버전 다운로드\n')
if q == '1':
    amadeus_login()
    print("연결중...")
    while True:
        amadeus_command()

if q == '2':
    webbrowser.open("http://download.amadeuspython.ml")
    

