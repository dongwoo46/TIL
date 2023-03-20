import sys
sys.stdin = open('input', 'r')

s = input()
end = len(s) - 1
for start in range(len(s) // 2):
    if end >= len(s) // 2 and s[start] == s[end]:
        end -= 1
        continue
    else:
        print(0)
        break
else:
    print(1)
