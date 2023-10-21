def gen_fibanoci(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a, b = b, a + b
    return output


for num in gen_fibanoci(10):
    print(num)


# YIELD KEYWORD
print("\n YIELD")


def gencubes(n):
    for num in range(n):
        yield num**3


for x in gencubes(10):
    print(x)
