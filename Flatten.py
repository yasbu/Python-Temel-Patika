liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_liste = []

def flatten(x):
    for i in x:
        if isinstance(i, list):
            flatten(i)
        else:
                new_liste.append(i)
flatten(liste)
print(new_liste)