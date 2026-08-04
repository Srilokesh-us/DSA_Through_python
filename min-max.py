#Find both maximum and minimum in one traversal
def main():
    arr = [10, 20, 30, 40, 50]

    minimum = arr[0]
    maximum = arr[0]

    for i in range(len(arr)):
        if minimum > arr[i]:
            minimum = arr[i]

        if maximum < arr[i]:
            maximum = arr[i]

    print(f"Maximum and minimum elements are {maximum}, {minimum}")


main()
