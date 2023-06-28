def insert(data, size, procent, method):
    output_list = [[]] * size
    number_of_tries = 0
    for i in range(int(size * procent / 100)):
        success = False
        hash_result = 0
        j = 0
        for letter in data[i]["nazwisko"]:
            hash_result = hash_result * 331 + ord(letter)
        while not success:
            number_of_tries += 1
            index = method(hash_result, j, size)
            if not output_list[index]:
                output_list[index] = data[i]
                success = True
            else:
                j += 1
                if j == size:
                    break

    if size < 30:
        return f"{output_list}\nŚrednia ilość prób dla {method.__name__}: {round(number_of_tries / (size * procent / 100), 4)} przy {procent}% zapełnieniu."
    else:
        return f"Średnia ilość prób dla {method.__name__}: {round(number_of_tries / (size * procent / 100), 4)} przy {procent}% zapełnieniu."


def linear_hash(hash_result, j, m):
    return (hash_result + j) % m


def quadratic_hash(hash_result, j, m):
    return (hash_result + j * j) % m


def double_hash(hash_result, j, m):
    return (hash_result + j * (1 + (hash_result % (m - 2)))) % m


def print_hash_results(data, size):
    print(f"------------ ROZMIAR: {size} ------------")
    for percentage in [50, 70, 90]:
        for hash_method in [linear_hash, quadratic_hash, double_hash]:
            print(insert(data, size, percentage, hash_method))
        print("")


with open("nazwiskaASCII", "r") as f:
    surnames = [{"ilosc": line.split()[0], "nazwisko": line.split()[1]} for line in f]

print_hash_results(surnames, 19)
print_hash_results(surnames, 5503)
print_hash_results(surnames, 18869)

# ------------ ROZMIAR: 19 ------------
# [{'ilosc': '131940', 'nazwisko': 'Kowalski'}, {'ilosc': '92945', 'nazwisko': 'Dabrowski'}, [], [], [], {'ilosc': '89366', 'nazwisko': 'Lewandowski'}, [], [], [], {'ilosc': '87935', 'nazwisko': 'Kaminski'}, [], [], {'ilosc': '220217', 'nazwisko': 'Nowak'}, [], {'ilosc': '87690', 'nazwisko': 'Kowalczyk'}, {'ilosc': '104418', 'nazwisko': 'Wisniewski'}, {'ilosc': '85988', 'nazwisko': 'Zielinski'}, [], {'ilosc': '88932', 'nazwisko': 'Wojcik'}]
# Średnia ilość prób dla linear_hash: 1.0526 przy 50% zapełnieniu.
# [{'ilosc': '131940', 'nazwisko': 'Kowalski'}, {'ilosc': '92945', 'nazwisko': 'Dabrowski'}, [], [], [], {'ilosc': '89366', 'nazwisko': 'Lewandowski'}, [], [], [], {'ilosc': '87935', 'nazwisko': 'Kaminski'}, [], [], {'ilosc': '220217', 'nazwisko': 'Nowak'}, [], {'ilosc': '87690', 'nazwisko': 'Kowalczyk'}, {'ilosc': '104418', 'nazwisko': 'Wisniewski'}, {'ilosc': '85988', 'nazwisko': 'Zielinski'}, [], {'ilosc': '88932', 'nazwisko': 'Wojcik'}]
# Średnia ilość prób dla quadratic_hash: 1.0526 przy 50% zapełnieniu.
# [{'ilosc': '131940', 'nazwisko': 'Kowalski'}, [], [], [], [], {'ilosc': '89366', 'nazwisko': 'Lewandowski'}, [], [], [], {'ilosc': '87935', 'nazwisko': 'Kaminski'}, [], [], {'ilosc': '220217', 'nazwisko': 'Nowak'}, [], {'ilosc': '87690', 'nazwisko': 'Kowalczyk'}, {'ilosc': '104418', 'nazwisko': 'Wisniewski'}, {'ilosc': '85988', 'nazwisko': 'Zielinski'}, {'ilosc': '92945', 'nazwisko': 'Dabrowski'}, {'ilosc': '88932', 'nazwisko': 'Wojcik'}]
# Średnia ilość prób dla double_hash: 1.0526 przy 50% zapełnieniu.
#
# [{'ilosc': '131940', 'nazwisko': 'Kowalski'}, {'ilosc': '92945', 'nazwisko': 'Dabrowski'}, {'ilosc': '72368', 'nazwisko': 'Kozlowski'}, [], [], {'ilosc': '89366', 'nazwisko': 'Lewandowski'}, [], [], {'ilosc': '65942', 'nazwisko': 'Jankowski'}, {'ilosc': '87935', 'nazwisko': 'Kaminski'}, {'ilosc': '84527', 'nazwisko': 'Szymanski'}, [], {'ilosc': '220217', 'nazwisko': 'Nowak'}, {'ilosc': '81390', 'nazwisko': 'Wozniak'}, {'ilosc': '87690', 'nazwisko': 'Kowalczyk'}, {'ilosc': '104418', 'nazwisko': 'Wisniewski'}, {'ilosc': '85988', 'nazwisko': 'Zielinski'}, [], {'ilosc': '88932', 'nazwisko': 'Wojcik'}]
# Średnia ilość prób dla linear_hash: 1.3534 przy 70% zapełnieniu.
# [{'ilosc': '131940', 'nazwisko': 'Kowalski'}, {'ilosc': '92945', 'nazwisko': 'Dabrowski'}, [], {'ilosc': '72368', 'nazwisko': 'Kozlowski'}, [], {'ilosc': '89366', 'nazwisko': 'Lewandowski'}, [], [], {'ilosc': '65942', 'nazwisko': 'Jankowski'}, {'ilosc': '87935', 'nazwisko': 'Kaminski'}, {'ilosc': '84527', 'nazwisko': 'Szymanski'}, [], {'ilosc': '220217', 'nazwisko': 'Nowak'}, {'ilosc': '81390', 'nazwisko': 'Wozniak'}, {'ilosc': '87690', 'nazwisko': 'Kowalczyk'}, {'ilosc': '104418', 'nazwisko': 'Wisniewski'}, {'ilosc': '85988', 'nazwisko': 'Zielinski'}, [], {'ilosc': '88932', 'nazwisko': 'Wojcik'}]
# Średnia ilość prób dla quadratic_hash: 1.2782 przy 70% zapełnieniu.
# [{'ilosc': '131940', 'nazwisko': 'Kowalski'}, [], [], {'ilosc': '72368', 'nazwisko': 'Kozlowski'}, [], {'ilosc': '89366', 'nazwisko': 'Lewandowski'}, {'ilosc': '84527', 'nazwisko': 'Szymanski'}, [], {'ilosc': '65942', 'nazwisko': 'Jankowski'}, {'ilosc': '87935', 'nazwisko': 'Kaminski'}, [], [], {'ilosc': '220217', 'nazwisko': 'Nowak'}, {'ilosc': '81390', 'nazwisko': 'Wozniak'}, {'ilosc': '87690', 'nazwisko': 'Kowalczyk'}, {'ilosc': '104418', 'nazwisko': 'Wisniewski'}, {'ilosc': '85988', 'nazwisko': 'Zielinski'}, {'ilosc': '92945', 'nazwisko': 'Dabrowski'}, {'ilosc': '88932', 'nazwisko': 'Wojcik'}]
# Średnia ilość prób dla double_hash: 1.2782 przy 70% zapełnieniu.
#
# [{'ilosc': '131940', 'nazwisko': 'Kowalski'}, {'ilosc': '92945', 'nazwisko': 'Dabrowski'}, {'ilosc': '72368', 'nazwisko': 'Kozlowski'}, {'ilosc': '59403', 'nazwisko': 'Kaczmarek'}, {'ilosc': '59069', 'nazwisko': 'Mazur'}, {'ilosc': '89366', 'nazwisko': 'Lewandowski'}, {'ilosc': '62629', 'nazwisko': 'Kwiatkowski'}, [], {'ilosc': '65942', 'nazwisko': 'Jankowski'}, {'ilosc': '87935', 'nazwisko': 'Kaminski'}, {'ilosc': '84527', 'nazwisko': 'Szymanski'}, [], {'ilosc': '220217', 'nazwisko': 'Nowak'}, {'ilosc': '81390', 'nazwisko': 'Wozniak'}, {'ilosc': '87690', 'nazwisko': 'Kowalczyk'}, {'ilosc': '104418', 'nazwisko': 'Wisniewski'}, {'ilosc': '85988', 'nazwisko': 'Zielinski'}, {'ilosc': '63519', 'nazwisko': 'Wojciechowski'}, {'ilosc': '88932', 'nazwisko': 'Wojcik'}]
# Średnia ilość prób dla linear_hash: 2.1637 przy 90% zapełnieniu.
# [{'ilosc': '131940', 'nazwisko': 'Kowalski'}, {'ilosc': '92945', 'nazwisko': 'Dabrowski'}, {'ilosc': '59403', 'nazwisko': 'Kaczmarek'}, {'ilosc': '72368', 'nazwisko': 'Kozlowski'}, [], {'ilosc': '89366', 'nazwisko': 'Lewandowski'}, {'ilosc': '62629', 'nazwisko': 'Kwiatkowski'}, [], {'ilosc': '65942', 'nazwisko': 'Jankowski'}, {'ilosc': '87935', 'nazwisko': 'Kaminski'}, {'ilosc': '84527', 'nazwisko': 'Szymanski'}, {'ilosc': '59069', 'nazwisko': 'Mazur'}, {'ilosc': '220217', 'nazwisko': 'Nowak'}, {'ilosc': '81390', 'nazwisko': 'Wozniak'}, {'ilosc': '87690', 'nazwisko': 'Kowalczyk'}, {'ilosc': '104418', 'nazwisko': 'Wisniewski'}, {'ilosc': '85988', 'nazwisko': 'Zielinski'}, {'ilosc': '63519', 'nazwisko': 'Wojciechowski'}, {'ilosc': '88932', 'nazwisko': 'Wojcik'}]
# Średnia ilość prób dla quadratic_hash: 1.6959 przy 90% zapełnieniu.
# [{'ilosc': '131940', 'nazwisko': 'Kowalski'}, {'ilosc': '59069', 'nazwisko': 'Mazur'}, {'ilosc': '63519', 'nazwisko': 'Wojciechowski'}, {'ilosc': '72368', 'nazwisko': 'Kozlowski'}, [], {'ilosc': '89366', 'nazwisko': 'Lewandowski'}, {'ilosc': '84527', 'nazwisko': 'Szymanski'}, {'ilosc': '62629', 'nazwisko': 'Kwiatkowski'}, {'ilosc': '65942', 'nazwisko': 'Jankowski'}, {'ilosc': '87935', 'nazwisko': 'Kaminski'}, [], {'ilosc': '59403', 'nazwisko': 'Kaczmarek'}, {'ilosc': '220217', 'nazwisko': 'Nowak'}, {'ilosc': '81390', 'nazwisko': 'Wozniak'}, {'ilosc': '87690', 'nazwisko': 'Kowalczyk'}, {'ilosc': '104418', 'nazwisko': 'Wisniewski'}, {'ilosc': '85988', 'nazwisko': 'Zielinski'}, {'ilosc': '92945', 'nazwisko': 'Dabrowski'}, {'ilosc': '88932', 'nazwisko': 'Wojcik'}]
# Średnia ilość prób dla double_hash: 1.8129 przy 90% zapełnieniu.
#
# ------------ ROZMIAR: 5503 ------------
# Średnia ilość prób dla linear_hash: 1.5344 przy 50% zapełnieniu.
# Średnia ilość prób dla quadratic_hash: 1.4759 przy 50% zapełnieniu.
# Średnia ilość prób dla double_hash: 1.4029 przy 50% zapełnieniu.
