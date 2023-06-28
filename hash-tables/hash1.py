def strong_hash(arg):
    output = 0
    for i in arg:
        output += 137 * ord(i)
    return output


def weak_hash(arg):
    return ord(arg[0])


def my_hash(func, list):
    return func % len(list)


def count_empty_lists(list):
    count = 0
    for i in list:
        if i == []:
            count += 1
    return count


def longest(list):
    max = 0
    for i in list:
        if len(i) > max:
            max = len(i)
    return max


def avg_len_nonempty_lists(list):
    no_empty_lists = [len(el) for el in list if el != []]
    return round(sum(no_empty_lists) / len(no_empty_lists), 3)


with open("3700.txt", "r") as file:
    data = file.read().split("\n")


# 17


def W17():
    T17 = [[] for _ in range(17)]

    for i in range(2 * len(T17)):
        T17[my_hash(hash(data[i]), T17)].append(data[i])

    print("W17")
    print("Ilość pustych list:", count_empty_lists(T17))
    print("Max długość listy:", longest(T17))
    print("Średnia długość listy:", avg_len_nonempty_lists(T17))
    print("")


def D17():
    T17 = [[] for _ in range(17)]

    for i in range(2 * len(T17)):
        T17[my_hash(strong_hash(data[i]), T17)].append(data[i])

    print("D17")
    print("Ilość pustych list:", count_empty_lists(T17))
    print("Max długość listy:", longest(T17))
    print("Średnia długość listy:", avg_len_nonempty_lists(T17))
    print("")


def S17():
    T17 = [[] for _ in range(17)]

    for i in range(2 * len(T17)):
        T17[my_hash(weak_hash(data[i]), T17)].append(data[i])

    print("S17")
    print("Ilość pustych list:", count_empty_lists(T17))
    print("Max długość listy:", longest(T17))
    print("Średnia długość listy:", avg_len_nonempty_lists(T17))
    print("")


# 103031


def W1031():
    T1031 = [[] for _ in range(1031)]

    for i in range(2 * len(T1031)):
        T1031[my_hash(hash(data[i]), T1031)].append(data[i])

    print("W1031")
    print("Ilość pustych list:", count_empty_lists(T1031))
    print("Max długość listy:", longest(T1031))
    print("Średnia długość listy:", avg_len_nonempty_lists(T1031))
    print("")


def D1031():
    T1031 = [[] for _ in range(1031)]

    for i in range(2 * len(T1031)):
        T1031[my_hash(strong_hash(data[i]), T1031)].append(data[i])

    print("D1031")
    print("Ilość pustych list:", count_empty_lists(T1031))
    print("Max długość listy:", longest(T1031))
    print("Średnia długość listy:", avg_len_nonempty_lists(T1031))
    print("")


def S1031():
    T1031 = [[] for _ in range(1031)]

    for i in range(2 * len(T1031)):
        T1031[my_hash(weak_hash(data[i]), T1031)].append(data[i])

    print("S1031")
    print("Ilość pustych list:", count_empty_lists(T1031))
    print("Max długość listy:", longest(T1031))
    print("Średnia długość listy:", avg_len_nonempty_lists(T1031))
    print("")


# 1024


def W1024():
    T1024 = [[] for _ in range(1024)]

    for i in range(2 * len(T1024)):
        T1024[my_hash(hash(data[i]), T1024)].append(data[i])

    print("W1024")
    print("Ilość pustych list:", count_empty_lists(T1024))
    print("Max długość listy:", longest(T1024))
    print("Średnia długość listy:", avg_len_nonempty_lists(T1024))
    print("")


def D1024():
    T1024 = [[] for _ in range(1024)]

    for i in range(2 * len(T1024)):
        T1024[my_hash(strong_hash(data[i]), T1024)].append(data[i])

    print("D1024")
    print("Ilość pustych list:", count_empty_lists(T1024))
    print("Max długość listy:", longest(T1024))
    print("Średnia długość listy:", avg_len_nonempty_lists(T1024))
    print("")


def S1024():
    T1024 = [[] for _ in range(1024)]

    for i in range(2 * len(T1024)):
        T1024[my_hash(weak_hash(data[i]), T1024)].append(data[i])

    print("S1024")
    print("Ilość pustych list:", count_empty_lists(T1024))
    print("Max długość listy:", longest(T1024))
    print("Średnia długość listy:", avg_len_nonempty_lists(T1024))
    print("")


W17()
D17()
S17()
print("---------------------------------------")
W1031()
D1031()
S1031()
print("---------------------------------------")
W1024()
D1024()
S1024()

# W17
# Ilość pustych list: 1
# Max długość listy: 5
# Średnia długość listy: 2.125
#
# D17
# Ilość pustych list: 1
# Max długość listy: 4
# Średnia długość listy: 2.125
#
# S17
# Ilość pustych list: 2
# Max długość listy: 5
# Średnia długość listy: 2.267
#
# ---------------------------------------
# W1031
# Ilość pustych list: 134
# Max długość listy: 8
# Średnia długość listy: 2.299
#
# D1031
# Ilość pustych list: 325
# Max długość listy: 13
# Średnia długość listy: 2.921
#
# S1031
# Ilość pustych list: 981
# Max długość listy: 183
# Średnia długość listy: 41.24
#
# ---------------------------------------
# W1024
# Ilość pustych list: 138
# Max długość listy: 7
# Średnia długość listy: 2.312
#
# D1024
# Ilość pustych list: 325
# Max długość listy: 13
# Średnia długość listy: 2.93
#
# S1024
# Ilość pustych list: 974
# Max długość listy: 183
# Średnia długość listy: 40.96

# lepsze wyniki daje rozmiar 1031
# Tak
