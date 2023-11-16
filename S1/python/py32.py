input_string=raw_input("enter a string: ")
char_frequency={}
for char in input_string:
	char_frequency[char]=char_frequency.get (char,0)+1
print("character frequency in the string:")
for char ,frequency in char_frequency.items():
	print("{},{}".format(char,frequency))
