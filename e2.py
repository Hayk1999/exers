# ######ONE####

# def get_val_len(md):
#     mdict = {len(value): value for value in md.values()}
#     print(mdict)

# colors = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
# print(get_val_len(colors))


# ######TWO######

# def get_min_max(md):
#     values = list(md.values())
#     print(max(values))
#     print(min(values))

# nums = {'hundred':100, 'thousand':1000, 'eight' :8}
# print(get_min_max(nums))


# ######THREE######

# import random

# def get_rand_item(ml):
#     mlist = random.choice(ml)
#     print(mlist)

# print(get_rand_item(['cwev', 'wvwvv', 'brebd']))


# ######FOUR#########

# def get_diff(ml, ml1):
#     cl1tocl2 = []
#     cl2tocl1 = []
#     for el in ml:
#         if el not in ml1:
#             cl1tocl2.append(el)
#         print(cl1tocl2)
#     for el in ml1:
#         if el not in ml:
#             cl2tocl1.append(el)
#         print(cl2tocl1)

# col_dict1 = ["red", "orange", "green", "blue", "white"]
# col_dict2 = ["black", "yellow", "green", "blue"]

# print(get_diff(col_dict1, col_dict2))


# ########FIVE##########
# ########Six###########

# ########SEVEN#########

# def get_unique(ml):



nl1 =[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
nl2 = [2, 4, 6, 8, 10, 12, 14]
print(get_unique(nl1))
print(get_unique(nl2))
