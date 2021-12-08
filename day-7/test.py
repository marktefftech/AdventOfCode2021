from collections import Counter

secret = '123'

secret = list(map(int,secret))

secret = Counter(secret)
print(secret)