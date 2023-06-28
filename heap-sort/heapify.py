def heapify(A, heapSize, i):
    for _ in range(heapSize):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < heapSize and A[left] > A[largest]:
            largest = left
        else:
            largest = i

        if right < heapSize and A[right] > A[largest]:
            largest = right

        A[i], A[largest] = A[largest], A[i]
        i = largest

    return A


def buildHeap(A):
    heapSize = len(A)
    k = int((len(A) - 2) / 2)

    for i in range(k, -1, -1):
        heapify(A, heapSize, i)

    return A


def heapSort(A):
    A = buildHeap(A)
    heapSize = len(A)

    for i in range(len(A) - 1, 0, -1):
        A[0], A[heapSize - 1] = A[heapSize - 1], A[0]
        heapSize -= 1
        heapify(A, heapSize, 0)

    return A


inputFile = open("./input.txt", "r")

if not inputFile.readable():
    print("ERROR")
    exit()
else:
    dataList = []
    for line in inputFile.readlines():
        dataList.append(int(line.replace("\n", "")))
    inputFile.close()

sorted_dataList = heapSort(dataList)

outputFile = open("./output.txt", "w")
for item in sorted_dataList:
    outputFile.write(f"{item}\n")
outputFile.close()
