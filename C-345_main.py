from word_filter import WordFilter


def main():
    # 初期設定
    NG_word = input("NGワードリストを登録してね(スペース区切り)> ")
    my_filter = WordFilter(NG_word.split(" "))

    switch = 1
    while switch:
        print(
            f'***WordFilter***\n現在のNGワード: {my_filter.NG_words}\n\t1.NGワードが含まれているか表示する\n\t2.NGワードを"<censor>"に変換する\n\t3.NGワードを好きな文字列に変換して表示する\n\t4.NGワードを変更する\n\t0.終了する')

        switch = int(input("コマンドを入力してください: "))

        # 指定した文字列の有無を表示する
        if switch == 1:
            target = input("検索する文字列は？ > ")
            print(my_filter.detect(target))

        elif switch == 2:
            target = input("検索する文字列は？ > ")
            print(my_filter.censor(target))

        elif switch == 3:
            target = input("検索する文字列は？ > ")
            censored = input("変換後の文字列は？ > ")
            print(my_filter.censor2(target, censored))

        elif switch == 4:
            NG_word = input("変更後のNGワードリストを入力してね(スペース区切り)> ")
            my_filter.change_NG_word(NG_word.split(" "))

        elif switch == 0:
            print("See you...")

        else:
            print("有効な数字を入れてください")


if __name__ == '__main__':
    main()
