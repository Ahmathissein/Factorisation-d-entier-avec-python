import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from math import sqrt

class FactorizationApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x500')
        self.master.title('Factorisation d\'un nombre entier')
        
        style = Style(theme='superhero')
        self.frame = ttk.Frame(self.master, padding=20)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.label = ttk.Label(self.frame, text='Entrez un nombre entier :')
        self.label.pack(pady=10)
        
        self.entree = ttk.Entry(self.frame)
        self.entree.pack(pady=10)
        
        self.bouton = ttk.Button(self.frame, text='Factoriser', command=self.factoriser)
        self.bouton.pack(pady=10)
        
        self.resultat = ttk.Label(self.frame, text='Résultat : ')
        self.resultat.pack(pady=10)
        
    def prime_factors(self, n):
        """Renvoie la liste des facteurs premiers de n"""
        factors = []
        i = 2
        while i <= sqrt(n):
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    def format_factorization(self, n):
        """Formate la factorisation de n en utilisant la notation exponentielle"""
        if n == 1:
            return "1"
        factors = self.prime_factors(n)
        factor_counts = [(factor, factors.count(factor)) for factor in set(factors)]
        factor_counts.sort()
        return f"{n} = " + ' × '.join([f'{factor}^{count}' if count > 1 else str(factor) for factor, count in factor_counts])

    def factoriser(self):
        """Factorise l'entier entré par l'utilisateur et affiche le résultat"""
        try:
            n = int(self.entree.get())
            if n <= 0:
                self.resultat.config(text='Erreur : Entier supérieur à zéro uniquement.')
            else:
                self.resultat.config(text=f'Résultat : {self.format_factorization(n)}')
        except ValueError:
            self.resultat.config(text='Erreur : Entrée invalide.')

root = tk.Tk()
app = FactorizationApp(root)
root.mainloop()
