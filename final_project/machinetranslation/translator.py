import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(english_text):

    if english_text == "":
        return ""

    translation_response = language_translator.translate(
    text = english_text,
    model_id = 'en-fr').get_result()

    translation = translation_response['translations'][0]['translation']
    frenchText = json.dumps(translation, indent=2, ensure_ascii=False)

    return frenchText

def frenchToEnglish(french_text):

    if french_text == "":
        return ""

    translation_response = language_translator.translate(
    text = french_text,
    model_id = 'fr-en').get_result()

    translation = translation_response['translations'][0]['translation']
    english_text = json.dumps(translation, indent=2, ensure_ascii=False)

    return english_text
