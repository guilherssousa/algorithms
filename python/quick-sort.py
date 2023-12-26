import time

from utils import generate_random_array


def qs(list, lo, hi):
    if lo >= hi:
        return

    partitionIndex = partition(list, lo, hi)

    qs(list, lo, partitionIndex - 1)
    qs(list, partitionIndex + 1, hi)


def partition(list, lo, hi):
    pivot = list[hi]

    index = lo - 1

    for i in range(lo, hi):
        if list[i] <= pivot:
            index += 1
            tmp = list[i]
            list[i] = list[index]
            list[index] = tmp

    index += 1
    list[hi] = list[index]
    list[index] = pivot

    return index


def quick_sort(list):
    qs(list, 0, len(list) - 1)


def main():
    sample_array = generate_random_array(100_000_0)
    # keep track of running time
    start = time.time()
    quick_sort(sample_array)
    end = time.time()

    print("Elapsed time:", end - start)


main()
