word = input()
first = ''
second = ''
third = ''
fourth = ''
fifth = ''
if len(word) == 1:
    first = '..#..'
    second = '.#.#.'
    third = '#.' + word + '.#'
    fourth = '.#.#.'
    fifth = '..#..'
print(first)
print(second)
print(third)
print(fourth)
print(fifth)