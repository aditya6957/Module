def binary_search(arr,SearchElement):
   l=0
   r=len(arr)-1
   while(l<=r):
      mid=(l+r)//2
      if(arr[mid]==SearchElement):
         return mid
      elif(SearchElement<arr[mid]):
         r=mid-1
      elif(SearchElement>arr[mid]):
         l=mid+1
   return -1

print("CREATE YOUR ARRAY")
test_array=list(map(int,input("array elements :").strip().split()))
test_array.sort()
print("Your Sorted Array: ", test_array)
SearchElement = int(input("ENTER THE ELEMENT YOU WANT TO SEARCH: "))
print(binary_search(test_array, SearchElement))