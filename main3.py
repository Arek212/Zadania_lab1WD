import random
# Zadanie1
# a = [1-x for x in range(1,10)]
# print(a)
# b = [4 ** x for x in range(8)]
# print(b)
# c = [x for x in b if x % 2 == 0]
# print(c)

# Zadanie2
# a = [random.randrange(1, 100) for x in range(10)]
# b = [x for x in a if x % 2 == 0]
# print(b)

# Zadanie3
# produkty = {'mleko' : 'l','jajka' : 'sztuki', 'batony' : 'sztuki', 'banany' : 'kg'}
# sztk = [x for x, value in produkty.items() if value.count("sztuki")]
# print(sztk)

# Zadanie4
# def pitagoras(a,b,c):
#     if a**2 + b**2 == c**2:
#         print("Trójkąt jest prostokątny")
#     else:
#         print("Trójkąt nie jest prostokątny")
# pitagoras(6,8,10)
# pitagoras(3,3,3)

# Zadanie5
# def ptrapez(a = 3, b = 4, h = 5):
#     p = ((a + b) * h) / 2
#     return p
# print(ptrapez())

# Zadanie6
# def ciag(a = 1, b = 4, ile = 10):
#     for x in range(ile):
#         a*=b
#     return a
# print(ciag())

# Zadanie 7
# def ciag(* a):
#     b = a[0]
#     for x in a:
#         b*=x
#     return b
# print(ciag(1,2,3,4))