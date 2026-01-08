import json


data ='{"name":"Ivan","age":30,"is_student":false}'
parsed_data = json.loads(data)

print(parsed_data, type(parsed_data))



