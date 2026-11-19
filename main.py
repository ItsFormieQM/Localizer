from localizer import *
from ext import clamp
from globalvars import *
from methods import *
while True:
    
    msg = []
    class Account:
        def __init__(self,name,age,pin):
            self.name = name
            self.age = age
            self.pin = pin
        pass
    cmds = [
        "Exit",
        "Switch_Language",
        "Clear",
    ]
    if debug:
        cmds.append("Push")
    print(text_setloc("---Bank with OOP + translation---","intro_1"))
    def execute_ind(indnum):
        if indnum >= len(cmds) or indnum < 0:
            print("Command doesn't exist!\n")
            return
        print(f"Selected {cmds[indnum]}")
        eval(cmds[indnum] + "()")
    print(text_setloc("---Command List---","cmdls_1"))
    for i in range(len(cmds)):
        print(f"{i+1}. {cmds[i]}")
    
    ind = int(input(text_setloc("Enter your index: ","indexsel_1")))-1
    execute_ind(ind)
