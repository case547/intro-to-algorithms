def insertion_sort(arr):
    for j in range(1, len(arr)):  # starting with second index in array
        key = arr[j]
        i = j - 1

        # Insert arr[j] into sorted sequence arr[0..j-1]
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]   # copy arr[i] value one space to the right
            i -= 1  # repeat while key < preceeding values

        arr[i+1] = key  # place key in position

    return arr