def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements_part, start, end):
    pivot_index = start
    pivot = elements_part[pivot_index]
    start = pivot_index + 1

    while start < end:
        while start < len(elements_part) and elements_part[start] <= pivot:
            start += 1
        while elements_part[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, elements_part)
    swap(pivot_index, end, elements_part)
    return end


def quick_sort(elements_, start, end):
    if start < end:
        pi = partition(elements_, start, end)
        quick_sort(elements_, start, pi - 1)
        quick_sort(elements_, pi + 1, end)


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, end=len(elements) - 1)
    print(elements)
