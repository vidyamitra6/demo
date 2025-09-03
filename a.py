# def longest_subsequence(arr, increasing=True):
#     n = len(arr)
#     dp = [1] * n

#     for i in range(1, n):
#         for j in range(i):
#             if increasing:
#                 if arr[i] >= arr[j]:  # non-decreasing
#                     dp[i] = max(dp[i], dp[j] + 1)
#             else:
#                 if arr[i] <= arr[j]:  # non-increasing
#                     dp[i] = max(dp[i], dp[j] + 1)
#     return max(dp)


# def removeMin(arr):
#     n = len(arr)
#     if n <= 1:
#         return 0

#     lis = longest_subsequence(arr, increasing=True)   # ascending
#     lds = longest_subsequence(arr, increasing=False)  # descending

#     longest = max(lis, lds)
#     return n - longest


# # Examples
# print(removeMin([1, 2, 3, 4, 5]))   # 0 (already sorted ascending)
# print(removeMin([5, 4, 3, 2, 1]))   # 0 (already sorted descending)
# print(removeMin([3, 1, 2, 4, 5]))   # 1 (remove 3)
# print(removeMin([1, 5, 3, 4, 2]))   # 2 (remove 5,4 -> [1,3,2] descending)
# print(removeMin([10]))              # 0 (single element)
# print(removeMin([2, 2, 2, 2]))      # 0 (all equal → both asc & desc)

# import math

# def ways(n):
#     count = 0 
#     for i in range(1,n//2+2):
#         sum = 0
#         for j in range(i,n//2+2):
#             # print(i,sum)
#             sum+=j
#             if sum==n:
#                 # print(sum)
#                 count+=1
#                 sum = 0
#                 break
#             if sum>n:
#                 sum = 0
#                 break

        
#         # print(sum)
#     return count
# print(ways(20))

# def countConsecutiveWays(N):
#     count = 0
#     k = 2  # at least 2 numbers
#     while (k * (k - 1)) // 2 < N:
#         numerator = N - (k * (k - 1)) // 2
#         if numerator % k == 0:
#             a = numerator // k
#             if a > 0:
#                 count += 1
#         k += 1
#     return count

# # Example test cases
# print(countConsecutiveWays(15))  # Output: 3
# print(countConsecutiveWays(50))  # Output: 4

# def checkPalindrom(str):
#     if str == str[::-1]:
#         return True
#     return False
# def subStrings(str):
#     count = 0
#     n = len(str)
#     val = set()
#     for i in range(n):
#         for j in range(i, n):
#             substr = str[i:j+1]
#             if substr not in val:
#                 val.add(substr)
#     for i in val:
#         if checkPalindrom(i):
#             count+=1
#     print(count)
# subStrings("abba")

# # def countUniquePalindromes(s):
#     n = len(s)
#     unique_palindromes = set()

#     # Expand around center
#     for center in range(n):
#         # Odd-length palindromes
#         l, r = center, center
#         while l >= 0 and r < n and s[l] == s[r]:
#             unique_palindromes.add(s[l:r+1])
#             l -= 1
#             r += 1

#         # Even-length palindromes
#         l, r = center, center + 1
#         while l >= 0 and r < n and s[l] == s[r]:
#             unique_palindromes.add(s[l:r+1])
#             l -= 1
#             r += 1

#     print(len(unique_palindromes))

# # Example
# countUniquePalindromes("abba")

import math

# def minimize_max(arr):
#     n = len(arr)
#     prefix_sum = 0
#     ans = 0
#     for i in range(n):
#         prefix_sum += arr[i]
#         avg = math.ceil(prefix_sum / (i + 1))
#         ans = max(ans, avg)
#     return ans

# # Example
# arr = [3, 1, 6, 4]
# print(minimize_max(arr))  # Output: 4

# def span(arr):
#     total = 0
#     n = len(arr)
#     for i in range(n):
#         count = 0
#         left = right = i
#         while left>=0 and arr[left]<=arr[i]:
#             count+=1
#             left-=1
#         while right<n and arr[right]<=arr[i]:
#             count+=1
#             right+=1
#         count-=1
#         total+=count
#     return total



# print(span([1, 1, 2, 1, 1]))

# def total_span(arr):
#     n = len(arr)
#     total = 0
    
#     for i in range(n):
#         # Count consecutive elements to the left
#         left_count = 1
#         j = i - 1
#         while j >= 0 and arr[j] <= arr[i]:
#             left_count += 1
#             j -= 1
            
#         # Count consecutive elements to the right
#         right_count = 1
#         j = i + 1
#         while j < n and arr[j] <= arr[i]:
#             right_count += 1
#             j += 1
            
#         # Total span for current element
#         total += left_count + right_count - 1  # subtract 1 because element counted twice
        
#     return total

# # Example usage
# arr = [3, 3, 3, 2, 1]
# print(total_span(arr))  # Output: 34

# arr2 = [3, 1, 2, 2, 1]
# print(total_span(arr2))  # Output: 8



# def isValid(word):
#     alpha = False
#     digit = False
#     special = True
#     for i in word:
#         if i.isalpha():
#             alpha = True
#         elif i.isdigit():
#             digit = True
#         else:
#             special = False
#             break
#     return alpha and digit and special
# def valid(str):
#     words = str.split()
#     count = 0
#     for word in words:
#         if isValid(word):
#             count+=1
#     return count

# print(valid("abc1 def2g 123a* A1e z9i! good1"))

# def validPara(str):
#     balanced = 0
#     insertion = 0
#     for i in str:
#         if i == "(":
#             balanced+=1
#         elif i == ")":
#             if balanced>0:
#                 balanced-=1
#             else:
#                 insertion+=1
#     return abs(balanced)+insertion
# print(validPara("())("))

# def removeDuplicates(self, s: str, k: int) -> str:        
#         stck = []    
        
#         for c in s:                            
#             if stck and stck[-1][0] == c: # check if stack is not empty
#                 stck[-1][1]+=1
#                 if stck[-1][1] == k:
#                     stck.pop()
#             else:
#                 stck.append([c, 1])            
        
#         return ''.join(c * cnt for c, cnt in stck) 

# from collections import defaultdict

# def minTaskTime(taskTypes, taskMemory, maxMemory):
#     # Step 1: Group tasks by type
#     type_to_memory = defaultdict(list)
#     for t, m in zip(taskTypes, taskMemory):
#         type_to_memory[t].append(m)

#     total_time = 0

#     # Step 2: Process each type separately
#     for t, memories in type_to_memory.items():
#         memories.sort()
#         i, j = 0, len(memories) - 1

#         while i < j:
#             if memories[i] + memories[j] <= maxMemory:
#                 # Pair these two tasks
#                 total_time += 1
#                 i += 1
#                 j -= 1
#             else:
#                 # Task at j runs alone
#                 total_time += 1
#                 j -= 1

#         # If one task is left unpaired
#         if i == j:
#             total_time += 1

#     return total_time


from collections import deque

# def minStepsKnight(n, start, target):
#     # Possible knight moves
#     dx = [2, 2, -2, -2, 1, -1, 1, -1]
#     dy = [1, -1, 1, -1, 2, 2, -2, -2]

#     # If already at target
#     if start == target:
#         return 0

#     visited = [[False]*n for _ in range(n)]
#     q = deque()
    
#     # Push starting position with 0 moves
#     q.append((start[0], start[1], 0))
#     visited[start[0]][start[1]] = True

#     while q:
#         x, y, dist = q.popleft()

#         # Explore all 8 knight moves
#         for i in range(8):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#                 if (nx, ny) == target:
#                     return dist + 1
#                 visited[nx][ny] = True
#                 q.append((nx, ny, dist + 1))
    
#     return -1  # If not reachable (shouldn’t happen in chessboard)


# def countInversionsSize3(arr):
#     n = len(arr)
#     total = 0

#     for j in range(1, n-1):  # middle element
#         leftGreater = 0
#         rightSmaller = 0

#         # Count elements greater than arr[j] on the left
#         for i in range(j):
#             if arr[i] > arr[j]:
#                 leftGreater += 1

#         # Count elements smaller than arr[j] on the right
#         for k in range(j+1, n):
#             if arr[k] < arr[j]:
#                 rightSmaller += 1

#         total += leftGreater * rightSmaller

#     return total


# def maxSumSwappableOnce(arr):
#     n = len(arr)
#     # Initial sum
#     base_sum = sum(arr[i] * i for i in range(n))
    
#     max_gain = 0
#     used = [False] * n
    
#     # Greedy approach: try best pair (i, j)
#     for i in range(n):
#         for j in range(i+1, n):
#             gain = (j - i) * (arr[i] - arr[j])
#             if gain > 0:
#                 max_gain = max(max_gain, gain)
    
#     return base_sum + max_gain

# def maxSumSwappableOnce(arr):
#     n = len(arr)
#     base_sum = sum(arr[i] * i for i in range(n))

#     best_gain = 0
#     min_val = float('inf')
#     min_index = -1

#     # Traverse from right to left
#     for j in range(n-1, -1, -1):
#         if min_val < arr[j]:  # possible gain
#             gain = (min_index - j) * (arr[j] - min_val)
#             best_gain = max(best_gain, gain)

#         # update minimum value seen so far
#         if arr[j] < min_val:
#             min_val = arr[j]
#             min_index = j

#     return base_sum + best_gain

# str = "abbaa"
# rev = str[::-1]

# n = len(str)
# count = 0
# for i in range(n):
#     if str[i]!=rev[i]:
#         count+=1
# if n%2==0 and count>0:
#     print(count-1)
# else:
#     print(count)

# def minInsertionsPalindrome(s: str) -> int:
#     n = len(s)
#     rev = s[::-1]

#     # DP for LCS(s, rev)
#     dp = [[0]*(n+1) for _ in range(n+1)]

#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if s[i-1] == rev[j-1]:
#                 dp[i][j] = 1 + dp[i-1][j-1]
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#     lps = dp[n][n]
#     return n - lps


def decodeString(s: str):
    freq = [0] * 26
    i = 0
    while i < len(s):
        # Case 1: Two-digit with #
        if i+2 < len(s) and s[i+2] == '#':
            num = int(s[i:i+2])  # 10-26
            ch = chr(ord('a') + num - 1)
            count = 1
            i += 3
            # check for (n)
            if i < len(s) and s[i] == '(':
                j = i+1
                while j < len(s) and s[j] != ')':
                    j += 1
                count = int(s[i+1:j])
                i = j+1
            freq[ord(ch)-ord('a')] += count

        # Case 2: Single digit (1-9)
        elif s[i].isdigit():
            num = int(s[i])
            ch = chr(ord('a') + num - 1)
            count = 1
            i += 1
            # check for (n)
            if i < len(s) and s[i] == '(':
                j = i+1
                while j < len(s) and s[j] != ')':
                    j += 1
                count = int(s[i+1:j])
                i = j+1
            freq[ord(ch)-ord('a')] += count

        else:
            i += 1  # skip unexpected chars

    return freq
