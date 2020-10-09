dir(dict)
print(dir(dict))

##   HOW TO SHOW THE VALUE IN THE FORM OF PERSENT 
# a={1:"anu", 2:"souvik", 3:"sonam", 4:"Ayan", 5:"Aryan", 6:"puja", 7:"priya"}
# print(a)
# print("my friend is %s" %a[7])  

# b={"a1":1,"a2":2,"a3":3,"a4":4, "a5":5, "a6":6, "a7":7}
# print(b)
# print("my choosen number is %d" %b["a5"])

##  HOW TO USE AN STRING METHOD IN THE DICTIONARY
# u=input("Enter your group : ")
# u1=u.upper()
# c={"A":30000, "B":22000, "C":15000, "D":10000}
# print("the salary of group ",u, " salary is ",c[u1])



##  HOW TO SHOW THE VALUES OF THE DISC.
# a={1:"anu", 2:"souvik", 3:"sonam", 4:"Ayan", 5:"Aryan", 6:"puja", 7:"priya"}
# print(a)
# m=a.values()
# print(m)

##  HOW TO UPDATE THE VALUE OF THE DISC 
# a={1:"anu", 2:"souvik", 3:"sonam", 4:"Ayan", 5:"Aryan", 6:"puja", 7:"priya"}
# print(a)
# a.update({4:"Ishita",7:"Sanjana"})
# print(a)


##  HOW TO USE THE UPDATE METHOD IN THE DISC. IN A MINI PROJECT FROM USER 
# a={1:"anu", 2:"souvik", 3:"sonam", 4:"Ayan", 5:"Aryan", 6:"puja", 7:"priya"}
# print(a)
# m=int(input ("Enter the index no. : "))
# m1=input("Enter your update name : ")
# a.update({m:m1})
# print(a)


##  HOW TO USE POPITEM IN DISC TO REMOVE THE LAST PAIR
# a={1:"anu", 2:"souvik", 3:"sonam", 4:"Ayan", 5:"Aryan", 6:"puja", 7:"priya"}
# print(a)
# a.popitem()
# print(a)


##  HOW TO USE POP IN DISC TO REMOVE THE FIRST PAIR
# a={1:"anu", 2:"souvik", 3:"sonam", 4:"Ayan", 5:"Aryan", 6:"puja", 7:"priya"}
# print(a)
# a.pop(5)
# print(a)


##  HOW TO USE KEY VALUES AND SHOW THE KEY AND VALUE SEPERETLY
# a={1:"anu", 2:"souvik", 3:"sonam", 4:"Ayan", 5:"Aryan", 6:"puja", 7:"priya"}
# print(a)
# a.keys()
# print(a.keys())
# print(a.values())


##  HOW TO USE ITEMS FOR SHOWING SEPRETALY IN PAIRS
# a={1:"anu", 2:"souvik", 3:"sonam", 4:"Ayan", 5:"Aryan", 6:"puja", 7:"priya"}
# b=a.items()
# print(b)


##  HOW TO USE GET FOR USING SHOW THE KEYS VALUE
# a={1:"anu", 2:"souvik", 3:"sonam", 4:"Ayan", 5:"Aryan", 6:"puja", 7:"priya"}
# b=a.get(2)
# print(b)


## HOW TO USE FOR CLEAR ALL THE VALUES AND KEYS
# a={1:"anu", 2:"souvik", 3:"sonam", 4:"Ayan", 5:"Aryan", 6:"puja", 7:"priya"}
# print(a)
# a.clear()
# print(a)


##HOW TO USE COPY FOR COPY ALL THE VALUES AND KEYS
# a={1:"anu", 2:"souvik", 3:"sonam", 4:"Ayan", 5:"Aryan", 6:"puja", 7:"priya"}
# print(a)
# b=a.copy()
# print(b)
