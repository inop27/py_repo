s = input()

counter_list = [0] * 2019
counter_list[0] = 1
cumulative_sum_list = [0] * (len(s) + 1)

for i in range(len(s)):
    cumulative_sum_list[i + 1] = int(s[len(s)-i-1:len(s)]) % 2019
    counter_list[cumulative_sum_list[i + 1]] += 1

ans = 0

for i in counter_list:
    ans += i * (i - 1) // 2

print(ans)
