import localizer
from math_ext import clamp
localizer.switch_lang("bis.json")
msg = []

langs = [
    "en.json",
    "ja.json",
    "bis.json"
]
print("---Languages---")
for i in range(len(langs)):
    print(f"{i}. {langs[i]}")
ind = int(input("Enter index: "))

localizer.switch_lang(langs[clamp(ind,0,len(langs)-1)])
msg.append(localizer.text_setloc(
    "You know. I used to hardcode my text before. But now that I started game dev. I've changed for the better. Hehehe",
    "test3"
))
msg.append(localizer.text_setloc(
    "I'm not scared of you!",
    "test9"
))
for i in msg:
    print(i, end="\n")
