def find(l):

    f = l[0]
    for ele in l[1:]:
        f = f^ele
    return f

print(find([4,1,2,1,2]))