# ml = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# ml1 = []

# for i in range(len(ml)):
#     ml1.append([i] * ml.count(i))



def roman_to_decimal(num):
    md = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    number = 0
    for i in range(len(num)):
        if md[num[i]] > md[num[i-1]]:
            number += md[num[i]] - md[num[i - 1]]
        else:
            number += md[num[i]]
        print(number)    

roman_to_decimal('III')

