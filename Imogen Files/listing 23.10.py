def computer_turn():
    global c_hand, deck, up_card, active_suit, blocked
    options = []
    for card in c_hand:
        if card.rank == '8':

            c_hand.remove(card)
            up_card  = card
            print " Computer played ", card.short_name
            suit_totals = [0, 0, 0, 0]
            for suit in range(1, 5):
                for card in c_hand:
                    if card.suit_id == suit:
                        suit_totals[suit-1] += 1
            long_suit = 0
            for i in range (4):
                if suit_totals[i] > long_suit:
                    long_suit = i
            if long_suit == 0:
                active_suit = "Diamonds"
            if long_suit == 1:
                active_suit = "Hearts"
            if long_suit == 2:
                active_suit = "Spades"
            if long_suit == 3:
                active_suit = "Clubs"
            print " Computer changed suit to ", active_suit
            return
        else:
            if card.suit == active_suit:
                options.append(card)
            elif card.rank == up_card.rank:
                options.append(card)

    if len(options) > 0:
        best_play = options[0]
        for card in options:
            if card.value > best_play.value:
                best_play = card

        c_hand.remove(best_play)
        up_card = best_play
        active_suit = up_card.suit
        print " Computerplayed ", best_play.short_name

    else:
        if len(deck) >0:
            next_card = random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print " Computer drew a card"
        else:
            print" Computer is blocked"
            blocked += 1
    print "Computer has %i cards left" % (len(c_hand))
