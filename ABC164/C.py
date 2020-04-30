#n = input()
#print(len(set(input() for num in range(int(n)))))

n = int(input())
giftSet = set(input() for num in range(n))

print(len(giftSet))
