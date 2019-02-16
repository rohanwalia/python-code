while True :
    player1 = input('Player 1 : Enter r , p , s : ')
    player2 = input('Player 2 : Enter r, p , s : ')
    winner = 'p1'
    if (player1 == 'r') :
        if(player2 == 'p') :
            winner = 'p2'
        if (player2 == 's') :
            winner = 'p1'


    if(winner == 'p1') :
        print("Winner is Player 1")
    else :
        print("Winner is player 2")

    response = input('You want to continue (y/n) ?')
    if(response == 'n') :
        break