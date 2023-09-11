def product_except_self(arr):
    array_hash = {}
    result = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if arr[i] != arr[j]:
                product *= arr[j]
        result.append(product)

    return result
                

    # pass


if __name__ == "__main__":
    arr = [2, 3, 4, 5]
    res = product_except_self(arr)
    print(res)
