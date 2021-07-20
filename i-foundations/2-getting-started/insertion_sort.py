'''2.1-1 Illustrate the opetation of Insertion Sort on the array [31,41,59,26,41,58]'''

def insertion_sort(arr):
    for j in range(1, len(arr)):  # starting with second index in array
        key = arr[j]
        i = j - 1

        # Insert arr[j] into sorted sequence arr[0..j-1]
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]   # move arr[i] value one space to the right
            i -= 1  # repeat while arr[j] < preceeding values

        arr[i+1] = key  # insert arr[j] in position

    return arr

print(insertion_sort([31,41,59,26,41,58]))


'''2.1-2 Rewrite the Insertion Sort procedure to sort into non-increasing instead of non-decreasing order'''

def insertion_sort_downward(arr):
    for j in range(1, len(arr)):  # starting with second index in array
        key = arr[j]
        i = j - 1

        # Insert arr[j] into sorted sequence arr[0..j-1]
        while i >= 0 and arr[i] < key:
            arr[i+1] = arr[i]   # move arr[i] value one space to the right
            i -= 1  # repeat while arr[j] < preceeding values

        arr[i+1] = key  # insert arr[j] in position

    return arr

print(insertion_sort_downward([31,41,59,26,41,58]))