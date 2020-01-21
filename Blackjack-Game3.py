'''
This is the main GamePlay for Blackjack with up to 4 players.
Double Down and holding blackjack has been taken into consideration.

Have fun playing the game! I'm always happy for feedback and new ideas 
'''
'''Import Section'''
from Gamebasis import Classes
from Gamebasis import functions2
import random
import time
'''Script Section for Gameplay'''


print('Herzlich Willkommen in unserem kleinen Black Jack-Casino!\nSie können in unserem Haus nur mit Chips spielen, die Sie kaufen müssen.\n')
again=0
start=0
player=Classes.Player()
while True:
    numplay=functions2.num_player(start)
    mindest=random.randint(1,30)
    print('\n'*100)
    player.get_names(start, numplay)
    player.buy_chips(mindest, start, numplay)
    print('\n'*100)
    if start<2:
        functions2.rules(start)
        input('Super, dann kanns ja jetzt losgehen. Drücken Sie bitte Enter um fortzufahren.')
        print('\n'*100)
    player.take_bet(mindest, numplay)
    print('\n'*100)
    print('Super, dann werden jetzt die Karten verteilt! Bitte warten Sie einen Moment!\n')
    
    # Create & shuffle the deck, deal two cards to each player
    deck=Classes.Deck()
    deck.shuffle()
    
    #Initialize Dealer Hand    
    dealer_hand=Classes.Hand()
    player.deal_cards(deck)
    dealer_hand.add_card(deck.deal())
    player.deal_cards(deck)
    
    # Show cards (players hold 2 cards, dealer 1, gets second after players took action)
    time.sleep(6)
    functions2.show_some(player,dealer_hand)
    time.sleep(5)
    
    turn=0 #Variable for calling players
    stillin=[] # Variable for checking if player is still in. 0: dropped out, 1: still in, 2: Blackjack
    
    ##Player's interaction
    while turn<numplay:
        first=0
        while True:
            hold=0
            double=0
           
            if first==0:  #check for blackjack and double down
                
                 # Check for Blackjack
                    
                if (player.hand[player.name[turn]].value==21):
                    print('\n'*100)
                    functions2.show_some(player,dealer_hand)
                    print(f'{player.name[turn]}, Sie halten ein Blackjack. Wenn der Croupier keinen Blackjack zieht, gewinnen Sie den 1,5-fachen Einsatz!')
                    stillin.append(2) #Continues Playing with Blackjack--> Checking with Dealers hand
                    break
                
                
                else: # Check for double down
                    double=player.double(deck, turn, double)  
                    print('\n'*100)
                    functions2.show_some(player, dealer_hand)

                    if double==1:# Double, check for exceeding 21
                        if player.hand[player.name[turn]].value>21:
                            print(f'\n{player.name[turn]}, Sie haben folgende Karte gezogen: {player.hand[player.name[turn]].cards[-1]}')
                            time.sleep(3)
                            print(f'\n{player.name[turn]}, es ist ein Bust. Sie haben hoch gepokert und verlieren Ihren Einsatz ({player.bet[player.name[turn]]} Chips)!')
                            player.lose_bet(turn)
                            stillin.append(0) # Drops out
                            break
                        else:
                            print(f'\n{player.name[turn]}, Sie haben folgende Karte gezogen: {player.hand[player.name[turn]].cards[-1]}')
                            time.sleep(3)
                            stillin.append(1) #Continues Playing--> Checking with Dealers hand
                            break
                    else: #No double down, jump to hit or stand
                        first+=1
                        continue
                        
                        
            else:#no black_jack or double down
                
                
                # Prompt for Player to Hit or Stand
                hold=player.hit_or_stand(deck, turn, hold)
                
                
                if hold==0: #Check for Player's new card exceeding 21

                    #Show Cards
                    print('\n'*100)
                    functions2.show_some(player, dealer_hand)

                    print(f'{player.name[turn]}, Sie haben folgende Karte gezogen: {player.hand[player.name[turn]].cards[-1]}')
                    if player.hand[player.name[turn]].value>21:
                        print(f'\n{player.name[turn]}, es ist ein Bust. Sie verlieren Ihren Einsatz ({player.bet[player.name[turn]]} Chips)!')
                        player.lose_bet(turn)
                        stillin.append(0) # Drops out
                        break
                    else:
                        first+=1
                        continue
                        
                else: #Player holds
                    print(f'{player.name[turn]} hält!')
                    stillin.append(1) #Continues Playing--> Checking with Dealers hand
                    break
                                   
        if turn<(numplay-1):
            input(f'{player.name[turn]}, drücken Sie Enter, um an {player.name[turn+1]} weiterzugeben.')
        turn+=1
    
    
    # If all Player have busted, game ends. Else comparison between players and dealer
    if (1 not in stillin) and (2 not in stillin):
        time.sleep(3)
        print('\nAlle Spieler haben einen Bust! Das Spiel ist beendet.')
        print('\n\nHier sehen Sie noch einmal eine Übersicht der Karten und Ihre noch verfügbaren Chips.\n')
        functions2.show_all(player,dealer_hand)                        
    
    else:#Check Dealer's Hand
        input(f'{player.name[-1]}, drücken Sie Enter, um an den Croupier weiterzugeben.')  
                                   
        # Hand out second card to dealer
        print('\nDer Croupier zieht seine zweite Karte!')
        time.sleep(3)
        dealer_hand.add_card(deck.deal())
        print('\n'*100)
        functions2.show_all(player,dealer_hand)
        
        # Check for Blackjack with Dealer's Cards
        if dealer_hand.value==21: # Dealer holds Blackjack
            time.sleep(4)
            print('\nDer Croupier hält einen Black Jack!\n')
            for num in range(0,numplay):
                if stillin[num]==2:
                    print(f'Ein Patt für Sie, {player.name[num]}! Sie verlieren nicht, gewinnen aber auch nichts.\n')
                elif stillin[num]==1: 
                    print(f'{player.name[num]}, Sie verlieren Ihren Einsatz.\n')
                    player.lose_bet(num)
        else:
            if dealer_hand.value<17:
                print('\nDer Croupier hat einen Kartenwert von weniger als 17. Er muss weitere Karten ziehen.')
                while dealer_hand.value<17:
                    functions2.hit(deck,dealer_hand)
                # Show all cards
                time.sleep(3)
                print('\n'*100)
                functions2.show_all(player,dealer_hand)
                        
            # Run different winning scenarios
            time.sleep(6)
            for num in range(0,numplay):
                if stillin[num]==2:
                    print(f'\n{player.name[num]}, Sie gewinnen mit Ihrem Blackjack den 1,5-fachen Einsatz.')
                    player.bet[player.name[num]]*=1.5
                    player.win_bet(num)
                        
                elif stillin[num]==1:
                    if dealer_hand.value>21: # Dealer Busting
                        print(f'\n{player.name[num]}, der Croupier hat einen Bust. Sie gewinnen Ihren Einsatz.')
                        player.win_bet(num)
                    
                    elif player.hand[player.name[num]].value>dealer_hand.value:  # Player holds higher value--> winning
                        print(f'\n{player.name[num]}, Ihr Kartenwert ist höher, als der des Croupier. Sie gewinnen Ihren Einsatz.')
                        player.win_bet(num)
                                  
                    elif player.hand[player.name[num]].value<dealer_hand.value:# Dealer holds higher value--> losing
                        print(f'\n{player.name[num]}, Ihr Kartenwert ist niedriger, als der des Croupier. Sie verlieren Ihren Einsatz.')
                        player.lose_bet(num)
                       
                    else:
                        print(f'Ein Patt für Sie, {player.name[num]}! Sie verlieren nicht, gewinnen aber auch nichts.\n')
        
        time.sleep(4)
        print('\n\nHier sehen Sie noch einmal eine Übersicht der Karten und Ihre noch verfügbaren Chips.\n')
        functions2.show_all(player,dealer_hand)     
           
    # Ask to play again
    if functions2.replay(player):
        print('\nDa ist wohl jemand angefixt. Sehr schön, dann auf in eine neue Runde!')
        start+=1
        continue
    else:
        print('\nIch hoffe es hat Spaß gemacht. Bis bald mal wieder!')
        break