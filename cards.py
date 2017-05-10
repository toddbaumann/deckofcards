import json
import urllib3
import os
import sys
urllib3.disable_warnings()

http = urllib3.PoolManager()
menu_actions = {} 
def newdeck():
    url = "https://deckofcardsapi.com/api/deck/new/"
    r = http.request('GET', url)
    d = json.loads(r.data.decode('utf-8'))
    newdeck.deckid = d['deck_id']
    main_menu()
def shuffledeck():
    shuffledeck.url = "https://deckofcardsapi.com/api/deck/%s/shuffle/" % (newdeck.deckid)
    r = http.request('GET', shuffledeck.url)
    print (r.data)
    print (r.status)
    main_menu()
    return
def drawcard():
    drawcard.url = "https://deckofcardsapi.com/api/deck/%s/draw/?count=1" % (newdeck.deckid)
    r = http.request('GET', drawcard.url)
    print (r.data)
    main_menu()

def main_menu():
    print ("1) NewDeck")
    print ("2) ShuffleDeck")
    print ("3) Drawcard")
    print ("4) exit")
    choice = input(" >> ")  
    exec_menu(choice) 
    return

def exec_menu(choice):
    ch = choice.lower()
    menu_actions[ch]()
    return
def exit():
    sys.exit()
menu_actions = { 
    'main_menu': main_menu, 
    '1': newdeck, 
    '2': shuffledeck,
    '3': drawcard,
    '4': exit,
} 
# MAin menu run 

main_menu()
#newdeck()
#shuffledeck()
#print newdeck.deckid
#print shuffledeck.url
