import blackjack

bj = blackjack.BlackJack(1)


def dealer(dealerHand: list) -> int:
    while True:
        dealerHand = bj.bestSum(dealerHand)
        total = sum(dealerHand)
        print("Dealer's Hand: {}\tSum: {}".format(dealerHand, sum(dealerHand)))
        if bj.checkBlackJack(dealerHand) == True:
            print("BlackJack")
            return total
        if bj.checkBust(dealerHand) == True:
            print("Bust")
            return total
        if sum(dealerHand) >= 17:
            print("Stand")
            return total
        dealerHand = bj.hit(dealerHand)


def player(playerHand: list) -> int:
    while True:
        total = sum(playerHand)
        print("Your Hand: {}\tSum: {}".format(playerHand, total))
        if bj.checkBlackJack(playerHand) == True:
            print("BlackJack")
            return total
        if bj.checkBust(playerHand) == True:
            print("Bust")
            return total
        choice = input('h/s/d: ')

        match choice:
            case "h":
                playerHand = bj.hit(playerHand)
                total = sum(playerHand)
                # print("Your Hand: {}\tSum: {}".format(playerHand, total))
            case "s":
                print("Stand")
                return total
            case "d":
                if len(playerHand) == 2:
                    playerHand = bj.hit(playerHand)
                    total = sum(playerHand)
                    # print("Your Hand: {}\tSum: {}".format(playerHand, total))
                    print("Double Down")
                    return total
            case _:
                pass


def outcome(playerOutcome: int, dealerOutcome: int) -> str:
    if playerOutcome == dealerOutcome:
        return 0

    if playerOutcome == 21:
        return 1

    if playerOutcome > 21:
        return -1

    if dealerOutcome > 21:
        return 1

    if playerOutcome > dealerOutcome:
        return 1

    if dealerOutcome > playerOutcome:
        return -1


def play() -> None:
    dealerHand = bj.dealHand()

    playerHand = bj.dealHand()

    print("Dealer Card: {}".format(dealerHand[0]))

    # print("Your Hand: {}".format(playerHand))

    playerOutcome = player(playerHand)

    print("\n--------------------------------------------------------------------\n")

    dealerOutcome = dealer(dealerHand)

    print("\n--------------------------------------------------------------------\n")

    print(outcome(playerOutcome, dealerOutcome))