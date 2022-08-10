liste = [[1, 2], [3, 4], [5, 6, 7]]

def döndür(x):

    liste.reverse()

    for i in liste:
        i.reverse()


    return x

döndür(liste)
print(liste)