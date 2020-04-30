'''
#二回ループを回していて効率が悪い
#文が無駄に長くなっているので、変数に代入して整理する
#出力が指定の通りになっていれば問題ないらしい
n = int(input())

num_list = list()
for num in range(n):
    num_list.append(int(input()))

for num in range(n-1):
    if num_list[num + 1] == num_list[num]:
        print('stay')
    elif num_list[num + 1] < num_list[num]:
        print('down[{0}]'.format(num_list[num] - num_list[num + 1]))
    elif num_list[num + 1] > num_list[num]:
        print('up[{0}]'.format(num_list[num + 1] - num_list[num]))
'''

n = int(input())
x = int(input())
for i in range(n-1):
    y = int(input())
    if x>y:
        print("down",x-y)
    elif x==y:
        print("stay")
    else:
        print("up",y-x)
    x = y
