import random
import os
import time
'''
0 la te bao chet
1 la te bao song
'''
class Grid:
    def __init__(self, numRow, numCol):
        self.row = numRow
        self.col = numCol
        self.grid = []
        self.coordList = []
        
    def numRow(self):       
        #hàm trả về số hàng
        return self.row
    
    def numCol(self):       
        #hàm trả về số cột
        return self.col

    def setRandomGrid(self):      
        #hàm khởi tạo khung có các ô có giá trị ngẫu nhiên
        for i in range(0,self.row+2):
            # Để tránh việc không đếm được hàng xóm còn sống của các ô ở cạnh ta mở rộng lưới với chiều dài và chiều rộng
            # là các ô có giá trị 0   
            self.grid.append([])
            for j in range(0,self.col+2):
                self.grid[i].append(0)
        for i in range(1,self.row+1):
            for j in range(1,self.col+1):
                self.grid[i][j] = random.randint(0,1)
               
    def drawRandomGrid(self):
        #Hàm vẽ lưới ngẫu nhiên và các thế hệ tiếp theo
        for i in range(1,self.row+1):
            for j in range(1,self.col+1):
                print(self.grid[i][j], end=" ")
            print()
        self.evolveGrid()
        time.sleep(1) 
        os.system("cls")
        
    def setGrid(self):
        #hàm khởi tạo khung
        for i in range(0, self.row+2):
            self.grid.append([])
            for j in range(0, self.col+2):
                self.grid[i].append(0)
                
        # Đặt các ô là sống theo toạ độ được cho
        for (i,j) in self.coordList :
            self.setCell(i,j)
            
    def drawGrid(self):
        #Hàm vẽ lưới với toạ độ đã cho và các thế hệ tiếp theo
        for i in range(1,self.row+1):
            for j in range(1,self.col+1):
                print(self.grid[i][j], end=" ")
            print()
        time.sleep(1) 
        os.system("cls")
        self.evolveGrid()
        self.drawGrid()
        
    def setCell(self,x,y):      
        # chuyển giá trị ô thành 1
        self.grid[x][y] = 1
        
    def clearCell(self, x, y):  
        # chuyển giá trị ô thành 0
        self.grid[x][y] = 0
        
    def numLiveNeighbors(self,x, y): 
        #đếm số hàng xóm
        count = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if self.isLiveCell(i,j):
                    count +=1
        if self.isLiveCell(x,y):
            # vì ta đếmm cả ô giữa nên nếu là sống thì phải trừ nó đi
            return count - 1     
        else:
            return count
        
    def isLiveCell(self,x, y):
        return self.grid[x][y] == 1
    
    def evolveGrid(self):
        killCell = []
        rebornCell = []
        for i in range(1,self.row+1):
            for j in range(1,self.col+1):
                neighbor = self.numLiveNeighbors(i, j)
                #Kiểm tra theo luật chơi
                if self.isLiveCell(i,j):
                    if neighbor <= 1:                  
                        killCell.append([i,j])
                    elif neighbor >= 4:                  
                        killCell.append([i,j])
                else:
                    if neighbor == 3:
                        rebornCell.append([i,j])
        #Thực hiện luật chơi
        for (i,j) in rebornCell:
            self.setCell(i,j)
        for (i,j) in killCell:
            self.clearCell(i,j)
            
    def inpCoord(self):
        numCoord = int(input("Enter the number of cells you want to have: "))
        print("Enter the coordinate of the live cells :")
        for t in range(1,numCoord+1):
            # Toạ độ một sẽ được nhập trên một dòng
            i, j = [int(i) for i in input().split()]
            self.coordList.append([i,j])


#Main nè---------------------------------------------------------------------------------------
while(True):
    print("         Welcome to The Game of Life")
    print("*******************MENU******************")
    print("* 1. Start game                         *")
    print("* 2. Rules                              *")
    print("* 3. Exit game                          *")
    print("*****************************************")
    pick = input("Please choose an action: ")
    os.system("cls")
    if(pick == '1'):
        print("This product is not a medicine and is not meant to replace medicine")
        print("                       1. Auto Mode")
        print("                      2. Type in Mode")
        p = input("                 Please select a gamemode: ")
        os.system("cls")
        if p == '1':
            try:
                print("Please type in the size of the grid:")
                row = int(input("Number of Row: "))
                column = int(input("Number of Column: "))
                t = float(input("Enter the period of time you want the game to be ran(seconds): "))
                os.system("cls")
                g = Grid(row,column)
                g.setRandomGrid()
                measure1 = time.time()
                measure2 = time.time()
                count = 0
                while(count < t):
                    # Lưới sẽ dừng sinh ra thế hệ tiếp theo sau t giây
                    if measure2 - measure1 >= 1:
                        g.drawRandomGrid()
                        measure1 = measure2
                        measure2 = time.time()
                        count += 1
                    else:
                        measure2 = time.time()
            except ValueError:
                print("Please enter a valid number") 
                os.system("pause")
                os.system("cls")
        elif p == '2':
            try:
                print("Please type in the size of the grid:")
                row = int(input("Number of Row: "))
                column = int(input("Number of Column: "))
                os.system("cls")
                g = Grid(row,column)
                g.inpCoord()
                g.setGrid()
                os.system("cls")
                g.drawGrid()
            except ValueError:
                print("Please enter a valid number") 
                os.system("pause")
                os.system("cls")
        else:
            print("Please enter a valid option")
            os.system("pause")
            os.system("cls")
    elif(pick == '2'):
        print("**************************SOME CONVENTIONS YOU NEED TO KNOW**************************")
        print("* 1. 0 means the cell is dead                                                       *")
        print("* 2. 1 means the cell is live                                                       *")
        print("* 3. The grid must be equal or larger than 3x3 for better experience                *")
        print("* 4. The grid will evolve every 1 second                                            *")
        print("* 5. The order of columns/rows in the grid starts at 1                              *")
        print("* 6. The coordinate of a cell is entered in 1 line                                  *")
        print("*************************************************************************************")
        os.system("pause")
        os.system("cls")
    elif(pick == '3'):
        print("❤ Goodbye! Hope you enjoyed the game❤")
        os.system("pause")
        os.system("cls")
        break
    else:
        print("Please enter a valid option!")
        os.system("pause")
        os.system("cls")
