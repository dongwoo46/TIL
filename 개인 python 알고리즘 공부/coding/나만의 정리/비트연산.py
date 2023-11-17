a = 10
b = '0b1010'
c = 7
print(f'{a:b}') #
#1010
print(f'{c:b}')
#111
print(f'{a:08b}') # a를 이진수로 찍되 8자리수로 만들어라 빈곳은 0으로 채운다.
#0001010
print(bin(a)) # a를 이진수로 만들어라
print(int(b,2)) # b를 이진수로 해석해라
print(f'{c:08b}')