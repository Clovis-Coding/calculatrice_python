import tkinter as tk

class calculatrice:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice")
        self.root.geometry("320x450")
        self.root.configure(bg="#1E1E24") 
        self.root.resizable(False, False)

        self.expression = ""

        self.equation_var = tk.StringVar()
        self.equation_var.set("0")
        
        affichage = tk.Label(self.root, textvariable=self.equation_var, 
                             font=("Helvetica", 36, "bold"), bg="#1E1E24", fg="#FFFFFF", 
                             anchor="e", padx=20, pady=20)
        affichage.pack(expand=False, fill="both")

        
        cadre_boutons = tk.Frame(self.root, bg="#1E1E24")
        cadre_boutons.pack(expand=True, fill="both", padx=5, pady=5)

        
        c_chiffre = "#2B2B36"
        c_texte = "#FFFFFF"
        c_op = "#FF9F0A"     
        c_clear = "#FF453A"  

        
        boutons = [
            ('7', c_chiffre), ('8', c_chiffre), ('9', c_chiffre), ('/', c_op),
            ('4', c_chiffre), ('5', c_chiffre), ('6', c_chiffre), ('*', c_op),
            ('1', c_chiffre), ('2', c_chiffre), ('3', c_chiffre), ('-', c_op),
            ('C', c_clear),   ('0', c_chiffre), ('=', c_op),      ('+', c_op)
        ]

        row_val = 0
        col_val = 0

        for (texte, couleur) in boutons:
            bouton = tk.Button(cadre_boutons, text=texte, font=("Helvetica", 20), 
                               bg=couleur, fg=c_texte, 
                               activebackground="#454552", activeforeground=c_texte,
                               borderwidth=0, cursor="hand2",
                               command=lambda t=texte: self.clic_bouton(t))
            
            bouton.grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(4):
            cadre_boutons.grid_columnconfigure(i, weight=1)
            cadre_boutons.grid_rowconfigure(i, weight=1)

    def clic_bouton(self, valeur):
        if valeur == 'C':
            self.expression = ""
            self.equation_var.set("0")
        elif valeur == '=':
            try:
                resultat = str(eval(self.expression))
                
                if resultat.endswith(".0"):
                    resultat = resultat[:-2]
                    
                self.equation_var.set(resultat)
                self.expression = resultat
            except ZeroDivisionError:
                self.equation_var.set("Erreur")
                self.expression = ""
            except Exception:
                self.equation_var.set("Erreur")
                self.expression = ""
        else:
            if self.expression == "" and valeur in "/*+":
                return
            if self.equation_var.get() == "0" or self.equation_var.get() == "Erreur":
                self.expression = ""
            
            self.expression += str(valeur)
            self.equation_var.set(self.expression)

if __name__ == "__main__":
    fenetre = tk.Tk()
    app = calculatrice(fenetre)
    fenetre.mainloop()