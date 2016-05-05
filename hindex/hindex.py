def hindex(sortedlist, countlist=None):
    if countlist == None:
        countlist = []
    # calculate the h-index
    print sortedlist
    for item in sortedlist:
        remaininglist = len(sortedlist[sortedlist.index(item):])
        if remaininglist > item:
            countlist.append(item)
        elif remaininglist == item:
            countlist.append(item)
            break
        else:
            while remaininglist < item:
                item -= 1
            else:
                countlist.append(item)
                break

    # return the h-index value
    print countlist
    return max(countlist)
