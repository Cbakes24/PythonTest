



def parse(romNum):
    romNumList= ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
    i = 0
    for i in range(len(romNumList)):
        if romNum == romNumList[i]:
            return i + 1
        i += 1
    else:
        return 'This number is not in the list'





    # if (romNum) == 'I':
    #     return 1
    # elif (romNum) == 'II':
    #     return 2
    # elif (romNum) == 'III':
    #     return 3
    # elif (romNum) == 'IV':
    #     return 4
    # elif (romNum) == 'V':
    #     return 5
    # elif (romNum) == 'VI':
    #     return 6
    # elif (romNum) == 'VII':
    #     return 7
    # elif (romNum) == 'VIII':
    #     return 8
