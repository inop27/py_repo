def main():
    s = input()

    counter_list = [0] * 2019
    counter_list[0] = 1
    cumulative_sum_list = [0]

    for i in range(len(s)):
        value = int(s[len(s)-i-1:len(s)]) % 2019
        cumulative_sum_list.append(value)
        counter_list[value] += 1

    ans = 0

    for i in counter_list:
        ans += i * (i - 1) // 2

    print(ans)

if __name__ == '__main__':
    main()
