# Quick Sort method with Lomuto partition scheme
# and median of three, or random pivot selection

import random

def partitionMed(vector,low,high):
    # Get the mid lenght of vector
    #
    mid = round((low+high)/2)

    # Compares elements and sort ascending
    #
    if vector[mid] < vector[low]:
        vector[mid],vector[low] = vector[low],vector[mid]

    
    if vector[high] < vector[low]:
        vector[high],vector[low] = vector[low],vector[high]


    if vector[mid] < vector[high]:
        vector[high],vector[mid] = vector[mid],vector[high]


    return vector[high]


def partitionRand(vector,low,high):
    
    # Uses random function to get index for pivot
    num = random.randint(low,high)

    # Swap pivot and high
    #
    vector[num],vector[high] = vector[high],vector[num]


    return vector[high]


def partitionLomuto(type_pivot,arr, low, high): 
    if type_pivot.lower() == 'median': 
        pivot = partitionMed(arr,low,high)

    if type_pivot.lower() == 'random': 
        pivot = partitionRand(arr,low,high)
      
    # Lomuto scheme for partition
    # if array[j] is smaller than pivot, swap in the beggining of the vector
    # counting i+1 to increment position
    #
    i = (low - 1) 
    for j in range(low, high): 
        if (arr[j] <= pivot): 
            i += 1 
            arr[i], arr[j] = arr[j], arr[i] 

    # Swap pivot and the greatest value, so the last is sorted
    #
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return new position of pivot
    return (i + 1)
      

def quickSortLomuto(type_pivot,arr, low, high): 
    if (low < high): 
          
        pi = partitionLomuto(type_pivot,arr, low, high) 
        
        print('Array State: ',vector)

        quickSortLomuto(type_pivot,arr, low, pi - 1)

        quickSortLomuto(type_pivot,arr, pi + 1, high)


if __name__ == "__main__":
    vector = [16,14,12,1,8,4,9,6,15,13,11,2,7,3,10,5]
    print('QuickSort Lomuto with median of three pivot:\n')
    quickSortLomuto('median',vector,0,len(vector)-1)

    
    vector = [16,14,12,1,8,4,9,6,15,13,11,2,7,3,10,5]
    print('\n\nQuickSort Lomuto with random pivot:\n')
    quickSortLomuto('random',vector,0,len(vector)-1)