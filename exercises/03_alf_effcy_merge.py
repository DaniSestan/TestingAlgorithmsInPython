# TODO: open and read from data file containing ~1000000 unsorted integers ranging from 1-1000000

count = 0


def merge_sort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list) // 2
        left_half = sort_list[:mid]
        right_half = sort_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sort_list[k] = left_half[i]
                i = i + 1
            else:
                sort_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            sort_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            sort_list[k] = right_half[j]
            j = j + 1
            k = k + 1

    global count
    count += 1
    if len(sort_list) == len(lst):
        print("Sorted: ", sort_list)
        print("Number of comparisons: ", count)