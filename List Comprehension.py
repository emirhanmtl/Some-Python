# Bir listeden başka bir liste oluşturmanın normal yöntemi

liste1 = [1,2,3,4,5]

liste2 = []

for i in liste1:

    liste2.append(i)

print(liste2)


#List Comprehension yöntemi

liste3 = [1,2,3,4,5]

liste4 = [i for i in liste3]

print(liste4)

