import json
import urllib3
import os
import sys
from collections import defaultdict
urllib3.disable_warnings()
choice = ''
http = urllib3.PoolManager()

def newdeck():
    url = "https://deckofcardsapi.com/api/deck/new/"
    r = http.request('GET', url)
    d = json.loads(r.data.decode('utf-8'))
    deck_id = d['deck_id']
    return deck_id

def draw(http, deck_id):
    url = http.request('GET', 'http://deckofcardsapi.com/api/deck/{}/draw/?count=1'.format(deck_id))
    d = json.loads(url.data.decode())
    return d
print('Yay Cards!')
while choice != 'q':
    print('[1] New Deck')
    print('[2] Draw Card')
    print('[3] Quit')

    choice = input("What to do, What to do...\n")

    if choice == '1' :
        deck_id = newdeck()
    elif choice == '2' :
        card = draw(http, deck_id)
        card_val = card['cards'][0]['value']
        print('Drew card {}'.format(card_val))
