from Tkinter import *
import math
import cmath
import random
from __builtin__ import round

root = Tk()

root.title("Settlers")
root.tk.call('wm', 'iconbitmap', root._w, '-default', 'catan.ico')

class Hex:
    '''Returns a hexagon generator for hexagons of the specified size.'''
    def __init__(self, num, terrain, name):

        self.roll_num = num
        self.terrain = terrain
        self.name = name

        if terrain == 'field':
            self.color = '#ffcc66' 
        elif terrain == 'forest':
            self.color = '#009933'
        elif terrain == 'pasture':
            self.color = '#ccff66'
        elif terrain == 'mountains':
            self.color = '#808080'
        elif terrain == 'hills':
            self.color = '#cc6600'
        elif terrain == 'desert':
            self.color = '#ffffcc'

    def setCoords(self, coords):
        self.coords = coords
        
        
def generate_hex(edge_length, offset):
    '''Generator for coordinates in a hexagon.'''
    coords = []
    x, y = offset
    coords.append([x,y])
    for angle in range(0, 360, 60):
        x += round(math.cos(math.radians(angle)) * edge_length,1)
        y += round(math.sin(math.radians(angle)) * edge_length,1)
        coords.append([x,y])
        
    coords.append([offset])
    return coords


def drawboard(canvas, tiles, harbors):

    canvas.delete("all")
    length = 50
    orig_x = 250
    orig_y = 200
    xspace = length*1.5+3
    yspace = length*0.866+1
    vspace = yspace*2+1
    x = orig_x
    y = orig_y
    i = 0
    
    
    harbtext = []
    harbcolor = []
    for j in range(0,len(harbors)):
        if harbors[j] == 'three':
            harbtext.append('3:1')
            harbcolor.append('blue')
        elif harbors[j] == 'brick':
            harbcolor.append('red')
            harbtext.append('2:1')
        elif harbors[j] == 'ore':
            harbcolor.append('grey')
            harbtext.append('2:1')            
        elif harbors[j] == 'grain':
            harbcolor.append('orange')
            harbtext.append('2:1')
        elif harbors[j] == 'lumber':
            harbcolor.append('brown')
            harbtext.append('2:1')
        elif harbors[j] == 'wool':
            harbcolor.append('white')
            harbtext.append('2:1') 

    canvas.create_polygon([430,30,690,180,690,480,430,630,170,480,170,180], fill = 'cyan',stipple = 'gray50', width = 0)
    for h in tiles:
        coords = generate_hex(length,(x,y))
        color = 'red'
        canvas.create_polygon(coords,fill = '#ffffe6', outline = '#ffffe6', width = 2)
        canvas.create_polygon(coords, tag=h.name ,fill = h.color,outline='#ffffe6', width = 3, stipple='gray75',activeoutline='red',activewidth=2)
        
        if h.name != 'desert':
            textcolor = 'black'
            if h.roll_num == 6 or h.roll_num == 8:
                textcolor = 'red'
            canvas.create_oval(x+10,y+29,x+40,y+59,fill = 'white', outline = 'white')
            canvas.create_text(x+25,y+44,text = str(h.roll_num),fill = textcolor)
        if h.name == 'desert':
            canvas.create_oval(x+12,y+31,x+38,y+57,fill = 'grey', stipple = 'gray75', outline = 'gray')
        

        harborcoords = [x,y],[x+length,y], [x+length, y-length/4],[x+length-5,y-length/4],[x+length-10, y-5],[x+10, y-5],[x+5,y-length/4],[x+0,y-length/4],[x,y]
        
        if i == 0:
            rotcoords = []
            cangle = cmath.exp(5*3.141/3*1j)
            center = complex(x+length/2,y+yspace)
            for x,y in harborcoords:
                v = cangle * (complex(x, y) - center) + center
                rotcoords.append(v.real)
                rotcoords.append(v.imag)
            canvas.create_polygon(rotcoords, fill = '#ffffe6', width=2)
            canvas.create_text(x-25,y+10, text = harbtext[0], fill = 'black')
            drawresource(harbors[0], x - 50, y, canvas)

        elif i == 3:
            canvas.create_polygon(harborcoords, fill = '#ffffe6', width=2)
            canvas.create_text(x+25,y-10, text = harbtext[1], fill = 'black')
            drawresource(harbors[1], x + 25, y - 30, canvas)

        elif i == 12:
            canvas.create_polygon(harborcoords, fill = '#ffffe6', width=2)
            canvas.create_text(x+25,y-10, text = harbtext[2], fill = 'black')
            drawresource(harbors[2], x + 25, y - 30, canvas)

        elif i == 16:
            rotcoords = []
            cangle = cmath.exp(3.141/3*1j)
            center = complex(x+length/2,y+yspace)
            for x,y in harborcoords:
                v = cangle * (complex(x, y) - center) + center
                rotcoords.append(v.real)
                rotcoords.append(v.imag)
            canvas.create_polygon(rotcoords, fill = '#ffffe6', width=2)
            canvas.create_text(x+75,y+10, text = harbtext[3],fill = 'black')
            drawresource(harbors[3], x + 100, y, canvas)

        elif i == 17:
            rotcoords = []
            cangle = cmath.exp(2*3.141/3*1j)
            center = complex(x+length/2,y+yspace)
            for x,y in harborcoords:
                v = cangle * (complex(x, y) - center) + center
                rotcoords.append(v.real)
                rotcoords.append(v.imag)
            canvas.create_polygon(rotcoords, fill = '#ffffe6', width=2)
            canvas.create_text(x+75,y+75, text = harbtext[4], fill = 'black')
            drawresource(harbors[4], x + 100, y+75, canvas)

        elif i == 15:
            rotcoords = []
            cangle = cmath.exp(2*3.141/3*1j)
            center = complex(x+length/2,y+yspace)
            for x,y in harborcoords:
                v = cangle * (complex(x, y) - center) + center
                rotcoords.append(v.real)
                rotcoords.append(v.imag)
            canvas.create_polygon(rotcoords, fill = '#ffffe6', width=2)
            canvas.create_text(x+75,y+75, text = harbtext[5], fill = 'black')
            drawresource(harbors[5], x + 100, y+75, canvas)

        elif i == 11:
            rotcoords = []
            cangle = cmath.exp(3.141*1j)
            center = complex(x+length/2,y+yspace)
            for x,y in harborcoords:
                v = cangle * (complex(x, y) - center) + center
                rotcoords.append(v.real)
                rotcoords.append(v.imag)
            canvas.create_polygon(rotcoords, fill = '#ffffe6', width=2)
            canvas.create_text(x+25,y+100, text = harbtext[6],fill = 'black')
            drawresource(harbors[6], x + 25, y+125, canvas)

        elif i == 6:
            rotcoords = []
            cangle = cmath.exp(4*3.141/3*1j)
            center = complex(x+length/2,y+yspace)
            for x,y in harborcoords:
                v = cangle * (complex(x, y) - center) + center
                rotcoords.append(v.real)
                rotcoords.append(v.imag)
            canvas.create_polygon(rotcoords, fill = '#ffffe6', width=2)
            canvas.create_text(x-25,y+75, text = harbtext[7], fill = 'black')
            drawresource(harbors[7], x - 50, y+75, canvas)

        elif i == 1:
            rotcoords = []
            cangle = cmath.exp(4*3.141/3*1j)
            center = complex(x+length/2,y+yspace)
            for x,y in harborcoords:
                v = cangle * (complex(x, y) - center) + center
                rotcoords.append(v.real)
                rotcoords.append(v.imag)
            canvas.create_polygon(rotcoords, fill = '#ffffe6', width=2)
            canvas.create_text(x-25,y+75, text = harbtext[8], fill = 'black')
            drawresource(harbors[8], x - 50, y+75, canvas)


                      


        i += 1
        if i < 3 or (i > 3 and i <7) or (i>7 and i< 12) or (i>12 and i<16) or (i>16 and i<20):
            x += 0
            y += vspace
        elif i == 3:
            x = orig_x + xspace
            y = orig_y -yspace
        elif i == 7:
            x = orig_x + 2*xspace
            y = orig_y - 2*yspace
        elif i == 12:
            x = orig_x + 3*xspace
            y = orig_y -yspace
        elif i == 16:
            x = orig_x + 4*xspace
            y = orig_y

def drawresource(type,x,y,canvas): 

    if type == 'three':
        canvas.create_text(x, y, font=("Arial", 20), text= "?", fill='blue')
    elif type == 'brick':
        canvas.create_polygon(x-15,y,x-1,y ,x-1,y+7,x-15,y+7,x-15,y, fill = 'red', width = 0)
        x +=16
        canvas.create_polygon(x-15,y,x-1,y ,x-1,y+7,x-15,y+7,x-15,y, fill = 'red', width = 0)
        x -= 8
        y -= 8
        canvas.create_polygon(x-15,y,x-1,y ,x-1,y+7,x-15,y+7,x-15,y, fill = 'red', width = 0)
    elif type == 'ore':
        canvas.create_polygon(x-14, y+2, x-10, y-4, x-1, y-8, x+6, y-8, x+12, y-3, x+10, y+8, x-6, y+10, x-14, y+2, fill = 'gray', width=0)
    elif type == 'grain':
        x -= 6
        y += 4
        canvas.create_polygon(x-1, y+5,x+1, y+5, x+1, y, x+5, y-5, x+5, y-15, x, y-20,x-5,y-15,x-5, y-5, x-1, y, x-1, y+5,  fill = 'orange', width =0)
        x += 12
        canvas.create_polygon(x-1, y+5,x+1, y+5, x+1, y, x+5, y-5, x+5, y-15, x, y-20,x-5,y-15,x-5, y-5, x-1, y, x-1, y+5,  fill = 'orange', width =0)
    elif type == 'lumber':
        canvas.create_polygon(x-7, y-10, x-5, y-12, x+5, y-12, x+7, y-10, x+7, y-2, x+11, y-5, x+10, y-3, x+7, y+1, x+7, y+10, x+5, y+12, x-5, y+12, x-7, y+10, x-7, y-10, fill = 'brown', width = 0)
    elif type == 'wool':
        canvas.create_oval(x-4, y-10,x+10, y, fill = 'white', width = 0)
        canvas.create_oval(x-15, y-5, x+3, y+10, fill = 'white', width = 0)
        canvas.create_oval(x, y-3, x+15, y+10, fill = 'white', width = 0)
   

def conflicts(board):
    #for 0 neighbors =                      i+1 i+3 i+4
    #for 1 neighbors =                  i-1 i+1 i+3 i+4
    #for 2 neighbors =                  i-1     i+3 i+4
    #for 3 neighbors =              i-3     i+1     i+4 i+5
    #for 4 neighbors =          i-4 i-3 i-1 i+1     i+4 i+5
    #for 5 neighbors =          i-4 i-3 i-1 i+1     i+4 i+5
    #for 6 neighbors =          i-4     i-1         i+4 i+5
    #for 7 neighbors =          i-4         i+1         i+5
    #for 8 neighbors =      i-5 i-4     i-1 i+1     i+4 i+5
    #for 9 neighbors =      i-5 i-4     i-1 i+1     i+4 i+5
    #for 10 neighbors =     i-5 i-4     i-1 i+1     i+4 i+5
    #for 11 neighbors =     i-5         i-1         i+4
    #for 12 neighbors =     i-5 i-4         i+1     i+4
    #for 13 neighbors =     i-5 i-4     i-1 i+1 i+3 i+4
    #for 14 neighbors =     i-5 i-4     i-1 i+1 i+3 i+4
    #for 15 neighbors =     i-5 i-4     i-1     i+3
    #for 16 neighbors =         i-4 i-3     i+1
    #for 17 neighbors =         i-4 i-3 i-1 i+1
    #for 18 neighbors =         i-4 i-3 i-1     

    reds = []
    conflict = 0
    for i in range(len(board)):
        if board[i].roll_num == 6 or board[i].roll_num == 8:
            reds.append(i)
    
    for i in range (len(reds)):
        if reds[i]+1 in reds or reds[i]+3 in reds or reds[i]+4 in reds or reds[i]+5 in reds:
            conflict +=1
    
    return conflict


def makenewboard(canvas, newharbors):
    ''' 
           w  __  3:1
          ,_,/  \,_,
    3:1,__/  \_7/  \__, 3:1
      ,/  \_3/  \12/  \,
       \_0/  \_8/  \16/
       /  \_4/  \13/  \
    o ,\_1/  \_9/  \17/,' b
       /  \_5/  \14/  \
       \_2/  \10/  \18/
       g  ,\_6/  \15/,' l 
              \11/
               ' ' 3:1 
    '''

    global hexlist
    global harbors

    random.seed()
    board = []

    harbors = ['three','wool','three','three','brick','lumber','three','grain','ore']
    nums = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    random.shuffle(nums)
    i = 0
    for j in range(4):
        terrain = 'field'
        name = 'field'+str(j)
        tile = Hex(nums[i],terrain,name)
        board.append(tile)

        terrain = 'pasture'
        name = 'pasture'+str(j)
        tile = Hex(nums[i+1],terrain,name)
        board.append(tile)

        terrain = 'forest'
        name = 'forest'+str(j)
        tile = Hex(nums[i+2],terrain,name)
        board.append(tile)
        i += 3

    for k in range(3):
        terrain = 'mountains'
        name = 'mountains'+str(k)
        tile = Hex(nums[i],terrain,name)
        board.append(tile)

        terrain = 'hills'
        name = 'hills'+str(k)
        tile = Hex(nums[i+1],terrain,name)
        board.append(tile)
        i+=2
     
    terrain = 'desert'
    name = 'desert'
    tile = Hex(7,terrain,name)
    board.append(tile)
    random.shuffle(board)

    while (conflicts(board)):
        random.shuffle(board)

    hexlist = board
    if newharbors == 1:
        random.shuffle(harbors)

    drawboard(canvas,hexlist,harbors)


def shuffleboard(canvas,newharbors):
    canvas.delete("all")
    global hexlist
    while conflicts(hexlist):
        random.shuffle(hexlist)

    if newharbors == 1:
        random.shuffle(harbors)
    drawboard(canvas,hexlist,harbors)


def rolldice(canvas):
    random.seed()

    border = canvas.create_rectangle(600,600, 799, 799, fill = 'white')
    canvas.create_text(700,610, text = 'Dice Roll')
    #reddice = canvas.create_rectangle(dice1x, dice1y, dice1x+50, dice1y+50, fill = "red")
    #yellowdice = canvas.create_rectangle(dice2x, dice2y, dice2x+50, dice2y+50, fill = "yellow")

    dice = 0
    val = [0, 0]
    for i in range(2):
        val[i] = random.randrange(1,6)
        if i == 0:
            x = random.randrange(620, 700)
        else:
            x = random.randrange(680, 760)
        y = random.randrange(620, 760)

        
        coords = [x+2, y], [x+38, y], [x+40, y+2],[x+40, y+38], [x+38, y+40],[x+2, y+40],[x,y+38], [x,y+2], [x,y] 
        if val[i] == 1:
            pips = [x+20,y+20]
        elif val[i] == 2:
            pips = [x+10,y+10],[x+30,y+30]
        elif val[i] == 3:
            pips = [x+10,y+10],[x+20,y+20],[x+30,y+30]
        elif val[i] == 4:
            pips = [x+10,y+10],[x+30,y+10],[x+30,y+30],[x+10,y+30]
        elif val[i] == 5:
            pips = [x+10,y+10],[x+30,y+10],[x+30,y+30],[x+10,y+30],[x+20,y+20]
        elif val[i] == 6:
            pips = [x+10,y+10],[x+10,y+20],[x+10,y+30],[x+30,y+10],[x+30,y+20],[x+30,y+30]

        rotcoords = []
        pipcoords = []
        angle = random.randrange(0,360)
        cangle = cmath.exp(angle/180.0*3.141*1j)
        center = complex(x+20,y+20)
        for x,y in coords:
            v = cangle * (complex(x, y) - center) + center
            rotcoords.append(v.real)
            rotcoords.append(v.imag)

        if val[i] == 1:
                x = pips[0]
                y = pips[1]
                print(x,y)
                v = cangle * (complex(x, y) - center) + center
                pipcoords.append((v.real,v.imag))              
        elif val[i] > 1:
            for x,y in pips:
                v = cangle * (complex(x, y) - center) + center
                pipcoords.append((v.real,v.imag))
        if i == 0:
            color = 'red'
        else:
            color = 'yellow'
        canvas.create_polygon(rotcoords, fill = color)
        for x,y in pipcoords:
            canvas.create_oval(x-2,y-2,x+2,y+2, fill = 'black')
 

    total = val[0]+val[1]

    for hex in hexlist:
        if hex.roll_num == total:
            name = hex.name
            id = canvas.find_withtag(name)
            canvas.itemconfig(id, outline = 'red')
        else:
            name = hex.name
            id = canvas.find_withtag(name)
            canvas.itemconfig(id, outline = '#ffffe6')
        


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text='Do nothing button')
   button.pack()


def play():
    menubar.entryconfig("Setup", state="disabled")

w = Canvas(root, width=800, height=800)
menubar = Menu(root)

newharbors = BooleanVar()
newharbors.set(False)

makenewboard(w,newharbors.get())

setupmenu = Menu(menubar, tearoff=0)
setupmenu.add_checkbutton(label='Randomize Harbors', onvalue = 1, offvalue = 0, variable=newharbors)
setupmenu.add_command(label='Make a New Board',command = lambda: makenewboard(w,newharbors.get()))
#setupmenu.add_command(label='Shuffle Board', command = lambda: shuffleboard(w,newharbors.get()))
setupmenu.add_separator()

setupmenu.add_command(label='Play', command = lambda:play())
setupmenu.add_command(label= 'Roll', command = lambda: rolldice(w))
menubar.add_cascade(label='Setup', menu = setupmenu)


filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label='Load Game', command=donothing)
filemenu.add_command(label='Save Game', command=donothing)
filemenu.add_command(label='Save as...', command=donothing)

filemenu.add_separator()

filemenu.add_command(label='Exit', command=lambda: root.destroy())
menubar.add_cascade(label='File', menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='Help Index', command=donothing)
helpmenu.add_command(label='About...', command=donothing)
menubar.add_cascade(label='Help', menu=helpmenu)


root.config(menu=menubar)
w.pack()



def click(event):
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    abs_coord_x = root.winfo_pointerx() - root.winfo_rootx()
    abs_coord_y = root.winfo_pointery() - root.winfo_rooty()

    print(abs_coord_x, abs_coord_y)
    
    if w.find_withtag(CURRENT):
        ids = w.find_withtag(CURRENT)
        #w.itemconfig(CURRENT, width = 4)
        w.update_idletasks()
        w.after(200)
        #w.itemconfig(CURRENT,width = 1)
        tags = w.itemcget(ids,'tag')
        name = tags.split(' ')[0]
        currhex = filter(lambda x: x.name == name, hexlist)
        if len(currhex) > 0:
            print(currhex[0].name)
            print(currhex[0].roll_num)
            print(newharbors)


w.bind('<Button-1>', click)

mainloop()

