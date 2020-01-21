'''This file holds all relevant classes necessary for getting the game started.
Definitions for Cards, Decks, Cards in Hand (Hand), Player.'''

'''Imports for Classes'''

import random

suits = ('Karo','Herz','Pik','Kreuz')*4
ranks = ('Zwei','Drei','Vier','Fünf','Sechs','Sieben','Acht','Neun','Zehn','Bube','Dame','König','Ass')
values = {'Zwei':2,'Drei':3,'Vier':4,'Fünf':5,'Sechs':6,'Sieben':7,'Acht':8,'Neun':9,'Zehn':10,'Bube':10,'Dame':10,'König':10,'Ass':11}

playing = True

# Definition of one Card
class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return f"{self.suit} {self.rank}"

    
# Definition of a set of Cards (Deck). It 
    
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))          
    
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+="\n " + card.__str__() # add each Card object's print string
        return 'Das Set besteht aus:' + deck_comp

        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card=self.deck.pop()
        return single_card
    
    def __len__(self):
        return len(self.deck)


#Add Cards to Players Hand/adjust for Ace

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=="Ass":
            self.aces+=1
    def adjust_for_ace(self):
        while self.value>21 and self.aces>=1:
            self.value-=10
            self.aces-=1

#Funktion um Kartenaufnahme abzubilden 
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
            
##Main Class for a relevant methods and attributes for players

class Player:
    
     
    def __init__(self):
        
        self.name=[]
        self.total={}
        self.bet={}
        self.hand={}
                
# Methode um Namen abzufragen

    def get_names(self, start, numplay):
        
        if start==0:
            print('\nHerzlich willkommen! Um die Atmosphäre angenehmer zu gestalten bitte ich Sie mir Ihre Namen mitzuteilen.\nDie Person, die neben dem Croupier sitzt, darf später anfangen.\n')
            nametest=input('Wie heißt die Person, die links neben dem Croupier sitzen möchte: ').capitalize()

        else:
            print('\nSchön, dass Sie nochmal spielen. Ich würde gerne wieder Ihre Namen wissen!\n')
            nametest=input('Wie heißt die Person, die diese Runde links neben dem Croupier sitzen möchte: ').capitalize()
        self.name.append(nametest)
        
        if numplay>1:
            print('\nUnd wie heißen Ihre Mitspieler? Geben Sie bitte die Namen nacheinander ein!')
            for n in range(1,numplay):
                while True:
                    nametest=input(f'Mitspieler {n}: ').capitalize()
                    if nametest in self.name:
                        print('Dieser Name wurde bereits genannt, bitte wählen Sie einen anderen Namen.')
                        continue
                    else:
                        self.name.append(nametest)
                        break
                    
         ##Initialisierung der Handobjekte nach erfolgter Namensabfrage
        for num in range(0,len(self.name)):
            self.hand[self.name[num]]=Hand()

# Methode um Chips zu kaufen
           
    def buy_chips(self,mindest, start, numplay):
        if start==0:
            print('\nDer Mindesteintrittpreis unseres Casinos beträgt 50 Chips!')
        for num in range(0, numplay):
            buymore=''
            while not (buymore=='n' or buymore=='j'):
                if self.name[num] not in self.total.keys():
                    while True:
                        try:
                            self.total[self.name[num]]=int(input(f'Wie viele Chips möchten Sie kaufen, {self.name[num]}?'))
                        except:
                            print('Es muss eine Zahl eingegeben werden! ')
                        else:
                            if self.total[self.name[num]]<50:
                                print('Sie müssen mindestens 50 Chips kaufen!')
                                continue
                            else:
                                break
                    buymore='n'
                elif (self.name[num] in self.total.keys()) and (self.total[self.name[num]]<mindest):
                    print(f'\n\nDer Mindesteinsatz für diese Runde liegt bei {mindest} Chips!')
                    print(f'{self.name[num]}, Sie haben nur noch {self.total[self.name[num]]} Chips insgesamt.\n')
                    print(f'Sie haben zu wenig Chips für den Mindesteinsatz in dieser Runde.\n{self.name[num]}, bitte kaufen Sie mindestens noch {mindest-self.total[self.name[num]]} Chips!')
                    while True:

                        try:      
                            buy=int(input(f'Wie viele Chips möchten Sie dazu kaufen, {self.name[num]}?'))
                        except:
                            print('Es muss eine Zahl eingegeben werden! ')
                        else:
                            self.total[self.name[num]]+=buy
                            if self.total[self.name[num]]<mindest:
                                print(f'Sie müssen mindestens {mindest} Chips haben, um mitzuspielen. {self.name[num]}, bitte kaufen Sie mindestens noch {mindest-self.total[self.name[num]]} Chips!')
                            else:
                                break
                    buymore='n'   

                else:
                     while True:
                        try:
                            buymore=input(f'\n\n{self.name[num]}, möchten Sie weitere Chips dazu kaufen? Ja oder Nein: ')[0].lower()
                        except:
                            print('Sie können nur ja oder nein eingeben.')
                        else:
                            if not (buymore=='j' or buymore=='n'):
                                print('Sie können nur ja oder nein eingeben.')
                            elif buymore=='j':
                                while True:
                                    try:
                                        buy2=int(input(f'Wie viele Chips möchten Sie zusätzlich kaufen, {self.name[num]}?'))
                                    except:
                                        print('Es muss eine Zahl eingegeben werden! ')
                                    else:
                                        self.total[self.name[num]]+=buy2
                                        buymore='n'
                                        break
                                break
                            else:
                                break

# Methode um Einsatz zu wählen
    
    def take_bet(self, mindest, numplay):
        print(f'\nDer Mindesteinsatz für diese Runde liegt bei {mindest} Chips!')
        for num in range(0,numplay):
            while True:
                try:
                    self.bet[self.name[num]]=int(input(f'\n{self.name[num]}, bitte bestimmen Sie jetzt Ihren Einsatz für diese Runde. Sie haben {self.total[self.name[num]]} Chips zur Verfügung: '))
                except ValueError:
                    print('Es muss eine ganze Zahl eingegeben werden!')
                else:
                    if self.bet[self.name[num]]<mindest:
                        print(f'Sie müssen mindestens {mindest} Chips setzen!')
                    elif self.bet[self.name[num]]>self.total[self.name[num]]:
                        print(f'{self.name[num]}, ihr Einsatz ist zu hoch! Sie haben nur {self.total[self.name[num]]} Chips zur Verfügung!')
                    else:
                        break

# Methode um Spieler zum ziehen oder halten aufzufordern

    def hit_or_stand(self, deck, turn, hold):
        
        while True:
            try:
                x=input(f"{self.name[turn]}, wollen Sie eine weitere Karte ziehen oder Ihr Blatt halten? Bitte geben Sie 'z' oder 'h' ein!")[0].lower()
            except:
                print("Sie können nur 'z' oder 'h' eingeben")
            else:
                if not (x=='z' or x=='h'):
                    print("Sie können nur 'z' oder 'h' eingeben.")
                    continue
                elif x=='z':
                    hit(deck, self.hand[self.name[turn]])
                    break
                else:
                    hold+=1
                    break
        return hold

#Distribution von Karten beim Spielanfang

    def deal_cards(self, deck):
               
        for num in range(0,len(self.name)):
            self.hand[self.name[num]].add_card(deck.deal())


# Double down, Einsatz verdoppeln, nachdem die ersten beiden Karten gezogen wurden

    def double(self, deck, turn, double):
        while True:
            try:
                x=input(f"{self.name[turn]}, wollen Sie Ihren Einsatz verdoppeln (Double Down), ja oder nein? Sie erhalten dann automatisch noch eine Karte!")[0].lower()
            except:
                print("Sie können nur 'ja' oder 'nein' eingeben")
            else:
                if not (x=='j' or x=='n'):
                    print("Sie können nur 'j' oder 'n' eingeben.")
                    continue
                elif x=='j':
                    self.bet[self.name[turn]]*=2
                    hit(deck,self.hand[self.name[turn]])
                    double+=1
                    break
                else:
                    break
        return double

#Abfrage der Anzahl der Spieler  
    def __len__(self):
        return len(self.name)
    
#Adjustierung Gesamtmenge Chips mit dem Wetteinsatz  ,

    def win_bet(self,turn):
        self.total[self.name[turn]]+=self.bet[self.name[turn]]
        
    def lose_bet(self,turn):
        self.total[self.name[turn]]-=self.bet[self.name[turn]]
        if self.total[self.name[turn]]<0:
            self.total[self.name[turn]]=0