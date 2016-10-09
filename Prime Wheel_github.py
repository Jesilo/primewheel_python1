#developed by Jesilo
#email: ernest.edifor@gmail.com
#python version 3.4
#cicle is built anti-clockwise, starting from the traditional 90 degree position.

import tkinter as tk

root = tk.Tk()
canvas=tk.Canvas(root,width=1200, height=1200, borderwidth=0,highlightthickness=0,bg='white')
canvas.grid()

primes=[2,3,5] #initial set of primes
number=480 #max number
centre=550 #centre position
r=0 #radius
r_size=60 #radius incremental number
sixty=0 #sixty counts in a round

#=======prime number functions===========
def is_Factor(x):
    for i in primes:
        if(x%i==0):
            return True
    return False

def is_Prime(x):
    for i in range(7,x+1):
        if (not is_Factor(i) and not i in primes):
            primes.append(i)

    if (x in primes):
        #print(x)
        return True
    else:
        return False

#========end functions==================

    
for i in range(0,number):
    color="#2EFE9A"
    global r; global r_size; global sixty
    
    if i%60==0:#start of each round
        r=r+r_size #increase radius
        sixty=0 #reset round counter
    else:
        sixty=sixty+6 #corresponds to 6 degrees
        
    if not is_Prime(i):
        color='white'

    c=canvas.create_arc(centre-r, centre-r, centre+r, centre+r, fill=color, outline="green",start=sixty, extent=6 )
    canvas.tag_lower(c)

root.wm_title('Prime Wheel')
root.mainloop()
