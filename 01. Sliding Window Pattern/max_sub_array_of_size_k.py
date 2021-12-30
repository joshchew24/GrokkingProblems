'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def max_sub_array_of_size_k(k, arr):
    result = 0
    windowStart = 0
    currSum = 0

    for windowEnd in range(len(arr)):
        # add next element
        currSum += arr[windowEnd]

        # once window size reached, begin updating results if currSum is higher than max so far
        if windowEnd < k - 1:
            continue
        
        # if currSum higher than result, update result with currSum
        if currSum > result:
            result = currSum
        
        # subtract element leaving window
        currSum -= arr[windowStart]
        # slide window forward
        windowStart += 1
    return result


def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

if __name__ == "__main__":
    main()