"""
Tile.py : this module calculates all the possible outcome from a 
wall with given height and length covered with bricks given width and length.
The user can choose one of the outcome and visualise it.
 __author__ = "张序年"
__pkuid__  = "1800094603"
__email__  = "1800094603@pku.edu.cn"
"""


import turtle

def test(brickheight,bricklength,row,column,walllength,wallheight,occupied,answer):
    """
    This fuction test either the position which 
    going to be used by the brick of the wall 
    is occupied or not.
    Moreover, it test whether the brick will exceed the wall or not.
    """
    if brickheight>wallheight or bricklength>walllength:
        return False
    elif over(brickheight,bricklength,row,column,walllength,wallheight):
        return False
    else:
        for x in range(column,column+bricklength):
            for y in range(row,row+brickheight):
                if (x,y) in occupied:
                    return False 
                    break
        else:
            return True
        
def put(brickheight,bricklength,row,column,walllength,wallheight,occupied,answer):
    """
    This fuction changes the status of the targeted position on the wall to occupied 
    by adding the coordinate of the wall to a list.
    """
    temp =[]
    for x in range(column,column+bricklength):
        for y in range(row,row+brickheight):
            occupied.append((x,y))
            temp.append(((y)*walllength+x))
    else:
        tempp = tuple(temp)
        answer.append(tempp)
        return occupied
    
def over(brickheight,bricklength,row,column,walllength,wallheight):
    """
    This function is used to prevent the coordinate outside of the wall being added 
    into the occupied list
    """
    if column + bricklength > walllength or row + brickheight > wallheight:
        return True
    else:
        return False
            
def end(brickheight,bricklength,walllength,wallheight,occupied,answer):
    """
    This function test whether the wall is fully covered by bricks or not
    by comparing the occupied list and the fully occupied list
    """
    occ = []
    for x in range(walllength):
        for y in range(wallheight):
            occ.append((x,y))
    occ.sort()
    occupied.sort()
    if occ == occupied:
        return True
    else:
        return False
    
def run(brickheight,bricklength,walllength,wallheight,occupied=[],answer=[],globall=[]):
    """
    This is the function which seperate square bricks and rectangular bricks
    If it is square,return the only answer it may have,
    If it is rectangle, try all the conditions it may have.
    If the bricks can be put both vertically and horizontally, do both
    if it only can be placed one of the methods, do that
    At last, it put all the possible answer in globall list and return it
    """
    if bricklength == brickheight:
        for t in range(walllength-bricklength+1):
            for s in range(wallheight-brickheight +1):
                column = t
                row = s
                if test(brickheight,bricklength,row,column,walllength,wallheight,occupied,answer):
                    put(brickheight,bricklength,row,column,walllength,wallheight,occupied,answer)
        if end(brickheight,bricklength,walllength,wallheight,occupied,answer):
            return answer
        else:
            return False
    if bricklength != brickheight:
        for t in range(walllength):
            for s in range(wallheight):
                column = t
                row = s

                if test(brickheight,bricklength,row,column,walllength,wallheight,occupied,answer) and \
                test(bricklength,brickheight,row,column,walllength,wallheight,occupied,answer):
                    occupied2 = occupied[:]
                    answer2 = answer[:]

                    put(bricklength,brickheight,row,column,walllength,wallheight,occupied,answer)
                    if not end(brickheight,bricklength,walllength,wallheight,occupied,answer):
                        run(brickheight,bricklength,walllength,wallheight,occupied,answer,globall)
                    else:
                        globall.append(answer)

                    put(brickheight,bricklength,row,column,walllength,wallheight,occupied2,answer2)
                    if not end(brickheight,bricklength,walllength,wallheight,occupied2,answer2):
                        run(brickheight,bricklength,walllength,wallheight,occupied2,answer2,globall)
                    else:
                        globall.append(answer)
                        
                elif test(brickheight,bricklength,row,column,walllength,wallheight,occupied,answer):
                    put(brickheight,bricklength,row,column,walllength,wallheight,occupied,answer)
                    if not end(brickheight,bricklength,walllength,wallheight,occupied,answer):
                        run(brickheight,bricklength,walllength,wallheight,occupied,answer,globall)
                    else:
                        globall.append(answer)
                        
                elif test(bricklength,brickheight,row,column,walllength,wallheight,occupied,answer):
                    put(bricklength,brickheight,row,column,walllength,wallheight,occupied,answer)
                    if not end(brickheight,bricklength,walllength,wallheight,occupied,answer):
                        run(brickheight,bricklength,walllength,wallheight,occupied,answer,globall)
                    else:
                        globall.append(answer)
        return globall
    
def numtocoor(lis,walllength,wallheight,x=10):
    """
    This function is used to change the numbers in the globall list into 
    coordinates respectively, the coordinates represents the two vertex 
    of the bricks
    """
    coorlist = []
    for tup in lis:
        tuplist = list(tup)
        tuplist.sort()
        
        big = max(tup)
        small = min(tup)
        coormax = ((big%walllength+1-walllength/2)*x,-(big//walllength+1+wallheight/2)*x)
        coormin = ((small%walllength-walllength/2)*x,-(small//walllength+wallheight/2)*x)
        coor = [coormax,coormin]
        coorlist.append(coor)
    return coorlist

def draw(coorlist):
    """
    By using the coordinate of vertex,
    draw how the bricks will be arranged on the wall
    """
    tur = turtle.Turtle()
    for coor in coorlist:
        tur.penup()
        tur.goto(coor[0][0],coor[0][1])
        tur.pendown()
        tur.goto(coor[0][0],coor[1][1])
        tur.goto(coor[1][0],coor[1][1])
        tur.goto(coor[1][0],coor[0][1])
        tur.goto(coor[0][0],coor[0][1])
            
def main():
    bricklength = int(input("请输入砖块长度"))
    brickheight = int(input("请输入砖块宽度"))
    walllength = int(input("请输入墙面长度"))
    wallheight = int(input("请输入墙面宽度"))
    hey = run(brickheight,bricklength,walllength,wallheight)
    for item in range(len(hey)):
        print(item+1,":\t",hey[item])
    inp = int(input("请输入选择的方案序号"))
    lis = hey[inp-1]
    draw(numtocoor(lis,walllength,wallheight))
    
if __name__ == '__main__':
    main()