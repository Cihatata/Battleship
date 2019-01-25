from random import randint

map= []
mapview=[]


#6x6 lik haritalar olusturuluyor
for item in range(6):
    map.append(["*"] * 6)
    mapview.append(["*"] * 6)
#harita goruntuleme
def print_map(map):
    for row in map:
        print (" ".join(row))
        print ("")
#oyun haritasi
def print_mapview(mapview):
    for row in mapview:
        print (" ".join(row))
        print ("")
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

#gemilerin yerlestirilmesi
map[hidden_row][hidden_column]="$"
if hidden_row==5 :
    map[hidden_row-1][hidden_column]="$"
else :
    map[hidden_row+1][hidden_column]="$"

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
        map[hidden_row2][hidden_column2+1]="$"
#hedefe vurus
value=0 #isabet sayisi
def hit(input_row,input_column):
    if map[input_row][input_column]=="$":
        print "YOU HIT (%s,%s)" %(input_row,input_column)
        mapview[input_row][input_column]="O"
        map[input_row][input_column]="O"
        global value
        value=value+1
        print (value)
        print_mapview(mapview)
    else :
        print "YOU DID NOT HIT"
        mapview[input_row][input_column]="X"
        print_mapview(mapview)

while True:
    input_row=int(raw_input("You must enter the destination(X-axis):   "))
    input_column=int(raw_input("You must enter the destination(Y-axis):   "))
    hit(input_row,input_column)
    #print (mapview.count("X"))
    if value==4 : #4 isabet yaptiginda kazaniyor.
        print "YOU WON"
        break
