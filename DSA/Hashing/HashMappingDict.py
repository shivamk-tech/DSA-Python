list = [1,2,3,4,4,7,4,9,2,7,9,4]
Hash_Dict = {}

for i in list:
    Hash_Dict[i] = Hash_Dict.get(i, 0) + 1 #here the get function will return an x if x return in the list and if not, the 0 will be returned

print(Hash_Dict)