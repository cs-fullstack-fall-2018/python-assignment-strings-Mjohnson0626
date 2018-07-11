import os

os.system("clear")
#
#
# bandmate = "Ringo"
# #1
# print("the name is this long", len(bandmate))
# #2
# print(bandmate.upper())
# print(bandmate.lower())
# #3
# print(bandmate[2])
# #4
# print(bandmate[1:4])
# #5
# print(bandmate[3:])


# yourname = input('what is your name')
# print(
# print("Hi",yourname)
# print("what is your mane".upper())

name1 = input("What are your names?")
name2 = input("Your name?")
name3 = input("And you?")
print(name1 + name2 + name3, "it is nice to meet you")
if(len(name3) > len(name1) and len(name2)):
    print(name3, "is the longest name with", len(name3),"letters")
elif(len(name1) or len(name2) > len(name3)):
    print(name3, "is not the longest name")
else:
    print(name3, "is not the longest name")