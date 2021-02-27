from bs4 import BeautifulSoup
import requests
from Participant import Participant

def import_ids(file):
    with open(file,'r') as f:
        return [Participant(i) for i in f.readlines()]


def get_participants(resp,soup):
    participants=[]
    s = [str(i)[6:-7] for i in soup.findAll('span') if str(i)[6:-7].strip() and str(i)[6:-7] != 'JA']
    n = 0
    try:
        index = s.index('KV.P')+2
        for t in s[index::5]:
            if n % 2 == 0:
                if t[:5] == 'class':
                    break
                #print(t + " " + s[s.index(t)+1] + " " + s[s.index(t)+2])
                participants.append(t + " " + s[s.index(t) + 1] + " " + s[s.index(t) + 2])
            n += 1
    except:
        index = s.index('AVPRICKAD')+2
        for t in s[index::5]:

            if t[:5] == 'class':
                break
            #print(t + " " + s[s.index(t)+1] + " " + s[s.index(t)+2])
            participants.append(t + " " + s[s.index(t)+1] + " " + s[s.index(t)+2])
    return participants


if __name__ == '__main__':
    #url = 'https://member.schack.se/ShowTournamentServlet?id=8798' #input("Turneringsurl")
    #resp = requests.get(url)
    #if resp.status_code == 200:
     #   soup = BeautifulSoup(resp.text, 'html.parser')
    #print(get_participants(resp,soup))
    x=import_ids("ids.txt")
    for y in x:
        print(y)
