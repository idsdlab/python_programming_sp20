# function annotation : https://bluese05.tistory.com/78
# https://www.python.org/dev/peps/pep-3107/
# https://wikidocs.net/16053
# https://53perc.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%86%8C%EC%88%98-%ED%8C%90%EB%B3%84%ED%95%98%EA%B8%B0


def is_prime_bad(n : int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i is 0:
            return False

    return True

print(len([x for x in range(1, 100000) if is_prime_bad(x)]))

