import math

def transpose(a):
    at=[]
    for i in range(len(a[0])):
        v=[]
        for j in range(len(a)):
            v.append(a[j][i])
        at.append(v)
    return at
        
print("\a\n\n\t\t\t\t<< NUMERALS >>\n\n\n\t\t\t       MATHEMATICS GAME\n\t\t\t     ====================\n\n\n\n\n\t\t\t\tAbout this game\n\t\t\t   ------------------------\n    Welcome to Numerals! Train your maths skill. It contains three levels:\n     . Beginner\n     . Intermediate\n     . Advanced\n    You will have three chances available for wrong answer after that\n    game will be over.")
start=input("\n\n    PRESS \'Y\' to Start the Game.  ")
while(start=='Y'or start=='y'):
    p=0
    l=3
    #p=point, l=life
    for i in range(1):
        print("\n\n\n________________________________________________________________________________\n\n\n\t\t\t    ----------------------\n\t\t\t   %c\t\t\t  %c\n\t\t\t   %c       \"WELCOME\"      %c\n\t\t\t   %c       %c%c%c%c%c%c%c%c%c      %c\n\t\t\t   %c\t\t\t  %c\n\t\t\t    ----------------------\n\n\n    Press Any Key.... "%(166,166,166,166,166,175,175,175,175,175,175,175,175,175,166,166,166),end="")
        key=input()
        numi=ord(key)
        z=0
        print("\n\n\n\n\n\t\t\t          |LEVEL 1|\n\t\t\t         -----------\n\t\t\t   ______________________\n\t\t\t   |    { BEGINNER }    |\n\t\t\t   %c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n"%(175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175))
        #ONE
        print("\n\n\n\t%c  %d + %d = "%(187,numi-10,numi-63),end="")
        ans=int(input())
        oans= (numi-10)+(numi-63)
        if(oans==ans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #Two
        print("\n\n\t%c  %d is Negative(n) or Positive(p) or Neither(o) = "%(187,numi-65),end="")
        ans=input()
        if(numi-65>0):
            oans='p'
        elif(numi-65<0):
            oans='n'
        elif(numi-65==0):
            oans='o'
        if(oans==ans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #Three
        print("\n\n\t%c  %d is Even(e) or Odd(o) or Neutral(n) = "%(187,numi+77),end="")
        ans=input()
        if((numi+77)%2==0):
            oans='e'
        elif((numi+77)%2!=0):
            oans='o'
        elif(numi+77==0):
            oans='n'
        if(oans==ans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #Four    
        print("\n\n\t%c  Factorial of %d = "%(187,p+3),end="")
        a_ans=int(input())
        f=1
        for j in range(1,p+4):
            f=f*j
        oans=f    
        if(oans==a_ans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #Five
        print("\n\n\t%c  %d%c, where a is %d = "%(187,p,170,l),end="")
        b_ans=int(input())
        oans= p**l
        if(oans==b_ans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #six
        print("\n\n\t%c  Any number %d>   >%d  = "%(187,numi+775,numi+702),end="")
        c_ans=int(input())
        if(c_ans>numi+702 and c_ans<numi+775):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        if(z==0):
            l+=1
            print("\n\n\n\t\t<< Amazing! Level Completed without losing a life. >>\n\n\t\t\t    %c YOU GOT A BONUS LIFE %c\n\t\t\t   --------------------------"%(186,186))
        print("\n\n\n\t\t\t      LEVEL 1 COMPLETED!!\n\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


        #LEVEL2
        z=0
        print("\n\n\n\n\n\t\t\t          |LEVEL 2|\n\t\t\t         -----------\n\t\t\t  __________________________\n\t\t\t  |    { INTERMEDIATE }    |\n\t\t\t  %c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n"%(175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175))
        #one
        val=round(a_ans/4)
        if(val>360):
            val=val-332
        print("\n\n\t%c  Value of Sin%d%c (Upto 3 decimal places) = "%(187,val,186),end="")
        ans=float(input())
        val=math.radians(val)
        oans=math.sin(val)
        ev=abs(oans-ans)
        ev=round(ev,2)
        if(ev==0):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #Two
        print("\n\n\t%c  If Right Angle Triangle has Base %dcm and hypotenuse\n\t   %dcm then Value of Perpendicular is = "%(187,p+37,p+62),end="")
        ans=float(input())
        d_oans=math.sqrt((p+62)**2-(p+37)**2)
        oans=d_oans
        ev=abs(oans-ans)
        ev=round(ev)
        if(ev==0):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #Three
        a=round(oans*12)
        b=round(oans+41)
        print("\n\n\t%c  GCD of %d and %d = "%(187,a,b),end="")
        ans=int(input())
        c=a%b
        while(c!=0):
            a,b=b,c
            c=a%b
        oans=b
        if(ans==oans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #four    
        print("\n\n\t%c  %f KG in G = "%(187,numi*67.5120),end="")
        e_ans=float(input())
        oans=(numi*67.5120)*1000
        if(e_ans==oans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #five
        if(c_ans==0):
            c_ans=24512    #c_ans is ans of number between
        digit=(c_ans*23)
        digit=round(abs(digit))
        print("\n\n\t%c  Sum of digits in %d is = "%(187,digit),end="")
        ans=int(input())
        s=0
        while(digit!=0):
            d=digit%10
            s=s+d
            digit=digit//10
        f_oans=s
        if(ans==f_oans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #six
        print("\n\n\t%c  %d is Prime(p) or Composite(c) Number = "%(187,f_oans+14),end="")
        ans=input()
        prime=0
        val=f_oans+14
        for k in range(1,val):
            if(val%k==0):
                prime=prime+1
        if(prime==1):
            oans='p'
        else:
            oans='c'
        if(ans==oans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #seven
        h=abs(b_ans)  #ans of power
        base=round(d_oans-10)     #Ans of pyth.theorem
        print("\n\n\t%c  A triangle of height %dcm and base %dcm\n\t   has an Area = "%(187,h,base),end="")
        ans=float(input())
        oans=(h*base)/2
        ev=abs(oans-ans)
        ev=round(ev,1)
        if(ev==0):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        if(z==0):
            l+=1
            print("\n\n\n\t\t<< Amazing! Level Completed without losing a life. >>\n\n\t\t\t    %c YOU GOT A BONUS LIFE %c\n\t\t\t   --------------------------"%(186,186))
        print("\n\n\n\t\t\t      LEVEL 2 COMPLETED!!\n\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


        #Level 3
        z=0
        print("\n\n\n\n\n\t\t\t          |LEVEL 3|\n\t\t\t         -----------\n\t\t\t   ______________________\n\t\t\t   |    { ADVANCED }    |\n\t\t\t   %c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n"%(175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175,175))
        #one
        print("\n\n\t%c  %d%cC(Celcius) into %cF(Farenheit) = "%(187,h+33,186,186),end="")
        ans=float(input())
        g_oans=((h+33)*9/5)+32
        ev=abs(g_oans-ans)
        ev=round(ev,2)
        if(ev==0):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #two
        g_oans=round(g_oans)    #g_oans is ans of c into F
        digit=g_oans+p+77
        print("\n\n\t%c  Product of digits in %d = "%(187,digit),end="")
        ans=int(input())
        s=1
        while(digit!=0):
            d=digit%10
            s=s*d
            digit=digit//10
        h_oans=s
        if(ans==h_oans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #three
        radius=round((f_oans+p)/2.3,2)
        height=round(d_oans/4.27,2)
        print("\n\n\t%c  Volume of Cylinder having Radius %.2fm and\n\n\t   Height %.2fm = "%(187,radius,height),end="")
        ans=float(input())
        pii=round(math.pi,3)
        i_oans=round(pii*(radius**2)*height,3)
        ev=abs(i_oans-ans)
        ev=round(ev,1)
        if(ev==0):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #four
        print("\n\n\t%c  Nature of Roots of Equation %dx^2+%dx+%d = 0 is = \n\t   Distinct Roots --> 1\n\t   Equal Roots --> 0\n\t   Complex Roots --> -1"%(187,l+2,l-1,p-14))
        ans=int(input("\t   Answer = "))
        nature=((l-1)**2)-(4*(l+2)*(p-14))
        if(nature>0):
            oans=1
        elif(nature==0):
            oans=0
        elif(nature<0):
            oans=-1
        if(ans==oans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #five
        rs=(numi+122)*10
        per=(l+2)*10
        print("\n\n\t%c  A manager's salary of Rs. %d is increased by %d%%.\n\n\t   His new salary is = "%(187,rs,per),end="")
        ans=int(input())
        oans=rs+(rs*per/100)
        if(ans==oans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #six
        row=abs(l-3)
        col=abs(l-4)
        num=round(radius)+p
        if(row==0):
            row=3
        if(col==0):
            col=1
        print("\n\n\t%c  Add %d in %d%c%d [Row %c Column] Element\n\t   of Matrix "%(187,num,row,215,col,215),end="")
        matrix=[[p+3,p+7,p+16],[p+22,p-10,p*2],[p-15,p+47,l*3]]
        r=len(matrix)
        c=len(matrix[0])
        for ii in range(r):
            print("\n\t\t     |",end="\t  ")
            for j in matrix[ii]:
                print(j,end="\t")
            print("|",end="")
        print("\n\t   Answer = ",end="")
        ans=int(input())
        row-=1
        col-=1
        oans=matrix[row][col]+num
        if(ans==oans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #seven
        a=p-10
        b=p+16
        c=oans
        x1=p-4
        print("\n\n\t%c  Slope of Tangent line to the curve %dx^2+%dx+%d = 0\n\t   at point x=%d is = "%(187,a,b,c,x1),end="")
        ans=int(input())
        x2=x1+0.000001
        y1=(a*(x1**2))+(b*x1)+c
        y2=(a*(x2**2))+(b*x2)+c
        oans=round((y2-y1)/(x2-x1))
        if(ans==oans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break
        #eight
        row=row+2
        col=abs(l-2)
        if(row>4):
            row=3
        if(col==0):
            col=2
        print("\n\n\t%c   Element at %d Row and %d Column of Matrix\n\t    after its Transpose is "%(187,row,col),end="")
        matrix=[[p+5,p+21,p-19],[p*15,p-45,34],[p-24,p+77,l*5],[oans+21,p+98,p+l]]
        r=len(matrix)
        c=len(matrix[0])
        for ii in range(r):
            print("\n\t\t     |",end="\t  ")
            for j in matrix[ii]:
                print(j,end="\t")
            print("|",end="")
        print("\n\t   Answer = ",end="")
        ans=int(input())
        matrix= transpose(matrix)
        row-=1
        col-=1
        oans=matrix[row][col]
        if(ans==oans):
            print("\t\t\t\t\t\t\t\t+1\n\t\t\t\t\t\t\t\t%c%c%c"%(175,175,175))
            p+=1
        else:
            print("\t\t\t\t\t\t\t\t+0    Life = %d\n\t\t\t\t\t\t\t\t%c%c   %c%c%c%c%c%c%c%c%c"%(l-1,175,175,175,175,175,175,175,175,175,175,175))
            l-=1
            z=1
            if(l<=0):
                print("\n\n\n\t\t\t     <<< GAME OVER >>>\n\n\t  Your Lives are Ended! Press \'Y\' if you want to Play Again.")
                break

        
    start=input()    
