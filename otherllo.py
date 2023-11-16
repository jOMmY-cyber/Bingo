import numpy as np




def display_board():
    print('    1   2   3   4   5   6   7   8')
    cnt = 1
    for row in board:
        print(cnt,'|',sep=' ',end= '')
        cnt += 1
        for i in row:
            if i == 0:
                print(' - |',end='')
            elif i == 100:
                print(' X |',end='')
            elif i == 200:
                print(' O |',end='')
        print('')
    
def plot(player):
    global board
    while True:
        try:
            a = input(player+'\'s turn:')
            if len(a) != 2: continue
            
            row = a[0]
            col = a[1]
            row = int(row)-1
            col = int(col)-1
            found = can_eat(row,col,player)
            print('found=',found)
        except:
            print('Try agian.')
            continue
        if board[row,col]==0 and found==1:
            board[row, col] = 100 if player == 'X' else 200
            break
        else: print('cannot plot this position.')
    return row,col

def swap():
    global player
    if player =='X':
        player = 'O'
    else:
        player = 'X'
def can_eat(row,col,player):
    found = 0
    pla = 100 if player == 'X' else 200
    current = pla
    i=1
    temp = []
    while True:
        if col-i <0 : break
        left = board[row,col-i]
        temp.append([row,col-i])
        if current == left and i>=2 :
            found=1
            print(1)
        if current == left:
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if col+i >7: break
        left = board[row,col+i]
        temp.append([row,col+i])
        if current == left and i>=2 :
            found=1
            print(2)
        if current == left:
            if i >=2: found = 1
           
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if row+i >7: break
        left = board[row+i,col]
        temp.append([row+i,col])
        if current == left and i>=2 :
            found=1
            print(3)
        if current == left:
            if i >=2: found = 1
           
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if row-i <0: break
        left = board[row-i,col]
        temp.append([row-i,col])
        if current == left and i>=2 :
            found=1
            print(4)
        if current == left:
            if i >=2: found = 1
           
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if row-i <0 or col-i<0: break
        left = board[row-i,col-i]
        temp.append([row-i,col-i])
        if current == left and i>=2 :
            found=1
            print(5)
        if current == left:
            if i >=2: found = 1
         
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if row-i <0 or col+i>7 : break
        left = board[row-i,col+i]
        temp.append([row-i,col+i])
        if current == left and i>=2 :
            found=1
            print(6)
        if current == left:
            if i >=2: found = 1
           
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if col+i>7 or row+i>7 : break
        left = board[row+i,col+i]
        temp.append([row+i,col+i])
        if current == left and i>=2 :
            found=1
            print(7)
        if current == left:
            if i >=2: found = 1
           
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if col-i<0 or row+i>7 : break
        left = board[row+i,col-i]
        temp.append([row+i,col-i])
        if current == left and i>=2 :
            found=1
            print(8)
        if current == left:
            if i >=2: found = 1
           
            break
        i += 1
        if left ==0: break
    return found

def eat(row,col,player):
    found = 0
    pla = 100 if player == 'X' else 200
    current = board[row,col]
    i=1
    temp = []
    while True:
        if col-i <0 : break
        left = board[row,col-i]
        temp.append([row,col-i])
        if current == left:
            if i >=2: found = 1
            for r, c in temp:
                board[r,c] = pla
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if col+i >7: break
        left = board[row,col+i]
        temp.append([row,col+i])
        if current == left:
            if i >=2: found = 1
            for r, c in temp:
                board[r,c] = pla
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if row+i >7: break
        left = board[row+i,col]
        temp.append([row+i,col])
        if current == left:
            if i >=2: found = 1
            for r, c in temp:
                board[r,c] = pla
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if row+i <0: break
        left = board[row-i,col]
        temp.append([row-i,col])
        if current == left:
            if i >=2: found = 1
            for r, c in temp:
                board[r,c] = pla
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if row-i <0 or col-i<0: break
        left = board[row-i,col-i]
        temp.append([row-i,col-i])
        if current == left:
            if i >=2: found = 1
            for r, c in temp:
                board[r,c] = pla
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if row-i <0 or col+i>7 : break
        left = board[row-i,col+i]
        temp.append([row-i,col+i])
        if current == left:
            if i >=2: found = 1
            for r, c in temp:
                board[r,c] = pla
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:

        if col+i>7 or row+i>7 : break
        left = board[row+i,col+i]
        temp.append([row+i,col+i])
        if current == left:
            if i >=2: found = 1
            for r, c in temp:
                board[r,c] = pla
            break
        i += 1
        if left ==0: break
        
    i=1
    temp = []
    while True:
        if col-i<0 or row+i>7 : break
        left = board[row+i,col-i]
        temp.append([row+i,col-i])
        if current == left:
            if i >=2: found = 1
            for r, c in temp:
                board[r,c] = pla
            break
        i += 1
        if left ==0: break
        

    return found



player = str('O')
board = np.zeros((8,8))
#start
board[3,4] =100
board[4,3] =100
board[4,4] =200
board[3,3] =200
display_board()
run = True
while run:
    row,col = plot(player)
    eat(row,col,player)
    display_board()
    swap()

