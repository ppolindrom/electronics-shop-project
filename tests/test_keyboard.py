from src.keyboard import KeyBoard

def test_keyboard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

    kb.language = 'CH'
    # AttributeError: property 'language' of 'KeyBoard' object has no setter