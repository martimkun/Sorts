# Shellsort method with printed list after each increment loop
#


def shellSort(vector,np):
    # np = steps vector
    # val = verificador de impressao referente à questao 1
    n = len(vector)
    for h in np:
        if h > 0:
            for i in range(h, n):
                c = vector[i]
                j = i
                while j >= h and c < vector[j - h]:
                    vector[j] = vector[j - h]
                    j = j - h
                    vector[j] = c
            print('After increments of size',h,'the list is',vector)


# Method that return the vector containing the steps to shellSort
#
# formula: SUM( vector size / 2^k ) till this division is greater than 1
#
def getNumPassos(vector):
    steps = []
    k = 1
    a = True
    while a:
        if (round(len(vector)/2**k)) >= 1 :
           steps.append(round(len(vector)/2**k))
           k += 1
        else:
            a = False
    return steps


if __name__ == "__main__":
    vec = [16,14,12,1,8,4,9,6,15,13,11,2,7,3,10,5]
    np = getNumPassos(vec)
    shellSort(vec,np)