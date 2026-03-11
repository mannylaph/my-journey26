oldnumber = "+49 (176) 123-4567"

newnumber = oldnumber.replace("+","").replace("(","").replace(")","").replace(" ","").replace("-","")

print(f" old number: {oldnumber}\nnew number: {newnumber}")