import requests
import re
import json

ETRI_OPEN_API_URL = "http://aiopen.etri.re.kr:8000/WikiQA"
RE_KANJI = re.compile (r'[㐀-䶵一-鿋豈-頻]')

def get_answer (question):
    from . import ACCESS_KEY

    requestJson = {
        "access_key": ACCESS_KEY,
        "argument": {
            "question": question,
            "type": "ENGINE_TYPE"
        }
    }
    response = requests.post (ETRI_OPEN_API_URL, json.dumps(requestJson), headers={"Content-Type": "application/json; charset=UTF-8"})
    result = response.json ()
    try:
        best = result ['return_object']['WiKiInfo']
        subject = best ['IRInfo'][0]['wiki_title']
        answer = best ['AnswerInfo'][0]['answer']
        answer = RE_KANJI.sub ('', answer)
    except (IndexError, KeyError):
        return {}
    else:
        return dict (
            best = best, answer = answer, subject = subject
        )
