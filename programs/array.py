from array import array
arr = array('i', [10, 20, 30, 40])
arr.append(50)
print("After Append:", arr)
arr.insert(1, 15)
print("After Insert:", arr)
arr.remove(30)
print("After Remove:", arr)
print("Element at index 2:", arr[2])
arr[0] = 5
print("After Updating Index 0:", arr)
print("Length of Array:", len(arr))
