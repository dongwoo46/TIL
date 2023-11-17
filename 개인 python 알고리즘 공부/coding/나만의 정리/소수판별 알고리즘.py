import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2,int(math.sqrt(x))+1):
        # x가 해당 수로 나눠떨어진다면
        if x%i == 0:
            return False # 소수가아님
    return True # 소수임

