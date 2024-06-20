import num2words


def test_supported_langauges():
    print("Verifying the Language Supported")
    languages = (num2words.supported_lang())
    
    # check if "en" is present in the available langauges list
    english_lang = 'lang_EN'
    assert english_lang in languages, "Error: English language is not available in the supported languages"
