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


def partitionHoare(type_pivot,arr,low,high):
    if type_pivot.lower() == 'median': 
       pivot = partitionMed(arr,low,high)

    if type_pivot.lower() == 'random': 
        pivot = partitionRand(arr,low,high)

    # Smallest index
    #
    i = low - 1

    for j in range(low, high):
         
        # If current element is smaller than or
        # equal to pivot, swap
        #
        if (arr[j] <= pivot):
            
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the high and the actual pivot
    # that is an element biggest than the pivot
    #
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return (i + 1)
     

      
def quickSortHoare(type_pivot,arr, low, high):
    if (low < high):      
        pi = partitionHoare(type_pivot,arr, low, high)

        print('Array State: ',vector)
        
        quickSortHoare(type_pivot,arr, low, pi-1)

        quickSortHoare(type_pivot,arr, pi + 1, high)


if __name__ == "__main__":
    vector = [16,14,12,1,8,4,9,6,15,13,11,2,7,3,10,5]
    print('QuickSort Lomuto with median of three pivot:\n')
    quickSortHoare('median',vector,0,len(vector)-1)

    
    vector = [16,14,12,1,8,4,9,6,15,13,11,2,7,3,10,5]
    print('\n\nQuickSort Lomuto with random pivot:\n')
    quickSortHoare('random',vector,0,len(vector)-1)