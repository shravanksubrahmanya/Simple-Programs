#Tic Tac Toe game

# This code is written for jupyter notebook
#DISPLAYING information

from IPython.display import clear_output # This works only in jupyter notebook

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
    
position1 = ['--','--','--']
position2 = ['--','--','--']
position3 = ['--','--','--']

chg = 0
global lis
lis = [1,2,3,4,5,6,7,8,9]
end ='YES'

def output_print():
    print(row1[0] + ' |' + row1[1] + ' |' + row1[2])
    print(" ".join(position1))
    print(row2[0] + ' |' + row2[1] + ' |' + row2[2])
    print(" ".join(position2))
    print(row3[0] + ' |' + row3[1] + ' |' + row3[2])
    print(" ".join(position3))

def out_check():
    for i in [0,1,2]:
        row1[i] =" "
        row2[i] =" "
        row3[i] =" "

def wrong_input(pos,sym):
        if pos <= 3:
            row1[pos-1] = sym
        elif (pos >3) and (pos <= 6):
            row2[pos - 4] = sym
        else:
            row3[pos - 7] = sym

def condition_tic(sym1,sym2):
    if row1[0] == sym1 and row1[1] == sym1 and row1[2] == sym1:
        return 'x'
    elif row2[0] == sym1 and row2[1] == sym1 and row2[2] == sym1:
        return 'x'
    elif row3[0] == sym1 and row3[1] == sym1 and row3[2] == sym1:
        return 'x'
    elif row1[0] == sym1 and row2[1] == sym1 and row3[2] == sym1:
        return 'x'
    elif row1[2] == sym1 and row2[1] == sym1 and row3[0] == sym1:
        return 'x'
    elif row1[0] == sym1 and row2[0] == sym1 and row3[0] == sym1:
        return 'x'
    elif row1[1] == sym1 and row2[1] == sym1 and row3[1] == sym1:
        return 'x'
    elif row1[2] == sym1 and row2[2] == sym1 and row3[2] == sym1:
        return 'x'
    
    if row1[0] == sym2 and row1[1] == sym2 and row1[2] == sym2:
        return 'y'
    elif row2[0] == sym2 and row2[1] == sym2 and row2[2] == sym2:
        return 'y'
    elif row3[0] == sym2 and row3[1] == sym2 and row3[2] == sym2:
        return 'y'
    elif row1[0] == sym2 and row2[1] == sym2 and row3[2] == sym2:
        return 'y'
    elif row1[2] == sym2 and row2[1] == sym2 and row3[0] == sym2:
        return 'y'
    elif row1[0] == sym2 and row2[0] == sym2 and row3[0] == sym2:
        return 'y'
    elif row1[1] == sym2 and row2[1] == sym2 and row3[1] == sym2:
        return 'y'
    elif row1[2] == sym2 and row2[2] == sym2 and row3[2] == sym2:
        return 'y'

def check(end):
    while (end != 'YES') or (end !='NO'):
        end = input('Do you want to play the game again? type YES or NO: ')
        if end =='YES':
            return 'c'
        elif end =='NO':
            return 'b'
        else:
            print('Please enter a valid answer! ')

while True:
    if end == 'YES':
        print('Please type EXIT if you want to exit from the game in the middle')
        print('NOTE: The valid value for the game is in the range 1 to 9')
        sym1 = input('Please Enter the symbol for Player1! ')
        sym2 = input('Please Enter the symbol for Player2! ')
        out_check()
        lis = [1,2,3,4,5,6,7,8,9]
        end =''
        
    if chg == 0:
        pos = input('Please enter the position for player1')
    else:
        pos = input('Please enter the position for player2')
    if pos == 'EXIT':
        break
    if int(pos) not in lis:
        print('Location is already occupied, Please enter diffrent location')
        continue
    if pos.isdigit() == False:
        print('Please enter a digit Value')
        continue
    elif (int(pos) <1) or (int(pos) >9):
        print('Value out of range, chose a valid value')
        continue
    else:
        lis.remove(int(pos))
        if chg == 0:
            wrong_input(int(pos),sym1)
            chg = 1
        else:
            wrong_input(int(pos),sym2)
            chg = 0
            
    clear_output()  # Remember, this only works in jupyter!        
    output_print()
    val = condition_tic(sym1,sym2)
    if val == 'x':
        print(f'Player 1 is the winner')
        v = check(end)
        if v == 'c':
            end = 'YES'
            continue
        else:
            break
    elif val == 'y':
        print(f'Player 2 is the winner')
        v = check(end)
        if v == 'c':
            end = 'YES'
            continue
        else:
            break
        
    if len(lis)==0:
        v = check(end)
        if v == 'c':
            end = 'YES'
            continue
        else:
            break
    