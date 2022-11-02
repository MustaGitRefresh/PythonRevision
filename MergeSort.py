def merge_two_sorted_lists(a_, b_):
    sorted_list = []
    len_a = len(a_)
    len_b = len(b)
    i, j = 0

    while i <= len_a and j <= len_b:
        if a[i] > b[j]:
            sorted_list.append(a[i])
    return sorted_list


if __name__ == '__main__':
    a = [5, 8, 12, 56]
    b = [7, 9, 45, 51]
    print(merge_two_sorted_lists(a, b))