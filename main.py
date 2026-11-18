import localizer
import globalvars

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
# Desired behavior: a failed switch should not leave us in a broken state.
check("failed switch keeps the previous language ('ja')", globalvars.lang, "ja")

# --- 7. get_text -----------------------------------------------------------
print("\n[7] get_text")
localizer.switch_lang("bis.json")
check("get_text('test1') returns that one string",
      localizer.get_text("test1"), "You fool thoust!")

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
