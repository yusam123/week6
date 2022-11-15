import logic
def show_board(board):
    for i in range(3):
        print('|',end='')
        for j in range(3):
            if board[i][j]==None:
                print(' ',end= '|')
            else:
                print(board[i][j], end = '|')
        print("")
        print("-------")

def mode1(game,human,bot):
    winner = None
    game.board = game.make_empty_board()
    player = 'O'
    while winner == None:
        print('=====================')
        show_board(game.board)
        print("player "+ player + " turn")
       # player = game.other_player(player)
        position = input("please enter (rows,cols),i.e. (1,1),(3,3): ")
        while game.board[int(position[1])-1][int(position[3])-1]!=None:
            position = input("Please enter (rows,cols), you can not overlap! : ")
                
        game.board = human1.input_position(position,game.board) 
        
        show_board(game.board)   
        winner = game.get_winner(game.board)
        if winner != None:
            break

        game.board = bot.random_input(game.board) 
        winner = game.get_winner(game.board)   
   
        if None in game.board[0] or None in game.board[1] or None in game.board[2] :
            continue
        else:
            game.board = game.make_empty_board()
    print(winner+" is the winner")

def mode2(game,human1,human2):
    winner = None
    game.board = game.make_empty_board()
    while winner == None:
        show_board(game.board)
        print("player "+ human1.role + " turn")
        position = input("please enter (rows,cols),i.e. (1,1),(3,3): ")
        while game.board[int(position[1])-1][int(position[3])-1]!=None:
            position = input("Please enter (rows,cols), you can not overlap! : ")      
        game.board = human1.input_position(position,game.board) 
        show_board(game.board)   
        winner = game.get_winner(game.board)
        if winner != None:
            break
        show_board(game.board)
        print("player "+ human2.role + " turn")
        position = input("please enter (rows,cols),i.e. (1,1),(3,3): ")
        while game.board[int(position[1])-1][int(position[3])-1]!=None:
            position = input("Please enter (rows,cols), you can not overlap! : ")      
        game.board = human2.input_position(position,game.board) 
        show_board(game.board)   
        winner = game.get_winner(game.board)
 
   
        if None in game.board[0] or None in game.board[1] or None in game.board[2] :
            continue
        else:
            game.board = game.make_empty_board()
    show_board(game.board)
    print(winner+" is the winner")

if __name__ == '__main__':
    game = logic.Game()
    human1 = logic.People("O")
    human2 = logic.People("X")
    bot = logic.Computer("X")
    mode = input("Please enter 1 or 2, 1 is for human v.s. bot, 2 is for human v.s. human: ")
    match mode:
        case "1":
            mode1(game,human1,bot)
        case "2":
            mode2(game,human1,human2)

    