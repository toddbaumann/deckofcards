import json
import urllib3
import os
urllib3.disable_warnings()

def newdeck():
    url = "https://deckofcardsapi.com/api/deck/new/"
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    d = json.loads(r.data.decode('utf-8'))
    newdeck.deckid = d['deck_id']
def shuffledeck():
    shuffledeck.url = "https://deckofcardsapi.com/api/deck/%s/shuffle/" % (newdeck.deckid)
    http = urllib3.PoolManager()
    r = http.request('GET', shuffledeck.url)
    print r.data
    #print r.status
def listoptions():
    print "1) New Deck"
    print "2) Shuffle Deck"
def exec_menu(selected):
    os.system('clear')
    ch = selected.lower()
    if ch == '':
        menu_actions['main_menu']()
if __name__=='__main__':
    listoptions()
    listalloptions = ["New Deck", "Shuffle Deck"]
    listallselect = input('Please select an option')
    selected = listalloptions[listallselect-1]
    listallselect
    exec_menu(selected)
#newdeck()
#shuffledeck()
#print newdeck.deckid
#print shuffledeck.url
