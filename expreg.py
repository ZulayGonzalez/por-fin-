import re



def ValidarExp(palabra):
    
  patron = re.compile('[a|b]+c{1}[a|b]+')
  
  if (patron.search(palabra)):
     resul = patron.search(palabra).group(0)
  else: 
     pass

  if(resul == palabra):   
      return 0
  else:   
      pass




