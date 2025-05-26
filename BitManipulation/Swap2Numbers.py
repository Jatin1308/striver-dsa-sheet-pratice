def swap2Numbers(a,b):
    # print(a,b)
    # temp = a
    # a = b
    # b = temp
    # temp = b
    # print(a,b)

    """ instead of using third variable we can use XOR """
    a = a^b
    b = a^b
    a = a^b
    print(a,b)


swap2Numbers(5,6)