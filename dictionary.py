info = {
    "name" : "talha",
    "address" : "pakpattan",
    "marks": 77,
"subjects" : ["C" , "c++" , "java"],
"tuple" : (5 , 6 , 3 , 2)

}
print(info)
#nested dictionary in which we add new dictionary
student = {
    "name" : "talha",
    "roll no": {
        "saad" : 5034,
        "afnan" : 5027,
    }
}
print(student ["roll no"]["afnan"])
#dictionary key
#if we print all key then we use mydic .key()
plyer = {
    "babar azam" : 76,
    "virat kholi" : 66,
    "sachin" : 99,
}
print(plyer.keys())
#dictionary value
#if we print all value then we use mydic. value()
plyer = {
    "babar azam" : 76,
    "virat kholi" : 66,
    "sachin" : 99,
}
print(plyer.values())
#item in which we print pair of tuple
plyer = {
    "babar azam" : 76,
    "virat kholi" : 66,
    "sachin" : 99,
}
print(plyer.items())
#update dictionary in which we add new kye and value
plyer = {
    "babar azam" : 76,
    "virat kholi" : 66,
    "sachin" : 99,
}
plyer.update({"city" : "pakpattan" ,})
print(plyer)
#my dic.get("key")
#they are use in program /n
# they not give error other line of program