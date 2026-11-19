from localizer import *
from ext import clamp
from globalvars import *
from methods import *
switch_lang("bis.json")
msg = []
class Account:
    def __init__(self,name,age,pin):
        self.name = name
        self.age = age
        self.pin = pin
    pass
langs = [
    "en.json",
    "ja.json",
    "bis.json"
]
print("---Languages---")
for i in range(len(langs)):
    print(f"{i}. {langs[i]}")
ind = clamp(int(input("Enter index: ")),0,len(langs)-1)
switch_lang(langs[ind])
msg.append(text_setloc(
    "GTA 6 RELEASED GUYS HOLY SHIT",
    "test2"
))

for i in msg:
    print(f"\n{i}")
