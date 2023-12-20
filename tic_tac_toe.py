board=['1','2','3','4','5','6','7','8','9']
game_on=True
## User Board 
def user_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("------")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("------")
    print(f"{board[6]}|{board[7]}|{board[8]}")
## User Marker
def user_marker():
    marker="xx"
    while marker not in ["X","O"]:
        marker=input("Player_1 please select your marker. X or O? ").upper()
        if marker not in ["X","O"]:
            print("Incorrect selection! Please select from X or O")
    if marker=="X":
        print("Player_1 is X and olayer_2 is O")
        return ["X","O"]
    else:
        print("Player_1 is O and player_2 is X")
        return ["O","X"]
## User input
def user_input():
    s="xxxx"
    while s not in ["1","2","3","4","5","6","7","8","9"]:
        s=input(f"{turn} Please select the position between 1-9.")
        if s not in ["1","2","3","4","5","6","7","8","9"]:
            print("Oops! Wrong input. Please enter between 1-9")
    return int(s)
## User position on board
def user_position(board,s,marker):
    board[s-1]=marker
## Win condition
def win():
    win=False
    ##Vertical
    if board[0]==board[3]==board[6] or board[1]==board[4]==board[7] or board[2]==board[5]==board[8]:
        win=True
    ##horizontal
    elif board[0]==board[1]==board[2] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8]:
        win=True
    ##diagonal
    elif board[0]==board[4]==board[8] or board[2]==board[4]==board[6]:
        win=True
    return win
## Draw condition
def draw():
    return win()==False and "1" not in board and "2" not in board and "3" not in board and "4" not in board and "5" not in board and "6" not in board and "7" not in board and "8" not in board and "9" not in board
## Check for empty space
def empty_space(board,s):
    return board[s-1]=="1" or board[s-1]=="2" or board[s-1]=="3" or board[s-1]=="4" or board[s-1]=="5" or board[s-1]=="6" or board[s-1]=="7" or board[s-1]=="8" or board[s-1]=="9"
print("Welcome To Tic Tac Toe!")
while True:
    board=board=['1','2','3','4','5','6','7','8','9']
    play_game=input("Are you ready to start the game? Enter Y for yes and N for no.").upper()
    if play_game=="Y":
        game_on=True
        print('\n'*100)
    else:
        print("Good Bye!")
        break
    user_board(board)
    player_1,player_2=user_marker()
    turn=player_1 or player_2
    while game_on:
        while turn==player_1:
            s=user_input()
            if empty_space(board,s)!=True:
                print("Position already taken! Please select a different position")
                s=user_input()
            else:
                user_position(board,s,player_1)
                print('\n'*100)
                user_board(board)
                print("Player_2's Turn now.")
                turn=player_2
        if win()==True:
            print("Congratualations! Player_1 Won!")
            break 
        elif draw()==True:
            print("Its a draw!")
            break
        while turn==player_2:
            s=user_input()
            if empty_space(board,s)!=True:
                print("Position already taken! Please select a different position")
                s=user_input()
            else:
                user_position(board,s,player_2)
                print('\n'*100)
                user_board(board)
                print("Player_1's Turn now.")
                turn=player_1
        if win()==True:
            print("Congratualations! Player_1 Won!")
            break
        elif draw()==True:
            print("Its a draw!")
            break
    if not input("Do you want to play again? Y or N?").upper().startswith("Y"):
        print("Good Bye!")
        break
    else:
        game_on==True


    
