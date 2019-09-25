# ワードフィルタークラス

class WordFilter():
    def __init__(self, NG_words):
        self.NG_words = NG_words

    def detect(self, string):
        boolean = False

        for NG_word in self.NG_words:
            boolean = NG_word in string
            if boolean:
                return boolean

        return boolean


    def censor(self, string):
        for NG_word in self.NG_words:
            string = string.replace(NG_word, "<censored>")

        return string


    def censor2(self, string, censored_word):
        for NG_word in self.NG_words:
            string = string.replace(NG_word, censored_word)

        return string

    def change_NG_word(self, NG_words):
        self.NG_words = NG_words
        return
