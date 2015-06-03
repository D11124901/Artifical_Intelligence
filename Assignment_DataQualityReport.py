####################################################
#                                                  #
#              Artificial Intelligence             #                         
#                   Assignment 1                   #
#                Data Quality Report               #
#                                                  #
#                 Stephen O'Keeffe                 #
#                     D11124901                    #
####################################################


def main():
    import math
    import statistics
    from statistics import mode
    from statistics import StatisticsError
    
    # open csv files and write
    fCAT = open("data/d11124901CAT.csv", 'w')
    fCAT.close()
    fCONT = open("data/d11124901CONT.csv", 'w')
    fCONT.close()
    
    # list called feat    
    feat = list()
    
    # open txt file and replace new line 
    with open("data/featureNames.txt") as f:
        for line in f:
            stri = line.replace("\n", "");
            feat.append(stri)

    # list called pplList            
    pplList = list()

    # open txt file and remove comma in file, add person list to pplList
    with open("data/DataSet.txt") as f:
        for line in f:
            p = list()
            info = line.strip().split(',')
            for line in info:
                p.append(line)
            pplList.append(p)


    # categories 
    def cat(i):
        total = 0
        mean = 0
        count = 0
        count1 = 0
        notin = 0
        miss = 0
        card = 0
        modecount = 0
        secondmode = 0

    # cardinality, mode and second mode list
        cardList = list()
        modeList = list()
        secmodeList = list()
        
    # count all records and add to cardList, count again and add records to count1
    # but dont include records from the first count
        for list2 in pplList:
            if (list2[i] != ' ?'):
                cardList.append(list2[i])
                count = count + 1
                count1 = count - notin
            else:
                notin = notin + 1
                count = count + 1

    # create set for cardList and get length. miss, mode and second mode calc
        ca = set(cardList)
        card = len(ca)
        miss = (notin / count) * 100
        modes = mode(cardList)

        for list2 in pplList:
            if (list2[i] != modes):
                secmodeList.append(list2[i])

        modecount = cardList.count(modes)
        modeper = (modecount / count) * 100

        secondmode = mode(secmodeList)

        secmodecount = secmodeList.count(secondmode)
        secmodeper = (secmodecount / count) * 100

        # Open a file
        foCAT = open("data/d11124901CAT.csv", "a")
        foCAT.write(feat[i])
        foCAT.write(",")
        foCAT.write(str(count1))
        foCAT.write(",")
        foCAT.write(str(round(miss, 2)))
        foCAT.write(",")
        foCAT.write(str(round(card, 2)))
        foCAT.write(",")
        foCAT.write(str(modes))
        foCAT.write(",")
        foCAT.write(str(round(modecount, 2)))
        foCAT.write(",")
        foCAT.write(str(round(modeper, 2)))
        foCAT.write(",")
        foCAT.write(str(secondmode))
        foCAT.write(",")
        foCAT.write(str(round(secmodecount, 2)))
        foCAT.write(",")
        foCAT.write(str(round(secmodeper, 2)))
        foCAT.write(",")
        foCAT.write("\n")
        # Close opend file
        foCAT.close()

    # continuous
    def cont(i):
        total = 0
        mean = 0
        count = 0
        count1 = 0
        notin = 0
        miss = 0
        card = 0
        mini = 0
        maxi = 0
        median = 0
        onestquart = 0
        threerdquart = 0
        stand_dev = 0
        square = 0
        sq_tot = 0
        sd_mean = 0
        j = 0

        # SortedList, medList and cardList
        sortedList = list()
        medList = list()
        cardList = list()
        
        
        for list2 in pplList:
            if (list2[i] != ' ?'):
                total = total + float(list2[i])
                cardList.append(float(list2[i]))
                medList.append(float(list2[i]))
                count = count + 1
                count1 = count - notin
            else:
                notin = notin + 1
                count = count + 1

        mean = statistics.mean(medList)
        for j in medList:
            square = float(i) - mean
            square = square * square
            sq_tot = sq_tot + square

        ca = set(cardList)
        card = len(ca)
        miss = (notin / count) * 100
        medList.sort()
        mini = min(medList)
        maxi = max(medList)
        median = medList[int(count / 2)]
        onestquart = medList[int((count / 2) / 2)]
        threerdquart = medList[int((count / 2) + ((count / 2) / 2))]
        sd_mean = sq_tot / count1
        stand_dev = math.sqrt(sd_mean)

        # Open a file
        foCONT = open("data/d11124901CONT.csv", "a")
        foCONT.write(feat[i]);
        foCONT.write(",");
        foCONT.write(str(count1));
        foCONT.write(",");
        foCONT.write(str(round(miss, 2)));
        foCONT.write(",");
        foCONT.write(str(round(card, 2)));
        foCONT.write(",");
        foCONT.write(str(round(mini, 2)));
        foCONT.write(",");
        foCONT.write(str(round(onestquart, 2)));
        foCONT.write(",");
        foCONT.write(str(round(mean, 2)));
        foCONT.write(",");
        foCONT.write(str(round(median, 2)));
        foCONT.write(",");
        foCONT.write(str(round(threerdquart, 2)));
        foCONT.write(",");
        foCONT.write(str(round(maxi, 2)));
        foCONT.write(",");
        foCONT.write(str(round(stand_dev, 2)));
        foCONT.write(",");
        foCONT.write("\n")
        # Close opend file
        foCONT.close()

    # open file and write table column headers
    fCAT = open("data/d11124901CAT.csv", 'a')
    fCAT.write("Categorical Table:")
    fCAT.write("\n")
    fCAT.write("Feature");
    fCAT.write(",");
    fCAT.write("Count");
    fCAT.write(",");
    fCAT.write("Miss%");
    fCAT.write(",");
    fCAT.write("Card");
    fCAT.write(",");
    fCAT.write("Mode");
    fCAT.write(",");
    fCAT.write("ModeCount");
    fCAT.write(",");
    fCAT.write("Mode%");
    fCAT.write(",");
    fCAT.write("2ndMode");
    fCAT.write(",");
    fCAT.write("2ndModeCount");
    fCAT.write(",");
    fCAT.write("2ndMode%");
    fCAT.write("\n");
    fCAT.close()

    # open file and write table column headers
    fCONT = open("data/d11124901CONT.csv", 'a')
    fCONT.write("Continuous Table:")
    fCONT.write("\n")
    fCONT.write("Feature");
    fCONT.write(",");
    fCONT.write("Count");
    fCONT.write(",");
    fCONT.write("Miss%");
    fCONT.write(",");
    fCONT.write("Card");
    fCONT.write(",");
    fCONT.write("Min");
    fCONT.write(",");
    fCONT.write("1stQuart");
    fCONT.write(",");
    fCONT.write("Mean");
    fCONT.write(",");
    fCONT.write("Median");
    fCONT.write(",");
    fCONT.write("3rdQuart");
    fCONT.write(",");
    fCONT.write("Max");
    fCONT.write(",");
    fCONT.write("StdDev");
    fCONT.write("\n")
    fCONT.close()

    # loop to check it feature is continous or categorical
    i = 0
    while i < len(feat):
        try:
            try:
                cont(i)
                i = i + 1
            except ValueError:
                try:
                    cat(i)
                    i = i + 1
                except StatisticsError:
                    i = i + 1
        except IndexError:
            i = i + 1


if __name__ == '__main__':
    main()

