import time
import tkinter as tk
import datetime
import os

def save(text, file):
    with open(file, "a") as f:
        f.write(text)

#on regarde si on a deja lancer le programme une fois dans la journé

def check_program_launch():
    today = datetime.date.today()
    file_path = "./program_launch.txt"
    
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            date_in_file = f.read()
            if date_in_file == str(today):
                print("Program has already been launched today.")
                return
            else:
                print("First launch of the day.")
                with open(file_path, "w") as f:
                    f.write(str(today))
                save(f"\nCalcul du {str(today)}\n\n", "./calcul.txt")

    else:
        with open(file_path, "w") as f:
            f.write(str(today))
        print("First launch of the day.")

check_program_launch()


def calcul(event):
    heure = time.strftime("%H:%M:%S")
    save(f"[{heure}] > {text_entry.get()} \n", "./calcul.txt")
    try :
        result = eval(text_entry.get())
    except: #noqa:E722
        result = "Les lettres ne sont pas compatible"
    
    text_entry.delete(0, tk.END)
    
    save(f"[{heure}] > ans : {str(result)} \n", "./calcul.txt")
    affiche()



#on affiche le contenu du fichier calcul.txt en haut et on l'aligne a droite et si la ligne contient le mot ans on met la ligne en vert #noqa E501

def affiche():
    with open("./calcul.txt", "r") as f:
        lines = f.readlines()
        text_widget.delete('1.0', tk.END)  # Effacer le contenu actuel du widget Text
        for line in lines:
            if "ans" in line:
                text_widget.insert(tk.END, line, 'green_tag')  # Insérer la ligne avec le tag 'green_tag' #noqa:E501
            else:
                text_widget.insert(tk.END, line)

window = tk.Tk()

window.geometry("800x500")
window.title("Mathematica")
window.configure(background="black")

text_entry = tk.Entry(window)
text_entry.bind("<Return>", calcul)
text_entry.pack(side=tk.BOTTOM, fill=tk.X)

text_widget = tk.Text(window, font=("Arial", 12), fg="white", bg="black", bd=0, highlightthickness=0, relief=tk.FLAT, wrap="word") #noqa:E501
text_widget.pack(anchor="w")

text_widget.tag_config('green_tag', foreground='green')  # Définir le tag 'green_tag' avec la couleur verte #noqa:E501

affiche()

# Run the window's event loop
window.mainloop()