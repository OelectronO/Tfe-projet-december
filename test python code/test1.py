ip = "156.25a6.15.5"
verif_ip = ip.replace(".", "0")
if ip.count(".") > 0 and verif_ip.isdigit() == True:
    print("c'est une bonne ip")
else : 
    print("l'ip est pas bonne")