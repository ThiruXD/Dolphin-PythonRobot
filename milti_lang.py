import os
from typing import List
from random import choice as choice_
import yaml

languages = {}
commands = {}


def _(word: str) -> str:
    return word.replace('_', ' ').lower()

def get_string(lang: str):
    return languages[lang]


for filename in os.listdir(r".wordlists"):
    if filename.endswith(".txt"):
        language_name = filename[:-4]
        commands[language_name] = yaml.safe_load(
            open(r"./wordlists/" + filename, encoding="utf8")
        )


for filename in os.listdir(r".wordlists/"):
    if "en" not in languages:
        languages["en"] = yaml.safe_load(
            open(r".wordlists/en.txt", encoding="utf8")
        )
    if filename.endswith(".txt"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        languages[language_name] = yaml.safe_load(
            open(r".wordlists/" + filename, encoding="utf8")
        )
        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]

