#場合分けを行う必要があると考えていたが、例外として処理すればまとめて簡単に表現できる
#int()で文字列を変換する際に、012のような数も12と正しく変換する

s = input()
try:
    ss = int(s)
    print(ss*2)
except ValueError:
    print('error')
