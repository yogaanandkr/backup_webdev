data = [10]
import pickle
bin_data = pickle.dumps(data)
file = open("bin_data.txt", "wb")
file.write(bin_data)
file.close()
# print(bin_data)
# dec_data = pickle.loads(b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.')
# print(dec_data)

# file = open("bin_data.txt", "a")
# file.write(f'   ===>   {str(pickle.loads(bin_data))}')
# file.close()

file = open("bin_data.txt", "rb")
file2 = open("bin_data.txt", "a")
a = file.read()
org_data = pickle.loads(bin_data)
file2.write(f'  ===>  {str(org_data)}')
print(org_data)
