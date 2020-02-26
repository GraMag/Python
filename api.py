#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests # si no esta instalado cmd pip install requests

r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Buenos%20Aires&units=metric&appid=0a213b927a602c0ca067808ede151751") 

d = r.json() #guarda el diccionario en una variable

print(d["main"]["temp"])
print(d["main"]["humidity"])
print(d["main"]["pressure"])
print(d["visibility"])
