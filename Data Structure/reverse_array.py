def reverse1(arr : list):
    n = len(arr)

    for i in range(0, int((n-1)/2)):
        # swap(i, n-1-i, arr)
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]

if __name__ == "__main__":
    arr = [453, 345, 75, 948, 43, 865, 87, 9865, 547, 88429, 309727, 65, 85, 498, 7, 23]
    
    reverse1(arr)

    print(arr)
