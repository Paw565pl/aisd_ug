from random import randint
from sys import setrecursionlimit
from timeit import default_timer as timer


def insertionSort(A):
    n = len(A)
    for j in range(1, n):
        pom = A[j]
        i = j - 1
        while i >= 0 and A[i] > pom:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = pom


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    if i < r:
        return i
    else:
        return i - 1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q)
        quickSort(A, q + 1, r)
    return A


def betterQuickSort(A, c):
    def quickSort(A, p, r, c):
        if p < r and c < r - p + 1:
            q = partition(A, p, r)
            quickSort(A, p, q, c)
            quickSort(A, q + 1, r, c)
        return A

    almostSorted = quickSort(A, 0, len(A) - 1, c)
    insertionSort(almostSorted)

    return A


def dane_losowe():
    print("Dane losowe")
    for n in nn:
        arr1 = [randint(1, n) for _ in range(n)]
        arr2 = arr1.copy()

        start1 = timer()
        quickSort(arr1, 0, len(arr1) - 1)
        stop1 = timer()

        time1 = stop1 - start1

        start2 = timer()
        betterQuickSort(arr2, 10)
        stop2 = timer()

        time2 = stop2 - start2

        print("quickSort", n, time1, " | ", "betterQuickSort", n, time2)


def dane_niekorzystne():
    print("Dane niekorzystne")
    for n in nn:
        arr1 = [x for x in range(n)]
        arr2 = arr1.copy()

        start1 = timer()
        quickSort(arr1, 0, len(arr1) - 1)
        stop1 = timer()

        time1 = stop1 - start1

        start2 = timer()
        betterQuickSort(arr2, 10)
        stop2 = timer()

        time2 = stop2 - start2

        print("quickSort", n, time1, " | ", "betterQuickSort", n, time2)


setrecursionlimit(1000000000)

nn = [1000, 5000, 10000, 15000]

dane_losowe()
print("")
dane_niekorzystne()

# zadanie 3.4

# Dane losowe
# quickSort 1000 0.001679699998931028  |  betterQuickSort 1000 0.0013226000010035932
# quickSort 5000 0.009902100006002001  |  betterQuickSort 5000 0.00807110000459943
# quickSort 10000 0.023759999996400438  |  betterQuickSort 10000 0.020386599993798882
# quickSort 15000 0.03172189999895636  |  betterQuickSort 15000 0.02650740000535734

# Dane niekorzystne
# quickSort 1000 0.039884099998744205  |  betterQuickSort 1000 0.039559700002428144
# quickSort 5000 1.0339317000034498  |  betterQuickSort 5000 1.0304617000074359
# quickSort 10000 4.12447599999723  |  betterQuickSort 10000 4.180870000011055
# quickSort 15000 9.263683299999684  |  betterQuickSort 15000 9.429881999996724
