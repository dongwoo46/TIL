def solution(nums):
    answer = 0
    pick = len(nums) // 2
    species = len(set(nums))
    if pick <= species:
        answer = pick
    elif species <= pick:
        answer = species
    print(pick)
    print(species)

    return answer