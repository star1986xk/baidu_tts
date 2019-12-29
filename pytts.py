# -*- coding: utf-8 -*-


import pyttsx3

with open("2.txt",'r',encoding='utf-8') as f:
    line = f.read()
list_line = line.split('\n')

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
for li in list_line:
    line_list = li.split(',')
    print(line_list)
    engine.say(line_list[0])
    engine.say(list(line_list[0]))
    engine.say(line_list[1])

    engine.say(line_list[0])
    engine.say(list(line_list[0]))
    engine.say(line_list[1])

    engine.say(line_list[0])
    engine.say(list(line_list[0]))
    engine.say(line_list[1])
    engine.runAndWait()
