import deepl
import os

AUTH_KEY = os.environ["AUTH_KEY"]
translator = deepl.Translator(AUTH_KEY)

text = input("Please write your sentence: ")
en_gb = translator.translate_text(f"イギリス英語: {text}", target_lang="EN-GB")
print(en_gb.text)
en_us = translator.translate_text(f"アメリカ英語: {text}", target_lang="EN-US")
print(en_us.text)

