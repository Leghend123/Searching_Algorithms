#implementing the linear search-----------

#function for linear search
def linear_search(arr,Length,x):
   
    #tranvese through the array
    for i in range(0,Length):
        if (arr[i] == x):
            return i
    return -1

if __name__ == "__main__":
    print("Enter the array")
    arr = list(map(int,input().split()))
    length = len(arr)
    x =int(input("enter the key"))
    result = linear_search(arr,length,x)

    if (result == -1):
        print("the element id not in the array")
    else:
        print("the element is at the index", result)
