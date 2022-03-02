from tkinter import *

class Application:
    def __init__(self,nom="",couleur="#AFBDD8",dim="400x200"):
        self.app = Tk()
        self.app.title(nom)
        self.app.geometry("400x200")
        self.app.configure(bg=couleur)

        self.widget1()
        self.widget2()
        self.widget3()
        self.widget4()
        self.widget5()
        self.bouton()
        self.app.mainloop()
        
    def widget1(self):
        
        self.l1 = Label(self.app, text="largeur de lame : ", background="#7289B6", foreground="white")
        self.l1.grid(row=0, column=0)
        self.en1 = Entry(self.app)
        self.en1.grid(row=0, column=1)

    def widget2(self):
        
        self.l2 = Label(self.app, text="longeur de lame : ")
        self.l2.grid(row=1, column=0)
        self.en2 = Entry(self.app)
        self.en2.grid(row=1, column=1)

    def widget3(self):
        
        self.l3= Label(self.app, text="m² : ", background="#7289B6", foreground="white")
        self.l3.grid(row=2, column=0)
        self.en3 = Entry(self.app)
        self.en3.grid(row=2, column=1)

    def widget4(self):
        
        self.l4 = Label(self.app, text="Espacement : ")
        self.l4.grid(row=3, column=0)
        self.en4 = Entry(self.app)
        self.en4.grid(row=3, column=1)

    def widget5(self):
        
        self.l5 = Label(self.app, text="prix HT : ", background="#7289B6", foreground="white")
        self.l5.grid(row=4, column=0)
        self.en5 = Entry(self.app)
        self.en5.grid(row=4, column=1)
        
    def bouton(self):
        self.b = Button(self.app,text="calculer", command=self.calcul, background = "#E7B575", foreground = "#588C72",activebackground="grey", activeforeground="white")
        self.b.grid(row=6,column=0)
        

    def calcul(self):
        try:
            largeur = float(self.en1.get())
            longueur = float(self.en2.get())
            m_2 = float(self.en3.get())
            espace = float(self.en4.get())
            p_ht = float(self.en5.get())
            
            c = espace*largeur/10000 # c= largeur de la planche * espace entre chaque planche pour obtenir le nombre de m² à enlever
            d=(longueur*largeur)/10000 # m² par planche
            e = m_2-c # e = nombre de metre carre total - c (nombre de m² à enlever)
            resultat = round(e/d) 

            if resultat>1:
                self.ltot = Label(self.app, text=f"Il vous faut {resultat} lames de bois en {longueur}cm x {largeur}cm", background="#AFBDD8" )
                self.ltot.grid(row=6, column=1)
            else:
                self.ltot = Label(self.app, text=f"Il vous faut {resultat} lames de bois en {longueur}cm x {largeur}cm", background="#AFBDD8")
                self.ltot.grid(row=6, column=1)

            self.prix=Label(self.app, text=f"Vous en aurez pour {round(e*(p_ht+(p_ht*20/100)),2)} euros TTC", background="#AFBDD8")
            self.prix.grid(row=7, column=1)

        except:
            self.erreur=Label(self.app, text="!!! une erreur s'est glissée... \n\
                 Verifiez ce que vous avez rentrer !!!", background="#AFBDD8",foreground="#D10F0F")
            self.erreur.grid(row=8, column=1)
           
    
app = Application("Calcul de terrasse en bois")

