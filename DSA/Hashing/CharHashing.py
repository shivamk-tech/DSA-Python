list = "abcdefgabfge"
Hash_List = [0]*26
print(len(list))

for ch in list:
    Hash_List[ord(ch) - ord('a')] += 1

print(Hash_List)