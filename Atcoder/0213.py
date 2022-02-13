# 236
# A
S = list(input())
a, b = map(int, input().split())

word_a = S[a - 1]
word_b = S[b - 1]

S[a - 1] = word_b
S[b - 1] = word_a

print("".join(S))

# B
N = int(input())
A = [int(x) for x in input().split()]

xs = [0] * (N + 1)

for a in A:
    xs[a] += 1

result = 0

for i, x in enumerate(xs):
    if x == 3:
        result = i
        break
