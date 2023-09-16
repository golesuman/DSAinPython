def topKFrequent(nums, k):
    count_dict = {}
    for element in nums:
        count_dict[element] = count_dict.get(element, 0) + 1

    result = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    return [key for key, value in result[:k]]


if __name__ == "__main__":
    t = topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5], 4)
    print(t)
