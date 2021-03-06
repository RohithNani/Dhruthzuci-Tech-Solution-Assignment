def print_intersection(arr1, arr2, n1, n2):
     svalues = set()

     #insert the elements in arr1[] to set s for i in range(0, n1):
     for i in range(0,n1):
         
         svalues.add(arr1[i])
     print("intersection:")
     for i in range(0,n2):
         if arr2[i] in svalues:
             print(arr2[i], end=" ")
#driver program
arr1=[]
n1 = int(input('enter no of elements for set-1 :'))

for i in range(0,n1):     
    x = int(input('enter the elements for set-1 :'))
    arr1.append(x)
arr2 = [ ]
n2 = int(input('enter no of elements for set-2 :'))
                 
for i in range(0,n2):                 
    x = int(input('enter the elements for set-2 :'))
    arr2.append(x)
print_intersection(arr1, arr2, n1, n2)
