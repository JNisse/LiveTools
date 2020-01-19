# Program körs i en prompt.
# Ber användaren om en URL till turnering i medlemssystemet (schack.se)
# Skriver lottningen i fönstret.
# Skriver en fil som heter lottnin.pgn till där de här programmet är sparat.




import requests
from bs4 import BeautifulSoup

  
def f(l,url):
    
    resp=requests.get(url)
    b=False
    if resp.status_code==200:
        
        soup=BeautifulSoup(resp.text,'html.parser')
        g=soup.find_all('span')
        contents=[]
        results=[]
        for i in g:
            contents.append(str(i))
        for j in contents:
            j=j[6:len(j)-7]
            if j=='RESULTAT':
                b=True 
            if b and j!='RESULTAT' and len(j)>5:
               results.append(j)
    else:
        print ("Error")
    for k in range (len(results)//2):
        l.append(results[2*k])
        l.append(results[2*k+1])
        print (results[2*k] + " - " + results[2*k+1])
def PGN(lista):
    with open ('lottning.pgn','w') as f:
        for k in range(len(lista)//2):
            f.write("[White\""+str(lista[2*k])+"\"]\n")
            f.write("[Black\""+str(lista[2*k+1])+"\"]\n")
            f.write("\n*\n")

lista=[]
url=input("Kopiera in webbadressen till turneringen")
f(lista,url)
PGN(lista)
print("done")
input('Press ENTER to exit')

