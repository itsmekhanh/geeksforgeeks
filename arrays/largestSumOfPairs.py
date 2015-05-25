def largestSumOfPairs(values):
    if len(values) < 2:
        print "Input array contains less than 2 values"
        return False

    largestPair = [None]*2
    for value in values:
        if largestPair[1] is None:
            largestPair[1] = value
        elif largestPair[1] < value:
            largestPair[0] = largestPair[1]
            largestPair[1] = value
        elif largestPair[0] < value:
            largestPair[0] = value

    return largestPair[0]+largestPair[1]

if __name__ == '__main__':
    print "Problem: Given an unsorted array, find the largest pair sum in it"
    print "Testing list: [12,40,10,6,34]"
    print "Sum is ", largestSumOfPairs([12,40,10,6,34])
    print "Testing list: [40,30,1,2,3,4]"
    print "Sum is ", largestSumOfPairs([40,30,1,2,3,4])

