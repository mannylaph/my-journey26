dirty ="968-Maria, ( D@t@ Engineer );; 27y.. "
clean =f"name: {dirty[4:9].lower()} | role:{dirty[12:26].lower().replace('@','a')} | age:{dirty[31:33]}"

print("*"*50)
print(dirty)
print("*"*50)
print(clean)

