from re import sub
""" Öppnar och läser innehållet i en PGN-fil.
filnamn är en sträng på formen: databas.pgn
"""
def read_pgn(filnamn):
    lines=[]
    with open(filnamn,'r') as f:
        for text in f:
            lines.append(text)
        f.close()
    return lines

"""Tar en lista från read_pgn och returnerar en lista med alla drag(ej från variantträd).
"""

def format_pgn(pgn):
    moves=[]
    for line in pgn:
        if line[0].isdigit():
       
            moves.append(sub(r'{.*$', '', line).rstrip())
    game=[x.split() for x in moves]
    game2=[]
    for x in game:
        game2.extend(x)
    for x in game2:
        if not x[0].isalpha():
            game2.remove(x)

    return game2


