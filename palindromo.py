from tkinter import*
import expreg
from time import*


ventana = Tk() 
ventana.title("Automata de pila")
ventana.minsize(1100,700)
ventana.maxsize(1100,700)

palabra = StringVar()
img = PhotoImage(file="1.png")
img2 = PhotoImage(file="2.png")
img3 = PhotoImage(file="3.png")
img4 = PhotoImage(file="4.png")
img5 = PhotoImage(file="5.png")
img6 = PhotoImage(file="6.png")

       
def MoverCabezal(posicion):
    
   lista = validarExpresion()
   c=0
   for x in range(len(lista)):
        if c==posicion: 
          cabeza.place(x=10+c*16,y=230)
        c+=1


def pintarCinta():
    
    if validarExpresion()!=0:
       lista_botones = validarExpresion()
       a=0
       for i  in range(len(lista_botones)): 
          lista_botones[i]  =  Button(ventana, text = lista_botones[i] ,font =("Agency FB", 14), activebackground="#F50743",bg="silver",command = validarExpresion).place(x=10+a,y=200)
          a+=16
    label_img = Label(ventana, image=img2).place(x=700, y=170)

def validarExpresion(): 
  
  lista_letras =[]
  lista_letras = list(palabra.get())

  if len(lista_letras)>1: 
     if expreg.ValidarExp(palabra.get())==0 and (len(lista_letras))%2!=0:  
          return lista_letras 
     else:
          return 0 
  else:
     return 0 



def apilar(posicion):
 
     
   lista_palindromo = validarExpresion()
   lista_pila = lista_palindromo
 
   lista_pila[posicion] = Button(ventana, text = lista_pila[posicion],font =("Agency FB", 16), activebackground="#F50743",bg="pink",command = validarExpresion)
   lista_pila[posicion].place(x=10,y=600-45*posicion)
   
   return lista_pila

  


def desapilar(posicion):     
        
         c=0
         lista = apilar(posicion)
      
         while c<2:
         #boton.remove(posicion1)
           print(lista[posicion])
          # lista[posicion].place_forget()
#           lista.pop(posicion)
           c+=1
            

def Palindro(mensaje,resultado):

  
  if resultado==False:  
     Mensaje = Label(ventana,text=mensaje,font =("Agency FB", 14),fg="red").place(x=10,y=260)
  elif resultado==True:   
     Mensaje = Label(ventana,text=mensaje,font =("Agency FB", 14),fg="Black").place(x=10,y=260) 


def simular_automata():
  

    
  posicion=0
  decremento=-1
  palindro=True

  
  lista_palindromo = validarExpresion()

  
  tamaño = (len(lista_palindromo)-1)/2

  lista_pila = lista_palindromo[0:int(tamaño)]

  # Simulacion de todo el automata
  while posicion <= len(lista_palindromo)-1:
      
      MoverCabezal(posicion)
      
      if posicion < tamaño:
         apilar(posicion)
         decremento =  int((len(lista_pila)-1))
         label_img = Label(ventana, image=img3).place(x=700, y=170)

      elif posicion>tamaño:

          if lista_pila[decremento] == lista_palindromo[posicion]:
             decremento-=1
             label_img = Label(ventana, image=img5).place(x=700, y=170) 
          else:
            palindro=False
            Palindro("¡No es Palindromo!",palindro)
            break   
      if posicion==tamaño:
        label_img = Label(ventana, image=img4).place(x=700, y=170)

      ventana.update()
      sleep(1)        
      posicion+=1

  if  palindro==True:  
    Palindro("¡Es Palindromo!",palindro)
    label_img = Label(ventana, image=img6).place(x=700, y=170)       

      
              

cabeza  =  Button(ventana, text = "•" ,font =("Agency FB", 14),bg="pink",command = validarExpresion)  
cabeza.place(x=10,y=230)     
cabeza.place_forget()
Validar = Button(ventana, text="Validar Expresion",font =("Agency FB", 14),activebackground="green",bg="pink",command = pintarCinta).place(x=280,y=100)
simular = Button(ventana, text="Simular Atomata",font =("Agency FB", 14),activebackground="green",bg="pink",command = simular_automata).place(x=400,y=100)

Entrada = Entry(ventana, textvariable = palabra).place(x=120,y=110)
       
label_Expresion = Label(ventana, text="Expresión",font =("Agency FB", 14), fg="black").place(x=50,y=100)
label_Cinta = Label(ventana, text="CINTA SIMULADA",font =("Agency FB", 14), fg="black").place(x=10,y=170)
label_Grafo = Label(ventana, text="AUTOMATA",font =("Agency FB", 14), fg="black").place(x=600,y=170)
label_titulo = Label(ventana, text="Este es un automata de de pila que tiene la funcionalidad de reconocer un palindromo de largo  impar, la cadena a ser aceptada toma la forma  l= ZcZ¨ donde Z pertenece a {a, b}*",font =("Agency FB", 14), fg="black").place(x=10,y=30) 
label_img = Label(ventana, image=img).place(x=700, y=170)
label_pila =  Label(ventana, text="Pila",font =("Agency FB", 14), fg="black").place(x=10,y=660)




ventana.mainloop()

