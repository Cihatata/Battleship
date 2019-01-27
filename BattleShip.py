from random import randint

map= []
mapview=[]

mapWe=[]
mapWeview=[]


#6x6 lik haritalar olusturuluyor
for item in range(6):
    map.append(["*"] * 6)
    mapview.append(["*"] * 6)
    mapWe.append(["*"] * 6)
    mapWeview.append(["*"] * 6)
#harita goruntuleme
def print_map(list):
    for row in list:
        print ("  ".join(row))
        print ("")
#oyun haritasi
#def print_mapview(list):
#    for row in mapview:
#        print ("  ".join(row))
#        print ("")

#rastgele satir

def random_row(map):
    row=randint(0, len(map)-1)
    print (row)
    return row
#rastgele sutun
def random_column(map):
    column=randint(0, len(map)-1)
    print (column)
    return column

#1x2 ve 2x1 lik iki gemimiz var
hidden_row= random_row(map)
hidden_column=random_column(map)

hidden_row2= random_row(map)
hidden_column2= random_column(map)



def place(x,y,x2,y2,list):
    list[x][y]="$"
    if x==5 :
        list[x-1][y]="$"
    else :
        list[x+1][y]="$"

    #gemi2
    if list[x2][y2]=="$":
        if y==5 :
            list[x2][y2-1]="$"
            list[x2][y2-2]="$"

        else :
            if y2==4 :
                list[x2][y2-1]="$"
                list[x2][y2-2]="$"

            else :
                list[x2][y2+1]="$"
                list[x2][y2+2]="$"


    else:
        list[x2][y2]="$"
        if y2==5 :
            list[x2][y2-1]="$"

        else :
            list[x2][y2+1]="$"



#gemilerin yerlestirilmesi
""" map[hidden_row][hidden_column]="$"
if hidden_row==5 :
    map[hidden_row-1][hidden_column]="$"
else :
    map[hidden_row+1][hidden_column]="$"

#gemi2
if map[hidden_row2][hidden_column2]=="$":
    if hidden_column2==5 :
        map[hidden_row2][hidden_column2-1]="$"
        map[hidden_row2][hidden_column2-2]="$"

    else :
        if hidden_column2==4 :
            map[hidden_row2][hidden_column2-1]="$"
            map[hidden_row2][hidden_column2-2]="$"

        else :
            map[hidden_row2][hidden_column2+1]="$"
            map[hidden_row2][hidden_column2+2]="$"


else:
    map[hidden_row2][hidden_column2]="$"
    if hidden_column2==5 :
        map[hidden_row2][hidden_column2-1]="$"

    else :
        map[hidden_row2][hidden_column2+1]="$" """


#hedefe vurus
value=0 #isabet sayisi
def hit(input_rowx,input_columnx):
    #print_map(map)
    #print "-------------"
    if map[input_rowx][input_columnx]=="$" or map[input_rowx][input_columnx]=="O" :
        print "YOU HIT (%s,%s)" %(input_rowx,input_columnx)
        mapview[input_rowx][input_columnx]="O"
        map[input_rowx][input_columnx]="O"
        global value
        value=value+1
        print (value)
        print_map(mapview)
    else :
        print "YOU DID NOT HIT"
        mapview[input_row][input_column]="X"
        print_map(mapview)

def pcHit(input_row,input_column):
    if mapWe[input_row][input_column]=="$" or mapWe[input_row][input_column]=="O" :
        print "YOU HIT (%s,%s)" %(input_row,input_column)
        mapWeview   [input_row][input_column]="O"
        mapWe[input_row][input_column]="O"
        global value2
        value2=value2+1
        print (value2)
        print_map(mapWeview)
    else :
        print "YOU DID NOT HIT"
        mapWeview[input_row][input_column]="X"
        print_map(mapWeview)




print "YOU MUST ENTER VALUE 0 between 5(first Ship)"

targetInputrow=int(raw_input("You must enter your first ship location(X-axis):   "))
targetInputcolumn=int(raw_input("You must enter your first ship location(Y-axis):   "))
print "YOU MUST ENTER VALUE 0 between 5(Second Ship)"

targetInputrow2=int(raw_input("You must enter your second ship location(X-axis):   "))
targetInputcolumn2=int(raw_input("You must enter your second ship location(Y-axis):   "))

place(hidden_row,hidden_column,hidden_row2,hidden_column2,map)

#gemilerin yerlestiriliyor
print "Your Ships"
place(targetInputrow,targetInputcolumn,targetInputrow2,targetInputcolumn2,mapWe)
print_map(mapWe)
print "================"


def random():
    bom=randint(0,len(map)-1)
    return bom


while True:


    #playertarget

    print "YOU MUST ENTER VALUE 0 between 5"
    input_row=int(raw_input("You must enter the destination(X-axis):   "))
    input_column=int(raw_input("You must enter the destination(Y-axis):   "))
    if input_row >= 0 and input_row <= 5 and input_column >= 0 and input_column <= 5 :

        hit(input_row,input_column)
        print "==========="
        print "Enemy Attack"
        pcHit(random(),random())
        #print (mapview.count("X"))
        if value==4 : #4 isabet yaptiginda kazaniyor.
            print "YOU WON"
            break
        elif value2==4:
            print "Enemy Won"
            break
    else :
        print "INVALID CHARACTER"
