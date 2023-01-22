class MergeSort:
    def merge_sort(self, arr):
        n = len(arr)
        if n == 1:
            return
        mid = n // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        self.merge_sort(left_arr)
        self.merge_sort(right_arr)

        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    def print_sorted_array(self, arr):
        print("Sorted array is %s" % arr)


if __name__ == "__main__":
    arr = [2, 3, 10, 7, 4, 11, 6]
    m1 = MergeSort()
    m1.merge_sort(arr)
    m1.print_sorted_array(arr)
