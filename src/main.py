name=input("enter name:")
previous=int(input("previous reading:"))
current =int(input("current readin:g"))

usage =current - previous
bill=usage * 150

print("usage:",usage)
print("bill:",bill)
