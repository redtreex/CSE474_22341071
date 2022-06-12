def make_square(tup):
    md = {}
    for i in range(tup[0], tup[1]+1):
        md[i] = i ** 2
    return md
print(make_square((5, 9)))
