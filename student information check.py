inf = {
    "24811A05F0": {
        "Name" : "Nanda kihsore",
        "dept" : "CSE",
    },"24811A05G9":{
        "Name" : "MANI",
        "dept" : "CSE",
    },"245811A05E6":{
        "Name" : "Manikanta",
        "dept" : "CSE",
    },"24811A05H0":{
        "Name" : "pavan siddu",
        "dept" : "CSE",
    }
}

roll_no = (input("enter your roll no : "))
name = input("enter your name : ")
dept = input("enter your deparment : ")


if roll_no  in inf :
    print(f" your roll no :- {roll_no}  already exists ")
else:
    inf[roll_no] = {
        "Name" : name,
        "dept" : dept
    }
print(inf)