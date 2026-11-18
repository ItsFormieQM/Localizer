import sys
import localizer
import globalvars

# Make sure Japanese prints correctly in terminals that default to another encoding.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

passed = 0
failed = 0


def check(name, actual, expected):
    """Compare actual vs expected and print PASS/FAIL."""
    global passed, failed
    if actual == expected:
        passed += 1
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")
        print(f"        expected: {expected!r}")
        print(f"        got:      {actual!r}")


EN = "So it stands, formerhyde"

# --- 1. Default state is English -------------------------------------------
print("\n[1] Default language")
localizer.reset_lang()
check("lang starts as 'en'", globalvars.lang, "en")
check("English returns the passed-in text", localizer.text_setloc(EN, "test3"), EN)

# --- 2. Switching to Bisaya ------------------------------------------------
print("\n[2] Switch to bis.json")
localizer.switch_lang("bis.json")
check("lang code is 'bis'", globalvars.lang, "bis")
check("test1 comes from bis.json", localizer.text_setloc("x", "test1"), "You fool thoust!")
check("test2 comes from bis.json", localizer.text_setloc("x", "test2"),
      "gi kuha nimo ang lorem ipsum sa yuta.")
check("English text is ignored when not 'en'", localizer.text_setloc(EN, "test3") != EN, True)

# --- 3. Switching to Japanese ----------------------------------------------
print("\n[3] Switch to ja.json")
localizer.switch_lang("ja.json")
check("lang code is 'ja'", globalvars.lang, "ja")
check("test1 comes from ja.json", localizer.text_setloc("x", "test1"), "この愚か者め！")
check("test3 comes from ja.json", localizer.text_setloc("x", "test3"), "arigato!")

# --- 4. Reset back to English ----------------------------------------------
print("\n[4] Reset to English")
localizer.reset_lang()
check("lang is 'en' again", globalvars.lang, "en")
check("English text returned again", localizer.text_setloc(EN, "test3"), EN)

# --- 5. Missing key --------------------------------------------------------
print("\n[5] Missing key")
localizer.switch_lang("bis.json")
check("unknown key gives the 'missing text' message",
      localizer.text_setloc("x", "doesnotexist"),
      'missing text for key: "doesnotexist"')
localizer.reset_lang()
check("unknown key is fine in English (key not needed)",
      localizer.text_setloc("hello", "doesnotexist"), "hello")

# --- 6. Missing language file ----------------------------------------------
print("\n[6] Missing language file")
localizer.switch_lang("ja.json")
localizer.switch_lang("nope.json")   # file does not exist
check("failed switch keeps the previous language ('ja')", globalvars.lang, "ja")

# --- 7. Dialogue: 20 lines, each checked in English, Bisaya and Japanese ---
# The English text is what the game code passes in; the other languages come
# from lang/bis.json and lang/ja.json.
DIALOGUE = {
    "test1": "You fool thoust!",
    "test2": "You picked up the lorem ipsum from the ground.",
    "test3": "You know. I used to hardcode my text before. But now that I started game dev. I've changed for the better. Hehehe",
    "test4": "* A cold wind blows through the empty hall.",
    "test5": "Welcome, traveler. You look tired.",
    "test6": "Do you have the key to the old gate?",
    "test7": "* You found a rusty key on the ground.",
    "test8": "* Your HP was restored.",
    "test9": "I'm not afraid of you!",
    "test10": "Please, don't go into the forest alone.",
    "test11": "* The shopkeeper smiles at you.",
    "test12": "That will be 50 gold.",
    "test13": "You don't have enough gold.",
    "test14": "Thank you for your help. I won't forget this.",
    "test15": "* The door is locked.",
    "test16": "Look out behind you!",
    "test17": "* You hear footsteps in the distance.",
    "test18": "The path ahead is long. Take this with you.",
    "test19": "Heh. Not bad for a beginner.",
    "test20": "Goodbye, and good luck on your journey."
}


def lookup(lang_file, key, english):
    """Switch language (or reset for English) and return the text for key."""
    if lang_file is None:
        localizer.reset_lang()
    else:
        localizer.switch_lang(lang_file)
    return localizer.text_setloc(english, key)


def dialogue_status(key, english):
    """Return 'ok' if the key works in all three languages, else a description."""
    if lookup(None, key, english) != english:
        return "English did not return the passed-in text"
    for lang_file in ("bis.json", "ja.json"):
        text = lookup(lang_file, key, english)
        if text.startswith("missing text"):
            return f"{lang_file}: key is missing"
        if not text.strip():
            return f"{lang_file}: text is empty"
    return "ok"


print("\n[7] Dialogue lines (en / bis / ja)")
for key, english in DIALOGUE.items():
    check(f"{key} works in en, bis and ja", dialogue_status(key, english), "ok")

# --- Summary ---------------------------------------------------------------
print(f"\n{passed} passed, {failed} failed")

# --- Original demo ---------------------------------------------------------
print("\n--- demo ---")
localizer.switch_lang("bis.json")
msg = []
msg.append(localizer.text_setloc(
    "You know. I used to hardcode my text before. But now that I started game dev. I've changed for the better. Hehehe",
    "test3"
))
localizer.reset_lang()
msg.append(localizer.text_setloc("So it stands, formerhyde", "test3"))
for m in msg:
    print(m)
    print("")

# --- Dialogue printout -----------------------------------------------------
print("--- dialogue ---")
for key, english in DIALOGUE.items():
    print(f"{key}")
    print(f"  en:  {lookup(None, key, english)}")
    print(f"  bis: {lookup('bis.json', key, english)}")
    print(f"  ja:  {lookup('ja.json', key, english)}")
localizer.reset_lang()
