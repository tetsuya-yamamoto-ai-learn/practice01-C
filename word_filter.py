# ワードフィルタークラス

class WordFilter():
    def __init__(self, NG_word):
        self.NG_word = NG_word

    def detect(self, string):
        return self.NG_word in string
