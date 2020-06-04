import json

with open("./parson.js", 'r') as data_file:
    pass_data = json.load(data_file)
#print(pass_data)
moha = pass_data['people'][0]
print("Hello world,this is " + moha["fullname"] + " with HNGi7 ID: " + moha['ID'] + " using " + moha[
    "language"] + " for stage 2 task " + " and " + moha[
          "email"])
