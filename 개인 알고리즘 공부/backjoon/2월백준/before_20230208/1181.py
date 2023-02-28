import sys
n = int(input())
word_list = []

for i in range(n):
    word_list.append(sys.stdin.readline().strip())
word_set = set(word_list)
word_list = list(word_set)
word_list.sort()
word_list.sort(key=len)
for word in word_list:
    print(word)


# n = int(input())
# words_list = []
# for i in range(n):
#     word = input()
#     words_list.append(word)
# a = set(words_list)
# b = list(a)
# for i in range(len(a)):
#     for j in range(0,len(a)-i-1):
#         if len(b[j])>len(b[j+1]):
#             b[j], b[j+1] = b[j+1], b[j]
#
# for word in b:
#     for numb in word:
#         if ord(numb)
