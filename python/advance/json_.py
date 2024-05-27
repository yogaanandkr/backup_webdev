# data = [1,2,3,4,5,6,7,8]
# import json
# enc_data = json.dumps(data)
# file = open('new.txt', 'w')
# file.write(enc_data)
# file.close()

a = open('new.txt', 'r')
enc_data = a.read()
import json
org_data = json.loads(enc_data)
print(type(org_data))   
print(org_data)
print(type(org_data))
a.close