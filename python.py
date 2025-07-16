# def rev(arr,start,end):
#     if start>=end:
#         return 
#     arr[start],arr[end] = arr[end],arr[start]
#     rev(arr,start+1,end-1)
# arr = [1,2,3,4,5]
# rev(arr,0,4)
# print(arr)

# def gcd(a,b):
#     while b :
#         a,b = a,a%b
#     return a
# print(gcd(5,15))

# def fib(n):
#     if n == 0 :
#         return 0 
#     if n ==1 :
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(5))

# def hashing(arr1,arr2):
#     d = dict()
#     for i in arr1:
#         if d.get(i):
#             d[i] = d[i]+1
#         else:
#             d[i] = 1
#     print(d)
# arr1 = [1, 2, 1, 3, 2]
# arr2 = [1, 3, 4, 2, 10]
# hashing(arr1,arr2)

# print(eval(input("Enter the expression :")))  # Example of using eval to evaluate an expression

# def bubble(arr):
#     n = len(arr)
#     for i in range(n-1,-1,-1):
#         for j in range(0,i):
#             if arr[j]>arr[j+1]:
#                 arr[j] ,arr[j+1] = arr[j+1],arr[j]
#     print(arr)
# bubble([5,4,3,2,1])

# def bubble(arr,n):
#     if n == 1:
#         return 
#     for i in range(n-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1] = arr[i+1],arr[i]
#     bubble(arr,n-1)
# arr = [5,4,3,2,1]
# print(arr)
# bubble(arr,5)
# print(arr)

# def insert(arr,n):
#     if n ==1 :
#         return 
#     for i in range(n-1,0,-1):
        

# def quickSort(arr,left,right):
#     if left < right :
#         pIndex = partition(arr,left,right)
#         quickSort(arr,left,pIndex-1)
#         quickSort(arr,pIndex+1,right)
# def partition(arr,left,right):
#     pivot = left 
#     i = left 
#     j = right
#     while i < j :
#         while arr[i]<=arr[pivot] and i<right:
#             i+=1
#         while arr[j] > arr[pivot] and j> left:
#             j-=1
#         if i < j :
#             arr[i] , arr[j] = arr[j],arr[i]
#     arr[left],arr[j] = arr[j],arr[left]
#     return j
# arr = [5,4,3,2,1]
# quickSort(arr,0,4)
# print(arr)

# def findSecondSmall(arr):
#     small = float('inf')
#     second_small = float('inf')
#     for i in arr:
#         if i < small:
#             second_small = small
#             small = i 
#         elif i < second_small and i!=small :
#             second_small = i
#     return second_small
# print(findSecondSmall([1,2,3,4,5]))

# def dup(arr):
#     i =  0 
#     n = len(arr)
#     for j in range(1,n):
#         if arr[i]!=arr[j] :
#             i+=1
#             arr[i] = arr[j]
#     print(arr[:i+1])
# dup([1,2,2,3,4,4,4,5])
            

# def rotate(arr):
#     n = len(arr)
#     first = arr[0]
#     for i in range(n-1):
#         arr[i] = arr[i+1]
#     arr[n-1] = first 
#     print(arr)
# rotate([1,2,3,4,5])
        
# def rotate(arr,k):
#     n = len(arr)
#     temp = []
#     for i in range(n-k,n):
#         temp.append(arr[i])
#     for i in range(n-k-1,-1,-1):
#         arr[i+k] = arr[i]
#     for i in range(k):
#         arr[i] = temp[i]
#     print(arr)
# rotate([1,2,3,4,5],3)

# def zero(arr):
#     n = len(arr)
#     last = n-1 
#     i = 0 
#     while i < last :
#         if arr[i] == 0 :
#             arr[i], arr[last] = arr[last] ,arr[i]
#             last-=1
#         else:
#             i+=1
#     print(arr)
# zero([1,0,3,0,5,0])

# def union(arr1,arr2):
#     i, j = 0,0
#     n,m = len(arr1),len(arr2)
#     un = []
#     while i<n and j < m :
#         if arr1[i]<=arr2[j]:
#             if len(un)==0 or un[-1]!=arr1[i]:
#                 un.append(arr1[i])
#             i+=1
#         else:
#             if len(un)==0 or un[-1]!=arr2[j]:
#                 un.append(arr2[j])
#             j+=1
#     while i < n and un[-1]!=arr1[i]:
#         un.append(arr1[i])
#         i+=1
#     while j < m and  un[-1]!=arr2[j]:
#         un.append(arr2[j])
#         j+=1
#     print(un)
# union([1,2,3,4,4,7,8],[1,1,5,6,7,8])        

# def maxOnes(arr):
#     count = 0 
#     maxi = 0 
#     for i in arr:
#         if i == 1:
#             count+=1
#             maxi = max(maxi,count)
#         else:
#             count = 0 
#     print(maxi)
# maxOnes([1,1,0,1,1,1])

# def majorityElement(arr):
#     # Size of the given array
#     n = len(arr)
#     cnt = 0  # Count
#     el = None  # Element

#     # Applying the algorithm
#     for i in range(n):
#         if cnt == 0:
#             cnt = 1
#             el = arr[i]
#         elif el == arr[i]:
#             cnt += 1
#         else:
#             cnt -= 1

#     # Checking if the stored element is the majority element
#     cnt1 = 0
#     for i in range(n):
#         if arr[i] == el:
#             cnt1 += 1

#     if cnt1 > (n / 2):
#         return el
#     return -1


# def maxProfit(arr):
#     maxPro = 0
#     minPrice = float('inf')
#     for i in range(len(arr)):
#         minPrice = min(minPrice, arr[i])
#         maxPro = max(maxPro, arr[i] - minPrice)
#     return maxPro

# def RearrangebySign(A, n):
#     # Define 2 lists, one for storing positive 
#     # and other for negative elements of the array.
#     pos = []
#     neg = []
    
#     # Segregate the array into positives and negatives.
#     for i in range(n):
#         if A[i] > 0:
#             pos.append(A[i])
#         else:
#             neg.append(A[i])
    
#     # If positives are lesser than the negatives.
#     if len(pos) < len(neg):
#         # First, fill array alternatively till the point 
#         # where positives and negatives are equal in number.
#         for i in range(len(pos)):
#             A[2*i] = pos[i]
#             A[2*i+1] = neg[i]
        
#         # Fill the remaining negatives at the end of the array.
#         index = len(pos)*2
#         for i in range(len(neg)-len(pos)):
#             A[index] = neg[len(pos)+i]
#             index += 1
    
#     # If negatives are lesser than the positives.
#     else:
#         # First, fill array alternatively till the point 
#         # where positives and negatives are equal in number.
#         for i in range(len(neg)):
#             A[2*i] = pos[i]
#             A[2*i+1] = neg[i]
        
#         # Fill the remaining positives at the end of the array.
#         index = len(neg)*2
#         for i in range(len(pos)-len(neg)):
#             A[index] = pos[len(neg)+i]
#             index += 1
    
#     return A
