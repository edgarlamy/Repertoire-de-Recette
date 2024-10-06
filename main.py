from tkinter import *
import csv
global rIdx

recettes = []
petit_dej_dico = []
dej_diner_dico = []
dessert_dico = []


def csv_list():
    global recettes
    with open('RECETTES.csv', 'r', encoding="utf-8") as recette:
        csv_reader = csv.DictReader(recette)
        recettes = [row for row in csv_reader]
    return recettes

rIdx=0

#Cette fonction permet de séparer les recettes en fonction de leur catégorie
#Cela ajoute le nom du recette a la liste
def type_recette():
    csv_list()
    for t in recettes:
        if t["Type_Repas"] == "Petit_Dej":
            petit_dej_dico.append(t)
        if t["Type_Repas"] == "Dej_Diner":
            dej_diner_dico.append(t)
        if t["Type_Repas"] == "Dessert":
            dessert_dico.append(t)


def signup():
    global messagelabel
    username = username_entry.get()
    password = password_entry.get()
    if username != "" and password != "":
        with open("UTILISATEUR.csv", "a", newline="") as csvf:
            writer_object = csv.writer(csvf)
            writer_object.writerow([username, password])
            csvf.close()
        messagelabel['text'] = "Vous vous êtes bien inscrit !"
        fenetre_login.after(2000, clear_message_label)
    else:
        messagelabel['text'] = "Inscription échouée; aucune saisie détectée"
        fenetre_login.after(2000, clear_message_label)


def login():
    username = username_entry.get()
    password = password_entry.get()

    with open("UTILISATEUR.csv", "r") as csvf:
        reader = csv.reader(csvf)
        for row in reader:
            if row[0] == username and row[1] == password:
                messagelabel['text'] = "Connection réussie!"
                fenetre_login.after(2000, clear_message_label)
                fenetre_login.destroy()
                main_page()
                return
        messagelabel['text'] = "Connection échouée! Mot de passe / utilisateur inconnu !"
        fenetre_login.after(2000, clear_message_label)
        clear_text_box_in_login()


def clear_text_box_in_login():
    username_entry.delete(0, END)
    password_entry.delete(0, END)


def clear_message_label():
    messagelabel['text'] = ""
    
def status_reset():
    statusLabel['text']="Veuillez rajouter la specificité de la recette que vous voulez ajouter. Ordre : nom -> ingredients -> preparation"

def quit_app():
    exit()


def Revenir(fen, page_avant):
    fen.destroy()
    page_avant()

#trueCake() et newRecipeInfo() rajoutent une recette à RECETTES.csv()


def trueCake(): 
    recipeAddition.destroy()
    main_page()
    nomNourriture=foodName.get()
    ingredients=ingredientsPack
    resetti=recipe
    typeOfFood=typeRepas.get()

    if nomNourriture != "" and ingredients != "" and resetti!="":
        if (typeOfFood=="Petit_Dej" or typeOfFood=="Dej_Diner" or typeOfFood=="Dessert"):
            with open("RECETTES.csv", "a", newline="") as csvf:
                writer_object = csv.writer(csvf)
                writer_object.writerow([rIdx+1, nomNourriture, ingredients, resetti, typeOfFood])
                csvf.close()
            statusLabel['text'] = "Vous avez bien rajouté la recette !"
        else:
            statusLabel['text']="Veuillez bien conformer au type de repas: Petit_Dej, Dej_Diner, Dessert"
        recipeAddition.after(2000, status_reset)
    else:
        statusLabel['text'] = "Entrées obligatoires manquantes !"
        recipeAddition.after(2000, status_reset)

def newRecipeInfo():
    main_fenetre.destroy()
    global foodName
    global ingredientsPack
    global recipe
    global typeRepas
    global statusLabel
    global orderLabel
    global recipeAddition
    
    recipeAddition=Tk()
    recipeAddition.title("Rajout de recette")
    recipeAddition.geometry('600x400')
    recipeAddition.configure(bg='light grey')

    revenir_button = Button(
        recipeAddition,
        text="Revenir",
        command=lambda: Revenir(recipeAddition, main_page))
    revenir_button.pack()
    
    statusLabel=Label(recipeAddition, text="Veuillez rajouter la specificité de la recette que vous voulez ajouter.", bg='light grey', fg="dark turquoise")
    statusLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

    statusLabel=Label(recipeAddition, text="Ordre : nom -> type de repas comme sur Main Page -> ingredients -> preparation", bg='light grey', fg="dark turquoise")
    statusLabel.place(relx=0.5, rely=0.15, anchor=CENTER)
    
    foodName=Entry(recipeAddition, width=35)
    foodName.place(relx=0.5, rely=0.25, anchor=CENTER)

    typeRepas=Entry(recipeAddition, width=10)
    typeRepas.place(relx=0.5, rely=0.35, anchor=CENTER)
    
    ingredientsPack=Text(recipeAddition, width=50, height=7)
    ingredientsPack.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    recipe=Text(recipeAddition, width=50, height=7)
    recipe.place(relx=0.5, rely=0.75, anchor=CENTER)

    addedRecipe=Button(recipeAddition, text="Confirmer", command=trueCake)
    addedRecipe.place(relx=0.5, rely=0.95, anchor=CENTER)



def recette_page_temp(recette_choisi, fenetre_avant):
    fenetre_temp = Tk()
    h = Scrollbar(fenetre_temp, orient="vertical")
    h.pack(side="right", fill="y")
    fenetre_temp.title(recette_choisi["Recette"])
    fenetre_temp.geometry('600x400')
    fenetre_temp.configure(bg="white")
    revenir_button = Button(
        fenetre_temp,
        text="Revenir",
        command=lambda: Revenir(fenetre_temp, fenetre_avant))
    revenir_button.pack()
    t = Text(fenetre_temp,
             width=15,
             height=23,
             wrap=NONE,
             yscrollcommand=h.set)
    t.insert(END, f'{recette_choisi["Recette"]}\n\n\n')
    t.insert(END, f'{recette_choisi["Ingredient"]}\n\n\n')
    t.insert(END, f'{recette_choisi["Etape"]}')

    Font_tuple = ("Helvetica", 12, "bold")
    t.configure(font=Font_tuple)
    t.config(state="disabled", wrap="word")
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)


def dessert():
    main_fenetre.destroy()
    global fenetre_dessert
    fenetre_dessert = Tk()
    h = Scrollbar(fenetre_dessert, orient="vertical")
    h.pack(side="right", fill="y")
    fenetre_dessert.title("Page Dessert")
    fenetre_dessert.geometry('600x400')
    fenetre_dessert.configure(bg="beige")

    h = Scrollbar(fenetre_dessert, orient="vertical")
    h.pack(side="right", fill="y")
    
    revenir_button = Button(
        fenetre_dessert,
        text="Revenir",
        command=lambda: Revenir(fenetre_dessert, main_page))
    revenir_button.pack(pady=(0,20))

    for i in dessert_dico:
        button = Button(fenetre_dessert,
                        text=i["Recette"],
                        command=lambda x=i: recette_page_temp(x, dessert), font=("Helvetica", 15))
        button.pack(pady=(0,10))

    Font_tuple = ("Helvetica", 12, "bold")
    t.configure(font=Font_tuple)
    t.config(state="disabled", wrap="word")
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)

    fenetre_dessert.mainloop()


def dej_din():
    main_fenetre.destroy()
    global fenetre_dej_din
    fenetre_dej_din = Tk()
    fenetre_dej_din.title("Page Dejeuner-Diner")
    fenetre_dej_din.geometry('600x400')
    fenetre_dej_din.configure(bg="beige")
    h = Scrollbar(fenetre_dej_din, orient="vertical")
    h.pack(side="right", fill="y")
    
    revenir_button = Button(
        fenetre_dej_din,
        text="Revenir",
        command=lambda: Revenir(fenetre_dej_din, main_page))
    revenir_button.pack(pady=(0,20))

    for i in dej_diner_dico:
        button = Button(fenetre_dej_din,
                        text=i["Recette"],
                        command=lambda x=i: recette_page_temp(x, dej_din), font=("Helvetica", 15))
        button.pack(pady=(0,10))

    fenetre_dej_din.mainloop()


def petit_dej():
    main_fenetre.destroy()
    global fenetre_petit_dej
    fenetre_petit_dej = Tk()
    fenetre_petit_dej.title("Page Petit Dejeuner")
    fenetre_petit_dej.geometry('600x400')
    fenetre_petit_dej.configure(bg="beige")

    h = Scrollbar(fenetre_petit_dej, orient="vertical")
    h.pack(side="right", fill="y")
    
    revenir_button = Button(
        fenetre_petit_dej,
        text="Revenir",
        command=lambda: Revenir(fenetre_petit_dej, main_page))
    revenir_button.pack(pady=(0,20))

    for i in petit_dej_dico:
        button = Button(fenetre_petit_dej,
                        text=i["Recette"],
                        command=lambda x=i: recette_page_temp(x, petit_dej), font=("Helvetica", 15))
        button.pack(pady=(0,10))

    fenetre_petit_dej.mainloop()


def signout():
    main_fenetre.destroy()
    login_page()


def main_page():
    global main_fenetre
    main_fenetre = Tk()
    main_fenetre.title("Main Page")
    main_fenetre.geometry('600x400')
    main_fenetre.configure(bg="White")

    img = PhotoImage(file="main_page_pic.png")
    bg_image = Label(main_fenetre, image=img, bg ="white")
    bg_image.place(x=290, y=200, relwidth=1, anchor=CENTER)
    
    petit_dej_button = Button(main_fenetre,
                              text="Petit_Dej",
                              command=petit_dej,
                              font=("Merriweather",17), bg="#FFE4B5", highlightthickness=1,
                              width=7,
                              height=1)
    petit_dej_button.place(relx=0.5, rely=0.2, anchor=CENTER)

    dej_button = Button(main_fenetre,
                        text="Dej_Diner",
                        command=dej_din,
                        font=("Merriweather",17), bg="#FFE4B5", highlightthickness=1,
                        width=7,
                        height=1)
    dej_button.place(relx=0.5, rely=0.4, anchor=CENTER)

    dessert_button = Button(main_fenetre,
                            text="Dessert",
                            command=dessert,
                            font=("Merriweather",17), bg="#FFE4B5", highlightthickness=1,
                            width=7,
                            height=1)
    dessert_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    newThingButton= Button(main_fenetre,
                           text="Nouvelle Recette",
                           command=newRecipeInfo,
                           font=("Merriweather",10), bg="#ADD8E6", width=12,
                          height=1)
    newThingButton.place(x=500,rely=0.7, anchor=CENTER)
    
    signout_button = Button(main_fenetre,
                            text="Sign Out",
                            command=signout,
                            font="Merriweather", bg="white", highlightthickness=1, width=8,
                            height=1)
    signout_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    quit_button = Button(main_fenetre,
                         text="Quit",
                         command=quit_app,
                         font="Merriweather", bg="#D22B2B", highlightthickness=1, width=8,
                         height=1)
    quit_button.place(relx=0.5, rely=0.9, anchor=CENTER)


    main_fenetre.mainloop()


def login_page():
    global fenetre_login
    global messagelabel
    global username_entry
    global password_entry
    fenetre_login = Tk()
    fenetre_login.title("Login")
    fenetre_login.geometry('600x400')
    fenetre_login.configure(bg="white")

    img = PhotoImage(file="login_page_pic.png").subsample(2, 2)
    bg_image = Label(fenetre_login, image=img, bg ="white")
    bg_image.place(x=290, y=200, relwidth=2, anchor=CENTER)
    
    messagelabel = Label(fenetre_login,
                         text="",
                         bg="white", font=("Merriweather", 11),
                         fg=('#8B0000'))
    messagelabel.pack()

    username_label = Label(fenetre_login, text="Username:", font="Merriweather", bg="white")
    username_label.pack(pady=(50,0))

    username_entry = Entry(fenetre_login)
    username_entry.pack(pady=(2,0))

    password_label = Label(fenetre_login, text="Password:", font="Merriweather", bg="white")
    password_label.pack(pady=(10,0))

    password_entry = Entry(fenetre_login, show="*")
    password_entry.pack(pady=(2,0))

    login_button = Button(fenetre_login, text="Login", command=login, font="Merriweather", bg="white", highlightthickness=0)
    login_button.pack(pady=(15,0))

    sign_up_button = Button(fenetre_login, text="Sign Up", command=signup, font="Merriweather", bg="white", highlightthickness=0)
    sign_up_button.pack(pady=(5,0))

    quit_button = Button(fenetre_login, text="Quit", command=quit_app, font="Merriweather", bg="white", highlightthickness=0)
    quit_button.pack(pady=(5,0))

    fenetre_login.mainloop()


type_recette()
login_page()
