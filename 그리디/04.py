x, k = map(int, input().split())
count = 0
while(1):
    if x == 1:
        break
    if x % k == 0:
        x //= k
        # print(x)
    else:
        x -= 1
        # print(x)
    count += 1

print(count)
    