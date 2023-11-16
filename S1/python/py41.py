import json
data={
	"name":"john",
	"age":30,
	"city":"new york"
}
json_data=json.dumps(data,indent=4)
print("json data:")
print(json_data)
json_string='{"name":"alice","age":25,"city":"london"}'
parsed_data=json.loads(json_string)
print("parsed data:")
print(parsed_data)
json_string='{"name":"alice","age":25,"city":"london"}'
parsed_data=json.loads(json_string)
print("json data:",parsed_data)
