my_dict={'one':1,'three':3,'five':5,'two':2,'four':4}
sorted_dict_asc=dict(sorted(my_dict.items()))
print("dictionary in asending order by keys:",sorted_dict_asc)
sorted_dict_desc=dict(sorted(my_dict.items(),reverse=True))
print("dictionary in desending order by keys:",sorted_dict_desc)
sorted_dict_asc_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary in Ascending Order by Values:", sorted_dict_asc_values)
sorted_dict_desc_values = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Dictionary in Descending Order by Values:", sorted_dict_desc_values)



