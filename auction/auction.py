more_people = True
auction = {}
while more_people:
  key = input("enter your name  ")
  bid = int(input("enter your bid  "))
  more = input("is there more people  ")
  if more == "no":
      more_people = False
  auction[key]=bid
max =0
name = ""
for keys in auction:
  if auction[keys]>max:
    max= auction[keys]
    name= key
print("    ",name)
  
