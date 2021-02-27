import requests
from bs4 import BeautifulSoup

def _print(rating,games,delta):
    for x in range(1,len(rating)):
        print(f"Månad {x} ")
        print(f"Ny rating: {rating[-x]} ")
        print(f"Antal spelade partier : {games[-x]}")
        print(f"Ratingförändring {delta[-x]}")
        print("------------------------------\n")
    print(f"Totalt antal partier : {sum(games)}")
def get_rating_info(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
    if url[-5:]!="chart":
        url=url+"/chart"
    #table

    sss=[str(s).split('</td>') for s in soup.findAll('tr')[15:]]
    rating=[int(s[1][-5:]) for s in sss ]
    games=[int(s[2][-3:])for s in sss]
    delta=[(rating[x]-rating[x-1])for x in range(len(rating))]
    return rating, games, delta
if __name__=='__main__':
    url='https://ratings.fide.com/profile/1723383'  #input("Ge Fide-url")
    rating,games,delta=get_rating_info(url)
    _print(rating,games,delta)