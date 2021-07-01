# C207 B問題
if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
 
    if b >= c * d:
        print(-1)
 
    else:
        blue = a
        red = 0
        cnt = 0
 
        while blue > red * d:
            blue += b
            red += c
            cnt += 1
 
        print(cnt)