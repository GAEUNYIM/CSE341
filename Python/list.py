def sum(x, n):
    sum = 0
    for i in range(n):
       sum += next(x)
    return sum

if __name__ == "__main__":
    gen = (x for x in range(1, 1000000000000000000000000000000000))
    print(gen)
    print(sum(gen, 3))
