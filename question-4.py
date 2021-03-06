def findSingle(ar, n):
  res = ar[0]

  for i in range(1,n):
      res = res ^ ar[i]

  return res

#driver program
arr1=[]
n1 = int(input('enter how many elements you want :'))
for i in range(0,n1):
    x = int(input('enter the number in array :'))
    arr1.append(x)
print("elements occureng once is ", findSingle(arr1,n1))
