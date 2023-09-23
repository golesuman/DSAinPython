def max_area(heights):
    left = 0
    right = len(heights) - 1
    largest = 0
    result = 0

    while left < right:
        result = abs(right - left) * min(heights[left], heights[right])
        if result > largest:
            largest = result

        if heights[left] < heights[right]:
            left += 1
        else:
            right += 1

        # pass
    return largest

if __name__ == "__main__":
    heights = [5,1,3,4,6]
    print(max_area(heights))
