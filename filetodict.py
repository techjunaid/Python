# a_dictionary = {}
# a_file = open("list.txt")
# for line a_file:
#     key,value = line.split()
#     
#     
# f = open("list.txt",'r')
# answer = {}
# for line in f :
#     k,v  = line.strip().split(' ')
#     answer[k.strip()] = v.strip()
# f.close()


d = {}
with open("list.txt") as f:
    for line in f:
        (key) = line.split()
        d[int(key)] = val

print(d)






