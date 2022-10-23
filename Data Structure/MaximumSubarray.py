from sys import maxsize

#brute force
def maxSubArray1(nums: list[int]):
    if len(nums) == 1:
        return nums[0]

    maxSum = -sys.maxsize - 1
    start = 0
    end = 0
    for i in range(0, len(nums)):
        tempsum = 0
        print(tempsum)
        for j in range(i, len(nums)):
            tempsum += nums[j]
            if(tempsum > maxSum):
                maxSum = tempsum
                start = i
                end = j
    print('Max sum: %d (%d, %d) ' % (maxSum, start, end))

# Kadane’s Algorithm
def maxSubArraySum(a,size):

    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0,size):

        max_ending_here += a[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1

    print ("Maximum contiguous sum is %d"%(max_so_far))
    print ("Starting Index %d"%(start))
    print ("Ending Index %d"%(end))

# Driver program to test maxSubArraySum


if __name__ == "__main__":
    arr = [-2, -1, 0, 1, 2, 3, 4]
    
    # maxSubArray1(arr)

    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    maxSubArraySum(a,len(a))