# Номер 1
# tuple1 = (1, 2, 3, 4, 5, 6, 7)
# tuple2 = (2, 12, 7, 4, 1, 98)
# tuple3 = (1, 98, 242, 4, 17, 24, 31, 7)
# tuple_list = []
#
# for i in tuple1:
#     if i in tuple2 and i in tuple3:
#         tuple_list.append(i)
#
# print(tuple(tuple_list))
from operator import index

# Номер 2
# tuple1 = (1, 2, 3, 4, 5, 6, 7)
# tuple2 = (2, 4, 7, 12, 1, 98)
# tuple3 = (4, 98, 242, 1, 17, 24, 31, 7)
# tuple_list1 = []
# tuple_list2 = []
# tuple_list3 = []
#
# for i in tuple1:
#     if i not in tuple2 and tuple3:
#         tuple_list1.append(i)
#
# for j in tuple2:
#     if j not in tuple1 and tuple3:
#         tuple_list2.append(j)
#
# for k in tuple3:
#     if k not in tuple1 and tuple2:
#         tuple_list3.append(k)
#
# print(tuple(tuple_list1))
# print(tuple(tuple_list2))
# print(tuple(tuple_list3))

# Номер 3
# tuple1 = (1, 2, 3, 4, 5, 6, 7)
# tuple2 = (2, 12, 7, 4, 1, 98)
# tuple3 = (1, 98, 242, 4, 17, 24, 31, 7)
# tuple_list = []
#
# min_length = min(len(tuple1), len(tuple2), len(tuple3))
#
# for i in range(min_length):
#     if tuple1[i] == tuple2[i] == tuple3[i]:
#        tuple_list.append(tuple1[i])
#
# print(tuple(tuple_list))
