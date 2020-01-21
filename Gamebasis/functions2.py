'''This file holds all relevant functions necessary for plotting the board.
Definitions for aasking for number of players, replaying and showing rules.'''


# Ask for number of players

def num_player(start):
    numplay=1
    if start==0:
        while True:
            try:
                numplay=int(input('\nWie viele Spieler wollen am Tisch Platz nehmen? (Maximal 4): '))
            except ValueError:
                print('Es muss eine ganze Zahl eingegeben werden!')
            else:
                if numplay==0:
                    print('Sie müssen mindestens 1 eingeben!')
                    continue
                elif numplay>4:
                    print('Es können maximal 4 Spieler am Tisch Platz nehmen!')
                else:
                    break
    else:
        while True:
            try:
                numplay=int(input('\nUnd wie viele Spieler werden in dieser Runde Platz nehmen? (Maximal 4): '))
            except ValueError:
                print('Es muss eine ganze Zahl eingegeben werden!')
            else:
                if numplay==0:
                    print('Sie müssen mindestens 1 eingeben!')
                    continue
                elif numplay>4:
                    print('Es können maximal 4 Spieler am Tisch Platz nehmen!')
                else:
                    break
    return numplay


#Funktion um Kartenaufnahme abzubilden 
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


#Funktionen zum Anzeigen der Karten. Dhow_some am Anfang, bevor Croupier dran ist, show_all, sobald Croupier spielt.
def show_some(player,dealer):

    print('\n'+'Folgende Karten liegen auf dem Spieltisch'.center(92)+'\n')
    print('+'*94)
    print('|'+'|'.rjust(93))
    print('|'+('*'*26).center(92)+'|')
    print('|'+'*  Karten des Croupiers: *'.center(92)+'|')
    print('|\t*'.expandtabs(34)+dealer.cards[0].__str__().center(24)+'*'+'\t|'.expandtabs(33))
    for card in range(1,len(dealer.cards)):
         print('|\t*'.expandtabs(34)+dealer.cards[card].__str__().center(24)+'*'+'\t|'.expandtabs(33))
    print('|'+('*'*26).center(92)+'|')
    print('|'+'|'.rjust(93))


    ###Plotting Player 1-2
    print('|\t'.expandtabs(9)+('*'*26)+'\t'.expandtabs(24)+('*'*26)+'\t|'.expandtabs(8))
    if len(player.name)<2:
        print('|\t*'.expandtabs(9)+f"{player.name[0]}'s Platz:".center(24)+'*'+'\t*'.expandtabs(24)+' Platz unbesetzt'.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Verfügbare Chips: {player.total[player.name[0]]}".center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Einsatz: {player.bet[player.name[0]]} Chips".center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+"".center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Karten auf der Hand:".center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        for card in range(0,len(player.hand[player.name[0]].cards)):
            print('|\t*'.expandtabs(9)+player.hand[player.name[0]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        print('|\t'.expandtabs(9)+('*'*26)+'\t'.expandtabs(24)+('*'*26)+'\t|'.expandtabs(8))
    else:
        print('|\t*'.expandtabs(9)+f" {player.name[0]}'s Platz:".center(24)+'*'+'\t*'.expandtabs(24)+f" {player.name[1]}'s Platz:".center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Verfügbare Chips: {player.total[player.name[0]]}".center(24)+'*'+'\t*'.expandtabs(24)+f' Verfügbare Chips: {player.total[player.name[1]]}'.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Einsatz: {player.bet[player.name[0]]} Chips".center(24)+'*'+'\t*'.expandtabs(24)+f' Einsatz: {player.bet[player.name[1]]} Chips'.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+"".center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Karten auf der Hand:".center(24)+'*'+'\t*'.expandtabs(24)+' Karten auf der Hand:'.center(24)+'*\t|'.expandtabs(9))
        for card in range(0,2):
            print('|\t*'.expandtabs(9)+player.hand[player.name[0]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(24)+player.hand[player.name[1]].cards[card].__str__().center(24)+'*\t|'.expandtabs(9))
        try:
            for card in range(2,len(player.hand[player.name[0]].cards)):
                print('|\t*'.expandtabs(9)+player.hand[player.name[0]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(24)+player.hand[player.name[1]].cards[card].__str__().center(24)+'*\t|'.expandtabs(9))
        except:
            for card in range(len(player.hand[player.name[1]].cards),len(player.hand[player.name[0]].cards)):
                print('|\t*'.expandtabs(9)+player.hand[player.name[0]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        else:
            for card in range(len(player.hand[player.name[0]].cards),len(player.hand[player.name[1]].cards)):
                print('|\t*'.expandtabs(9)+''.center(24)+'*'+'\t*'.expandtabs(24)+player.hand[player.name[1]].cards[card].__str__().center(24)+'*\t|'.expandtabs(9))
        print('|\t'.expandtabs(9)+('*'*26)+'\t'.expandtabs(24)+('*'*26)+'\t|'.expandtabs(8))
    print('|'+'|'.rjust(93))

    ###Close Board if players<2
    if len(player.name)<3:
        print('+'*94)
        print('\n')

        
    ###Plotting Player 3-4
    else:
        print('|\t'.expandtabs(18)+('*'*26)+'\t'.expandtabs(6)+('*'*26)+'\t|'.expandtabs(17))
        if len(player.name)<4:
            print('|\t*'.expandtabs(18)+f"{player.name[2]}'s Platz:".center(24)+'*'+'\t*'.expandtabs(6)+'Platz unbesetzt'.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Verfügbare Chips: {player.total[player.name[2]]}".center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Einsatz: {player.bet[player.name[2]]} Chips".center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+''.center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Karten auf der Hand:".center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            for card in range(0,len(player.hand[player.name[2]].cards)):
                print('|\t*'.expandtabs(18)+player.hand[player.name[2]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            print('|\t'.expandtabs(18)+('*'*26)+'\t'.expandtabs(6)+('*'*26)+'\t|'.expandtabs(17))

        else:
            print('|\t*'.expandtabs(18)+f" {player.name[2]}'s Platz:".center(24)+'*'+'\t*'.expandtabs(6)+f" {player.name[3]}'s Platz:".center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Verfügbare Chips: {player.total[player.name[2]]}".center(24)+'*'+'\t*'.expandtabs(6)+f' Verfügbare Chips: {player.total[player.name[3]]}'.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Einsatz: {player.bet[player.name[2]]} Chips".center(24)+'*'+'\t*'.expandtabs(6)+f' Einsatz: {player.bet[player.name[3]]} Chips'.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+''.center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Karten auf der Hand:".center(24)+'*'+'\t*'.expandtabs(6)+' Karten auf der Hand:'.center(24)+'*\t|'.expandtabs(18))
            for card in range(0,2):
                print('|\t*'.expandtabs(18)+player.hand[player.name[2]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(6)+player.hand[player.name[3]].cards[card].__str__().center(24)+'*\t|'.expandtabs(18))
            try:
                for card in range(2,len(player.hand[player.name[2]].cards)):
                    print('|\t*'.expandtabs(18)+player.hand[player.name[2]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(6)+player.hand[player.name[3]].cards[card].__str__().center(24)+'*\t|'.expandtabs(18))
            except:
                for card in range(len(player.hand[player.name[3]].cards),len(player.hand[player.name[2]].cards)):
                    print('|\t*'.expandtabs(18)+player.hand[player.name[2]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            else:
                for card in range(len(player.hand[player.name[2]].cards),len(player.hand[player.name[3]].cards)):
                    print('|\t*'.expandtabs(18)+''.center(24)+'*'+'\t*'.expandtabs(6)+player.hand[player.name[3]].cards[card].__str__().center(24)+'*\t|'.expandtabs(18))
            print('|\t'.expandtabs(18)+('*'*26)+'\t'.expandtabs(6)+('*'*26)+'\t|'.expandtabs(17))
        print('|'+'|'.rjust(93))
        print('+'*94)   
        print('\n')
        

##Funktion zur Anzeige aller Kartenwerte!
def show_all(player, dealer):
    
    print('\n'+'Folgende Karten liegen auf dem Spieltisch'.center(92)+'\n')
    print('+'*94)
    print('|'+'|'.rjust(93))
    print('|'+('*'*26).center(92)+'|')
    print('|'+'*  Karten des Croupiers: *'.center(92)+'|')
    for card in range(0,len(dealer.cards)):
         print('|\t*'.expandtabs(34)+dealer.cards[card].__str__().center(24)+'*'+'\t|'.expandtabs(33))
    print('|\t*'.expandtabs(34)+f'Kartenwert: {dealer.value}'.center(24)+'*'+'\t|'.expandtabs(33))
    print('|'+('*'*26).center(92)+'|')
    print('|'+'|'.rjust(93))


    ###Plotting Player 1-2
    print('|\t'.expandtabs(9)+('*'*26)+'\t'.expandtabs(24)+('*'*26)+'\t|'.expandtabs(8))
    if len(player.name)<2:
        print('|\t*'.expandtabs(9)+f"{player.name[0]}'s Platz:".center(24)+'*'+'\t*'.expandtabs(24)+' Platz unbesetzt'.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Verfügbare Chips: {player.total[player.name[0]]}".center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Einsatz: {player.bet[player.name[0]]} Chips".center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+"".center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Karten auf der Hand:".center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        for card in range(0,len(player.hand[player.name[0]].cards)):
            print('|\t*'.expandtabs(9)+player.hand[player.name[0]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Kartenwert: {player.hand[player.name[0]].value}".center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        print('|\t'.expandtabs(9)+('*'*26)+'\t'.expandtabs(24)+('*'*26)+'\t|'.expandtabs(8))
    else:
        print('|\t*'.expandtabs(9)+f" {player.name[0]}'s Platz:".center(24)+'*'+'\t*'.expandtabs(24)+f" {player.name[1]}'s Platz:".center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Verfügbare Chips: {player.total[player.name[0]]}".center(24)+'*'+'\t*'.expandtabs(24)+f' Verfügbare Chips: {player.total[player.name[1]]}'.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Einsatz: {player.bet[player.name[0]]} Chips".center(24)+'*'+'\t*'.expandtabs(24)+f' Einsatz: {player.bet[player.name[1]]} Chips'.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+"".center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Karten auf der Hand:".center(24)+'*'+'\t*'.expandtabs(24)+' Karten auf der Hand:'.center(24)+'*\t|'.expandtabs(9))
        for card in range(0,2):
            print('|\t*'.expandtabs(9)+player.hand[player.name[0]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(24)+player.hand[player.name[1]].cards[card].__str__().center(24)+'*\t|'.expandtabs(9))
        try:
            for card in range(2,len(player.hand[player.name[0]].cards)):
                print('|\t*'.expandtabs(9)+player.hand[player.name[0]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(24)+player.hand[player.name[1]].cards[card].__str__().center(24)+'*\t|'.expandtabs(9))
        except:
            for card in range(len(player.hand[player.name[1]].cards),len(player.hand[player.name[0]].cards)):
                print('|\t*'.expandtabs(9)+player.hand[player.name[0]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(24)+''.center(24)+'*\t|'.expandtabs(9))
        else:
            for card in range(len(player.hand[player.name[0]].cards),len(player.hand[player.name[1]].cards)):
                print('|\t*'.expandtabs(9)+''.center(24)+'*'+'\t*'.expandtabs(24)+player.hand[player.name[1]].cards[card].__str__().center(24)+'*\t|'.expandtabs(9))
        print('|\t*'.expandtabs(9)+f"Kartenwert: {player.hand[player.name[0]].value}".center(24)+'*'+'\t*'.expandtabs(24)+f"Kartenwert: {player.hand[player.name[1]].value}".center(24)+'*\t|'.expandtabs(9))
        print('|\t'.expandtabs(9)+('*'*26)+'\t'.expandtabs(24)+('*'*26)+'\t|'.expandtabs(8))
    print('|'+'|'.rjust(93))

    ###Close Board if players<2
    if len(player.name)<3:
        print('+'*94)

    ###Plotting Player 3-4
    else:
        print('|\t'.expandtabs(18)+('*'*26)+'\t'.expandtabs(6)+('*'*26)+'\t|'.expandtabs(17))
        if len(player.name)<4:
            print('|\t*'.expandtabs(18)+f"{player.name[2]}'s Platz:".center(24)+'*'+'\t*'.expandtabs(6)+'Platz unbesetzt'.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Verfügbare Chips: {player.total[player.name[2]]}".center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Einsatz: {player.bet[player.name[2]]} Chips".center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+''.center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Karten auf der Hand:".center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            for card in range(0,len(player.hand[player.name[2]].cards)):
                print('|\t*'.expandtabs(18)+player.hand[player.name[2]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Kartenwert: {player.hand[player.name[2]].value}".center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            print('|\t'.expandtabs(18)+('*'*26)+'\t'.expandtabs(6)+('*'*26)+'\t|'.expandtabs(17))

        else:
            print('|\t*'.expandtabs(18)+f" {player.name[2]}'s Platz:".center(24)+'*'+'\t*'.expandtabs(6)+f" {player.name[3]}'s Platz:".center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Verfügbare Chips: {player.total[player.name[2]]}".center(24)+'*'+'\t*'.expandtabs(6)+f' Verfügbare Chips: {player.total[player.name[3]]}'.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Einsatz: {player.bet[player.name[2]]} Chips".center(24)+'*'+'\t*'.expandtabs(6)+f' Einsatz: {player.bet[player.name[3]]} Chips'.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+''.center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Karten auf der Hand:".center(24)+'*'+'\t*'.expandtabs(6)+' Karten auf der Hand:'.center(24)+'*\t|'.expandtabs(18))
            for card in range(0,2):
                print('|\t*'.expandtabs(18)+player.hand[player.name[2]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(6)+player.hand[player.name[3]].cards[card].__str__().center(24)+'*\t|'.expandtabs(18))
            try:
                for card in range(2,len(player.hand[player.name[2]].cards)):
                    print('|\t*'.expandtabs(18)+player.hand[player.name[2]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(6)+player.hand[player.name[3]].cards[card].__str__().center(24)+'*\t|'.expandtabs(18))
            except:
                for card in range(len(player.hand[player.name[3]].cards),len(player.hand[player.name[2]].cards)):
                    print('|\t*'.expandtabs(18)+player.hand[player.name[2]].cards[card].__str__().center(24)+'*'+'\t*'.expandtabs(6)+''.center(24)+'*\t|'.expandtabs(18))
            else:
                for card in range(len(player.hand[player.name[2]].cards),len(player.hand[player.name[3]].cards)):
                    print('|\t*'.expandtabs(18)+''.center(24)+'*'+'\t*'.expandtabs(6)+player.hand[player.name[3]].cards[card].__str__().center(24)+'*\t|'.expandtabs(18))
            print('|\t*'.expandtabs(18)+f"Kartenwert: {player.hand[player.name[2]].value}".center(24)+'*'+'\t*'.expandtabs(6)+f"Kartenwert: {player.hand[player.name[3]].value}".center(24)+'*\t|'.expandtabs(18))
            print('|\t'.expandtabs(18)+('*'*26)+'\t'.expandtabs(6)+('*'*26)+'\t|'.expandtabs(17))
        print('|'+'|'.rjust(93))
        print('+'*94)                  
        
# Definition der Spielregeln
def rules(start):
    while True:
        if start==0:
            print('Schön, dass Sie sich für eine kleine Partie entschieden haben!')
            try:
                rule=input('Sind Sie bereits mit den Spielregeln vertraut?')[0].lower()
            except:
                print("Sie können nur Ja oder Nein eingeben!")
            else:
                if not (rule=='j' or rule=='n'):
                    print("Sie können nur Ja oder Nein eingeben")
                    continue
                else:
                    break
        elif start>0 and start<3:
            try:
                rule=input('Haben Sie die Spielregeln noch im Kopf?')[0].lower()
            except:
                print("Sie können nur Ja oder Nein eingeben!")
            else:
                if not (rule=='j' or rule=='n'):
                    print("Sie können nur Ja oder Nein eingeben")
                    continue
                else:
                    break
    if rule=='n':
        print('\nOk. Hier die Kurzfassung:\n\nBei Black Jack geht es darum möglichst nahe an die Zahl 21 zu kommen, aber nicht darüber.\nEs wird mit französischem Blatt mit 4 Kartensätzen (208 Karten) gespielt.\nJede Karte hat dabei Ihren aufgedruckten Wert, mit Ausnahme von Bube, Dame und König. Diese haben den Wert 10')
        print('Eine Besonderheit ist das Ass; es kann den Wert 11 oder 1 annehmen.\nDie Wertung erfolgt immer dann mit 1, wenn der Wert der Karten auf Ihrer Hand sonst die 21 übersteigen würde.\nEs werden am Anfang des Spiels Karten aus dem gemischten Kartensatz an Sie und den Croupier ausgegeben.')
        print('Die Karten sind für alle sichtbar. Die Spieler bekommen dann jeweils noch eine zweiter Karte, der Croupier erst nachdem alle Spieler ihre Züge ausgeführt haben und nicht alle verloren haben.\n')
        print('So viel zu den Karten. Jetzt zum Geld!\n')
        print('Sie müssen für die Teilnahme am Spiel einen Einsatz von mindestens den angezeigten Wert setzen.\nWenn Sie gewinnen, erhalten Sie diesen Einsatz ausgezahlt, ansonsten geht Ihr Einsatz an die Bank.')
        print('Wenn Sie mit Ihren ersten beiden Karten auf den Wert von 21 kommen (Ass+Zehn/Dame/König/Bube) halten Sie einen Blackjack.\nWenn der Croupier ebenfalls einen Blackjack hält, ist dies ein Patt für Sie, ansonsten erhalten Sie den 1,5-fachen Wettwert.')
        print('Wenn Sie Ihre ersten beiden Karten gesehen haben und keinen BlackJack haben, können Sie entscheiden, ob Sie Ihren Einsatz verdoppeln möchten (Double down).\nWenn Sie verdoppeln, bekommen Sie automatisch noch eine Karte.')
        print('Möchten Sie nicht verdoppeln, können Sie entscheiden, ob Sie eine weitere Karte ziehen möchten, um näher an die 21 zu kommen, oder Ihr Blatt halten.')
        print('Wenn Sie mit der neuen Karte über 21 kommen, haben Sie sofort verloren, ansonsten können Sie wieder entscheiden, ob Sie eine neue Karte ziehen möchten.\n')
        print('Möchten Sie keine neue Karte ziehen, ist der Croupier dran und erhält eine neue Karte.\nSofern der Croupier Karten unter einem Wert von 17 hat, muss er eine neue Karte ziehen.')
        print('Hat der Croupier einen Wert über 21, haben Sie gewonnen. Hat er einen Blackjack verlieren alle Spieler, es sei denn sie halten auch einen Blackjack.')
        print('Hat er hingegen einen Wert größer als Sie und zwischen 17 und 21, verlieren Sie Ihren Einsatz.\n')
        
    else:
        print('\nWenn Sie meinen, dass Sie schon alles wissen, dann viel Erfolg!\n')
        
# Definition Wiederholung:
def replay(player):
    again=0
    p=''
    while True:
        try:
            p=input('\nSpannendes Spiel! Wollen Sie noch einmal spielen?')[0].lower()
        except:
            print("Sie können nur Ja oder Nein eingeben!")
        else:
            if not (p=='j' or p=='n'):
                print("Sie können nur Ja oder Nein eingeben")
                continue
            elif p=='j':
                again=1
                player.hand={}
                player.bet={}
                while True:
                    try:
                        p=input('\nSoll die Zusammensetzung der Spieler (Anzahl und Teilnehmer) in der nächsten Runde bestehen bleiben?')[0].lower()
                    except:
                        print("Sie können nur Ja oder Nein eingeben!")
                    else:
                        if not (p=='j' or p=='n'):
                            print("Sie können nur Ja oder Nein eingeben")
                            continue
                        elif p=='n':
                            player.name=[]
                            break
                        else:
                            break
                break
            else:
                break
    
    return again
