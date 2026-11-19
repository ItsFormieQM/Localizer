from pathlib import Path
import json
import globalvars as globalv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def dump_text(jsonname):
    txt = {}
    actualstr = ""
    for i in range(len(jsonname)):
        if jsonname[i] == ".":
            break
        actualstr += jsonname[i]

    if actualstr == "en":
        reset_lang()
        return
    jsonname = f"lang/{jsonname}"
    json_ex = Path(jsonname)

    if not json_ex.exists() or not json_ex.is_file():
        print(f"error, {jsonname} not found!")
        print("language switch failed")
        return False
    else:

        with open(f"{jsonname}", "r", encoding="utf-8") as file:
            txt = json.load(file)
        globalv.text = txt
    return True


def text_setloc(entxt, translkey):
    if globalv.lang == "en":
        return entxt
    else:
        try:
            return globalv.text[translkey]
        except KeyError:
            return f'missing text for key: "{translkey}" on language {globalv.lang}'


def switch_lang(jsonname):
    check = dump_text(jsonname)
    actualstr = ""
    for i in range(len(jsonname)):
        if jsonname[i] == ".":
            break
        actualstr += jsonname[i]

    if actualstr == "en":

        return
    if not check:
        print(
            f"Error, json file {jsonname} does not exist in the lang directory and language wasn't set!"
        )
        return

    globalv.lang = actualstr


def reset_lang():
    globalv.lang = "en"
    globalv.text = {}
def text_function_setloc(entxt,translkey,function):
    if globalv.lang == "en":
        return [entxt,entxt,function]
    else:
        return [globalv.text[translkey],entxt,function]

if __name__ == "__main__":
    print("dont run this directly, just import")
    print("pls run main.py instead")
    raise TypeError("pls run main.py instead")
