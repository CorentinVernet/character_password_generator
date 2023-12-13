import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

def generer_mot_de_passe_clicked():
    try:
        longueur_mot_de_passe = int(entry_longueur.get())
        mot_de_passe_genere = generer_mot_de_passe(longueur_mot_de_passe)
        pyperclip.copy(mot_de_passe_genere)  # Copier le mot de passe généré dans le presse-papiers
        messagebox.showinfo("Mot de passe généré", f,"Votre mot de passe généré a été copié dans le presse-papiers:\n{mot_de_passe_genere}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide pour la longueur.")

def on_enter_key(event):
    generer_mot_de_passe_clicked()

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Générateur de mot de passe aléatoire")
fenetre.geometry("300x150")

label_longueur = tk.Label(fenetre, text="Longueur du mot de passe :")
label_longueur.pack()

entry_longueur = tk.Entry(fenetre)
entry_longueur.pack()
entry_longueur.bind("<Return>", on_enter_key)  # Associer la touche "Enter" à la fonction on_enter_key

btn_generer = tk.Button(fenetre, text="Générer le mot de passe", command=generer_mot_de_passe_clicked)
btn_generer.pack()

fenetre.mainloop()