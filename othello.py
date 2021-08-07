 # Thomas Patsanis , A.M: 3318

white = 1
black = 2

#create the board and return it
def create_board():
    board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    return board


        
#print the board              
def print_board(board):
    table = board
    y = 0
    print('','','','','0  1  2  3  4  5  6  7 ')
    print('--------------------------')
    for i in table:
        lst = str(i)
        x = lst.replace(',','|').replace('[','').replace(']','')
        print(y,'|',x)
        y += 1
    print('--------------------------')



#inversions left
def left(board,x,y,c):
    lst = []
    k = 0
    if y > 0:
        if c == 1:
            for i in range(8):
                k += 1
                if y-k <= 0:
                    lst = []
                    break
                else:
                    if board[x][y-k] == 2:
                        lst.append([x,y-k])
                    elif board[x][y-k] == 1:
                        break
                    elif board[x][y-k] == 0:
                        lst = []
                        break
            return lst
        if c == 2:
            for i in range(8):
                k += 1
                if y-k <= 0:
                    lst = []
                    break
                else:
                    if board[x][y-k] == 1:
                        lst.append([x,y-k])
                    elif board[x][y-k] == 2:
                        break
                    elif board[x][y-k] == 0:
                        lst = []
                        break
            return lst
    else:
        return lst
    
    


#inversions right
def right(board,x,y,c):
    lst = []
    k = 0
    if y < 7:
        if c == 1:
            for i in range(8):
                k += 1
                if y+k >= 7:
                    lst = []
                    break
                else:
                    if board[x][y+k] == 2:
                        lst.append([x,y+k])
                    elif board[x][y+k] == 0:
                        lst = []
                        break
                    elif board[x][y+k] == 1:
                        break
            return lst
        if c == 2:
           for i in range(8):
                k += 1
                if y+k >= 7:
                    lst = []
                    break
                else:
                    if board[x][y+k] == 1:
                        lst.append([x,y+k])
                    elif board[x][y+k] == 0:
                        lst = []
                        break
                    elif board[x][y+k] == 2:
                        break
        return lst
    else:
        return lst
    



#inversions down
def down(board,x,y,c):
    lst = []
    k = 0
    if x < 7:
        if c == 1:
          for i in range(8):
                k += 1
                if x+k >= 7:
                    lst = []
                    break
                else:
                    if board[x+k][y] == 2:
                        lst.append([x+k,y])
                    elif board[x+k][y] == 1:
                        break
                    elif board[x+k][y] == 0:
                        lst = []
                        break
               
        if c == 2:
           for i in range(8):
                k += 1
                if x+k >= 7:
                    lst = []
                    break
                else:
                    if board[x+k][y] == 1:
                        lst.append([x+k,y])
                    elif board[x+k][y] == 2:
                        break
                    elif board[x+k][y] == 0:
                        lst = []
                        break
    return lst
            


#inversions up
def up(board,x,y,c):
    lst = []
    k = 0
    if x > 0:
        if c == 1:
            for i in range(8):
                k += 1
                if x-k <= 0:
                    lst = []
                    break
                else:
                    if board[x-k][y] == 2:
                        lst.append([x-k,y])
                    elif board[x-k][y] == 1:
                        break
                    elif board[x-k][y] == 0:
                        lst = []
                        break
            return lst
        if c == 2:
             for i in range(8):
                k += 1
                if x-k <= 0:
                    lst = []
                    break
                else:
                    if board[x-k][y] == 1:
                        lst.append([x-k,y])
                    elif board[x-k][y] == 2:
                        break
                    elif board[x-k][y] == 0:
                        lst = []
                        break
        return lst
    else:
        return lst
    

#inversions diagonial up-left                
def diag_up_left(board,x,y,c):
    lst = []
    a = 0
    b = 0
    if x > 0 and y > 0:
        if c == 1:
            for i in range(8):
                a += 1
                b += 1
                if x-b <= 0 or y <= 0:
                    lst = []
                    break
                else:
                    if board[x-b][y-a] == 2:
                        lst.append([x-b,y-a])
                    elif board[x-b][y-a] == 0:
                        lst = []
                        break
                    elif board[x-b][y-a] == 1:
                        break
        if c == 2:
            for i in range(8):
                a += 1
                b += 1
                if x-b <= 0 or y <= 0:
                    lst = []
                    break
                else:
                    if board[x-b][y-a] == 1:
                        lst.append([x-b,y-a])
                    elif board[x-b][y-a] == 0:
                        lst = []
                        break
                    elif board[x-b][y-a] == 2:
                        break
                
    return lst


#inversions diagonial up_right
def diag_up_right(board,x,y,c):
    lst = []
    a = 0
    b = 0
    if x > 0 and y <7:
        if c == 1:
            for i in range(8):
                a += 1
                b += 1
                if x-a <= 0 or y+b >= 7:
                    lst = []
                    break
                else:
                    if board[x-a][y+b] == 2:
                        lst.append([x-a,y+b])
                    elif board[x-a][y+b] == 1:
                        break
                    elif board[x-a][y+b] == 0:
                        lst = []
                        break
        if c == 2:
            for i in range(8):
                a += 1
                b += 1
                if x-a <= 0 or y+b >= 7:
                    lst = []
                    break
                else:
                    if board[x-a][y+b] == 1:
                        lst.append([x-a,y+b])
                    elif board[x-a][y+b] == 2:
                       break
                    elif board[x-a][y+b] == 0:
                        lst = []
                        break
    return lst


#inversions diagonial down_right
def diag_down_right(board,x,y,c):
    lst = []
    a = 0
    b = 0
    if x < 7 and y < 7:
        if c == 2:
          for i in range(8):
              a += 1
              b += 1
              if x+a >= 7 or y+b >= 7:
                  lst = []
                  break
              else:
                  if board[x+a][y+b] == 1:
                      lst.append([x+a,y+b])
                  elif board[x+a][y+b] == 2:
                      break
                  elif board[x+a][y+b] == 0:
                      lst = []
                      break
        if c == 1:
            for i in range(8):
              a += 1
              b += 1
              if x+a >= 7 or y+b >= 7:
                  lst = []
                  break
              else:
                  if board[x+a][y+b] == 2:
                      lst.append([x+a,y+b])
                  elif board[x+a][y+b] == 1:
                      break
                  elif board[x+a][y+b] == 0:
                      lst = []
                      break
    return lst


#inversions diagonial down_left
def diag_down_left(board,x,y,c):
    lst = []
    a = 0
    b = 0
    if x < 7 and y > 0:
        if c == 1:
            for i in range(8):
                a += 1
                b += 1
                if x+a >= 7 or y-b <= 0:
                    lst = []
                    break
                else:
                    if board[x+a][y-b] == 2:
                        lst.append([x+a,y-b])
                    elif board[x+a][y-b] == 1:
                        break
                    elif board[x+a][y-b] == 0:
                        lst = []
                        break
        if c == 2:
             for i in range(8):
                a += 1
                b += 1
                if x+a >= 7 or y-b <= 0:
                    lst = []
                    break
                else:
                    if board[x+a][y-b] == 1:
                        lst.append([x+a,y-b])
                    elif board[x+a][y-b] == 2:
                        break
                    elif board[x+a][y-b] == 0:
                        lst = []
                        break
    return lst
            
        

#number of inversions
def reverse_count(board,x,y,c):
    xamos = left(board,x,y,c)+right(board,x,y,c)+down(board,x,y,c)+up(board,x,y,c)+diag_up_left(board,x,y,c)+diag_up_right(board,x,y,c)+diag_down_right(board,x,y,c)+diag_down_left(board,x,y,c)
    if len(xamos) == 0 or board[x][y] != 0:
        return 0
    else:
        return len(xamos)



#calculate the best moves for pc
def compute_counts(board,c):
    moves = []
    for i in range(len(board)):
        l = []
        for j in range(len(board[i])):
           z = reverse_count(board,i,j,c)
           l.append(z)
        moves.append(l)
    return moves



#make the inversions and put the checker
def add_checker(board,x,y,c):
    lpo = []
    e1 = left(board,x,y,c)
    e2 = right(board,x,y,c)
    e3 = down(board,x,y,c)
    e4 = up(board,x,y,c)
    e5 = diag_up_left(board,x,y,c)
    e6 = diag_up_right(board,x,y,c)
    e7 = diag_down_right(board,x,y,c)
    e8 = diag_down_left(board,x,y,c)
    board[x][y] = c
    lpo = e1+e2+e3+e4+e5+e5+e6+e7+e8
    lpofinal = [g for g in lpo if g != []] 
    for i in range(len(lpofinal)):
        s = lpofinal[i][0]
        d = lpofinal[i][1]
        board[s][d] = c

#the game
def human_play(board,c):
    f = False
    q = compute_counts(board,c)
    for i in range(8):
        for j in range(8):
            if q[i][j] != 0:
                f = True
                break
    if f == True:
        while True:
            try:
                x = int(input('Give the row: '))
                y = int(input('Give the column: '))
                raise AssertionError
            except Exception:
                print('You did not give a number')
            if 0 <= x <= 7 and 0 <= y <= 7:    
                if reverse_count(board,x,y,c) != 0:
                    add_checker(board,x,y,c)
                    break
    return f


#computers game
def computer_play(board):
    r = compute_counts(board,1)
    max_inversions = 0
    h = 0
    g = 0
    kapsimo = False
    for i in range(8):
        for j in range(8):
            if r[i][j] > max_inversions:
                max_inversions = r[i][j]
                h = i
                g = j
    if max_inversions == 0:
        return kapsimo
    else:
        kapsimo = True
        add_checker(board,h,g,white)
        return kapsimo


#score
def print_score(board):
    score1 = 0
    score2 = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 2:
                score1 += 1
            elif board[i][j] == 1:
                score2 += 1
    print("PLAYER'S 1 SCORE: ",score1)
    print("PLAYER'S 2 SCORE: ",score2)
    return score1,score2

#starting the game
def start_game1():
    board = create_board()
    print_board(board)
    player_move = True
    pc_move = True
    root.destroy()
    while player_move == True or pc_move == True:
        player_move = human_play(board,black)
        print_board(board)
        print_score(board)
        pc_move = computer_play(board)
        print_board(board)
        Score1, Score2 = print_score(board)
    if Score1 > Score2:
        print('YOU WIN')
    elif Score1 == Score2:
        print('DRAW')
    else:
        print('COMPUTER WINS')



def start_game2():
    board = create_board()
    print_board(board)
    player1_move = True
    player2_move = True
    root.destroy()
    while player1_move == True or player2_move == True:
        player1_move = human_play(board,black)
        print_board(board)
        print_score(board)
        player2_move = human_play(board,white)
        print_board(board)
        Score1, Score2 = print_score(board)
    if Score1 > Score2:
        print('PLAYER 1 WINS')
    elif Score1 == Score2:
        print('DRAW')
    else:
        print('PLAYER 2 WINS')
    
    



#main programme
from tkinter import Tk,Button
root = Tk()
button = Button(root, text='1 player', height=5, width=16, command=start_game1)
players = Button(root, text='2 players', height=5, width=16, command=start_game2)
button.pack()
players.pack()
root.mainloop()
