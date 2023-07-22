def printTable(table):
    for i in range(0,3):
        for j in range(0,2):
            print(table[i][j],"| ",end="")
        print(table[i][2])
        print("----------")

def formTable(array):
    mat=[]
    for i in range(0,3):
        rowList=[]
        for j in range(0,3):
            rowList.append(array[3*i+j])
        mat.append(rowList)
    return mat

def isFoundWinner(table) -> bool:
    for i in range(0,3):
        if table[i][0]==table[i][1]==table[i][2]:
            return True
    for j in range(0,3):
        if table[0][j]==table[1][j]==table[2][j]:
            return True
    if table[0][0]==table[1][1]==table[2][2]:
        return True
    if table[0][2]==table[1][1]==table[2][0]:
        return True
    return False

while True:

    isPlayerX=True
    turn: int = 0
    
    existsWinner=False
    array=list(range(1,10))
    table = formTable(array)
    printTable(table)

    while not existsWinner and turn<=8:
        try:
            choice=int(input("Your choice(a number between 1 and 9): "))
        except:
            print("choose a number please")
        else:
            if not 0 <= choice <= 9:
                print ('Out of range. Try again')
            else:
                array[choice-1]="X" if isPlayerX else "0"
                turn+=1
                isPlayerX = not isPlayerX
                table = formTable(array)
                printTable(table)
                if(turn>=5):
                    existsWinner=isFoundWinner(table)
                    if existsWinner:
                        winner=2 if isPlayerX else 1
                        print("player", winner,"has won")
    if not existsWinner:
        print("there is no winner")
    answer=input("Do you still want to play?('yes'/any other key for 'no'): ").lower()
    if answer=="yes":
        continue
    else:
        break