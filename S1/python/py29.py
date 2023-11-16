numbers=raw_input("enter a list of numbers seperated by spaces: ")
numbers_list=list(map(int,numbers.split()))
total_sum=sum(numbers_list)
print("sum of all items int the list:",total_sum)
