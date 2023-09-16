def longest_consecutive_sequence(array):
    # array = sorted(array)
    current_count = 1
    max_count = 1
    for i in range(len(array) - 1):
        current_element = array[i]
        next_element = array[i + 1]
        if (next_element - current_element) == 1:
            current_count += 1
            max_count = max(current_count, max_count)
        else:
            current_count = 1
    return max_count


if __name__ == "__main__":
    print(longest_consecutive_sequence([1, 2, 5, 10, 5, 6, 7, 8, 9, 11]))
