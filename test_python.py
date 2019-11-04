import math
err='Косяк'
assert round(math.pi, 2) == 3.14, err
# assert round(math.pi, 2) == 5.14, err

assert math.sqrt(4) == 2, err
# assert math.sqrt(4) == 2, err

assert math.pow(2,2) == 4, err
# assert math.pow(2,2) == 4, err

assert math.hypot(3,4) == 5, err
# assert math.hypot(3,4) == 5, err

a=(6,4,7,9,3)

assert sorted(a) == [3, 4, 6, 7, 9], err
# assert sorted(a) == [3, 4, 456456456, 7, 9], err
assert list(map(lambda x: x**2, a)) == [36, 16, 49, 81, 9], err
# assert list(map(lambda x: x**2, a)) == [36, 16, 44444444, 81, 9], err
assert list(filter(lambda x: x>4, a)) == [6, 7, 9], err
# assert list(filter(lambda x: x>4, a)) == [6, 55555, 9], err

