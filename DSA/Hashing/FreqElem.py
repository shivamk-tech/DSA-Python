list = [1,2,3,4,4,7,4,9,2,7,9,4]
Hash_List = [0]*13
print(len(list))

for i in range(len(list)):
    Hash_List[i] = 0

for i in list:
    Hash_List[i] += 1

print(Hash_List)
