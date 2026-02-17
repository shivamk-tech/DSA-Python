str1 = "my first name is shivam and iam from bareilyy "
str2 = "my last name is kumar and iam from bareilly too"
indexf = str1.find("shivam")
indexl = str2.find("kumar")
first = str1[indexf:]
last = str2[indexl:]
spcaef = first.index(" ")
spcael = last.index(" ")
firsn = first[:spcaef]
lastn = last[:spcael]

sentence = print(f"Hello {firsn} {lastn} Taylor! You just delved into python.")


