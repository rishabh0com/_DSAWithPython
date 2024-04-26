thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

demodict = {"brand": "Mahidra", "model": "Mustang", "year": 1964}


print("thisdict : ", thisdict)
print("demodict : ", demodict)
print()

print("> access items form dictionary:")
print("thisdict['brand'] #", thisdict["brand"])
print("thisdict.get('brand') #", thisdict.get("brand"))
print()

print("> thisdict.keys() #", thisdict.keys())
print()

print("> thisdict.values() #", thisdict.values())
print()

print("> thisdict.items() #", thisdict.items())
print()

print("> change or update values in dictionary :")
print("thisdict['year'] = 2003;")
thisdict["year"] = 2003
print("thisdict.update({'model':'Endever'})")
thisdict.update({"model": "Endever"})
print()

print("> add items in dictionary:")
demodict["color"] = "red"
print("demodict['color'] = 'red' #", demodict.items())
demodict.update({"wheels": 4})
print("demodict.update({'wheels': 4}) #", demodict.items())
print()

print("> remove or delete key:value and dictionary:")
demodict.pop("model")
print("demodict.pop('model') #", demodict.items())
demodict.popitem()
print("demodict.popitem(): it removes last item # ", demodict.items())
print()


print("> looping on dictionary:\n for key in thisdict:")
for key in thisdict:
    print("     print(key,':',thisdict[key]) #", key, ":", thisdict[key])
print()

print("for key in demodict.keys():")
for key in demodict.keys():
    print("    print(key) #", key)
print()

print("for value in demodict.values():")
for value in demodict.values():
    print("    print(value) #", value)
print()

print("for key,value in demodict.items():")
for key, value in demodict.items():
    print("   print(key,values) #", key, value)
print()

print("> check if itme is exsist or not:")
if "model" in thisdict:
    print("if 'model' in thisdict:", "yes")
if "mode" not in thisdict:
    print("if 'mode' not in thisdict:", "yes")
