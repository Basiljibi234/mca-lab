color_name=raw_input("enter comma-seperated color name:")
colors=color_name.split(',')
color=[color.strip() for color in colors]
if len(colors)>=2:
	print("first color: ",colors[0])
	print("last color: ",color[-1])
else:
	print("please enter at least two color names.")
