#coding=UTF-8
# import io 
# data_file = io.open("F:\\MyPro\\data.yaml", "r", encoding='utf-8')
# file= open('data.text', mode="w")
# file.write('你好')
# file.close()

# with open('data.text', mode = "w") as file:
#     file.write('HOLA, 你好')

# with open('data.text', mode = "r") as file:
#     data = file.read()
#     print(data, 'data')

# with open('data.text', mode = "w") as file:
#     file.write('5\n3')

# sum=0
# with open('data.text', mode = "r") as file:
#     for item in file:
#         sum+=int(item)
#         print(sum)


import json
with open('config.json', mode="r") as file:
    data = json.load(file)
    print(data['name'])
    data["name"] = 'Bill'
with open('config.json', mode="w") as file:
    json.dump(data, file)

