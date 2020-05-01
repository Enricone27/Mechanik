from tkinter import *
from turtle import *
from time import *
# Objekt des Erstellens des Fensters
class Fenster:
    #Die EingabeFelder und Ausführung des Horizontalen Wurfs
    class Eingaben:
        # Die diversen Widgets
        def Widgets(self):
            self.Anfangsgeschwindigkeit = Entry(self.eingaben, width = 25 )  
            self.Wurfhöhe = Entry(self.eingaben, width=25)
            self.DAnfangsgeschwindigkeit = Label(self.eingaben, text="Anfangsgeschwindigkeit: [m/sec]")
            self.DWurfhöhe = Label(self.eingaben, text="Wurfhöhe: [m]")

            self.Anfangsgeschwindigkeit.grid(row=0, column=1)
            self.Wurfhöhe.grid(row=1, column=1)
            self.DAnfangsgeschwindigkeit.grid(row=0, column=0)
            self.DWurfhöhe.grid(row=1, column=0, sticky=E)
   

            self.los = Button(self.eingaben, text="Los!",command=self.Los)
            self.los.grid(row=2, columnspan=2)
        #Werte werden genommen und weitergegeben
        def Los(self):
            self.Ag =(self.Anfangsgeschwindigkeit.get())
            self.Wh=(self.Wurfhöhe.get())
            self.ü.exe.exer.Ausführ()

        #Frame wird erstellt ;Übertragungsvariable ü
        def __init__(self,master,ü):
            self.eingaben = Frame(master)
            self.eingaben.pack()
            self.ü = ü
            self.Widgets()

    # Dort wo gemahlt wird hat ein eigenes Objekt
    class Mahlen:
        #Das zeichnes des Kooordinatensystems
        class Grid:
            #Turtel wird erstellt und versteckt
            def __init__(self,master):
                self.turtle = RawTurtle(master)
                self.turtle.ht()
                self.los()


            # basic schlechtes System mahlen
            def los(self):
                self.turtle.forward(100)
                self.turtle.left(180)
                self.turtle.forward(100)
                self.turtle.right(90)
                self.turtle.forward(50)

        # Klasse des wirklichen Zeichnens
        class Exer:
            #2. Turtle wird erstellt. 
            def __init__(self, master,ü):
                self.ü = ü
                self.turtle = RawTurtle(master)
                self.turtle.ht()
            #Wenn Ausführ aufgerufen wird Horizontalerwurf gemacht.
            def Ausführ(self):
                self.exe = horizontalerWurf(self.turtle,self.ü)

        # Canvas Fenster erstellen und Grid und Exer reintun
        def __init__(self,master,ü):
            self.draw = Frame(master)
            self.draw.pack()
            self.ebene = Canvas(master, width=1000, height=500)
            self.ebene.pack()

            self.grid = self.Grid(self.ebene)
            self.exer = self.Exer(self.ebene,ü)

  
  
    #Frames zum eingeben der Daten, Gemahlen, und eine Statusbar
    def __init__ (self, master):
        self.inputs = self.Eingaben(master,self)
        
        self.exe = self.Mahlen(master,self)

        self.status = Frame(master)
        self.status.pack()





# Horizontaler Wurf hat eine Klasse
class horizontalerWurf:
    #Turtle wird reingebracht; Parameter reingetan, und Turtle eingerichtet, Wurf ausgeführt
    def __init__(self,turtle,ü):

        """ Sh(t) = V0*t """
        """ Sv(t) = H0 + (-1/2) * g * t^2 """
        Ag = ü.inputs.Ag
        Wh = ü.inputs.Wh
        self.t = 0.01
        self.V0 = float(Ag)
        self.g = 9.8
        self.H0 = float(Wh)
        self.tS = (-self.H0/-(0.5*self.g))**(1/2)
        self.A =10

        self.tur= turtle
        self.tur.clear()
        self.tur.speed(0)

        self.Wurf()



    #Der Wurf wird ausgeführt
    def Wurf(self):
        tstart = self.t
        self.Sv_t = 0
        self.Sh_t = 0
        self.tur.penup()
        self.tur.goto(0,(self.H0*self.A))
        #self.tur.goto(-(self.V0*self.tS)*self.A,(self.H0*self.A))
        self.tur.pendown()

        #Die einzelnen Schritte pro 1/100 Sekunde passieren hier
        def Wurfrechnung():
            hs = self.Sh_t
            vs = self.Sv_t

            self.Sh_t = (self.V0*self.t)
            self.Sv_t = (0.5 * self.g * self.t**2)

            self.esh = (self.Sh_t-hs)*self.A
            self.esv = (self.Sv_t-vs)*self.A


        #Solange die Zeit nicht erreicht wird bis am Boden angekommen ist wird jeder Schritt ausgeführt
        while self.t < self.tS:

            Wurfrechnung()

            self.tur.forward(self.esh)
            self.tur.right(90)
            self.tur.forward(self.esv)
            self.tur.left(90)
            
            self.t = self.t + tstart




root = Tk()


win = Fenster(root)
root.mainloop()