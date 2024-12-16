#Heirs' input

#-------------------------------------Validation using Flag for Input Variables-------------------------------------

from time import sleep                      #For Delay 
from art import tprint                      #For Starting font
import matplotlib.pyplot as plt             #For Pie Chart
from rich.tree import Tree                  #For Tree Structure
from rich import print                      #console.print > for Table 
from rich.console  import Console           #Needed this library for Table
from rich.table import Table                #For Table Structure
from rich.progress import track             #For Scrapping Data Representation
from fractions import Fraction              #For Fractions in case of Non-reccuring

console = Console()

tree = Tree("Tree view")

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Relation", style="dim", width=23)
table.add_column("Prescribed share")
table.add_column("Percentage", justify="right")
table.add_column("Inherited amount", justify="right")

tprint("     Welcome   ",font="tarty1")
sleep(1)
tprint("\n      To",font="tarty1")
sleep(1)
tprint("\n      Inheritance",font="tarty1")
sleep(1)
tprint("\n      Calculator",font="tarty1")
sleep(1)
tprint("\n      by           Arub!",font="tarty1")
sleep(1)

    #Husband + Wife
inp=False
while not inp:
    try:        
            
            #Husband
            print("\n       Enter surviving [green]Husband[/green] (0 or 1) ?        ")
            h=int(input("                                            "))
     
            if h<0 or h>1:
                print("       [red]Husband can only be 1 or 0[/red]")
            else:
                while not inp:

                    #Wife
                    print("\n       Enter surviving [green]Wives[/green] (0 to 4) ?        ")
                    w=int(input("                                            "))
                    if w<0 or w>4:
                         print("       [red]Wives can only be from 0 to 4[red]")
                    else:

                        #Husband + Wife
                        if h>0 and w>0:
                            inp = False
                            print("\n       [red]Husband & Wife both cannot be alive[/red]")
                        else:
                            inp = True
   
    except ValueError:
        print("\n       [red]Please give valid input[/red]")
        
#Father
inp=False
while not inp :
    try:
        print("\n       Enter surviving [green]Father[/green] (0 or 1) ?        ")
        f = int(input("                                            "))
        if f == 0 or f == 1 :
            inp=True   
        else :
            print("\n       [red]Father can not be more than 1 or less than 0")
            #print("\n       Kindly Re-enter")
            inp=False
    except ValueError :
        print("\n       [red]Please give valid input")

#Mother
inp=False
while not inp :
    try:
        print("\n       Enter surviving [green]Mother[/green] (0 or 1) ?        ")
        m = int(input("                                            "))
        if m == 0 or m == 1 :
            inp=True   
        else :
            print("\n       [red]Mother can not be more than 1 or less than 0")
            inp=False
    except ValueError :
        print("\n       [red]Please give valid input")
        
#Daughter
inp=False
while not inp :
    try:
        print("\n       Enter surviving [green]Daughter(s)[/green] ?        ")
        d = int(input("                                            "))
        if d >= 0 :
            inp=True   
        else :
            print("\n       [red]Daughter can not be less than 0")
            inp=False
    except ValueError :
        print("\n       [red]Please give valid input")

#Son
inp=False
while not inp :
    try:
        print("\n       Enter surviving [green]Son(s)[/green] ?        ")
        s = int(input("                                            "))
        if s >= 0 :
            inp=True   
        else :
            print("\n       [red]Son can not be less than 0")
            inp=False
    except ValueError :
        print("\n       [red]Please give valid input")


#Brother
inp=False
while not inp :
    try:
        print("\n       Enter surviving [green]Brother(s)[/green] ?        ")
        b = int(input("                                            "))
        if b >= 0 :
            inp=True   
        else :
            print("\n       [red]Brother can not be less than 0")
            inp=False
    except ValueError :
        print("\n       [red]Please give valid input")


#Sister
inp=False
while not inp :
    try:
        print("\n       Enter surviving [green]Sister(s)[/green] ?        ")
        si = int(input("                                            "))
        if si >= 0 :
            inp=True   
        else :
            print("\n       [red]Mother can not be more than 1 or less than 0")
            inp=False
    except ValueError :
        print("\n       [red]Please give valid input")


#Paternal Grand Father
inp=False
while not inp :
    try:
        print("\n       Enter surviving [green]Paternal Grand Father[/green] (0 or 1) ?        ")
        pgf = int(input("                                            "))

        if pgf == 0 or pgf == 1 :
            inp=True   
        else :
            print("\n       [red]Paternal Grand Father can not be more than 1 or less than 0")
            #print("\n       Re-enter")
            inp=False
    except ValueError :
        print("\n       [red]Please give valid input")


#Paternal Grand Mother
inp=False
while not inp :
    try:
        print("\n       Enter surviving [green]Paternal Grand Mother[/green] (0 or 1) ?        ")
        pgm = int(input("                                            "))
        if pgm == 0 or pgm == 1 :
            inp=True   
        else :
            print("\n       [red]Paternal Grand Mother can not be more than 1 or less than 0")
            #print("\n       Re-enter")
            inp=False
    except ValueError :
        print("\n       [red]Please give valid input")


#Maternal Grand Mother
inp=False
while not inp :
    try:
        print("\n       Enter surviving [green]Maternal Grand Mother[/green] (0 or 1) ?        ")
        mgm = int(input("                                            "))
        if mgm == 0 or mgm == 1 :
            inp=True   
        else :
            print("\n      [red]Maternal Grand Mother can not be more than 1 or less than 0")
            #print("\n       Re-enter")
            inp=False
    except ValueError :
        print("\n       [red]Please give valid input")

#Grand Son
inp=False
while not inp :
    try:
        print("\n       Enter surviving [green]Grand Son(s)[/green] ?        ")
        gs = int(input("                                            "))
        if gs >= 0 :
            inp=True   
        else :
            print("\n       [red]Grand Son can not be less than 0")
            inp=False
    except ValueError :
        print("\n       [red]Please give valid input")


#Grand Daughter
inp=False
while not inp :
    try:
        print("\n       Enter surviving [green]Grand Daughter(s)[/green] ?        ")
        gd = int(input("                                            "))
        if gd >= 0 :
            inp=True   
        else :
            print("\n       [red]Grand Daughter can not be less than 0")
            inp=False
    except ValueError :
        print("\n       [red]Please give valid input")        



#Inheritance applicable amount calculation
first_amount = -1
while first_amount <= 0 :

    print("\n       (i) [bold][red]Zakat[/red][/bold], (ii) [bold][red]Wife's Mehr[/red][/bold] and (iii) [bold][red]Loan[/red][/bold] have to be paid first from the leftover Wealth. \n       So kindly enter respective amounts : ")
            
    inp=False
    while not inp : #Wealth
        try:
            print("\n       Enter [green]wealth of deceased[/green] :   ")
            wealth = int(input("                                            "))
            if wealth <0:
                print("       [red]Give [bold]positive[/bold] number")
                inp=False
            else :
                inp=True
        except ValueError :
            print("\n     [red]  Please give valid input")


    inp=False
    while not inp : #Zakat
        try:
            print("\n       Enter any [green]outstanding zakat :   ")
            zakat = int(input("                                           "))
            if zakat <0:
                print("       [red]Give [bold]positive[/bold] amount")
                #print("\n       Re-enter")
                inp=False
            else :
                inp=True
        except ValueError :
            print("\n       [red]Please give valid input")
                

    inp=False
    while not inp : #Mehr
        try:
            print("\n       Enter [green]Mehr[/green] (if not paid yet to wife) :   ")      
            mehr = int(input("                                           "))
            if mehr <0:
                print("       [red]Give [bold]positive[/bold] amount")
                #print("\n       Re-enter")
                inp=False
            else :
                inp=True
        except ValueError :
            print("\n       [red]Please give valid input")


    inp=False
    while not inp : #Loan
        try:
            print("\n       Enter any [green]outstanding loan :   ")
            loan = int(input("                                           "))
            if loan <0:
                print("       [red]Give [bold]positive[/bold] amount")
                #print("\n       Re-enter")
                inp=False
            else :
                inp=True
        except ValueError :
            print("\n       [red]Please give valid input")

    print("\n      :point_right: [bold][u][yellow]Maximum 1/3rd of WILL (wasiyat) by deceased, can be executed in favor of Non-Heirs [red]only.")

    inp=False
    while not inp : #Will
        try:
            print("\n       Enter amount of [green]WILL[/green] if any : ")
            will = int(input("                                           "))
            if will <0:
                print("\n       [red]Give [bold]positive[/bold] amount")
                #print("\n       Re-enter")
                inp=False
            else :
                inp=True
        except ValueError :
            print("\n       [red]Please give valid input")


    first_amount = wealth - zakat - mehr - loan
    if first_amount <=0:
        print("       :red_circle:   ",first_amount," [red]is not applicable for Inheritance distribution[/red]. Kindly re-enter the amounts.")
        sleep(2)


#Adjusting the WILL to 1/3rd at most
if will<= first_amount/3:
    amount = first_amount - will
    print("\n      [blue][bold] :large_blue_circle: Applicable amount for inheritance is : :point_right: ", amount,"\n\n")

else :
    will= first_amount/3
    amount = first_amount - will
    print("\n       [blue][bold]:large_blue_circle: Applicable amount for inheritance is : :point_right: ", amount,"\n\n")

#-----------------------------------------Validation completed-----------------------------------------
        
#initial heirs' shares
hs = 0
ws = 0
fs = 0
ms = 0
ds = 0  
ss = 0
pgfs = 0 
pgms = 0
mgms = 0
bs = 0
sis = 0
gss = 0
gds = 0

#-----------------------------------------Scenario 1: Son alive---------------------------------------------------------
if s >= 1 :

    #Husband
    if h == 1 :        
        hs = (1/4)*amount
        sleep(1)
        hsp=hs/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance share for Husband'):
            sleep(.1)
            step
        print("\n       :small_red_triangle: Husband gets 1/4th prescribed share: " , round(hs,3),"\n\n")
        tree.add("Husband 1/4 " + str(round(hs,3))).add("[green] 1/4").add("[blue] "+str(round(hs,3)))
        table.add_row("Husband", "1/4", str(round(hsp,3)) + '%', str(round(hs,3)))
        sleep(1)

    #wife
    elif h == 0 and w == 1:        
        ws = (1/8)*amount
        sleep(1)
        wsp=ws/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance for Wife            '):
            sleep(.1)
            step
        print("\n       :small_red_triangle: Wife gets 1/8th prescribed share: " , round(ws,3),"\n\n")
        tree.add("Wife 1/8 " + str(round(ws,3))).add("[green] 1/8").add("[blue] "+str(round(ws,3)))
        table.add_row("Wife", "1/8", str(round(wsp,3)) + '%', str(round(ws,3)))
        sleep(1)

    #Multiple Wives
    elif h == 0 and w > 1 :
        ws = (1/8)*amount
        wsp=ws/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance for Wives           '):
            sleep(.1)
            step
        print("\n       :small_red_triangle: All wives combined get 1/8th prescribed share:" , round(ws,3))
        tree.add("Wives 1/8 " + str(round(ws,3))).add("[green] 1/8").add("[blue] "+str(round(ws,3)))
        table.add_row("Wives", "1/8", str(round(wsp,3)) + '%', str(round(ws,3)))
        ews=ws/w
        ewsp=ews/amount*100

        if w==3 :
            table.add_row("  Each wife", "1/24", str(round(ewsp,3)) + '%', str(round(ews,3)))
        else :
            ewsf=1/8/w
            table.add_row("  Each wife", str(Fraction(ewsf)), str(round(ewsp,3)) + '%', str(round(ews,3)))

        sleep(1)
        print("\n       Each wife gets: ", ews,"\n\n")
        sleep(1)

    #Father
    if f == 1 :        
        fs = (1/6)*amount
        sleep(1)
        fsp=fs/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance share for Father    '):
            sleep(.1)
            step
        print("\n       :small_red_triangle: Father gets 1/6th prescribed share: " , round(fs,3),"\n\n")
        tree.add("Father 1/6 " + str(round(fs,3))).add("[green] 1/6").add("[blue] "+str(round(fs,3)))
        table.add_row("Father", "1/6", str(round(fsp,3)) + '%', str(round(fs,3)))
        sleep(1)

    #Paternal Grand Father
    elif pgf == 1 and f == 0:     
        pgfs = (1/6)*amount
        sleep(1)
        pgfsp=pgfs/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance share for Paternal Grand Father'):
            sleep(.1)
            step
        print("\n       :small_red_triangle: Paternal Grand Father gets 1/6th prescribed share: " , round(pgfs,3),"\n\n")
        tree.add("Paternal Grand Father 1/6 " + str(round(pgfs,3))).add("[green] 1/6").add("[blue] "+str(round(pgfs,3)))
        table.add_row("Paternal Grand Father", "1/6", str(round(pgfsp,3)) + '%', str(round(pgfs,3)))
        sleep(1)


    #Mother
    if m == 1 :        
        ms = (1/6)*amount
        sleep(1)
        msp=ms/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance share for Mother    '):
            sleep(.1)
            step
        print("\n       :small_red_triangle: Mother gets 1/6th prescribed share: " , round(ms,3),"\n\n")
        tree.add("Mother 1/6 " + str(round(ms,3))).add("[green] 1/6").add("[blue] "+str(round(ms,3)))
        table.add_row("Mother", "1/6", str(round(msp,3)) + '%', str(round(ms,3)))
        sleep(1)


    #Paternal Grand Mother
    elif pgm == 1 and f == 0 and m == 0 and mgm == 0 :
        pgms=(1/6)*amount
        sleep(1)
        pgmsp=pgms/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance share for Paternal Grand Mother'):
            sleep(.1)
            step
        print("\n       :small_red_triangle: Paternal Grand Mother gets 1/6th prescribed share: " , round(pgms,3),"\n\n")
        tree.add("Paternal Grand Mother 1/6 " + str(round(pgms,3))).add("[green] 1/6").add("[blue] "+str(round(pgms,3)))
        table.add_row("Paternal Grand Mother", "1/6", str(round(pgmsp,3)) + '%', str(round(pgms,3)))
        sleep(1)



    #Paternal + Maternal Grandmother
    elif pgm == 1 and f == 0 and m == 0 and mgm == 1 :
        pgms=(1/12)*amount
        pgmsp=pgms/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance share for both Paternal & Maternal Grand Mothers'):
            sleep(.1)
            step
        print("\n       :small_red_triangle: Paternal Grand Mother gets 1/12th prescribed share: " , round(pgms,3),"\n")
        tree.add("Paternal Grand Mother 1/12 " + str(round(pgms,3))).add("[green] 1/12").add("[blue] "+str(round(pgms,3)))
        table.add_row("Paternal Grand Mother", "1/12", str(round(pgmsp,3)) + '%', str(round(pgms,3)))
        sleep(1)
        
        mgms=(1/12)*amount
        mgmsp=mgms/amount*100
        
        print("\n       :small_red_triangle: Maternal Grand Mother gets 1/12th prescribed share: " , round(mgms,3),"\n\n")
        tree.add("Maternal Grand Mother 1/12 " + str(round(mgms,3))).add("[green] 1/12").add("[blue] "+str(round(mgms,3)))
        table.add_row("Maternal Grand Mother", "1/12", str(round(mgmsp,3)) + '%', str(round(mgms,3)))
        sleep(1)


    #Maternal Grand Mother
    elif mgm == 1 and m == 0 :
        mgms=(1/6)*amount
        sleep(1)
        mgmsp=mgms/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance share for Maternal Grand Mother'):
            sleep(.1)
            step
        print("\n       :small_red_triangle: Maternal Grand Mother gets 1/6th prescribed share: " , round(mgms,3),"\n\n")
        tree.add("Maternal Grand Mother 1/6 " + str(round(mgms,3))).add("[green] 1/6").add("[blue] "+str(round(mgms,3)))
        table.add_row("Maternal Grand Mother", "1/6", str(round(mgmsp,3)) + '%', str(round(mgms,3)))
        sleep(1)
    

    #Sum Of Prescribed Shares + Remainder
    sops = ( hs + ws + fs + ms + ds + ss + pgfs + pgms + mgms )
    remainder = amount - sops
    

    #Daughter 
    if d == 1 :
        ds=d/((s*2)+d)*(remainder)
        dsp=ds/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance share for Daughter  '):
            sleep(.1)
            step
        print("\n       :small_red_triangle: Daughter gets half ratio to son from remaining: " , round(ds,3),"\n\n")
        tree.add("Daughter 1:2 Ratio to Son(s) " + str(round(ds,3))).add("[green] Ratio").add("[blue] "+str(round(ds,2)))
        table.add_row("Daughter", "1:2 Ratio with Son(s)", str(round(dsp,3)) + '%', str(round(ds,3)))
        sleep(1)


    #Multiple Daughters
    elif d > 1 :
        ds=d/((s*2)+d)*(remainder)
        dsp=ds/amount*100
        edsp=ds/d/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance share for Daughters '):
            sleep(.1)
            step
        print("\n       :small_red_triangle: All Daughters combined, get half ratio to sons from remaining: " , round(ds,3))
        tree.add("Daughters 1:2 Ratio to Son " + str(round(ds,3))).add("[green] Ratio").add("[blue] "+str(round(ds,2)))
        table.add_row("Daughter(s)", "1:2 Ratio to Son", str(round(dsp,3)) + '%', str(round(ds,3)))
        table.add_row("  Each Daughter", "1:2 Ratio to Son", str(round(edsp,3)) + '%', str(round(ds/d,3)))
        
        
        sleep(1)
        
        print("\n       Each daughter gets : " , round(ds/d,3),"\n\n")

        sleep(1)


    #Sons
    if s == 1:    
        ss=s*2/((s*2)+d)*(remainder)
        ssp=ss/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance share for Son       '):
            sleep(.1)
            step
        print("\n       :small_red_triangle: Son gets remaining OR twice to daughter: " , round(ss,3),"\n\n")
        tree.add("Son Remaining OR 2:1 to Daughter(s) " + str(round(ss,3))).add("[green] Remaining OR Ratio").add("[blue] "+str(round(ss,2)))
        table.add_row("Son", "Remaining OR 2:1 to Daughter", str(round(ssp,3)) + '%', str(round(ss,3)))

        sleep(1)
    #Multiple Sons
    elif s > 1:
        ss=s*2/((s*2)+d)*(remainder)
        ssp=ss/amount*100
        essp=ss/s/amount*100
        for step in track(range(15), description='[green]    Calculating Inheritance share for Sons      '):
            sleep(.1)
            step
        print("\n       :small_red_triangle: All Sons combined, get remaining OR twice to daughter: " , round(ss,3))
        tree.add("Son Remaining OR 2:1 to Daughter(s) " + str(round(ss,3))).add("[green] Remaining OR Ratio").add("[blue] "+str(round(ss,2)))
        table.add_row("Sons", "Remaining OR 2:1 to Daughter", str(round(ssp,3)) + '%', str(round(ss,3)))
        table.add_row("  Each Son", "2:1 to Daughter", str(round(essp,3)) + '%', str(round(ss/s,3)))
        sleep(1)
        print("\n       Each son gets: " , round(ss/s,3),"\n\n")
        sleep(1)

    #Inheritance distributed
    #print(remainder)
    print("\n        [green]*** All inheritance distributed ***\n\n")

#-----------------------------------------Scenario 2: No Son but Daughter alive-----------------------------------------
if s==0 and d >= 1 : 
                
        #Husband 
        if h == 1 :        
            hs = (1/4)*amount
            sleep(1)
            hsp=hs/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance share for Husband'):
                sleep(.1)
                step
            print("\n       :small_red_triangle: Husband gets 1/4th prescribed share: " , round(hs,3),"\n\n")
            tree.add("Husband 1/4 " + str(round(hs,3))).add("[green] 1/4").add("[blue] "+str(round(hs,3)))
            table.add_row("Husband", "1/4", str(round(hsp,3)) + '%', str(round(hs,3)))
            sleep(1)
                

        #Wife
        elif h == 0 and w == 1:        
            ws = (1/8)*amount
            sleep(1)
            wsp=ws/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance for Wife            '):
                sleep(.1)
                step
            print("\n       :small_red_triangle: Wife gets 1/8th prescribed share: " , round(ws,3),"\n\n")
            tree.add("Wife 1/8 " + str(round(ws,3))).add("[green] 1/8").add("[blue] "+str(round(ws,3)))
            table.add_row("Wife", "1/8", str(round(wsp,3)) + '%', str(round(ws,3)))
            sleep(1)


        #Multiple Wives
        elif h == 0 and w > 1 :
            ws = (1/8)*amount
            wsp=ws/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance for Wives           '):
                sleep(.1)
                step
            print("\n       :small_red_triangle: All wives combined get 1/8th prescribed share:" , round(ws,3))
            tree.add("Wives 1/8 " + str(round(ws,3))).add("[green] 1/8").add("[blue] "+str(round(ws,3)))
            table.add_row("Wives", "1/8", str(round(wsp,3)) + '%', str(round(ws,3)))
            ews=ws/w
            ewsp=ews/amount*100

            if w==3 :
                table.add_row("  Each wife", "1/24", str(round(ewsp,3)) + '%', str(round(ews,3)))
            else :
                ewsf=1/8/w
                table.add_row("  Each wife", str(Fraction(ewsf)), str(round(ewsp,3)) + '%', str(round(ews,3)))

            sleep(1)
            print("\n       Each wife gets: ", ews,"\n\n")
            sleep(1)

        #Daughter
        if d == 1 :
            ds=(1/2)*amount
            dsp=ds/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance share for Daughter  '):
                sleep(.1)
                step
            print("\n       :small_red_triangle: Daughter gets 1/2 prescribed share: " , round(ds,3),"\n\n")
            tree.add("Daughter 1/2 " + str(round(ds,3))).add("[green] 1/2").add("[blue] "+str(round(ds,2)))
            table.add_row("Daughter", "1/2", str(round(dsp,3)) + '%', str(round(ds,3)))
            sleep(1)
            

        #Multiple Daughters
        elif d > 1 :
                ds=(2/3)*amount
                dsp=ds/amount*100
                edsp=ds/d/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Daughters '):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: All Daughters combined, get 2/3: " , round(ds,3))
                tree.add("Daughters 2/3 " + str(round(ds,3))).add("[green] 2/3").add("[blue] "+str(round(ds,2)))
                table.add_row("Daughter(s)", "2/3", str(round(dsp,3)) + '%', str(round(ds,3)))
                edsf=2/3/d
                table.add_row("  Each Daughter", str(Fraction(edsf)) , str(round(edsp,3)) + '%', str(round(ds/d,3)))
                sleep(1)
                print("\n       Each daughter gets : " , round(ds/d,3),"\n\n")
                sleep(1)


        #Father
        if f == 1 :        
            fs = (1/6)*amount
            sleep(1)
            fsp=fs/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance share for Father    '):
                sleep(.1)
                step
            print("\n       :small_red_triangle: Father gets 1/6th prescribed share: " , round(fs,3),"\n\n")
            tree.add("Father 1/6 " + str(round(fs,3))).add("[green] 1/6").add("[blue] "+str(round(fs,3)))
            table.add_row("Father", "1/6", str(round(fsp,3)) + '%', str(round(fs,3)))
            sleep(1)


        #Paternal Grand Father
        elif pgf == 1 and f == 0:     
            pgfs = (1/6)*amount
            sleep(1)
            pgfsp=pgfs/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance share for Paternal Grand Father'):
                sleep(.1)
                step
            print("\n       :small_red_triangle: Paternal Grand Father gets 1/6th prescribed share: " , round(pgfs,3),"\n\n")
            tree.add("Paternal Grand Father 1/6 " + str(round(pgfs,3))).add("[green] 1/6").add("[blue] "+str(round(pgfs,3)))
            table.add_row("Paternal Grand Father", "1/6", str(round(pgfsp,3)) + '%', str(round(pgfs,3)))
            sleep(1)


        #Mother
        if m == 1 :        
            ms = (1/6)*amount
            sleep(1)
            msp=ms/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance share for Mother    '):
                sleep(.1)
                step
            print("\n       :small_red_triangle: Mother gets 1/6th prescribed share: " , round(ms,3),"\n\n")
            tree.add("Mother 1/6 " + str(round(ms,3))).add("[green] 1/6").add("[blue] "+str(round(ms,3)))
            table.add_row("Mother", "1/6", str(round(msp,3)) + '%', str(round(ms,3)))
            sleep(1)


        #Paternal Grand Mother
        elif pgm == 1 and f == 0 and m == 0 and mgm == 0 :
            pgms=(1/6)*amount
            sleep(1)
            pgmsp=pgms/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance share for Paternal Grand Mother'):
                sleep(.1)
                step
            print("\n       :small_red_triangle: Paternal Grand Mother gets 1/6th prescribed share: " , round(pgms,3),"\n\n")
            tree.add("Paternal Grand Mother 1/6 " + str(round(pgms,3))).add("[green] 1/6").add("[blue] "+str(round(pgms,3)))
            table.add_row("Paternal Grand Mother", "1/6", str(round(pgmsp,3)) + '%', str(round(pgms,3)))
            sleep(1)


        #Paternal Grand Mother + Maternal Grand Mother                
        elif pgm == 1 and f == 0 and m == 0 and mgm == 1 :
            pgms=(1/12)*amount
            pgmsp=pgms/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance share for both Paternal & Maternal Grand Mothers'):
                sleep(.1)
                step
            print("\n       :small_red_triangle: Paternal Grand Mother gets 1/12th prescribed share: " , round(pgms,3),"\n")
            tree.add("Paternal Grand Mother 1/12 " + str(round(pgms,3))).add("[green] 1/12").add("[blue] "+str(round(pgms,3)))
            table.add_row("Paternal Grand Mother", "1/12", str(round(pgmsp,3)) + '%', str(round(pgms,3)))
            sleep(1)
            
            mgms=(1/12)*amount
            mgmsp=mgms/amount*100
            
            print("\n       :small_red_triangle: Maternal Grand Mother gets 1/12th prescribed share: " , round(mgms,3),"\n\n")
            tree.add("Maternal Grand Mother 1/12 " + str(round(mgms,3))).add("[green] 1/12").add("[blue] "+str(round(mgms,3)))
            table.add_row("Maternal Grand Mother", "1/12", str(round(mgmsp,3)) + '%', str(round(mgms,3)))
            sleep(1)



        #Maternal Grand Mother
        elif mgm == 1 and m == 0 :
            mgms=(1/6)*amount
            sleep(1)
            mgmsp=mgms/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance share for Maternal Grand Mother'):
                sleep(.1)
                step
            print("\n       :small_red_triangle: Maternal Grand Mother gets 1/6th prescribed share: " , round(mgms,3),"\n\n")
            tree.add("Maternal Grand Mother 1/6 " + str(round(mgms,3))).add("[green] 1/6").add("[blue] "+str(round(mgms,3)))
            table.add_row("Maternal Grand Mother", "1/6", str(round(mgmsp,3)) + '%', str(round(mgms,3)))
            sleep(1)


        # Grand Daughter 1/6th Share
        if gd == 1 and gs == 0 and d == 1 :
            gds=(1/6)*amount
            sleep(1)
            gdsp=gds/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Daughter       '):
                sleep(.1)
                step
            print("\n       :small_red_triangle: Grand Daughter gets 1/6th prescribed share: " , round(gds,3),"\n\n")
            tree.add("Grand Daughter 1/6 " + str(round(gds,3))).add("[green] 1/6").add("[blue] "+str(round(gds,3)))
            table.add_row("Grand Daughter", "1/6", str(round(gdsp,3)) + '%', str(round(gds,3)))
            sleep(1)

        if gd > 1 and gs == 0 and d == 1 :
            gds=(1/6)*amount
            sleep(1)
            gdsp=gds/amount*100
            egds=gds/gd
            egdsp=egds/amount*100
            for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Daughters       '):
                sleep(.1)
                step
            print("\n       :small_red_triangle: All Grand Daughters combined, get 1/6th prescribed share: " , round(gds,3))
            tree.add("Grand Daughters 1/6 " + str(round(gds,3))).add("[green] 1/6").add("[blue] "+str(round(gds,3)))
            table.add_row("Grand Daughter(s)", "1/6", str(round(gdsp,3)) + '%', str(round(gds,3)))
            egdsf=1/6/gd
            table.add_row("  Each Grand Daughter", egdsf , str(round(egdsp,3)) + '%', str(round(egds,3)))
            sleep(1)

            print("\n       Each Grand daughter gets : " , round(egds,3),"\n\n")
        

        #Sum Of Prescribed Shares + Remainder
        sops = ( hs + ws + fs + ms + ds + ss + pgfs + pgms + mgms + gds )
        remainder = amount - sops


        #Inheritance distributed
        if remainder == 0 :
                print("\n        [green]*** All inheritance distributed ***")


#-------------------------Scenario 2---A: No Son but Daughter alive --- Amount Leftover----------------------------
        remainder=round(remainder,0)
        if remainder > 0 :
                print("\n       Prescribed shares distribution has leftover amount : ", remainder,"\n\n       [bold][blue]Tasib will be checked\n\n")
                

                #Grand Son
                if gs >= 1 and gd == 0:
                    
                    
                    gss=remainder
                    if gs == 1:
                        sleep(1)
                        gssp=gss/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Son'):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: Grand Son gets all remaining: " , round(gss,3),"\n\n")
                        tree.add("Grand Son : Tasib" + str(round(gss,3))).add("[green] All remaining").add("[blue] "+str(round(gss,3)))
                        table.add_row("Grand Son", "Tasib", str(round(gssp,3)) + '%', str(round(gss,3)))
                        sleep(1)
                        
                    
                    elif gs > 1:
                        gss=remainder
                        gssp=gss/amount*100
                        egssp=gss/gs/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Sons      '):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: All Grand Sons combined, get remaining: " , round(gss,3))
                        tree.add("Grand Sons : Tasib " + str(round(gss,3))).add("[green] Remaining").add("[blue] "+str(round(gss,2)))
                        table.add_row("Grand Sons", "Tasib", str(round(gssp,3)) + '%', str(round(gss,3)))
                        table.add_row("  Each Grand Son", "Tasib", str(round(egssp,3)) + '%', str(round(gss/gs,3)))
                        sleep(1)
                        print("\n       Each Grand Son gets: " , round(gss/gs,3),"\n\n")
                        sleep(1)

                    

                elif gs >= 1 and gd >=1:
                        
                        #Grand Son + Grand Daughter Shares
                        gss=gs*2/(gs*2+gd)*remainder
                        gds=gd/(gs*2+gd)*remainder
                        
                        #Grand Son + Grand Daughter Percentages
                        gssp=gss/amount*100
                        egssp=gss/gs/amount*100
                        gdsp=gds/amount*100
                        egdsp=gds/gd/amount*100


                        for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Sons      '):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: All Grand Sons to Grand Daughter 2:1 Tasib: " , round(gss,3))
                        tree.add("Grand Son(s) 2:1 to Grand Daughter(s) " + str(round(gss,3))).add("[green] Ratio").add("[blue] "+str(round(gss,2)))
                        table.add_row("Grand Sons", "2:1 to Grand Daughter", str(round(gssp,3)) + '%', str(round(gss,3)))
                        table.add_row("  Each Grand Son", "2:1 to Grand Daughter", str(round(egssp,3)) + '%', str(round(gss/gs,3)))
                        sleep(1)
                        print("\n       Each Grand Son gets: " , round(gss/gs,3),"\n\n")
                        sleep(1)

                        
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Daughters '):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: All Grand Daughters to Grand Sons 1:2 Tasib: " , round(gds,3))
                        tree.add("Grand Daughter(s) 1:2 Ratio to Grand Son(s) " + str(round(gds,3))).add("[green] Ratio").add("[blue] "+str(round(gds,2)))
                        table.add_row("Grand Daughter(s)", "1:2 Ratio to Son", str(round(gdsp,3)) + '%', str(round(gds,3)))
                        table.add_row("  Each Grand Daughter", "1:2 Ratio to Grand Son", str(round(egdsp,3)) + '%', str(round(gds/gd,3)))
                        sleep(1)
                        print("\n       Each Grand Daughter gets : " , round(gds/gd,3),"\n\n")
                        sleep(1)


                #Father
                elif gs == 0:
                    if f == 1 :        
                        fs = fs + remainder
                        sleep(1)
                        fsp=fs/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Father    '):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: Father gets gets all remaining: " , round(fs,3),"\n\n")
                        tree.add("Father : Tasib " + str(round(fs,3))).add("[green] All Remaining").add("[blue] "+str(round(fs,3)))
                        table.add_row("Father", "Tasib", str(round(fsp,3)) + '%', str(round(fs,3)))
                        sleep(1)

                    #No Father
                    elif f == 0 :


                            #Only Brother
                            if b > 0 and si == 0 :
                                   

                                   #Brother = 1
                                    if b == 1:
                                        
                                        bs=remainder
                                        sleep(1)
                                        bsp=bs/amount*100

                                        for step in track(range(15), description='[green]    Calculating Inheritance share for Brother'):
                                            sleep(.1)
                                            step
                                        print("\n       :small_red_triangle: Brother gets all remaining: " , round(bs,3),"\n\n")
                                        tree.add("Brother : Tasib" + str(round(bs,3))).add("[green] All remaining").add("[blue] "+str(round(bs,3)))
                                        table.add_row("Brother", "Tasib", str(round(bsp,3)) + '%', str(round(bs,3)))
                                        sleep(1)


                                    #Brother > 1
                                    elif b > 1 :

                                        bs=remainder
                                        bsp=bs/amount*100
                                        ebsp=bs/b/amount*100

                                        for step in track(range(15), description='[green]    Calculating Inheritance share for Brothers      '):
                                            sleep(.1)
                                            step
                                        print("\n       :small_red_triangle: All Brothers combined, get remaining: " , round(bs,3))
                                        tree.add("Brother(s) : Tasib " + str(round(bs,3))).add("[green] Remaining").add("[blue] "+str(round(bs,2)))
                                        table.add_row("Brother", "Tasib", str(round(bsp,3)) + '%', str(round(bs,3)))
                                        table.add_row("  Each Brother", "Tasib", str(round(ebsp,3)) + '%', str(round(bs/b,3)))
                                        sleep(1)
                                        print("\n       Each Brother gets: " , round(bs/b,3),"\n\n")
                                        sleep(1)
                                        

                            #Only Sister
                            elif b == 0 and si > 0 :
                                    #Sister = 1
                                    if si == 1:
                                        
                                        sis=remainder
                                        sleep(1)
                                        sisp=sis/amount*100

                                        for step in track(range(15), description='[green]    Calculating Inheritance share for Sister'):
                                            sleep(.1)
                                            step
                                        print("\n       :small_red_triangle: Sister gets all remaining: " , round(sis,3),"\n\n")
                                        tree.add("Sister : Tasib" + str(round(sis,3))).add("[green] All remaining").add("[blue] "+str(round(sis,3)))
                                        table.add_row("Sister", "Tasib", str(round(sisp,3)) + '%', str(round(sis,3)))
                                        sleep(1)


                                    #Sister > 1
                                    elif si > 1 :

                                        sis=remainder
                                        sisp=sis/amount*100
                                        esisp=sis/si/amount*100

                                        for step in track(range(15), description='[green]    Calculating Inheritance share for Sisters      '):
                                            sleep(.1)
                                            step
                                        print("\n       :small_red_triangle: All Sisters combined, get remaining: " , round(sis,3))
                                        tree.add("Sisters : Tasib " + str(round(sis,3))).add("[green] Remaining").add("[blue] "+str(round(sis,2)))
                                        table.add_row("Sisters ", "Tasib", str(round(sisp,3)) + '%', str(round(sis,3)))
                                        table.add_row("  Each Sister", "Tasib", str(round(esisp,3)) + '%', str(round(sis/si,3)))
                                        sleep(1)
                                        print("\n       Each Sister gets: " , round(sis/si,3),"\n\n")
                                        sleep(1)
                                        
                            
                            #Brother + Sister
                            elif b >= 1 and si >=1:
                        
                                #Grand Son + Grand Daughter Shares
                                bs=b*2/(b*2+si)*remainder
                                sis=si/(b*2+si)*remainder
                                
                                #Grand Son + Grand Daughter Percentages
                                bsp=bs/amount*100
                                ebsp=bs/b/amount*100
                                sisp=sis/amount*100
                                esisp=sis/si/amount*100


                                for step in track(range(15), description='[green]    Calculating Inheritance share for Brothers      '):
                                    sleep(.1)
                                    step
                                print("\n       :small_red_triangle: All Brothers to Sisters 2:1 Tasib : " , round(bs,3))
                                tree.add("Brother(s) 2:1 to Sister(s) " + str(round(bs,3))).add("[green] Ratio").add("[blue] "+str(round(bs,2)))
                                table.add_row("Brothers", "2:1 to Sister", str(round(bsp,3)) + '%', str(round(bs,3)))
                                table.add_row("  Each Brother", "2:1 to Sister", str(round(ebsp,3)) + '%', str(round(bs/b,3)))
                                sleep(1)
                                print("\n       Each Brother gets: " , round(bs/b,3),"\n\n")
                                sleep(1)

                                
                                for step in track(range(15), description='[green]    Calculating Inheritance share for Sisters '):
                                    sleep(.1)
                                    step
                                print("\n       :small_red_triangle: All Sisters to Brothers 1:2 Tasib: " , round(sis,3))
                                tree.add("Sisters 1:2 Ratio to Brother " + str(round(sis,3))).add("[green] Ratio").add("[blue] "+str(round(sis,2)))
                                table.add_row("Sister(s)", "1:2 Ratio to Brother", str(round(sisp,3)) + '%', str(round(sis,3)))
                                table.add_row("  Each Sister", "1:2 Ratio to Brother", str(round(esisp,3)) + '%', str(round(sis/si,3)))
                                sleep(1)
                                print("\n       Each Sister gets : " , round(sis/si,3),"\n\n")
                                sleep(1)

                            #No Brother + Sister Shares increase proportionally
                            elif b + si == 0 :
                                    print("\n\n       :arrow_up: [green]RADD Case :arrow_up: : Therefore, Shares will now be increased proportionally except the spouse\n")
                                    

                                    #Daughter & GrandDaughter
                                    if  d == 1 :
                                        ds=ds+(ds/(sops-hs-ws)*remainder)
                                        dsp=ds/amount*100
                                        for step in track(range(15), description='[green]    Calculating Inheritance share for Daughter  '):
                                            sleep(.1)
                                            step
                                        print("\n       :small_red_triangle: Daughter now gets 1/2 + Increment : " , round(ds,3),"\n\n")
                                        tree.add("Daughter [REVISED] 1/2 + Increment " + str(round(ds,3))).add("[green] 1/2").add("[blue] "+str(round(ds,2)))
                                        table.add_row("Daughter [REVISED]", "1/2 + Increment", str(round(dsp,3)) + '%', str(round(ds,3)))
                                        sleep(1)

                                        if gd >= 1 and gs == 0 : #gs condition is extra
                                            gds=gds+(gds/(sops-hs-ws)*remainder)
                                            gdsp=gds/amount*100
                                            egds=gds/gd
                                            egdsp=egds/amount*100
                                            if gd > 1 :
                                                for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Daughters  '):
                                                    sleep(.1)
                                                    step
                                                print("\n       :small_red_triangle: Grand Daughters now get 1/6 + Increment : " , round(gds,3),"\n\n")
                                                tree.add("Grand Daughters [REVISED] 1/6 + Increment" + str(round(gds,3))).add("[green] 1/6").add("[blue] "+str(round(gds,3)))
                                                table.add_row("Grand Daughters [REVISED]", "1/6 + Increment", str(round(gdsp,3)) + '%', str(round(gds,3)))
                                                table.add_row("  Each Grand Daughter [REVISED]", "1/6 + Increment", str(round(egdsp,3)) + '%', str(round(egds,3)))
                                                sleep(1)
                                                print("\n       Each Grand Daughters now gets:" , gds/gd)
                                            elif gd==1 :
                                                for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Daughter  '):
                                                    sleep(.1)
                                                    step
                                                print("\n       :small_red_triangle: Grand Daughters now get 1/6 + Increment : " , round(gds,3),"\n\n")
                                                tree.add("Grand Daughter [REVISED] 1/6 + Increment" + str(round(gds,3))).add("[green] 1/6").add("[blue] "+str(round(gds,3)))
                                                table.add_row("Grand Daughter [REVISED]", "1/6 + Increment", str(round(gdsp,3)) + '%', str(round(gds,3)))
                                                sleep(1)
                                                print("\n       Each Grand Daughters now gets:" , gds/gd)
                                                
                                                print("Grand Daughter now gets:" , gds)

                                    elif d > 1 :
                                        ds=ds+(ds/(sops-hs-ws)*remainder)
                                        dsp=ds/amount*100
                                        edsp=ds/d/amount*100
                                        for step in track(range(15), description='[green]    Calculating Inheritance share for Daughters  '):
                                            sleep(.1)
                                            step
                                        print("\n       :small_red_triangle: Daughters get 2/3 prescribed share + Increment: " , round(ds,3),"\n\n")
                                        tree.add("Daughters [REVISED] 2/3 + Increment" + str(round(ds,3))).add("[green] 2/3 + Increment").add("[blue] "+str(round(ds,2)))
                                        table.add_row("Daughter(s) [REVISED]", "2/3 + Increment", str(round(dsp,3)) + '%', str(round(ds,3)))
                                        table.add_row("  Each Daughter [REVISED]", "2/3 + Increment", str(round(edsp,3)) + '%', str(round(ds/d,3)))
                                        sleep(1)
                                        print("\n       All Daughters combined now get:" , ds)
                                        
                                        print("\n       Each Daughter now gets:" , ds/d)
                                    
                            
                                    #Paternal Grand Father
                                    if pgf == 1 :
                                            pgfs=pgfs+(pgfs/(sops-hs-ws)*remainder)
                                            sleep(1)
                                            pgfsp=pgfs/amount*100
                                            for step in track(range(15), description='[green]    Calculating Inheritance share for Paternal Grand Father'):
                                                sleep(.1)
                                                step
                                            print("\n       :small_red_triangle: Paternal Grand Father now gets 1/6th prescribed share + Increment: " , round(pgfs,3),"\n\n")
                                            tree.add("Paternal Grand Father [REVISED] 1/6 + Increment " + str(round(pgfs,3))).add("[green] 1/6 + Increment").add("[blue] "+str(round(pgfs,3)))
                                            table.add_row("Paternal Grand Father [REVISED]", "1/6 + Increment", str(round(pgfsp,3)) + '%', str(round(pgfs,3)))
                                            sleep(1)



                                    #Paternal Grand Mother
                                    if pgm == 1 :
                                            pgms=pgms+(pgms/(sops-hs-ws)*remainder)
                                            sleep(1)
                                            pgmsp=pgms/amount*100
                                            for step in track(range(15), description='[green]    Calculating Inheritance share for Paternal Grand Mother'):
                                                sleep(.1)
                                                step
                                            print("\n       :small_red_triangle: Paternal Grand Mother gets 1/6th prescribed share + Increment: " , round(pgms,3),"\n\n")
                                            tree.add("Paternal Grand Mother [REVISED] 1/6 + Increment " + str(round(pgms,3))).add("[green] 1/6 + Increment").add("[blue] "+str(round(pgms,3)))
                                            table.add_row("Paternal Grand Mother [REVISED]", "1/6 + Increment", str(round(pgmsp,3)) + '%', str(round(pgms,3)))
                                            sleep(1)


                                    #Maternal Grand Mother
                                    if mgm == 1 :
                                            mgms=mgms+(mgms/(sops-hs-ws)*remainder)
                                            sleep(1)
                                            mgmsp=mgms/amount*100
                                            for step in track(range(15), description='[green]    Calculating Inheritance share for Maternal Grand Mother'):
                                                sleep(.1)
                                                step
                                            print("\n       :small_red_triangle: Maternal Grand Mother gets 1/6th prescribed share + Increment: " , round(mgms,3),"\n\n")
                                            tree.add("Maternal Grand Mother [REVISED] 1/6 + Increment " + str(round(mgms,3))).add("[green] 1/6 + Increment").add("[blue] "+str(round(mgms,3)))
                                            table.add_row("Maternal Grand Mother [REVISED]", "1/6 + Increment", str(round(mgmsp,3)) + '%', str(round(mgms,3)))
                                            sleep(1)
                                    
                                    
                                    #Mother
                                    if m == 1 :
                                            ms=ms+((ms/(sops-hs-ws))*remainder)
                                            sleep(1)
                                            msp=ms/amount*100
                                            for step in track(range(15), description='[green]    Calculating Inheritance share for Mother    '):
                                                sleep(.1)
                                                step
                                            print("\n       :small_red_triangle: Mother gets 1/6th prescribed share + Increment: " , round(ms,3),"\n\n")
                                            tree.add("Mother 1/6 + Increment " + str(round(ms,3))).add("[green] 1/6 + Increment").add("[blue] "+str(round(ms,3)))
                                            table.add_row("Mother", "1/6 + Increment", str(round(msp,3)) + '%', str(round(ms,3)))
                                            sleep(1)

                                
                print("\n       [green]***All inheritance distributed***\n")
                        
#-------------------------Scenario 2---B: No Son but Daughter alive---Amount Exceeded----------------------------
        
        if remainder < 0 :

                #Absolute remainder as [remainer < 0]
                remainder=abs(remainder)
                
                print("\n       [red]Prescribed shares distribution has exceeded the amount by ",remainder,".")
                print("\n\n       :arrow_down: [red]AWL Case :arrow_down: : Therefore, Shares will now be reduced proportionally\n\n")

                #Decreased share of Husband
                if h == 1 :
                        hs=(hs-((hs/sops))*remainder)
                        sleep(1)
                        hsp=hs/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Husband'):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: Husband gets 1/4th prescribed share - Decrement: " , round(hs,3),"\n\n")
                        tree.add("Husband [REVISED] 1/4 - Decrement " + str(round(hs,3))).add("[green] 1/4 - Decrement").add("[blue] "+str(round(hs,3)))
                        table.add_row("Husband [REVISED]", "1/4 - Decrement", str(round(hsp,3)) + '%', str(round(hs,3)))
                        sleep(1)


                #Decreased share of Wife
                if w == 1 :
                    ws=(ws-((ws/sops))*remainder)
                    sleep(1)
                    wsp=ws/amount*100
                    for step in track(range(15), description='[green]    Calculating Inheritance for Wife            '):
                        sleep(.1)
                        step
                    print("\n       :small_red_triangle: Wife gets 1/8th prescribed share - Decrement: " , round(ws,3),"\n\n")
                    tree.add("Wife [REVISED] 1/8 - Decrement " + str(round(ws,3))).add("[green] 1/8 - Decrement").add("[blue] "+str(round(ws,3)))
                    table.add_row("Wife [REVISED]", "1/8 - Decrement", str(round(wsp,3)) + '%', str(round(ws,3)))
                    sleep(1)

                if w > 1 :
                        ws=(ws-((ws/sops))*remainder)
                        print("All Wives combined get:" , ws)
                        print("Each Wife now gets:" , ws/w)
                        wsp=ws/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance for Wives           '):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: All wives combined get 1/8th prescribed share - Decrement:" , round(ws,3))
                        tree.add("Wives [REVISED] 1/8 - Decrement " + str(round(ws,3))).add("[green] 1/8 - Decrement").add("[blue] "+str(round(ws,3)))
                        table.add_row("Wives [REVISED]", "1/8 - Decrement", str(round(wsp,3)) + '%', str(round(ws,3)))
                        
                        ews=ws/w
                        ewsp=ews/amount*100

                        if w==3 :
                            table.add_row("  Each wife [REVISED]", "1/24 - Decrement", str(round(ewsp,3)) + '%', str(round(ews,3)))
                        else :
                            ewsf=1/8/w
                            table.add_row("  Each wife [REVISED]", str(Fraction(ewsf)), str(round(ewsp,3)) + '%', str(round(ews,3)))

                        sleep(1)
                        print("\n       Each wife gets: ", ews,"\n\n")
                        sleep(1)


                #Decreased share of Father
                if f == 1 :
                        fs=(fs-((fs/sops))*remainder)
                        sleep(1)
                        fsp=fs/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Father    '):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: Father gets 1/6th prescribed share - Decrement: " , round(fs,3),"\n\n")
                        tree.add("Father [REVISED] 1/6 - Decrement " + str(round(fs,3))).add("[green] 1/6 - Decrement").add("[blue] "+str(round(fs,3)))
                        table.add_row("Father [REVISED]", "1/6 - Decrement", str(round(fsp,3)) + '%', str(round(fs,3)))
                        sleep(1)


                #Decreased share of Mother
                if m == 1 :
                        ms=(ms-((ms/sops))*remainder)
                        sleep(1)
                        msp=ms/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Mother    '):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: Mother gets 1/6th prescribed share - Decrement: " , round(ms,3),"\n\n")
                        tree.add("Mother [REVISED] 1/6 - Decrement " + str(round(ms,3))).add("[green] 1/6 - Decrement").add("[blue] "+str(round(ms,3)))
                        table.add_row("Mother [REVISED]", "1/6 - Decrement", str(round(msp,3)) + '%', str(round(ms,3)))
                        sleep(1)


                #Decreased share of Daughter & Grand Daughter
                if d == 1 :
                    ds=ds-(ds/sops*remainder)
                    dsp=ds/amount*100
                    for step in track(range(15), description='[green]    Calculating Inheritance share for Daughter  '):
                        sleep(.1)
                        step
                    print("\n       :small_red_triangle: Daughter gets 1/2 prescribed share - Decrement: " , round(ds,3),"\n\n")
                    tree.add("Daughter [REVISED] 1/2 - Decrement" + str(round(ds,3))).add("[green] 1/2 - Decrement").add("[blue] "+str(round(ds,2)))
                    table.add_row("Daughter [REVISED]", "1/2 - Decrement", str(round(dsp,3)) + '%', str(round(ds,3)))
                    sleep(1)

                    if gd >= 1 and gs == 0 : #gs condition is extra
                        gds=gds-(gds/(sops)*remainder)
                        sleep(1)
                        gdsp=gds/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Daughter       '):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: Grand Daughter gets 1/6th prescribed share - Decrement: " , round(gds,3),"\n\n")
                        tree.add("Grand Daughter [REVISED] 1/6 - Decrement " + str(round(gds,3))).add("[green] 1/6 - Decrement").add("[blue] "+str(round(gds,3)))
                        table.add_row("Grand Daughter [REVISED]", "1/6 - Decrement", str(round(gdsp,3)) + '%', str(round(gds,3)))
                        sleep(1)

                if d > 1 :
                    ds=ds-(ds/sops*remainder)
                    dsp=ds/amount*100
                    edsp=ds/d/amount*100
                    for step in track(range(15), description='[green]    Calculating Inheritance share for Daughters '):
                        sleep(.1)
                        step
                    print("\n       :small_red_triangle: All Daughters combined, get 2/3 - Decrement: " , round(ds,3))
                    tree.add("Daughters [REVISED] 2/3 - Decrement " + str(round(ds,3))).add("[green] 2/3 - Decrement").add("[blue] "+str(round(ds,2)))
                    table.add_row("Daughter(s) [REVISED]", "2/3 + Decrement", str(round(dsp,3)) + '%', str(round(ds,3)))
                    edsf=2/3/d
                    table.add_row("  Each Daughter [REVISED]", str(Fraction(edsf)) , str(round(edsp,3)) + '%', str(round(ds/d,3)))
                    sleep(1)
                    print("\n       Each daughter gets : " , round(ds/d,3),"\n\n")
                    sleep(1)

                
                #Decreased share of Paternal Grand Father        
                if pgf == 1 and f == 0: 
                        pgfs=(pgfs-(pgfs/sops)*remainder)
                        sleep(1)
                        pgfsp=pgfs/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Paternal Grand Father'):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: Paternal Grand Father gets 1/6th prescribed share - Decrement: " , round(pgfs,3),"\n\n")
                        tree.add("Paternal Grand Father [REVISED] 1/6 - Decrement " + str(round(pgfs,3))).add("[green] 1/6 - Decrement").add("[blue] "+str(round(pgfs,3)))
                        table.add_row("Paternal Grand Father [REVISED]", "1/6 - Decrement", str(round(pgfsp,3)) + '%', str(round(pgfs,3)))
                        sleep(1)


                #Decreased share of Paternal Grand Mother
                if pgm == 1 and m == 0:
                        pgms=(pgms-(pgms/sops)*remainder)
                        sleep(1)
                        pgmsp=pgms/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Paternal Grand Mother'):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: Paternal Grand Mother gets 1/6th prescribed share - Decrement: " , round(pgms,3),"\n\n")
                        tree.add("Paternal Grand Mother [REVISED] 1/6 - Decrement " + str(round(pgms,3))).add("[green] 1/6 - Decrement").add("[blue] "+str(round(pgms,3)))
                        table.add_row("Paternal Grand Mother [REVISED]", "1/6 - Decrement", str(round(pgmsp,3)) + '%', str(round(pgms,3)))
                        sleep(1)
                

                #Decreased share of Maternal Grand Mother
                if mgm == 1 and m == 0:
                        mgms=(mgms-(mgms/sops)*remainder)
                        sleep(1)
                        mgmsp=mgms/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Maternal Grand Mother'):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: Maternal Grand Mother gets 1/6th prescribed share - Decrement: " , round(mgms,3),"\n\n")
                        tree.add("Maternal Grand Mother [REVISED] 1/6 - Decrement " + str(round(mgms,3))).add("[green] 1/6 - Decrement").add("[blue] "+str(round(mgms,3)))
                        table.add_row("Maternal Grand Mother [REVISED]", "1/6 - Decrement", str(round(mgmsp,3)) + '%', str(round(mgms,3)))
                        sleep(1)
                

                print()
                print("\n       [green]***All inheritance distributed.***")
                print()


#-----------------------------------------Scenario 3: No Son + No Daughter----------------------------------------------

'''old
if s + d == 0 :


    #Brother + Sister is less than 2 i.e. No multiple siblings.
    if b + si <= 1: #Brother + Sister is less than 2 i.e. No multiple siblings.
        

        #Father + Mother both alive, while one of Husband or Wife is alive
        if f + m == 2 and h + w == 1 : #Umar (RA)'s Fatwa
 

            #Wife
            if w == 1 :
                ws = (1/4) * amount
                print("Wife gets:" , ws)


            #Multiple Wives
            elif w >= 1 and w <= 4 : 
                ws = (1/4) * amount
                print("Wives get:" , ws)
                print("Each Wife gets:" , ws/w)
            

            #Husband
            elif h == 1 :
                hs = (1/2) * amount
                print("Husband gets:" , hs)
            

            #Sum Of Prescribed Shares + Remainder
            sops = ( hs + ws + fs + ms + ds + ss + pgfs + pgms + mgms )
            remainder = amount - sops
            
            
            #Father
            if f == 1 :
                fs = f*2/((f*2)+m)*(remainder)
                print("Father gets:" , fs)
            
            
            #Mother
            if m == 1 :
                ms = m/((f*2)+m)*(remainder)
                print("Mother gets:" , ms)
    

        else :
            
            
            #Husband
            if h == 1 :        
                hs = (1/2)*amount
                print("Husband gets:" , hs)


            #wife
            elif h == 0 and w == 1:
                ws = (1/4)*amount
                print("Wife gets:" , ws)


            #Multiple Wives
            elif h == 0 and w > 1 :
                ws = (1/4)*amount
                print("Wives get:" , ws)
                print("Each wife gets:" , ws/w)


            #Father
            if f == 1 :
                fs = (1/3)*amount
                print("Father prescribed share :" , fs)


            #Paternal Grand Father
            elif pgf == 1 and f == 0:
                pgfs = (1/6)*amount
                print("Paternal Grand Father gets:" , pgfs)


            #Mother
            if m == 1 :
                    ms=(1/3)*amount
                    print("Mother gets:" , ms)


            #Paternal Grand Mother
            elif pgm == 1 and f == 0 and m == 0 and mgm == 0 :
                    pgms=(1/6)*amount
                    print("Paternal Grand Mother gets" , pgms)


            #Paternal Grand Mother + Maternal Grand Mother
            elif pgm == 1 and f == 0 and m == 0 and mgm == 1 :
                    pgms=(1/12)*amount
                    print("Paternal Grand Mother gets" , pgms)
                    mgms=(1/12)*amount
                    print("Paternal Grand Mother gets" , mgms)


            #Maternal Grand Mother
            elif mgm == 1 and m == 0 :
                    mgms=(1/6)*amount
                    print("Maternal Grand Mother gets" , mgms)


            #Sum Of Prescribed Shares + Remainder
            sops = ( hs + ws + fs + ms + ds + ss + pgfs + pgms + mgms )
            remainder = amount - sops
            #print("REMAINDER",remainder)


            #No remainder
            if remainder == 0 :
                    print("       [green]***All inheritance distributed, No remainder:",remainder)

#-------------------------Scenario 3---A: No Son + No Daughter---Amount Leftover----------------------------
            #Remainder left to distribute    
            if remainder > 0 :
                print("Prescribed shares distribution has leftover amount : ", remainder,"\n\n")

                #Father
                if f == 1 :
                    fs=fs+remainder
                    print()
                    print("Father now gets all remaining,:" , remainder, "since he is the only heir left.  Thus total for father becomes",fs)
                    print()


                #Brother
                elif b > 0 and si == 0 :
                    bs=bs+remainder
                    print("Brother gets all remaining: ",remainder, "since he is the only heir left.")
                        

                #Sister
                elif b == 0 and si > 0 :
                    sis=sis+remainder
                    print("Sister gets all remaining: ",remainder, "since she is the only heir left.")


                #Paternal Grand Father
                elif pgf == 1:
                    pgfs=pgfs+remainder
                    print()
                    print("Paternal Grand Father now gets all remaining,:" , remainder, "since he is the only heir left.  Thus total for Paternal Grand Father becomes",pgfs)
                    print()
'''                    

if s + d == 0 :

    #Brother + Sister is less than 2 i.e. No multiple siblings.
    if b + si <= 1: #Brother + Sister is less than 2 i.e. No multiple siblings.

        #Father + Mother both alive, while one of Husband or Wife is alive
        if f + m == 2 and h + w == 1 : #Umar (RA)'s Fatwa
 

            #Wives              
            if w == 1:
                ws = (1/4) * amount
                sleep(1)
                wsp=ws/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance for Wife            '):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Wife gets 1/4th prescribed share: " , round(ws,3),"\n\n")
                tree.add("Wife 1/4 " + str(round(ws,3))).add("[green] 1/4").add("[blue] "+str(round(ws,3)))
                table.add_row("Wife", "1/4", str(round(wsp,3)) + '%', str(round(ws,3)))
                sleep(1)
                

            #Multiple Wives
            elif w >= 2 and w <= 4 :# Wives >= 2 here unlike above code as multiple starts from 2
                ws = (1/4)*amount
                wsp=ws/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance for Wives           '):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: All wives combined get 1/4th prescribed share:" , round(ws,3))
                tree.add("Wives 1/4 " + str(round(ws,3))).add("[green] 1/4").add("[blue] "+str(round(ws,3)))
                table.add_row("Wives", "1/4", str(round(wsp,3)) + '%', str(round(ws,3)))
                ews=ws/w
                ewsp=ews/amount*100

                if w == 2 :
                    table.add_row("  Each wife", "1/8", str(round(ewsp,3)) + '%', str(round(ews,3)))
                elif w == 3 :
                    table.add_row("  Each wife", "1/12", str(round(ewsp,3)) + '%', str(round(ews,3)))
                elif w == 4:
                    table.add_row("  Each wife", "1/16" , str(round(ewsp,3)) + '%', str(round(ews,3)))

                sleep(1)
                print("\n       Each wife gets: ", ews,"\n\n")
                sleep(1)

                '''#Husband
                elif h == 1 :
                    hs = (1/2) * amount
                    print("Husband gets:" , hs)'''
                

            #Husband
            elif h == 1 :
                hs = (1/2) * amount    
                sleep(1)
                hsp=hs/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Husband'):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Husband gets 1/2th prescribed share: " , round(hs,3),"\n\n")
                tree.add("Husband 1/2 " + str(round(hs,3))).add("[green] 1/4").add("[blue] "+str(round(hs,3)))
                table.add_row("Husband", "1/2", str(round(hsp,3)) + '%', str(round(hs,3)))
                sleep(1)


            #Sum Of Prescribed Shares + Remainder
            sops = ( hs + ws + fs + ms + ds + ss + pgfs + pgms + mgms )
            remainder = amount - sops
            
            
    
            #Father
            if f == 1 :
                fs = f*2/((f*2)+m)*(remainder)
                sleep(1)
                fsp=fs/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Father    '):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Father gets twice of mother's share: " , round(fs,3),"\n\n")
                tree.add("Father 2:1 " + str(round(fs,3))).add("[green] 2:1").add("[blue] "+str(round(fs,3)))
                table.add_row("Father", "2:1", str(round(fsp,3)) + '%', str(round(fs,3)))
                sleep(1)
                
            

            #Mother
            if m == 1 :        
                ms = m/((f*2)+m)*(remainder)
                sleep(1)
                msp=ms/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Mother    '):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Mother gets half of Father's share: " , round(ms,3),"\n\n")
                tree.add("Mother 1:2 " + str(round(ms,3))).add("[green] 1:2").add("[blue] "+str(round(ms,3)))
                table.add_row("Mother", "1:2", str(round(msp,3)) + '%', str(round(ms,3)))
                sleep(1)

        else :


            #Husband
            if h == 1 :        
                hs = (1/2)*amount
                sleep(1)
                hsp=hs/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Husband'):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Husband gets 1/2 prescribed share: " , round(hs,3),"\n\n")
                tree.add("Husband 1/2 " + str(round(hs,3))).add("[green] 1/2").add("[blue] "+str(round(hs,3)))
                table.add_row("Husband", "1/2", str(round(hsp,3)) + '%', str(round(hs,3)))
                sleep(1)


            #wife
            elif h == 0 and w == 1:
                ws = (1/4)*amount
                sleep(1)
                wsp=ws/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance for Wife            '):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Wife gets 1/4th prescribed share: " , round(ws,3),"\n\n")
                tree.add("Wife 1/4 " + str(round(ws,3))).add("[green] 1/4").add("[blue] "+str(round(ws,3)))
                table.add_row("Wife", "1/4", str(round(wsp,3)) + '%', str(round(ws,3)))
                sleep(1)


            #Multiple Wives
            elif h == 0 and w > 1 :
                ws = (1/4)*amount
                wsp=ws/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance for Wives           '):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: All wives combined get 1/4th prescribed share:" , round(ws,3))
                tree.add("Wives 1/4 " + str(round(ws,3))).add("[green] 1/4").add("[blue] "+str(round(ws,3)))
                table.add_row("Wives", "1/4", str(round(wsp,3)) + '%', str(round(ws,3)))
                ews=ws/w
                ewsp=ews/amount*100

                if w == 2 :
                    table.add_row("  Each wife", "1/8", str(round(ewsp,3)) + '%', str(round(ews,3)))
                elif w == 3 :
                    table.add_row("  Each wife", "1/12", str(round(ewsp,3)) + '%', str(round(ews,3)))
                elif w == 4:
                    table.add_row("  Each wife", "1/16" , str(round(ewsp,3)) + '%', str(round(ews,3)))

                sleep(1)
                print("\n       Each wife gets: ", ews,"\n\n")
                sleep(1)

            #Father
            if f == 1 :
                fs = (1/3)*amount
                sleep(1)
                fsp=fs/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Father    '):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Father gets 1/3th prescribed share: " , round(fs,3),"\n\n")
                tree.add("Father 1/3 " + str(round(fs,3))).add("[green] 1/3").add("[blue] "+str(round(fs,3)))
                table.add_row("Father", "1/3", str(round(fsp,3)) + '%', str(round(fs,3)))
                sleep(1)


            #Paternal Grand Father
            elif pgf == 1 and f == 0:
                pgfs = (1/6)*amount
                sleep(1)
                pgfsp=pgfs/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Paternal Grand Father'):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Paternal Grand Father gets 1/6th prescribed share: " , round(pgfs,3),"\n\n")
                tree.add("Paternal Grand Father 1/6 " + str(round(pgfs,3))).add("[green] 1/6").add("[blue] "+str(round(pgfs,3)))
                table.add_row("Paternal Grand Father", "1/6", str(round(pgfsp,3)) + '%', str(round(pgfs,3)))
                sleep(1)



            #Mother
            if m == 1 :
                ms=(1/3)*amount
                sleep(1)
                msp=ms/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Mother    '):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Mother gets 1/3rd prescribed share: " , round(ms,3),"\n\n")
                tree.add("Mother 1/3 " + str(round(ms,3))).add("[green] 1/3").add("[blue] "+str(round(ms,3)))
                table.add_row("Mother", "1/3", str(round(msp,3)) + '%', str(round(ms,3)))
                sleep(1)


            #Paternal Grand Mother
            elif pgm == 1 and f == 0 and m == 0 and mgm == 0 :
                pgms=(1/6)*amount
                sleep(1)
                pgmsp=pgms/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Paternal Grand Mother'):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Paternal Grand Mother gets 1/6th prescribed share: " , round(pgms,3),"\n\n")
                tree.add("Paternal Grand Mother 1/6 " + str(round(pgms,3))).add("[green] 1/6").add("[blue] "+str(round(pgms,3)))
                table.add_row("Paternal Grand Mother", "1/6", str(round(pgmsp,3)) + '%', str(round(pgms,3)))
                sleep(1)



            #Paternal + Maternal Grandmother
            elif pgm == 1 and f == 0 and m == 0 and mgm == 1 :
                pgms=(1/12)*amount
                pgmsp=pgms/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for both Paternal & Maternal Grand Mothers'):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Paternal Grand Mother gets 1/12th prescribed share: " , round(pgms,3),"\n")
                tree.add("Paternal Grand Mother 1/12 " + str(round(pgms,3))).add("[green] 1/12").add("[blue] "+str(round(pgms,3)))
                table.add_row("Paternal Grand Mother", "1/12", str(round(pgmsp,3)) + '%', str(round(pgms,3)))
                sleep(1)
                
                mgms=(1/12)*amount
                mgmsp=mgms/amount*100
                
                print("\n       :small_red_triangle: Maternal Grand Mother gets 1/12th prescribed share: " , round(mgms,3),"\n\n")
                tree.add("Maternal Grand Mother 1/12 " + str(round(mgms,3))).add("[green] 1/12").add("[blue] "+str(round(mgms,3)))
                table.add_row("Maternal Grand Mother", "1/12", str(round(mgmsp,3)) + '%', str(round(mgms,3)))
                sleep(1)

            #Maternal Grand Mother
            elif mgm == 1 and m == 0 :
                mgms=(1/6)*amount
                sleep(1)
                mgmsp=mgms/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Maternal Grand Mother'):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Maternal Grand Mother gets 1/6th prescribed share: " , round(mgms,3),"\n\n")
                tree.add("Maternal Grand Mother 1/6 " + str(round(mgms,3))).add("[green] 1/6").add("[blue] "+str(round(mgms,3)))
                table.add_row("Maternal Grand Mother", "1/6", str(round(mgmsp,3)) + '%', str(round(mgms,3)))
                sleep(1)

            if gd == 1 and gs == 0 :
                gds=(1/2) * amount
                sleep(1)
                gdsp=gds/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Daughter       '):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: Grand Daughter gets 1/2th prescribed share: " , round(gds,3),"\n\n")
                tree.add("Grand Daughter 1/2 " + str(round(gds,3))).add("[green] 1/2").add("[blue] "+str(round(gds,3)))
                table.add_row("Grand Daughter", "1/2", str(round(gdsp,3)) + '%', str(round(gds,3)))
                sleep(1)

            elif gd > 1 and gs == 0 :
                gds=(2/3) * amount
                sleep(1)
                gdsp=gds/amount*100
                egds=gds/gd
                egdsp=egds/amount*100
                for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Daughters       '):
                    sleep(.1)
                    step
                print("\n       :small_red_triangle: All Grand Daughters combined, get 2/3 prescribed share: " , round(gds,3))
                tree.add("Grand Daughters 2/3 " + str(round(gds,3))).add("[green] 2/3").add("[blue] "+str(round(gds,3)))
                table.add_row("Grand Daughter(s)", "2/3", str(round(gdsp,3)) + '%', str(round(gds,3)))
                egdsf=1/6/gd
                table.add_row("  Each Grand Daughter", egdsf , str(round(egdsp,3)) + '%', str(round(egds,3)))
                sleep(1)

                print("\n       Each Grand daughter gets : " , round(egds,3),"\n\n")

            #Sum Of Prescribed Shares + Remainder
            sops = ( hs + ws + fs + ms + ds + ss + pgfs + pgms + mgms + gds)
            remainder = amount - sops


            #No remainder
            if remainder == 0 :
                print("All inheritance distributed, No remainder:",remainder)


#-------------------------Scenario 3---A: No Son + No Daughter---Amount Leftover----------------------------
            #Remainder left to distribute    
            if remainder > 0 :

                #Grand Son
                if gs >= 1 and gd == 0:
                    
                    
                    gss=remainder
                    if gs == 1:
                        sleep(1)
                        gssp=gss/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Son'):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: Grand Son gets all remaining: " , round(gss,3),"\n\n")
                        tree.add("Grand Son Taseeb" + str(round(gss,3))).add("[green] All remaining").add("[blue] "+str(round(gss,3)))
                        table.add_row("Grand Son", "Taseeb", str(round(gssp,3)) + '%', str(round(gss,3)))
                        sleep(1)
                        
                    
                    elif gs > 1:
                        gss=remainder
                        gssp=gss/amount*100
                        egssp=gss/gs/amount*100
                        for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Sons      '):
                            sleep(.1)
                            step
                        print("\n       :small_red_triangle: All Grand Sons combined, get remaining: " , round(gss,3))
                        tree.add("Grand Son Remaining " + str(round(gss,3))).add("[green] Remaining").add("[blue] "+str(round(gss,2)))
                        table.add_row("Grand Sons", "Remaining", str(round(gssp,3)) + '%', str(round(gss,3)))
                        table.add_row("  Each Grand Son", "Remaining", str(round(egssp,3)) + '%', str(round(gss/gs,3)))
                        sleep(1)
                        print("\n       Each Grand Son gets: " , round(gss/gs,3),"\n\n")
                        sleep(1)

                    

                elif gs >= 1 and gd >=1:
                    
                    #Grand Son + Grand Daughter Shares
                    gss=gs*2/(gs*2+gd)*remainder
                    gds=gd/(gs*2+gd)*remainder
                    
                    #Grand Son + Grand Daughter Percentages
                    gssp=gss/amount*100
                    egssp=gss/gs/amount*100
                    gdsp=gds/amount*100
                    egdsp=gds/gd/amount*100


                    for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Sons      '):
                        sleep(.1)
                        step
                    print("\n       :small_red_triangle: All Grand Sons combined, get twice to Grand Daughter: " , round(gss,3))
                    tree.add("Grand Son 2:1 to Grand Daughter(s) " + str(round(gss,3))).add("[green] Ratio").add("[blue] "+str(round(gss,2)))
                    table.add_row("Grand Son", "2:1 to Grand Daughter", str(round(gssp,3)) + '%', str(round(gss,3)))
                    table.add_row("  Each Grand Son", "2:1 to Grand Daughter", str(round(egssp,3)) + '%', str(round(gss/gs,3)))
                    sleep(1)
                    print("\n       Each Grand Son gets: " , round(gss/gs,3),"\n\n")
                    sleep(1)

                    
                    for step in track(range(15), description='[green]    Calculating Inheritance share for Grand Daughters '):
                        sleep(.1)
                        step
                    print("\n       :small_red_triangle: All Grand Daughters combined, get half ratio to Grand Sons from remaining: " , round(gds,3))
                    tree.add("Grand Daughters 1:2 Ratio to Grand Son " + str(round(gds,3))).add("[green] Ratio").add("[blue] "+str(round(gds,2)))
                    table.add_row("Grand Daughter(s)", "1:2 Ratio to Son", str(round(gdsp,3)) + '%', str(round(gds,3)))
                    table.add_row("  Each Grand Daughter", "1:2 Ratio to Grand Son", str(round(egdsp,3)) + '%', str(round(gds/gd,3)))
                    sleep(1)
                    print("\n       Each Grand Daughter gets : " , round(gds/gd,3),"\n\n")
                    sleep(1)

                print("Prescribed shares distribution has leftover amount : ", remainder)
                if f == 1 :        
                    fs = fs + remainder
                    sleep(1)
                    fsp=fs/amount*100
                    for step in track(range(15), description='[green]    Calculating Inheritance share for Father    '):
                        sleep(.1)
                        step
                    print("\n       :small_red_triangle: Father gets 1/6th prescribed share + Remaining: " , round(fs,3),"\n\n")
                    tree.add("Father Taseeb " + str(round(fs,3))).add("[green] All Remaining").add("[blue] "+str(round(fs,3)))
                    table.add_row("Father", "Taseeb", str(round(fsp,3)) + '%', str(round(fs,3)))
                    sleep(1)

                elif gs == 0:
                    if f == 1 :
                

                            #Only Brother
                            if b > 0 and si == 0 :
                                   

                                   #Brother = 1
                                    if b == 1:
                                        
                                        bs=remainder
                                        sleep(1)
                                        bsp=bs/amount*100

                                        for step in track(range(15), description='[green]    Calculating Inheritance share for Brother'):
                                            sleep(.1)
                                            step
                                        print("\n       :small_red_triangle: Brother gets all remaining: " , round(bs,3),"\n\n")
                                        tree.add("Brother Taseeb" + str(round(bs,3))).add("[green] All remaining").add("[blue] "+str(round(bs,3)))
                                        table.add_row("Brother", "Taseeb", str(round(bsp,3)) + '%', str(round(bs,3)))
                                        sleep(1)


                                    #Brother > 1
                                    elif b > 1 :

                                        bs=remainder
                                        bsp=bs/amount*100
                                        ebsp=bs/b/amount*100

                                        for step in track(range(15), description='[green]    Calculating Inheritance share for Brothers      '):
                                            sleep(.1)
                                            step
                                        print("\n       :small_red_triangle: All Brothers combined, get remaining: " , round(bs,3))
                                        tree.add("Brother Remaining " + str(round(bs,3))).add("[green] Remaining").add("[blue] "+str(round(bs,2)))
                                        table.add_row("Brother", "Remaining", str(round(bsp,3)) + '%', str(round(bs,3)))
                                        table.add_row("  Each Brother", "Remaining", str(round(ebsp,3)) + '%', str(round(bs/b,3)))
                                        sleep(1)
                                        print("\n       Each Brother gets: " , round(bs/b,3),"\n\n")
                                        sleep(1)
                                        

                            #Only Sister
                            elif b == 0 and si > 0 :
                                    #Sister = 1
                                    if si == 1:
                                        
                                        sis=remainder
                                        sleep(1)
                                        sisp=sis/amount*100

                                        for step in track(range(15), description='[green]    Calculating Inheritance share for Sister'):
                                            sleep(.1)
                                            step
                                        print("\n       :small_red_triangle: Sister gets all remaining: " , round(sis,3),"\n\n")
                                        tree.add("Sister Remaining" + str(round(sis,3))).add("[green] All remaining").add("[blue] "+str(round(sis,3)))
                                        table.add_row("Sister", "Taseeb", str(round(sisp,3)) + '%', str(round(sis,3)))
                                        sleep(1)


                                    #Sister > 1
                                    elif si > 1 :

                                        sis=remainder
                                        sisp=sis/amount*100
                                        esisp=sis/si/amount*100

                                        for step in track(range(15), description='[green]    Calculating Inheritance share for Sisters      '):
                                            sleep(.1)
                                            step
                                        print("\n       :small_red_triangle: All Sisters combined, get remaining: " , round(sis,3))
                                        tree.add("Sister Remaining " + str(round(sis,3))).add("[green] Remaining").add("[blue] "+str(round(sis,2)))
                                        table.add_row("Sister", "Remaining", str(round(sisp,3)) + '%', str(round(sis,3)))
                                        table.add_row("  Each Sister", "Remaining", str(round(esisp,3)) + '%', str(round(sis/si,3)))
                                        sleep(1)
                                        print("\n       Each Sister gets: " , round(sis/si,3),"\n\n")
                                        sleep(1)
                                        
                            
                            #Brother + Sister
                            elif b >= 1 and si >=1:
                        
                                #Grand Son + Grand Daughter Shares
                                bs=b*2/(b*2+si)*remainder
                                sis=si/(b*2+si)*remainder
                                
                                #Grand Son + Grand Daughter Percentages
                                bsp=bs/amount*100
                                ebsp=bs/b/amount*100
                                sisp=sis/amount*100
                                esisp=sis/si/amount*100


                                for step in track(range(15), description='[green]    Calculating Inheritance share for Brothers      '):
                                    sleep(.1)
                                    step
                                print("\n       :small_red_triangle: All Brothers combined, get twice to Sisters: " , round(bs,3))
                                tree.add("Brother(s) 2:1 to Sister(s) " + str(round(bs,3))).add("[green] Ratio").add("[blue] "+str(round(bs,2)))
                                table.add_row("Brother", "2:1 to Sister", str(round(bsp,3)) + '%', str(round(bs,3)))
                                table.add_row("  Each Brother", "2:1 to Sister", str(round(ebsp,3)) + '%', str(round(bs/b,3)))
                                sleep(1)
                                print("\n       Each Brother gets: " , round(bs/b,3),"\n\n")
                                sleep(1)

                                
                                for step in track(range(15), description='[green]    Calculating Inheritance share for Sisters '):
                                    sleep(.1)
                                    step
                                print("\n       :small_red_triangle: All Sisters combined, get half ratio to Brothers from remaining: " , round(sis,3))
                                tree.add("Sisters 1:2 Ratio to Brother " + str(round(sis,3))).add("[green] Ratio").add("[blue] "+str(round(sis,2)))
                                table.add_row("Sister(s)", "1:2 Ratio to Brother", str(round(sisp,3)) + '%', str(round(sis,3)))
                                table.add_row("  Each Sister", "1:2 Ratio to Brother", str(round(esisp,3)) + '%', str(round(sis/si,3)))
                                sleep(1)
                                print("\n       Each Sister gets : " , round(sis/si,3),"\n\n")
                                sleep(1)


                #Paternal Grand Father
                elif pgf == 1:
                    pgfs=pgfs+remainder
                    sleep(1)
                    pgfsp=pgfs/amount*100
                    for step in track(range(15), description='[green]    Calculating Inheritance share for Paternal Grand Father'):
                        sleep(.1)
                        step
                    print("\n       :small_red_triangle: Paternal Grand Father now gets 1/6th prescribed share + Increment: " , round(pgfs,3),"\n\n")
                    tree.add("Paternal Grand Father 1/6 + Increment " + str(round(pgfs,3))).add("[green] 1/6 + Increment").add("[blue] "+str(round(pgfs,3)))
                    table.add_row("Paternal Grand Father", "1/6 + Increment", str(round(pgfsp,3)) + '%', str(round(pgfs,3)))
                    sleep(1)
          

#-------------------------Scenario 3---B: No Son + No Daughter---Amount Exceeded----------------------------
            #Amount exceeded
            if remainder < 0 :
                
                
                remainder=abs(remainder)
                print("Prescribed shares distribution has exceeded the amount by ",remainder,".  Therefore shares will be reduced proportionally")
                   

                #Decreased share of Husband
                if h == 1 :
                    hs=(hs-((hs/sops))*remainder)
                    print("Husband now gets:" , hs)


                #Decreased share of Wife
                if w >= 1 :
                    ws=(ws-((ws/sops))*remainder)
                    print("Wife now gets:" , ws)


                #Decreased share of Father
                if f == 1 :
                    fs=(fs-((fs/sops))*remainder)
                    print("Father now gets:" , fs)


                #Decreased share of Mother
                if m == 1 :
                    ms=(ms-((ms/sops))*remainder)
                    print("Mother now gets:" , ms)


                #Decreased share of Daughter
                if d > 0 :
                    ds=ds-(ds/sops*remainder)
                    print("Daughter(s) now get(s):" , ds)


                #Decreased share of Paternal Grand Father        
                if pgf == 1 :
                    pgfs=(pgfs-(pgfs/sops)*remainder)
                    print("Paternal Grand Father now gets:" , pgfs)


                #Decreased share of Paternal Grand Mother
                if pgm == 1 :
                    pgms=(pgms-(pgms/sops)*remainder)
                    print("Paternal Grand Mother now gets:" , pgms)


                            #Increased share of Maternal Grand Mother
                if mgm == 1 :
                    mgms=(mgms-(mgms/sops)*remainder)
                    print("Maternal Grand Mother now gets:" , mgms)


                print()
                print("All inheritance distributed, No remainder")
                print()


    #Brother + Sister are equals to or more than 2
    if b + si >= 2 :
        

        #Husband
        if h == 1 :        
            hs = (1/2)*amount
            print("Husband gets:" , hs)


        #wife
        elif h == 0 and w == 1:
            ws = (1/4)*amount
            print("Wife gets:" , ws)


        #Multiple Wives
        elif h == 0 and w > 1 :
            ws = (1/4)*amount
            print("Wives get:" , ws)
            print("Each wife gets:" , ws/w)


        #Father
        if f == 1 :
            fs = (1/3)*amount
            print("Father prescribed share :" , fs)


        #Paternal Grand Father
        elif pgf == 1 and f == 0:
            pgfs = (1/6)*amount
            print("Paternal Grand Father gets:" , pgfs)


        #Mother
        if m == 1 :
                ms=(1/6)*amount
                print("Mother gets:" , ms)


        #Paternal Grand Mother
        elif pgm == 1 and f == 0 and m == 0 and mgm == 0 :
                pgms=(1/6)*amount
                print("Paternal Grand Mother gets" , pgms)
                

        #Paternal Grand Mother + Maternal Grand Mother
        elif pgm == 1 and f == 0 and m == 0 and mgm == 1 :
                pgms=(1/12)*amount
                print("Paternal Grand Mother gets" , pgms)
                mgms=(1/12)*amount
                print("Paternal Grand Mother gets" , mgms)
        
        #Maternal Grand Mother
        elif mgm == 1 and m == 0 :
                mgms=(1/6)*amount
                print("Maternal Grand Mother gets" , mgms)


        #Sum Of Prescribed Shares + Remainder
        sops = ( hs + ws + fs + ms + ds + ss + pgfs + pgms + mgms )
        remainder = amount - sops
        print("REMAINDER",remainder)


        #No Remainder
        if remainder == 0 :
                print("All inheritance distributed, No remainder:",remainder)


        #Remainder left to be distributed
        remainder=round(remainder)
        if remainder > 0 :


            #Father
            if f == 1 :
                fs=fs+remainder
                print("Father gets:" , fs)


            #Brother    
            elif b > 0 and si == 0 :
                bs=bs+remainder
                print("Brother gets:",bs)


            #Sister    
            elif b == 0 and si > 0 :
                sis=sis+remainder
                print("Sister gets:",sis)


            #Brother + Sister    
            elif b > 0 and si > 0 :
                bs=bs+((b*2)/((b*2)+si))*remainder
                sis=sis+((si)/((b*2)+si))*remainder
                print("Brother(s) get:",bs)
                print("Sister(s) get:",sis)
            

        #Exceeded Amount
        if remainder < 0 :


            remainder=abs(remainder)
            print("Exceeded amount, Reducing",remainder)
            print("Shares decrease proportionally")
                
            #Decreased share of Husband
            if h == 1 :
                hs=(hs-((hs/sops))*remainder)
                print("Husband now gets:" , hs)


            #Decreased share of Wife
            if w >= 1 :
                ws=(ws-((ws/sops))*remainder)
                print("Wife now gets:" , ws)


            #Decreased share of Father
            if f == 1 :
                fs=(fs-((fs/sops))*remainder)
                print("Father now gets:" , fs)


            #Decreased share of Mother
            if m == 1 :
                ms=(ms-((ms/sops))*remainder)
                print("Mother now gets:" , ms)


            #Decreased share of Daughter
            if d > 0 :
                ds=ds-(ds/sops*remainder)
                print("Daughter(s) now get(s):" , ds)


            #Decreased share of Paternal Grand Father        
            if pgf == 1 :
                pgfs=(pgfs-(pgfs/sops)*remainder)
                print("Paternal Grand Father now gets:" , pgfs)


            #Decreased share of Paternal Grand Mother
            if pgm == 1 :   
                pgms=(pgms-(pgms/sops)*remainder)
                print("Paternal Grand Mother now gets:" , pgms)


            #Decreased share of Maternal Grand Mother
            if mgm == 1 :
                mgms=(mgms-(mgms/sops)*remainder)
                print("Maternal Grand Mother now gets:" , mgms)

            #End
            print()
            print("All inheritance distributed")
            print()
            print()

relations=s+d+h+w+f+m+pgf+pgm+mgm+b+si+gs+gd

if relations >0:

    #Tree Structure
    sleep(1)
    for step in track(range(40), description='[gblue]    Generating Tree structure                    '):
        sleep(.04)
        step
    sleep(1)
    print("   ",tree)
    print("\n\n")

    #Table Structurex
    for step in track(range(40), description='[blue]    Generating Table view                        '):
        sleep(.04)
        step
    sleep(3)
    print("\n")
    console.print(table)
    sh=[ss,ds,hs,ws,fs,ms,pgfs,pgms,mgms,bs,sis,gss,gds]
    names=['Sons','Daughters','Husband','Wives', 'Father', 'Mother', 'P GrandFather', 'P GrandMother','M GrandMother','Brothers','Sisters','GrandSons','GrandDaughters']
    #plt.pie(sh,labels=names,autopct='%1.1f%%')

    #Pie Chart
    for step in track(range(40), description='[red]    Generating Pie chart                        '):
        sleep(.04)
        step
    sleep(3)
    #plt.show()
    print("\n\n")
    piesh=[]
    pinames=[]
    i=0
    for x in sh:
        
        if x != 0:
            piesh.append(x)
            print(piesh)
            #name.append()
            pinames.append(names[i])
            print(pinames)
        i=i+1

    plt.pie(piesh,labels=pinames,autopct='%1.1f%%')
    #plt.pie(piesh,labels=pinames)
    plt.show()


else:
    print("       No relative was entered. Inheritance will go to Islamic government.")