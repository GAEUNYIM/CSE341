def A(I, P):

    def B():
        print(I)

    if I > 1:
        P()
    else:
        A(2, B)


def C():
    pass


if __name__ == "__main__":
    A(1, C)
