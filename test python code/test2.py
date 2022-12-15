phrase = "45563"

phrase_replace = phrase.replace(".", "0")

print(phrase_replace)

if phrase_replace.isdigit() == True :
    print("c'est bien une ip correct")
else :
    print("ip incorrect")
