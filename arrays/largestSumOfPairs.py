def largestSumOfPairs(values):
    if len(values) < 2:
        print "Input array contains less than 2 values"
        return False

    largestPair = []
    for value in values:
        if largestPair[1] is None:
            largestPair[1] = value
        elif largestPair[1] < value:
            largestPair[0] = largestPair[1]
            largestPair[1] = value
        elif largestPair[0] < value:
            largest[0] = value

    return largestPair[0]+largestPair[1]

if __name__ == '__main__':
    print "Problem: Given an unsorted array, find the largest pair sum in it\n"
    print "Testing list: [12,40,10,6,34]\n"
    print "Sum is " + largestSumOfPairs([12,40,10,6,34])+"\n"

