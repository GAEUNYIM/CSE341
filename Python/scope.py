def A(I, P):

    def B(J):
        print('B: I = ' + str(I))
        print('B: J = ' + str(J))

    print('A: I = ' + str(I))
    if I > 2:
        P(I)
    else:
        A(I + 1, B)


def C():
    pass


if __name__ == "__main__":
    A(1, C)
