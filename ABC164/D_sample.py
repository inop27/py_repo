def main():
    A = input()[::-1]
    A = "0" + A

    S = [0] * len(A)
    cnt = [0] * 2019
    cnt[0] = 1

    for i in range(len(A) - 1):
        S[i + 1] = (S[i] + int(A[i + 1]) * pow(10, i, 2019)) % 2019
        cnt[S[i + 1] % 2019] += 1

    print(S)

    ans = 0

    #余りが等しい桁の中から2つを選ぶ組み合わせの数(nC2)の計算
    for i in cnt:
        ans += i * (i - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
