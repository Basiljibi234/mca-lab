list1=input("enter the first list:")
list2=input("enter the second list:")
if(len(list1)==len(list2)):
	print("the two lists are of the same length")
else:
	print("the two lists are  not of the same length")
sum1=sum(list1)
sum2=sum(list2)
if sum1==sum2:
	print("the two lists are of the same value")
else:
	print("the two lists are not of the same value")
set1=set(list1)
set2=set(list2)
intersection = set1&set2
if intersection :
	print("the two list have at least one value in common")
else:
	print("the two list have no value in common")
