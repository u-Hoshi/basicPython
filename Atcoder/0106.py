# abc 233
# A
X, Y = map(int, input().split())
tmp = (Y - X) // 10
if (Y - X) % 10 != 0:
    tmp += 1
if tmp < 0:
    tmp = 0
print(tmp)

# B
l, r = map(int, input().split())
l = l - 1
s = list(input())

s[l:r] = s[l:r][::-1]
print(*s, sep="")
