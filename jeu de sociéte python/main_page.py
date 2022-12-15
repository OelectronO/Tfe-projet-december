import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import tkinter
import time
from tkinter import messagebox


import socket


#fenêtre 

win = tk.Tk()


#variable
    #
    # #081621
    # #0C2233
color_background ="#0C2233"
    #input variable
player_name = ""
player_ip = ""
player_port = ""


#connection au hub avec toute les verif
#text input placeholder
    #name

    

image_logo = Image.open("images\logo.png")
image_logo= image_logo.resize((175,175), Image.ANTIALIAS)
image_logo= ImageTk.PhotoImage(image_logo)

testtt = Image.open("images\logo.png") #Lg_Villageoi.png"

img = ImageTk.PhotoImage(Image.open("images\logo.png")) #Lg_Villageoi.png"


# image size

lengths = 125
lenght = 125

Lg_Villageois = Image.open("images\cartes\Lg_Villageois.png")
Lg_Villageois= Lg_Villageois.resize((lengths,lenght), Image.ANTIALIAS)
Lg_Villageois= ImageTk.PhotoImage(Lg_Villageois)

Lg_LoupGarou = Image.open("images\cartes\Lg_LoupGarou.png")
Lg_LoupGarou= Lg_LoupGarou.resize((lengths,lenght), Image.ANTIALIAS)
Lg_LoupGarou= ImageTk.PhotoImage(Lg_LoupGarou)

Lg_Chasseur = Image.open("images\cartes\Lg_Chasseur.png")
Lg_Chasseur= Lg_Chasseur.resize((lengths,lenght), Image.ANTIALIAS)
Lg_Chasseur= ImageTk.PhotoImage(Lg_Chasseur)

Lg_Voyante = Image.open("images\cartes\Lg_Voyante.png")
Lg_Voyante= Lg_Voyante.resize((lengths,lenght), Image.ANTIALIAS)
Lg_Voyante= ImageTk.PhotoImage(Lg_Voyante)

Lg_Sorciere = Image.open("images\cartes\Lg_Sorcière.png")
Lg_Sorciere= Lg_Sorciere.resize((lengths,lenght), Image.ANTIALIAS)
Lg_Sorciere= ImageTk.PhotoImage(Lg_Sorciere)

player_list_image= Image.open("images\cartes\Lg_button_test.png")
player_list_image= player_list_image.resize((500,100), Image.ANTIALIAS)
player_list_image= ImageTk.PhotoImage(player_list_image)

class login_page():
    def __init__(self):
        def click_name(event):

            name_input.config(state=NORMAL)
            name_input.delete(0, END)
            #ip
        def click_ip(event):

            ip_input.config(state=NORMAL)
            ip_input.delete(0, END)
            #port
        def click_port(event):

            port_input.config(state=NORMAL)
            port_input.delete(0, END)
            #end

        #button press action run --->
        def click_action_joindre():

            self.player_name = name_input.get()
            self.player_ip = ip_input.get()
            self.player_port = port_input.get()
            player_name = name_input.get()
            player_ip = ip_input.get()
            player_port = port_input.get()
            frame.destroy()
            sous_frame1.destroy()
            sous_frame2.destroy()
            connection_verif()
            #print("le nom du client est "+player_name)
            


        #setup de la page

        win.title("loup Garou")
        win.geometry("1600x900")
        #win.minsize(1600, 900)
        win.iconbitmap("images\logo.ico")
        win.config(background=color_background)



        #creer une boite
        frame = Frame(win, bg=color_background)

        sous_frame1 = Frame(frame, bg=color_background)
        sous_frame2 = Frame(frame, bg=color_background)
        button_frame = Frame(sous_frame2, bg=color_background)

        #texte
        label_title = Label(frame, text="Loup Garou", font=("Impact", 40), bg="#f2654b", fg="white")


        #texte/logo
            #Logo image
        label_logo = tkinter.Label(sous_frame1, image=image_logo, background=color_background)
        label_logo.pack()
            #texte
        label_title = Label(sous_frame1, text="Loup Garou", font=("Impact", 40), bg=color_background, fg="#03090D")
        label_title.pack()
            #end

        #text input
            #name
        name_input = Entry(sous_frame2, justify=CENTER, textvariable=player_name , font=("Segoe UI Black", 20), bg=color_background, relief=SOLID, fg="#03090D")
        #name_input.insert(0,"Votre Pseudo")
        name_input.insert(0,"OelectronO")
        name_input.config()
        name_input.bind("<Button-1>", click_name)
        name_input.pack(pady=5, ipady=10)

            #ip
        ip_input = Entry(sous_frame2, justify=CENTER, textvariable=player_ip, font=("Segoe UI Black", 20), bg=color_background, relief=SOLID, fg="#03090D")
        #ip_input.insert(0,"L'ip de connexion")
        ip_input.insert(0,"localhost")
        ip_input.config()
        ip_input.bind("<Button-1>", click_ip)
        ip_input.pack(pady=5, ipady=10)

            #port
        port_input = Entry(sous_frame2, justify=CENTER, textvariable=player_port, font=("Segoe UI Black", 20), bg=color_background, relief=SOLID, fg="#03090D")
        #port_input.insert(0,"le port de connexion")
        port_input.insert(0,"5456")
        port_input.config()
        port_input.bind("<Button-1>", click_port)
        port_input.pack(pady=5, ipady=10)

            #end

        # bouton
        connexion_button = Button(button_frame, text="Rejoindre", font=("Segoe UI Black", 25), bg=color_background, fg="#03090D", activebackground=color_background, activeforeground="#03090D" ,command=click_action_joindre, relief=SOLID, bd=1, width=15)
        connexion_button.pack()

        # ajouter
        frame.pack(expand=YES)
        sous_frame1.pack(expand=YES, pady=50)
        sous_frame2.pack(expand=YES)
        button_frame.pack(expand=YES, pady=30)

        

        #affichage

test = login_page()


def send_message(message):
    hub_player_name = "{}".format(test.player_name)
    hub_player_ip = "{}".format(test.player_ip)
    hub_player_port = "{}".format(test.player_port)
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((str(hub_player_ip),int(hub_player_port)))

    data = str(hub_player_name)
    clientSocket.send(data.encode())

def connection_verif():
    hub_player_name = "{}".format(test.player_name)
    hub_player_ip = "{}".format(test.player_ip)
    hub_player_port = "{}".format(test.player_port)
    #clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #clientSocket.connect((str(hub_player_ip),int(hub_player_port)))

    #data = str(hub_player_name)+" connexion vérif"
    #clientSocket.send(data.encode())
    hub_page()
    #dataFromServer = clientSocket.recv(1024)
    #print(dataFromServer.decode())
    #if dataFromServer.decode() == "bonjour" :
    #    hub_page()
    #    print("connexion ok")
    #else :
    #    print("connexion fail")
        #fail_connexion()


def fail_connexion():
    print("fail_page")

    fail_page = Frame(win, bg=color_background)
    label_title = Label(fail_page, text="Connexion fail", font=("Impact", 40), bg=color_background, fg="#03090D")
    label_title.pack()
    fail_page.pack(expand=YES)
def hub_page():
    hub_player_name = "{}".format(test.player_name)
    hub_player_ip = "{}".format(test.player_ip)
    hub_player_port = "{}".format(test.player_port)
    print("hub_page")
    #création de la frame
    
    role_list = Frame(win, bg=color_background)
    player_list = Frame(win, bg=color_background)




    label_title = Label(role_list, text="Rôle list", font=("Impact", 40), bg=color_background, fg="#03090D")
    label_title.pack()

    label_title = Label(player_list, text="List des joueurs", font=("Impact", 40), bg=color_background, fg="#03090D")
    label_title.pack()

    player_list_button = ["player1","player2","player3","player4","player5","player6","player7","player8"]

    for i in range(6):
        player_list_button[i] = Button(player_list, text="waiting player", font=("Segoe UI Black", 20), bg=color_background, activebackground=color_background, activeforeground="#03090D",width=15 , relief=SOLID, bd=1) #image=player_list_image
        player_list_button[i].pack(pady=10)
    

    # affichage des joueur en ligne ----> version beta
    if player_list_button[0].cget('text') == "waiting player" :
        player_list_button[0].config(text=hub_player_name)


    #scroll bar test



    role_image_list = [Lg_Villageois,Lg_LoupGarou,Lg_Chasseur,Lg_Voyante,Lg_Sorciere]

    for i in range(5) :
        panel = tkinter.Label(role_list, image=role_image_list[i], background=color_background)
        panel.pack(side = "bottom", fill = "both", expand = "yes")

    

    #Let us create a dummy button and pass the image
    
    
    #déclaration de la frame
    role_list.pack(expand=YES, side=RIGHT)
    player_list.pack(expand=YES, side=LEFT)

def on_closing():
    if messagebox.askokcancel("Logout", "Are you sure you want to disconnect ?"):
        print("exit")
        win.destroy()


win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()