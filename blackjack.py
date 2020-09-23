
import random
import math

# Python program for hit or sit game

def face_to_value(arg):
    switcher = {
        'J': 10,
        'Q': 10,
        'K': 10,
        }
    # default case of the switch statement
    return switcher.get(arg, "Not Possible")
def ace_to_value(count):
        return 1
def ace_algo(count, hand):
    hand_length = len(hand)
    for i in range(hand_length):
        if hand[i] == 'A':
           # print("found an ace in your hand!")
            if count + 10 <= 21:
                print("an 11 is more beneficial b/c you'll have:", count+10)
                count += 10
                return count
            else:
                print("an 11 is not beneficial")
                return count
        
  #  print("there was no Ace in the hand")
    
    return count
    
def user_input(arg):
    switcher = {
        'y': 1,
        "yes": 1,
        'Y': 1,
        'n': 0,
        'N': 0,
        "no": 0,
        }
    return switcher.get(arg, 2)

def sit_hit(arg):
    switcher = {
        'hit': 1,
        "Hit": 1,
        'h': 1,
        'stand': 0,
        'Stand': 0,
        "s": 0,
        }
    #fix the default case
    return switcher.get(arg, 2)

def bet(wallet, bet_amount):

    if bet_amount > 0 and bet_amount <= wallet:
        return True
    else:
        return False

# 2-10 = face value
# J, Q , K = 10
# A can be 1 or 11 based on hand
def card_to_index(arg):
    switcher = {
        2: 0,
        3: 1,
        4: 2,
        5: 3,
        6: 4,
        7: 5,
        8: 6,
        9: 7,
        10: 8,
        'J': 9,
        'Q': 10,
        'K': 11,
        'A': 12,
        }
    return switcher.get(arg, "Card doesn't exist")

def show_mid_hands(players_cards, dealers_cards):
    print("This is your current hand: ")
    hand_length = len(players_cards)
    for i in range(hand_length):
        print(str(players_cards[i]), end =" ")
    print(" ")

    print("This is the dealer's hand: ")
    dealer_hand_length = len(dealers_cards)
        
    for i in range(dealer_hand_length-1):
        print(str(dealers_cards[i+1]), end=" ")
    print(" ")

def show_end_hands(players_cards, dealers_cards, count, dealer_count, bet_amount, wallet):
    print("Please show your hand")
    hand_length = len(players_cards)
    
    for i in range(hand_length):
        print(str(players_cards[i]), end =" ")
    print(" ")
    print(" ")
    print("This was how much was in your hand: " + str(count))
    
    print(" ")
    # print("everything from dealer's hand:", dealers_cards)
    print("The Dealer will now show their hand")

    # for now, print the dealer's hand too as if they give up
    dealer_hand_length = len(dealers_cards)
    
    for i in range(dealer_hand_length):
        print(str(dealers_cards[i]), end =" ")
    print(" ")
    print("This was how much was in the Dealer's hand: " + str(dealer_count))
    print(" ")
    print("Results:")
    wallet = determine_winner(bet_amount, wallet, count, dealer_count)
    return wallet

def immediate_BJ(dealer_count, count, dealers_cards, users_cards, bet_amount, wallet):
    win_rate = 1.5


    count = ace_algo(count, users_cards)

    dealer_count = ace_algo(count, dealers_cards)
    if dealer_count == 21 and count == 21:
        print("There was a TIE")
        print("This is the dealer's hand: ")
        dealer_hand_length = len(dealers_cards)
            
        for i in range(dealer_hand_length):
            print(str(dealers_cards[i]), end=" ")
        print("You get to keep your", bet_amount, "dollar(s)")
        print(" ")
        return wallet
    elif count == 21:
        print("BLACKJACK, you win")
        cash_back = win_rate*bet_amount
        print("NICE, you get", cash_back, "dollars")
        wallet = wallet + cash_back
        return wallet
    elif dealer_count == 21:
        print("Dealer Black Jack")
        
        wallet = wallet - bet_amount
        print("This is the dealer's hand: ")
        dealer_hand_length = len(dealers_cards)
            
        for i in range(dealer_hand_length):
            print(str(dealers_cards[i]), end=" ")
        print("You lost the amount that you just bet to the Dealer!")
        print("you now have", wallet, "dollars")
        print(" ")
        
        return wallet
    return wallet

def determine_winner(bet_amount, wallet, count, dealer_count):
    win_rate = 1.5
    cash_back = bet_amount*win_rate

    if dealer_count == count:
        print("TIE")
        print("You get to keep your", bet_amount, "dollar(s)")
    elif dealer_count > 21 and count <= 21:
        print("dealer bust, but you win")
        print("NICE, you get", cash_back, "dollars")
        wallet = wallet + cash_back
    elif dealer_count <= 21 and count > 21:
        print("you bust, dealer wins")
        wallet = wallet - bet_amount
        print("You lost the amount that you just bet to the Dealer!")
        print("you now have", wallet, "dollars")
    elif dealer_count <= 21 and dealer_count >= count:
        print("dealer wins!")
        wallet = wallet - bet_amount
        print("You lost the amount that you just bet to the Dealer!")
        print("you now have", wallet, "dollars")
    elif count >= dealer_count and count <= 21:
        print("You win!")
        print("NICE, you get", cash_back, "dollars")
        wallet = wallet + cash_back
    elif count > 21:
        print("BUST, dealer wins")
        wallet = wallet - bet_amount
        print("You lost the amount that you just bet to the Dealer!")
        print("you now have", wallet, "dollars")
    print(" ")
    return wallet

def dealer_repeater(deck, times_seen, dealers_cards, dealer_count, dealer_hand_count):
    dealer_hits = False
    print("Dealer hits!")
    #dealer only hits if they're not close to 21
    if dealer_count >= 17 and dealer_count <= 21:
      #  print("dealer's current hand is p good")
        pass
    elif dealer_count < 17:
        # we want the dealer to hit
      #  print("dealer's hand is less than 18")
        dealer_card = random.choice(deck)
        print("this is the dealer's card:", dealer_card)
        dealer_hand_count = dealer_hand_count + 1
        dealers_cards.append(dealer_card)
        dealer_hits = True
    # print("everything from dealer's hand:", dealers_cards)
    print("This is the dealer's hand: ")
    dealer_hand_length = len(dealers_cards)
        
    for i in range(dealer_hand_length-1):
        print(str(dealers_cards[i+1]), end=" ")
    print(" ")

    # decrement from the deck IF Dealer hits
    if dealer_hits == True: # we can try later if just (dealer_hits) works
        index2 = card_to_index(dealer_card)
        times_seen[index2] = times_seen[index2] + 1

        letter2 = str(dealer_card)
        if letter2.isalpha():
            if letter2 == 'A':
                dealer_count = dealer_count + ace_to_value(dealer_count)
            else:
                dealer_count = dealer_count + face_to_value(dealer_card)
        else:
            dealer_count = dealer_count + dealer_card
        dealer_hits = False

    return deck, times_seen, dealers_cards, dealer_count, dealer_hand_count

def draw_card_user(deck, user_cards, count, times_seen, hand_count):
    # function to draw a card for anyone
    card = random.choice(deck)
    user_cards.append(card)
    hand_count = hand_count + 1

    # check if already 4 instances of that card so
    # we can pop that element from the deck
    ts_length = len(times_seen)
    for i in range(ts_length):
        if times_seen[i] == 4:
            deck.pop(i)
            times_seen.pop(i)
            

    
    # decrement from the overall deck, that card
    index = card_to_index(card)
    times_seen[index] = times_seen[index] + 1

    # let the user know the value of their hand
    letter = str(card)
    if letter.isalpha():
        if letter == 'A':
            count = count + ace_to_value(count)
        else:
            count = count + face_to_value(card)
    else:
        count = count + card

    return deck, user_cards, count, times_seen, hand_count

# assuming 1D array for the user hand
def check_split(user_hand):
    no_dupes = list(set(user_hand))
    print("user_hand in func:", user_hand)
    print("no_dupes in funct:", no_dupes)

    # there are no dupes
    if len(no_dupes) == len(user_hand):
        print("there are no dupes in func")
        return False
    print("there ARE dupes in func")
    return True

def create_split(user_hand):
    tmp_array = []
    result = []
    for i in user_hand:
        tmp_array.append(i)
        result.append(tmp_array)
        tmp_array = []
    return result

def repeater(deck, times_seen, players_cards, count, hand_count, dealers_cards, dealer_count, dealer_hand_count, bet_amount, wallet):
        # random sampling
 
        #print("this is how many cards you have so far: " + str(hand_count))
        if hand_count >= 4:
            print("You got more than 4 cards buddy, seems pretty risky")
            #return
        win_rate = 1.5
       # dealer_less_than = False
        #print("dealer's cards look like this:", dealers_cards)
        card = random.choice(deck)
        hand_count = hand_count + 1
        players_cards.append(card)
        print("This is your card: " + str(card))
        
        show_mid_hands(players_cards, dealers_cards)

        # check if already 4 instances of that card so
        # we can pop that element from the deck
        ts_length = len(times_seen)
        for i in range(ts_length):
            if times_seen[i] == 4:
                deck.pop(i)
                times_seen.pop(i)

        # decrement from the overall deck, that card
        index = card_to_index(card)
        times_seen[index] = times_seen[index] + 1
        
       # print("this was the index: " + str(index))
       # print("index's current value is now: " + str(times_seen[index]))
        
        # let the user know the value of their hand
        letter = str(card)
        if letter.isalpha():
            if letter == 'A':
                count = count + ace_to_value(count)
            else:
                count = count + face_to_value(card)
        else:
            count = count + card
            
        #check split from beginning
        if check_split(players_cards):
            print("you'are able to split with this!")
        while True:
            
            sh_prompt = input("Would you like to hit or stand? ")
            if sit_hit(sh_prompt) == 2:
                print("That's not a choice buddy")
                continue
            else:
                break
        

        #hit case
        if sit_hit(sh_prompt) == 1:
            #do some func call to allow user to get
            # more cards, inc the times_seen, and inc count
            print("you wanted to hit")
            dealer_less_than = False
            return repeater(deck, times_seen, players_cards, count, hand_count, dealers_cards, dealer_count, dealer_hand_count, bet_amount, wallet)

        #sit case
        elif sit_hit(sh_prompt) == 0:
            # please show your hand
            # this was how much you had
            print("you chose to stand")

            count = ace_algo(count, players_cards)

            #function call to Dealer_repeater
            while dealer_count < 17:
                #print("this is the dealer count in repeater func in loop:", dealer_count)
                # function call to dealer_repeater
                deck, times_seen, dealers_cards, dealer_count, dealer_hand_count = dealer_repeater(deck, times_seen, dealers_cards, dealer_count, dealer_hand_count)
            print("Dealer chose to stand")
            dealer_cont = ace_algo(dealer_count, dealers_cards)
            wallet = show_end_hands(players_cards, dealers_cards, count, dealer_count, bet_amount, wallet)
            while True:

                if wallet <= 0:
                    break
            
                replay = input("Would you like to keep playing? ")
                if user_input(replay) == 2:
                    print("Sorry, you need to speak louder. My eyes aren't what they used to be")
                    
                elif user_input(replay) == 1:
                    black_jack(wallet)
                else:
                    break

def black_jack(money_given):
    #13 unique elements, 4 of each copy
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    times_seen = [0]*13

    # for now, assume hand is only 4 cards
    players_cards = []*4
    players_hand = []
    dealers_cards = []*4
    hand_count = 0
    dealer_hand_count = 0
    
    print(
        '''
    Welcome to


         (                                                              
         )\ )          )    )                  )                  (     
        (()/( (     ( /( ( /(               ( /(     )        (   )\ )  
         /(_)))\ )  )\()))\())  (    (      )\()) ( /(  (    ))\ (()/(  
        (_)) (()/( (_))/((_)\   )\   )\ )  ((_)\  )(_)) )\  /((_) ((_)) 
        | _ \ )(_))| |_ | |(_) ((_) _(_/(  | |(_)((_)_ ((_)(_))   _| |  
        |  _/| || ||  _|| ' \ / _ \| ' \)) | '_ \/ _` |(_-</ -_)/ _` |  
        |_|   \_, | \__||_||_|\___/|_||_|  |_.__/\__,_|/__/\___|\__,_|  
              |__/                                                      

    

▀█████████▄   ▄█          ▄████████  ▄████████    ▄█   ▄█▄           ▄█    ▄████████  ▄████████    ▄█   ▄█▄ 
  ███    ███ ███         ███    ███ ███    ███   ███ ▄███▀          ███   ███    ███ ███    ███   ███ ▄███▀ 
  ███    ███ ███         ███    ███ ███    █▀    ███▐██▀            ███   ███    ███ ███    █▀    ███▐██▀   
 ▄███▄▄▄██▀  ███         ███    ███ ███         ▄█████▀             ███   ███    ███ ███         ▄█████▀    
▀▀███▀▀▀██▄  ███       ▀███████████ ███        ▀▀█████▄             ███ ▀███████████ ███        ▀▀█████▄    
  ███    ██▄ ███         ███    ███ ███    █▄    ███▐██▄            ███   ███    ███ ███    █▄    ███▐██▄   
  ███    ███ ███▌    ▄   ███    ███ ███    ███   ███ ▀███▄          ███   ███    ███ ███    ███   ███ ▀███▄ 
▄█████████▀  █████▄▄██   ███    █▀  ████████▀    ███   ▀█▀      █▄ ▄███   ███    █▀  ████████▀    ███   ▀█▀ 
             ▀                                   ▀              ▀▀▀▀▀▀                            ▀         
                                              
                                                                                                                                                     

    Directions:

    1) The goal of Black Jack is to beat the dealer's hand
    without going over 21.
        
    2) Face cards are worth 10 and Aces are either worth 1 or 11.
    You get to decide to go with whichever suits you.

    3) To 'Hit' is to ask for another card. To 'Stand' is to
    hold your total and end your turn.

    4) You will lose if you go over 21 or
    if the dealer's hand is higher than yours.
        
        '''
        )
    # beating the dealer by getting closer to 21 thna the dealer without
    # going over 21 (game otherwise known as 21)

    #ways to lose:
    # Dealer closer to 21 than you
    # you're over 21 (immediate lose)
    
    #more instructions later

    # dealer and player dealt 2 cards, but one card of dealer is shown
    # player ALWAYS goes first, have option to hit or stand
    
    # if dealer amnt is same as player, then push
    # if player > dealer and <= 21, then win

    ## remember, since the player plays first, if both player and dealer bust,
    ## then player loses

    ## if player is dealt a black jack (A + Face card) they win immediately (paid 3:2/ 150%)
    ## UNLESS dealer also has a blackjack

    ## user has choices:
    ## -> hitting (tap/ swipe) to get another card
    ## -> standing (wave) good hand/ don't want a bust
    ## -> splitting (same card)
    ## -> doubling down (placing equal bet to previous bet)


    # edge case
    if (money_given <= 0):
        print("get out, you got no money")
        return
    while True:

        prompt = input("Ready to play? y or n: ")
        if user_input(prompt) == 2:
            print("Sorry, your response was not loud enough")
            continue
        else:
            break
    if user_input(prompt) == 1:
        print("you said yes")

        # give $100 to spend
        # ask: how much do you want to bet?
        wallet = money_given
        win_rate = 1.5
        print("you have currently: $", wallet, "dollars")
        #bet_amount = input("How much do you want to bet? ")

        while True:

            bet_amount = int(math.floor(float(input("How much do you want to bet? "))))
            if bet(wallet, bet_amount) == False:
                print("Looks like you're trying to cheat somehow. Try again")
                continue
            else:
                break
                

        # assuming no cards, give the player a card
        # initialization of card count
        count = 0
        dealer_count = 0




        #first card sampling
        deck, players_cards, count, times_seen, hand_count = draw_card_user(deck, players_cards, count, times_seen, hand_count)

        
        deck, dealers_cards, dealer_count, times_seen, dealer_hand_count = draw_card_user(deck, dealers_cards, dealer_count, times_seen, dealer_hand_count)

    
        # random sampling (SECOND CARD)


        deck, players_cards, count, times_seen, hand_count = draw_card_user(deck, players_cards, count, times_seen, hand_count)
        deck, dealers_cards, dealer_count, times_seen, dealer_hand_count = draw_card_user(deck, dealers_cards, dealer_count, times_seen, dealer_hand_count)

        #check split from beginning
        
        
        show_mid_hands(players_cards, dealers_cards)
        split_possible = check_split(players_cards)
        yes_to_split = False
        if split_possible:
            print("you'are able to split with this!")
            while True:

                split_prompt = input("would you like to split?")
                if user_input(split_prompt) == 2:
                    print("Sorry, your response was not loud enough")
                    continue
                elif user_input(split_prompt) == 1:
                    yes_to_split = True
                    print(create_split(players_cards))
                    break
                else:
                    yes_to_split = False
                    break

        
        
        old_wallet = wallet
        wallet = immediate_BJ(dealer_count, count, dealers_cards, players_cards, bet_amount, wallet)

        if wallet != old_wallet: # wallet was updated
            while True:
                
            
                replay = input("Would you like to keep playing? ")
                if user_input(replay) == 2:
                    print("Sorry, you need to speak louder. My eyes aren't what they used to be")
                elif user_input(replay) == 1:
                    black_jack(wallet)
                else:
                    break
        while True:
            sh_prompt = input("Would you like to hit or stand? ")
            if sit_hit(sh_prompt) == 2:
                print("That's not a choice buddy")
                continue
            else:
                break

        #hit case
        if sit_hit(sh_prompt) == 1:
            #do some func call to allow user to get
            # more cards, inc the times_seen, and inc count
            print("you wanted to hit")
            repeater(deck, times_seen, players_cards, count, hand_count, dealers_cards, dealer_count, dealer_hand_count, bet_amount, wallet)
            

        #sit case
        elif sit_hit(sh_prompt) == 0:
            # please show your hand
            # this was how much you had
            print("you chose to stand")


            count = ace_algo(count, players_cards)

            while dealer_count < 17:
                #print("this is the dealer count in main in loop:", dealer_count)
                # function call to dealer_repeater
                deck, times_seen, dealers_cards, dealer_count, dealer_hand_count = dealer_repeater(deck, times_seen, dealers_cards, dealer_count, dealer_hand_count)
            print("Dealer chose to stand")
            dealer_count = ace_algo(dealer_count, dealers_cards)
            wallet = show_end_hands(players_cards, dealers_cards, count, dealer_count, bet_amount, wallet)
            while True:

                if wallet <= 0:
                    break
            
                replay = input("Would you like to keep playing? ")
                if user_input(replay) == 2:
                    print("Sorry, you need to speak louder. My eyes aren't what they used to be")
                elif user_input(replay) == 1:
                    black_jack(wallet)
                else:
                    break

        #code to run for black_jack
        #prompt the user to play again
    elif user_input(prompt) == 0:
        print("you said no")
        #thank the player
    

    print("thanks for playing")
    # implement a retry that recalls the main function

    


