def pythagoreanTriplet(values):
    squares = [];
    for value in values:
        squares.append(value*value)

    squares = sorted(squares)
    end = len(squares)-1

    while end > 1:
        value = squares[end]
        left = 0
        right = end-1

        while left < right:
            sum = squares[left]+squares[right]
            if sum == value:
                return True
            elif sum < value:
                left += 1
            else:
                right -= 1
        end -= 1
    return False


if __name__ == "__main__":
    print "pythagoreanTriplet() - Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2"
    print "testing [3,1,4,6,5]"
    print "Yes there is a triplet!" if pythagoreanTriplet([3,1,4,6,5]) else "There is no triplet in this array"

