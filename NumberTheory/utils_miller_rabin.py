def function(n):
    num = n - 1
    values = []
    for k in range(1, num):
        val = num // pow(2, k)
        mod_val = num % pow(2, k)
        values.append((val, k))
        if mod_val != 0:
            return values


if __name__ == "__main__":
    n = int(input("Enter the number "))
    m = function(n)[-2][0]
    k = function(n)[-2][1]
    print(function(n))
    print(m, k)
