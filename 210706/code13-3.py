def binSearch(ary,fData):
    start = 0
    pos = -1
    end=len(ary)-1
    while start <= end:
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData < mid:
            end = mid+1
        else:
            start = mid-1
    return pos


detArray = [50,60,105,120,160,162,168,177,188]
findData = 162
print('배열---> ', detArray)
position = binSearch(detArray,findData)
if position == -1:
    print(findData,'is NOT FOUND.')
else:
    print(findData,'is exist at',position)
