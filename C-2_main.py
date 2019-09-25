from word_filter import WordFilter


def main():
    my_filter = WordFilter("アーセナル")

    # NGワードが含まれている場合
    print(my_filter.censor("昨日のアーセナルの試合アツかった！"))  # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！

    # NGワードが含まれていない場合
    print(my_filter.censor("昨日のリバプールの試合アツかった！"))  # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！


if __name__ == '__main__':
    main()
