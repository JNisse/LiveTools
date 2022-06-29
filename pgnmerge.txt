PATH = ''
FILES = []
ARCHIVEPATH=''
def get_pgn(path):
    with open(path,'r') as f:
        data = ''.join(f.readlines())
    return data

clipboard = [get_pgn(PATH+i+'.pgn') for i in FILES]
with open(ARCHIVEPATH,'w') as f:
    f.writelines(clipboard)
