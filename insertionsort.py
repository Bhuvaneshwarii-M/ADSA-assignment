def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Input array
arr = [5, 2, 9, 1, 5, 6]

# Apply Insertion Sort
insertion_sort(arr)

# Output the sorted array
print(arr)

"""
Time Complexity:

1)Best-case time complexity: O(n) when the input array is already sorted.
2)Average-case time complexity: O(n^2) where n is the number of elements in the array.
3)Worst-case time complexity: O(n^2) when the input array is in reverse order.

Stability:

Insertion Sort is a stable sorting algorithm. This means that it maintains the relative order of equal elements in the sorted output as they were in the original input.

Performance on Different Input Data:

Best-case: Insertion Sort performs well when the input is nearly sorted because it has a linear time complexity in this case.
Worst-case: It performs poorly on large, unsorted datasets due to its quadratic time complexity.
Insertion Sort can be practical for small datasets or when the input is already partially sorted.

Merge Sort:

Best-case, Average-case, and Worst-case time complexity: O(n log n).
Merge Sort is not influenced by the initial order of elements and performs consistently well on all types of input data.
It is more efficient than Insertion Sort for larger datasets.

"""
