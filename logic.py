from translate import Translator
from collections import defaultdict

questions = {"adın ne?": "ben süper havalı bir botum ve amacım size yardım etmek!",
             "kaç yaşındasın?": "bu çok felsefi bir soru..."}

class TextAnalysis():
    
    memory = defaultdict(list)

    def __init__(self, text, owner):

        TextAnalysis.memory[owner].append(self)

        self.text = text
        self.translation = self.__translate(self.text, "tr", "en")

        if self.text in questions.keys():
            self.response = questions[self.text]
        else:
            self.response = self.get_answer() 

    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "tr")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation
        except:
            return "Çeviri girişimi başarısız oldu."
