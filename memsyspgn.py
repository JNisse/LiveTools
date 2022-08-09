from requests import get
from bs4 import BeautifulSoup as bs
import sys

if len(sys.argv)==2:
    if sys.argv[1].isnumeric():
        url = f'https://resultat.schack.se/ShowTournamentServlet?id={sys.argv[1]}'
    else:
        url = sys.argv[1]
else:
    url = input('Klistra in en URL')
resp = get(url)
if resp.status_code==200:
    soup = bs(resp.text,'html.parser')
    tag_strings =  [x.string for x in soup.findAll('span')]
    res = tag_strings[tag_strings.index('RESULTAT')+1:]
    white = res[2::11]
    black = res[7::11]
    with open ('lottning.pgn','w') as f:
            for i,item in enumerate(white):
                f.write("[White\""+item+"\"]\n")
                f.write("[Black\""+black[i]+"\"]\n")
                f.write("\n*\n")
else:
    print('Websidans HTML var inte tillgänglig')
print('Nu finns en fil \"lottning.pgn\" i samma map som det här programmet')
input('Tryck ENTER för att lämna')

