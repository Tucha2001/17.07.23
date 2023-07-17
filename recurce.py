# def main(n: int):
#     print(n)
#     if n == 1:
#         return 1
#     return main(n - 1)

# print(main(5))


# s = '13' # 1 + 3 = 4

# s = '256'  # 2 + 5 + 6 = 13 -> 1 + 3 = 4 

# def main(s: str):
#     if len(s) == 1:
#         return int(s)
#     return main(str(sum(map(int, s))))

# print(main('256'))



# def factorial(n: int):
#     print(n)
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(3))
# # print(factorial(10))




# a = [[[[[[[1,3,[[[[[[[[[4,[[[[[[[[5]]]]]]]],4]]]]]]]],7]]]]],8]]]

# new = []

# def rec(a):
#     for i in a:
#         if type(i) == int:
#             new.append(i)
#         else:
#             rec(i)

# rec(a)

# print(new)
# new = []

# for i in a:
#     if type(i) == int:
#         new.append(i)
#     else:
#         for j in i:
#             if type(j) == int:
#                 new.append(j)
#             else:
#                 for k in j:
#                     if type(k) == int:
#                         new.append(k)
#                     else:
#                         for l in k:
#                             if type(l) == int:
#                                 new.append(l)
#                             else:
#                                 for m in l:
#                                     if type(m) == int:
#                                         new.append(m)
#                                     else:
#                                         for n in m:
#                                             if type(n) == int:
#                                                 new.append(n)

# print(new)


# print(a[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0])

# while a != 5:
#     a = a[0]
#     print(a)

# def rec(a):
#     if a == 5:
#         return 5
#     return rec(a[0])

# print(rec(a))