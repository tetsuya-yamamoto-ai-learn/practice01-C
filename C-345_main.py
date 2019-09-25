from word_filter import WordFilter


def main():
    my_filter = WordFilter(["アーセナル", "試合"])

    # NGワードが含まれている場合
    print(my_filter.censor2("昨日のアーセナルの試合アツかった！", "XX"))  # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！

    # NGワードが含まれていない場合
    print(my_filter.censor2("昨日のリバプールの試合アツかった！", "XX"))  # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！


if __name__ == '__main__':
    main()
