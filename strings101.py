# # sentence = """I love Python.
# # Python is very easy, Python is also very
# # powerful. AI depends mostly on python.
# # Python can be used for.
# # - AI
# # - Web Design
# # - Automations
# # Python is a highly versatile language
# # """
# # print(sentence.replace('Python','Java').replace('python','Java'))

# # eurodate = "2026/03/11"
# # print(eurodate.replace("/","-"))
# name = "Manny"
# surname = "Eze"
# age = 34

# fullname =name+' '+surname
# # print("My name is ",fullname+" i am "+str(age) + " years old")
# print(f"My name is {fullname}.I am {age} years old.\nIn the next ten year, i will be {age+10} years old")


# timestamp1 = '2026-12-23'

customerinfo = "Mary-23-female-kogi"
# print(customerinfo)
print(customerinfo.split("-"))
name, age,gender,state = customerinfo.split("-")
print(f"""Customer name: {name}
          Age:{age}
          Gender:{gender}
          State of Origin: {state}
      """)
csvfile = "Rice,Naira,Africa,Market"

csvfile.split(',')
