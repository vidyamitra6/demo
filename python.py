# # # # # # # 1) Baisc and arrays

# # # # # # # def rev(arr,start,end):
# # # # # # #     if start>=end:
# # # # # # #         return 
# # # # # # #     arr[start],arr[end] = arr[end],arr[start]
# # # # # # #     rev(arr,start+1,end-1)
# # # # # # # arr = [1,2,3,4,5]
# # # # # # # rev(arr,0,4)
# # # # # # # print(arr)

# # # # # # # def gcd(a,b):
# # # # # # #     while b :
# # # # # # #         a,b = a,a%b
# # # # # # #     return a
# # # # # # # print(gcd(5,15))

# # # # # # # def fib(n):
# # # # # # #     if n == 0 :
# # # # # # #         return 0 
# # # # # # #     if n ==1 :
# # # # # # #         return 1
# # # # # # #     return fib(n-1) + fib(n-2)
# # # # # # # print(fib(5))

# # # # # # # def hashing(arr1,arr2):
# # # # # # #     d = dict()
# # # # # # #     for i in arr1:
# # # # # # #         if d.get(i):
# # # # # # #             d[i] = d[i]+1
# # # # # # #         else:
# # # # # # #             d[i] = 1
# # # # # # #     print(d)
# # # # # # # arr1 = [1, 2, 1, 3, 2]
# # # # # # # arr2 = [1, 3, 4, 2, 10]
# # # # # # # hashing(arr1,arr2)

# # # # # # # print(eval(input("Enter the expression :")))  # Example of using eval to evaluate an expression

# # # # # # # def bubble(arr):
# # # # # # #     n = len(arr)
# # # # # # #     for i in range(n-1,-1,-1):
# # # # # # #         for j in range(0,i):
# # # # # # #             if arr[j]>arr[j+1]:
# # # # # # #                 arr[j] ,arr[j+1] = arr[j+1],arr[j]
# # # # # # #     print(arr)
# # # # # # # bubble([5,4,3,2,1])

# # # # # # # def bubble(arr,n):
# # # # # # #     if n == 1:
# # # # # # #         return 
# # # # # # #     for i in range(n-1):
# # # # # # #         if arr[i]>arr[i+1]:
# # # # # # #             arr[i],arr[i+1] = arr[i+1],arr[i]
# # # # # # #     bubble(arr,n-1)
# # # # # # # arr = [5,4,3,2,1]
# # # # # # # print(arr)
# # # # # # # bubble(arr,5)
# # # # # # # print(arr)

# # # # # # # def insert(arr,n):
# # # # # # #     if n ==1 :
# # # # # # #         return 
# # # # # # #     for i in range(n-1,0,-1):
        

# # # # # # # def quickSort(arr,left,right):
# # # # # # #     if left < right :
# # # # # # #         pIndex = partition(arr,left,right)
# # # # # # #         quickSort(arr,left,pIndex-1)
# # # # # # #         quickSort(arr,pIndex+1,right)
# # # # # # # def partition(arr,left,right):
# # # # # # #     pivot = left 
# # # # # # #     i = left 
# # # # # # #     j = right
# # # # # # #     while i < j :
# # # # # # #         while arr[i]<=arr[pivot] and i<right:
# # # # # # #             i+=1
# # # # # # #         while arr[j] > arr[pivot] and j> left:
# # # # # # #             j-=1
# # # # # # #         if i < j :
# # # # # # #             arr[i] , arr[j] = arr[j],arr[i]
# # # # # # #     arr[left],arr[j] = arr[j],arr[left]
# # # # # # #     return j
# # # # # # # arr = [5,4,3,2,1]
# # # # # # # quickSort(arr,0,4)
# # # # # # # print(arr)

# # # # # # # def findSecondSmall(arr):
# # # # # # #     small = float('inf')
# # # # # # #     second_small = float('inf')
# # # # # # #     for i in arr:
# # # # # # #         if i < small:
# # # # # # #             second_small = small
# # # # # # #             small = i 
# # # # # # #         elif i < second_small and i!=small :
# # # # # # #             second_small = i
# # # # # # #     return second_small
# # # # # # # print(findSecondSmall([1,2,3,4,5]))

# # # # # # # def dup(arr):
# # # # # # #     i =  0 
# # # # # # #     n = len(arr)
# # # # # # #     for j in range(1,n):
# # # # # # #         if arr[i]!=arr[j] :
# # # # # # #             i+=1
# # # # # # #             arr[i] = arr[j]
# # # # # # #     print(arr[:i+1])
# # # # # # # dup([1,2,2,3,4,4,4,5])
            

# # # # # # # def rotate(arr):
# # # # # # #     n = len(arr)
# # # # # # #     first = arr[0]
# # # # # # #     for i in range(n-1):
# # # # # # #         arr[i] = arr[i+1]
# # # # # # #     arr[n-1] = first 
# # # # # # #     print(arr)
# # # # # # # rotate([1,2,3,4,5])
        
# # # # # # # def rotate(arr,k):
# # # # # # #     n = len(arr)
# # # # # # #     temp = []
# # # # # # #     for i in range(n-k,n):
# # # # # # #         temp.append(arr[i])
# # # # # # #     for i in range(n-k-1,-1,-1):
# # # # # # #         arr[i+k] = arr[i]
# # # # # # #     for i in range(k):
# # # # # # #         arr[i] = temp[i]
# # # # # # #     print(arr)
# # # # # # # rotate([1,2,3,4,5],3)

# # # # # # # def zero(arr):
# # # # # # #     n = len(arr)
# # # # # # #     last = n-1 
# # # # # # #     i = 0 
# # # # # # #     while i < last :
# # # # # # #         if arr[i] == 0 :
# # # # # # #             arr[i], arr[last] = arr[last] ,arr[i]
# # # # # # #             last-=1
# # # # # # #         else:
# # # # # # #             i+=1
# # # # # # #     print(arr)
# # # # # # # zero([1,0,3,0,5,0])

# # # # # # # def union(arr1,arr2):
# # # # # # #     i, j = 0,0
# # # # # # #     n,m = len(arr1),len(arr2)
# # # # # # #     un = []
# # # # # # #     while i<n and j < m :
# # # # # # #         if arr1[i]<=arr2[j]:
# # # # # # #             if len(un)==0 or un[-1]!=arr1[i]:
# # # # # # #                 un.append(arr1[i])
# # # # # # #             i+=1
# # # # # # #         else:
# # # # # # #             if len(un)==0 or un[-1]!=arr2[j]:
# # # # # # #                 un.append(arr2[j])
# # # # # # #             j+=1
# # # # # # #     while i < n and un[-1]!=arr1[i]:
# # # # # # #         un.append(arr1[i])
# # # # # # #         i+=1
# # # # # # #     while j < m and  un[-1]!=arr2[j]:
# # # # # # #         un.append(arr2[j])
# # # # # # #         j+=1
# # # # # # #     print(un)
# # # # # # # union([1,2,3,4,4,7,8],[1,1,5,6,7,8])        

# # # # # # # def maxOnes(arr):
# # # # # # #     count = 0 
# # # # # # #     maxi = 0 
# # # # # # #     for i in arr:
# # # # # # #         if i == 1:
# # # # # # #             count+=1
# # # # # # #             maxi = max(maxi,count)
# # # # # # #         else:
# # # # # # #             count = 0 
# # # # # # #     print(maxi)
# # # # # # # maxOnes([1,1,0,1,1,1])

# # # # # # # def majorityElement(arr):
# # # # # # #     # Size of the given array
# # # # # # #     n = len(arr)
# # # # # # #     cnt = 0  # Count
# # # # # # #     el = None  # Element

# # # # # # #     # Applying the algorithm
# # # # # # #     for i in range(n):
# # # # # # #         if cnt == 0:
# # # # # # #             cnt = 1
# # # # # # #             el = arr[i]
# # # # # # #         elif el == arr[i]:
# # # # # # #             cnt += 1
# # # # # # #         else:
# # # # # # #             cnt -= 1

# # # # # # #     # Checking if the stored element is the majority element
# # # # # # #     cnt1 = 0
# # # # # # #     for i in range(n):
# # # # # # #         if arr[i] == el:
# # # # # # #             cnt1 += 1

# # # # # # #     if cnt1 > (n / 2):
# # # # # # #         return el
# # # # # # #     return -1


# # # # # # # def maxProfit(arr):
# # # # # # #     maxPro = 0
# # # # # # #     minPrice = float('inf')
# # # # # # #     for i in range(len(arr)):
# # # # # # #         minPrice = min(minPrice, arr[i])
# # # # # # #         maxPro = max(maxPro, arr[i] - minPrice)
# # # # # # #     return maxPro

# # # # # # # def RearrangebySign(A, n):
# # # # # # #     # Define 2 lists, one for storing positive 
# # # # # # #     # and other for negative elements of the array.
# # # # # # #     pos = []
# # # # # # #     neg = []
    
# # # # # # #     # Segregate the array into positives and negatives.
# # # # # # #     for i in range(n):
# # # # # # #         if A[i] > 0:
# # # # # # #             pos.append(A[i])
# # # # # # #         else:
# # # # # # #             neg.append(A[i])
    
# # # # # # #     # If positives are lesser than the negatives.
# # # # # # #     if len(pos) < len(neg):
# # # # # # #         # First, fill array alternatively till the point 
# # # # # # #         # where positives and negatives are equal in number.
# # # # # # #         for i in range(len(pos)):
# # # # # # #             A[2*i] = pos[i]
# # # # # # #             A[2*i+1] = neg[i]
        
# # # # # # #         # Fill the remaining negatives at the end of the array.
# # # # # # #         index = len(pos)*2
# # # # # # #         for i in range(len(neg)-len(pos)):
# # # # # # #             A[index] = neg[len(pos)+i]
# # # # # # #             index += 1
    
# # # # # # #     # If negatives are lesser than the positives.
# # # # # # #     else:
# # # # # # #         # First, fill array alternatively till the point 
# # # # # # #         # where positives and negatives are equal in number.
# # # # # # #         for i in range(len(neg)):
# # # # # # #             A[2*i] = pos[i]
# # # # # # #             A[2*i+1] = neg[i]
        
# # # # # # #         # Fill the remaining positives at the end of the array.
# # # # # # #         index = len(neg)*2
# # # # # # #         for i in range(len(pos)-len(neg)):
# # # # # # #             A[index] = pos[len(neg)+i]
# # # # # # #             index += 1
    
# # # # # # #     return A

# # # # # # # def nextGreaterPermutation(A: List[int]) -> List[int]:
# # # # # # #     n = len(A) # size of the array.

# # # # # #     # # Step 1: Find the break point:
# # # # # #     # ind = -1 # break point
# # # # # #     # for i in range(n-2, -1, -1):
# # # # # #     #     if A[i] < A[i + 1]:
# # # # # #     #         # index i is the break point
# # # # # #     #         ind = i
# # # # # #     #         break

# # # # # #     # # If break point does not exist:
# # # # # #     # if ind == -1:
# # # # # #     #     # reverse the whole array:
# # # # # #     #     A.reverse()
# # # # # #     #     return A

# # # # # #     # # Step 2: Find the next greater element
# # # # # #     # #         and swap it with arr[ind]:
# # # # # #     # for i in range(n - 1, ind, -1):
# # # # # #     #     if A[i] > A[ind]:
# # # # # #     #         A[i], A[ind] = A[ind], A[i]
# # # # # #     #         break

# # # # # #     # # Step 3: reverse the right half:
# # # # # #     # A[ind+1:] = reversed(A[ind+1:])

# # # # # #     # return A
    
# # # # # #     # def mergeOverlappingIntervals(arr: List[List[int]]) -> List[List[int]]:
# # # # # #     # n = len(arr) # size of the array

# # # # # #     # # sort the given intervals:
# # # # # #     # arr.sort()

# # # # # #     # ans = []

# # # # # #     # for i in range(n):
# # # # # #     #     # if the current interval does not
# # # # # #     #     # lie in the last interval:
# # # # # #     #     if not ans or arr[i][0] > ans[-1][1]:
# # # # # #     #         ans.append(arr[i])
# # # # # #     #     # if the current interval
# # # # # #     #     # lies in the last interval:
# # # # # #     #     else:
# # # # # #     #         ans[-1][1] = max(ans[-1][1], arr[i][1])
# # # # # #     # return ans

# # # # # # def merge(arr : List[int], low : int, mid : int, high : int) -> int:
# # # # # #     temp = []   # temporary array
# # # # # #     left = low  # starting index of left half of arr
# # # # # #     right = mid + 1 # starting index of right half of arr

# # # # # #     cnt = 0     # Modification 1: cnt variable to count the pairs

# # # # # #     # storing elements in the temporary array in a sorted manner
# # # # # #     while (left <= mid and right <= high):
# # # # # #         if (arr[left] <= arr[right]):
# # # # # #             temp.append(arr[left])
# # # # # #             left += 1
# # # # # #         else:
# # # # # #             temp.append(arr[right])
# # # # # #             cnt += (mid - left + 1)  # Modification 2
# # # # # #             right += 1

# # # # # #     # if elements on the left half are still left
# # # # # #     while (left <= mid):
# # # # # #         temp.append(arr[left])
# # # # # #         left += 1

# # # # # #     # if elements on the right half are still left
# # # # # #     while (right <= high):
# # # # # #         temp.append(arr[right])
# # # # # #         right += 1

# # # # # #     # transfering all elements from temporary to arr
# # # # # #     for i in range(low, high + 1):
# # # # # #         arr[i] = temp[i - low]

# # # # # #     return cnt   # Modification 3

# # # # # # def mergeSort(arr : List[int], low : int, high : int) -> int:
# # # # # #     cnt = 0
# # # # # #     if low >= high:
# # # # # #         return cnt
# # # # # #     mid = math.floor((low + high) / 2)
# # # # # #     cnt += mergeSort(arr, low, mid)    # left half
# # # # # #     cnt += mergeSort(arr, mid + 1, high)  # right half
# # # # # #     cnt += merge(arr, low, mid, high)  # merging sorted halves
# # # # # #     return cnt

# # # # # # def numberOfInversions(a : List[int], n : int) -> int:
# # # # # #     # Count the number of pairs:
# # # # # #     n = len(a)
# # # # # #     # Count the number of pairs:
# # # # # #     return mergeSort(a, 0, n - 1)

# # # # # # Next

# # # # # def merge(arr, low, mid, high):
# # # # #     temp = []  # temporary array
# # # # #     left = low  # starting index of left half of arr
# # # # #     right = mid + 1  # starting index of right half of arr

# # # # #     # storing elements in the temporary array in a sorted manner
# # # # #     while left <= mid and right <= high:
# # # # #         if arr[left] <= arr[right]:
# # # # #             temp.append(arr[left])
# # # # #             left += 1
# # # # #         else:
# # # # #             temp.append(arr[right])
# # # # #             right += 1

# # # # #     # if elements on the left half are still left
# # # # #     while left <= mid:
# # # # #         temp.append(arr[left])
# # # # #         left += 1

# # # # #     # if elements on the right half are still left
# # # # #     while right <= high:
# # # # #         temp.append(arr[right])
# # # # #         right += 1

# # # # #     # transferring all elements from temporary to arr
# # # # #     for i in range(low, high + 1):
# # # # #         arr[i] = temp[i - low]

# # # # # def countPairs(arr, low, mid, high):
# # # # #     right = mid + 1
# # # # #     cnt = 0
# # # # #     for i in range(low, mid + 1):
# # # # #         while right <= high and arr[i] > 2 * arr[right]:
# # # # #             right += 1
# # # # #         cnt += (right - (mid + 1))
# # # # #     return cnt

# # # # # def mergeSort(arr, low, high):
# # # # #     cnt = 0
# # # # #     if low >= high:
# # # # #         return cnt
# # # # #     mid = (low + high) // 2
# # # # #     cnt += mergeSort(arr, low, mid)  # left half
# # # # #     cnt += mergeSort(arr, mid + 1, high)  # right half
# # # # #     cnt += countPairs(arr, low, mid, high)  # Modification
# # # # #     merge(arr, low, mid, high)  # merging sorted halves
# # # # #     return cnt

# # # # # def team(skill: [int], n: int) -> int:
# # # # #     return mergeSort(skill, 0, n - 1)

# # # # # if __name__ == "__main__":
# # # # #     a = [4, 1, 2, 3, 1]
# # # # #     n = 5
# # # # #     cnt = team(a, n)
# # # # #     print("The number of reverse pair is:", cnt).



# # # # # next

# # # # # def binary(arr,x):
# # # # #     n = len(arr)
# # # # #     low = 0 
# # # # #     high = n-1
# # # # #     ans = -1
# # # # #     while low<=high:
# # # # #         mid = (low+high)//2
# # # # #         if arr[mid] == x:
# # # # #             ans = mid
# # # # #             high = mid-1
# # # # #         elif arr[mid]>x:
# # # # #             high = mid -1
# # # # #         else:
# # # # #             low = mid+1
# # # # #     return ans
# # # # # print(binary([1,2,2,3,3,3,3,4,5],3))

# # # # # def sq(n):
# # # # #     low = 1 
# # # # #     high = n 
# # # # #     ans = 1
# # # # #     while low<=high:
# # # # #         mid = (low+high)//2
# # # # #         val = mid * mid
# # # # #         if val<=n:
# # # # #             low = low +1
# # # # #             ans = mid
# # # # #         else:
# # # # #             high = high -1
# # # # #     return high
# # # # # print(sq(25))

# # # # # print(1<<1)

# # # # class NQueen:
# # # #     def __init__(self, n):
# # # #         self.n = n
# # # #         self.count = 0

# # # #     def solve(self):
# # # #         a = [0] * self.n
# # # #         self.fill(a, 0)
# # # #         print(f"No of possibilities for {self.n} Queens = {self.count}")

# # # #     def fill(self, a, k):
# # # #         if k == self.n:
# # # #             self.print_solution(a)
# # # #             return
# # # #         for i in range(self.n):
# # # #             if self.is_safe(i, k, a):
# # # #                 a[k] = i
# # # #                 self.fill(a, k + 1)

# # # #     def is_safe(self, i, k, a):
# # # #         for j in range(k):
# # # #             if i == a[j] or abs(k - j) == abs(i - a[j]):
# # # #                 return False
# # # #         return True

# # # #     def print_solution(self, a):
# # # #         print(" ".join(map(str, a)))
# # # #         self.count += 1


# # # # if __name__ == "__main__":
# # # #     n = 5
# # # #     queen = NQueen(n)
# # # #     queen.solve()



# # # import sys

# # # def matrix_chain_order(p):
# # #     n = len(p) - 1  # Number of matrices
# # #     dp = [[0] * n for _ in range(n)]

# # #     # l is chain length
# # #     for l in range(2, n + 1):
# # #         for i in range(n - l + 1):
# # #             j = i + l - 1
# # #             dp[i][j] = sys.maxsize
# # #             for k in range(i, j):
# # #                 cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
# # #                 if cost < dp[i][j]:
# # #                     dp[i][j] = cost
# # #     return dp[0][n-1]

# # # # Example usage
# # # p = [40, 20, 30, 10, 30]  # Dimensions of matrices A1(40x20), A2(20x30), A3(30x10), A4(10x30)
# # # print("Minimum number of multiplications is", matrix_chain_order(p))


# # Edge    Weight
# # 0 - 1   4
# # 1 - 2   8
# # 2 - 3   7
# # 3 - 4   9
# # 2 - 5   4
# # 5 - 6   2
# # 6 - 7   1
# # 2 - 8   2


# class Item:
#     def __init__(self, weight, rate):
#         self.weight = weight
#         self.rate = rate

# def knapsack(n, w, items):
#     if n == 0 or w == 0:
#         return 0
#     if items[n-1].weight <= w:
#         return max(
#             items[n-1].rate + knapsack(n-1, w - items[n-1].weight, items),
#             knapsack(n-1, w, items)
#         )
#     else:
#         return knapsack(n-1, w, items)

# # Example usage
# if __name__ == "__main__":
#     n = 4
#     weights = [3, 2, 5, 4]  # Change to [4, 5, 2, 6] for other test case
#     rates = [20, 16, 45, 40]  # Change to [30, 20, 60, 20] for other test case
#     W = 8  # Knapsack capacity; change to 10 for other test case

#     items = [Item(weights[i], rates[i]) for i in range(n)]
#     print(knapsack(n, W, items))

