s="arun,vivek,ebin,mega,anagha,athul,jon"
c=s.split(",")
print(c)
name=[i for i in c if i[0] not in 'aeiou']
print(name)