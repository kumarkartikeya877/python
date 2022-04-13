import random
from blackjack_art import logo
def deal_cards():
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(deck)
def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare_score(player_score,dealer_score):
    if player_score>21:
        return "___YOU LOSE___"
    elif dealer_score >21   :
        return "___YOU WIN___"
    elif player_score == dealer_score:
        return "___DRAW___"
    elif dealer_score == 0:
        return "___YOU LOSE___"
    elif player_score == 0:
        return "___YOU WIN___"
    elif player_score>dealer_score:
        return "___YOU WIN___"
    else :
        return "___YOU LOSE___"
def play_game():
    player = []
    dealer = []
    is_game_over = False
    print(logo)
    for _ in range(2):
        player.append(deal_cards())
        dealer.append(deal_cards())
    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)
    while not is_game_over:
        print("your cards:",player,"|| score:",player_score)
        print("dealer first card:",dealer[0])
        if player_score == 0 or dealer_score == 0 or player_score>21:
            is_game_over = True
        else:
            if input("want another card ?  ")=="y":
                player.append(deal_cards())
                player_score = calculate_score(player)
                
            else:
                is_game_over = True
        while dealer_score < 17 and dealer_score!=0:
            dealer.append(deal_cards())
            dealer_score = calculate_score(dealer)
            
    print("your final hand:",player,"|| score:",player_score)
    print("dealer final hand:",dealer,"|| score:",dealer_score)
    print(compare_score(player_score,dealer_score))
while input("do you wanna play a game of blackJack ? type 'y' or 'n': ")=="y":
    play_game()

    
        
                
               
    
