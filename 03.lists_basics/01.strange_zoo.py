tail = str(input())
body = str(input())
head = str(input())

meerkat = [tail, body, head]

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)

# или:
# temp = meerkat[0]
# meerkat[0] = meerkat[2]
# meerkat[2]= temp

# или:
# meerkat = [head, body, tail]
# print(meerkat)

# или:
# meerkat = []
# meerkat.append(input())
# meerkat.append(input())
# meerkat.append(input())
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
#
# print(meerkat)