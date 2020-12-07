# Radix Sort method using MSD to sort
# is useful to order  alphabetically
#
# In this example i will use entry generic .txt files to sort
# and in the main function will have a vector with some inputs too,
# to exemplify the non-external input mode.
#
# The objective is to make the method witout any external library or
# function to help. 
# e.g. create an sorted array with unique elements:
# in the method we use a for loop, but
# you can use x = list(set(...))
#

import os

filepath = os.path.dirname(os.path.abspath(__file__))


# Method that gathers the input file and appends its lines to an array
#
def getInput(name):
    entry = open(filepath+'\\'+name+'.txt','r')

    lines = []
    for line in entry:
        lines.append(line)
    
    return lines
    

# Method that gathers all words from file
#
def getWords():
    lines = getInput('filename')

    words = []

    for i in range(len(lines)):
        words.append(lines[i].split())

    return words


# Sorting method with MSD
#
def MSD_radixSort(L, i):

    if len(L) <= 1:
        return L

    done_bucket = []
    buckets = [ [] for x in range(26) ]

    # Compares each char and orders it
    # 
    for s in L:
        if i >= len(s):
            done_bucket.append(s)
        else:
            index = ord(s[i].lower()) - ord('a')
            buckets[index].append(s)

    # Gather all ordered words by recursion
    #
    buckets = [ MSD_radixSort(b, i + 1) for b in buckets ]

    return done_bucket + [ b for blist in buckets for b in blist ]


# Method that writes the output file cointaining
# the ordered words
#
def outputFile(dic,val):
    if val == True:
        with open(filepath+'(\\ or \)filename','w') as file:
            for line in dic:
                file.write(line+'\n')
        file.close()


# Method that writes the output file containing
# the count of each unique word occurrency
#
def outputFilePeriods(dic,count):
    with open(filepath+'(\\ or \)filename','w') as file:
        for i in range(len(dic)):
            for j in range(len(dic[i])):
                file.write(dic[i][j]+' '+str(count[i])+'\n')
    file.close()

    return file


# Method that counts each word occurrency
#
def periodWords():
    words = getWords()

    count = []

    aux = 1

    # If next word is different, append aux value
    # to the position of each unique word in array
    #
    for j in range(len(words)-1):
        if j == (len(words)-2):
            if words[j] == words[j+1]:
                aux += 1
                count.append(aux)
            else:
                count.append(aux)
                aux = 1
                count.append(aux)
        else:
            if words[j] == words[j+1]:
                aux += 1
            else:
                count.append(aux)
                aux = 1

    aux = 1

    words_final = []

    # Filters the unique words to send it to the output file
    #
    for word in words: 
        if word not in words_final: 
            words_final.append(word)


    outputFilePeriods(words_final,count)


if __name__ == "__main__":
    words = getWords()

    for i in range(len(words)):
        dic = MSD_radixSort(words[i],0)
        outputFile(dic,True)