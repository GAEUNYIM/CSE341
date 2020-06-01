def div(x, y):
    yield int(x / y)


def three(x):
    return 3


if __name__ == "__main__":
    print(next(div(4, 2)))
    print(three(div(1, 0)))
