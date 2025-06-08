#!/usr/bin/python3
import json
import requests
from datetime import date
import sys
# Ej färdigställt!
def init_tournament(t_id):
    r_json = requests.get(f"https://member.schack.se/public/api/v1/tournamentresults/table/id/{t_id}", headers={'accept': '*/*'}).text
    with open("users",'a') as f:
        for x in json.loads(r_json):
            f.write(f'{x["playerInfo"]["id"]};{x["playerInfo"]["lastName"]}, {x["playerInfo"]["firstName"]}\n')
def gen_pgn(t_id):
    req = requests.get(f"https://member.schack.se/public/api/v1/tournamentresults/team/roundresults/id/{t_id}", headers = {'accept':'*/*'}).text
    data = json.loads(req)
    curr_round = max([x['roundNr'] for x in data])
    gms = [ a for a in data if a['roundNr'] == curr_round]
    with open("users",'r') as f:
        players = dict([ a.rstrip("\n").split(';') for a in f.readlines() ])

    for game in gms:
        w_id = str(game["homeId"])
        if w_id not in players.keys():
           name = add_player(w_id)
           players[w_id] = name
        b_id = str(game["awayId"])
        if b_id not in players.keys():
           name = add_player(b_id)
           players[b_id] = name
        print(f'{players[w_id]} - {players[b_id]}')
        with open(f"r{curr_round}.pgn",'a') as f:
            f.write(f'White "{players[w_id]}"\n')
            f.write(f'Black "{players[b_id]}"\n')
            f.write("\n*\n\n")

def add_player(ssf_id):
    if ssf_id == '-100':
        with open("users",'a') as f:
            f.write('-100;WO\n')
        return 'WO'
    
    now = date.today().strftime("%Y-%m-%d")
    r_json = requests.get(f"https://member.schack.se/public/api/v1/player/{ssf_id}/date/{now}", headers={'accept': '*/*'}).text
    x = json.loads(r_json)
    with open("users",'a') as f:
        f.write(f'{x["id"]};{x["lastName"]},{x["firstName"]}\n')
    
    return f'{x["lastName"]},{x["firstName"]}'

def main():
    if len(sys.argv) > 1:
        t_id = sys.argv[1]
        init_tournament(t_id)
        gen_pgn(t_id)
    else:
        print("Usage: ./genpgn.py tournament_id")
if __name__ == '__main__':
    main()
