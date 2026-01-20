import os, sys, pyperclip
from rich import print
from rich.console import Console

lenpersons = 9
attributes = [
    'sports',
    'drinks',
    'tools',
    'hats',
    'socmed',
    'games',
    'vehicles',
    'names',
    'pets',
    'weather',
    'occupation',
]
objects = {
    'sports':['volleyball','ballet','basketball','soccer','baseball','hockey','boxing','bowling','rugby'],
    'drinks':['coffee','lemonade','milkshake','nonalcohol','water','milk','coke','energydrink','watermelon'],
    'tools':['wheelbarrow','handsaw','chainsaw','clamp','drill','tablesaw','shovel','wrench','hammer'],
    'hats':['feather','cowboy','baseballcap','helmet','santa','wizard','detective','crown','graduation'],
    'socmed':['skype','facebook','youtube','ebay','linkedin','instagram','google','pinterest','twitter'],
    'games':['computer','headphone','handheld','mouse','joystick','drivingwheel','wii','xbox','playstation'],
    'vehicles':['car','truck','tank','bike','train','zeppelin','helicopter','submarine','ambulance'],
    'names':['R','F','W','M','J','L','S','C','P'],
    'pets':['rabbit','rat','lion','panda','fox','frog','elephant','cat','dog'],
    'weather':['sun','rain','thunder','cloud','eclipse','snow','night','sunrise','tornado'],
    'occupation':['engineer','doctor','scientist','photographer','teacher','police','painter','pilot','dentist'],

    #'costume':['sultan', 'devil','judge','queen','sombrero','superman','unclesam','king','angel'],
    #'meds':['bloodbag','pressure','bandagecross','thermometer','syringe','scalpel','microscope','pill','orthopedic'],
    #'money':['C1','C5','C10','C25','USD1','USD5','USD10','USD20','USD50'],
    #'music':['violin','trumpet','tambourine','xylophone','flute','saxophone','keyboard','harp','guitar'],
    #'food':['banana','cheese','cherry','corn','mushroom','pasta','pineapple','steak','tomato'],
}
rules = [
    ['tablesaw','sunrise','rabbit','rugby','ebay','wizard'],
    ['water','train'],
    ['milkshake','snow','santa','pilot','bike','headphone'],
    ['playstation','panda','detective'],
    ['cowboy','drivingwheel'],
    ['energydrink','C'],
    ['car','thunder','computer'],
    ['skype','S','cat'],
    ['wheelbarrow','eclipse','tank'],
    ['helicopter','photographer','facebook','baseballcap'],
    ['truck','sun','hammer'],
    ['feather','doctor','watermelon'],
    ['F','elephant','teacher','baseball'],
    ['P','lion'],
    ['basketball','rain'],
    ['graduation','xbox'],
    ['bowling','twitter'],
    ['milk','J'],
    ['youtube','fox','tornado'],
    ['L','engineer','mouse'],
    ['shovel','scientist','nonalcohol','W','rat'],
    ['pinterest','handheld'],
    ['instagram','dog'],
    ['frog','night'],
]
rulesnegative = [
    ['dog','thunder',],
    ['train','engineer',],
    ['submarine','painter',],
    ['L','dog',],
    ['hockey','sun',],
    ['google','teacher',],
    ['instagram','tank',],
    ['chainsaw','zeppelin',],
    ['bike','dog',],
    ['wii','fox',],
    ['drill','feather',],
    ['clamp','night',],
    ['detective','truck',],
    ['zeppelin','painter',],
    ['linkedin','teacher',],
    ['chainsaw','cat',],
    ['youtube','drivingwheel',],
    ['linkedin','scientist',],
    ['panda','rain',],
    ['tank','panda',],
    ['tank','lion',],
    ['ballet','playstation',],
    ['coke','P',],
    ['R','tornado',],
    ['crown','elephant',],
    ['volleyball','truck',],
    ['google','panda',],
    ['soccer','ambulance',],
    ['wrench','doctor',],
    ['linkedin','police',],
    ['wrench','helicopter',],
    ['ballet','night',],
    ['basketball','police',],
    ['hockey','painter',],
    ['P','pilot',],
    ['chainsaw','photographer',],
    ['coffee','eclipse',],
    ['helicopter','R',],
    ['volleyball','P',],
    ['volleyball','painter']
    ['basketball','chainsaw',],
    ['drill','night',],
    ['nonalcohol','doctor',],
    ['rain','doctor',],
    ['wrench','cat',],
    ['playstation','R',],
    ['zeppelin','sunrise',],
    ['coke','F',],
    ['dog','sun',],
    ['twitter','police',],
    ['volleyball','night',],
    ['drivingwheel','R',],
    ['hockey','night',],
    ['mouse','tornado',],
    ['J','night',],
    ['rain','painter',],
    ['hockey','doctor',],
]

def getattitem(myitem):
    for object in objects:
        for item in objects[object]:
            if(item == myitem):
                return object

def safetomove(tfrom, tto):
    source = placeholder[tfrom]
    dest = placeholder[tto]
    temp = placeholder[tfrom] | placeholder[tto]
    myvalues = temp.values()
    for rules in rulesnegative:
        count = 0
        for rule in rules:
            if rule in myvalues:
                count += 1
        if(count==2):
            return False
    if source.keys() & dest.keys():
        return False
    else:
        return True

def safetoinput(col, att, item):
    myreturn = True
    for eachatt in placeholder[col]:
        for rulepair in rulesnegative:
            if placeholder[col][eachatt] in rulepair:
                item1 = rulepair[0]
                item2 = rulepair[1]
                #my = input(f'{placeholder[col][eachatt]} {item1} {item2}')
                if item == item1 or item == item2:
                    return False
    return myreturn

def checknegativewithin(col, possobject, att):
    for object in possobject:
        for rulepair in rulesnegative:
            if object in rulepair:
                item1 = rulepair[0]
                item2 = rulepair[1]
                for item in placeholder[col]:
                    if placeholder[col][item] == item1 or placeholder[col][item] == item2:
                        possobject.remove(object)

def checkatt(col, att, attvalue):
    att1 = ''
    att2 = ''
    for rulepair in rulesnegative:
        if attvalue in rulepair:
            att1 = getattitem(rulepair[0])
            att2 = getattitem(rulepair[1])

def printposs(possibilities, possobject, tposs):
    try:
        scol,att = possibilities.split(',')
        col=int(scol)
        colhighlight = col
        #temp=[]
        if not objects.get(att) is None:
            possobject = objects[att].copy()
            for i, place in enumerate(placeholder):
                if i==col:
                    continue
                if safetomove(i, col):
                    #temp.append(i)
                    value=place.get(att)
                    if value is not None:
                        tposs.append([i,col, value])
                    else:
                        pass
                        #tposs.append([i,col])
                else:
                    value=place.get(att)
                    #if checkatt(col, att, value):
                        #pass
                    if not value is None:
                        possobject.remove(value)
            if (len(tposs)==1):
                print(' 🛑 ', end='')
            elif(len(tposs)<3):
                print(' 🟡 ', end='')
            else:
                print(' ⚪️ ', end='')
            checknegativewithin(col, possobject, att)
            if(len(possobject)==1):
                print(' 🛑 ', end='')
            elif(len(possobject)<3):
                print(' 🟡 ', end='')
            else:
                print(' ⚪️ ', end='')
            tposs.append(possobject)
    except:
        pass

def printrules(highlight, colhighlight):
    print(''.ljust(14), end='')
    for i in range(len(placeholder)):
        print(str(i).ljust(14), end='')
    print('')
    mykeys = placeholder[int(colhighlight)].keys()
    for i, att in enumerate(attributes):
        print('[blue]' + att.ljust(14) + '[/blue]', end='')
        for i in range(len(placeholder)):
            value = placeholder[i].get(att)
            if(value is not None):
                highlighted = (att==highlight or i==int(colhighlight))
                if(highlighted):
                    print('[#ffff00]'+value.ljust(14)+'[/#ffff00]', end='')
                else:
                    if att in mykeys and colhighlight!=-1:
                        print('[red]'+value.ljust(14)+'[/red]', end='')
                    else:
                        print(value.ljust(14), end='')
            else:
                if(att in mykeys and colhighlight!=-1):
                    print('[green]'+('░░░░░'.ljust(14))+'[/green]', end='')
                else:
                    print(''.ljust(14), end='')
        print()
        console.rule(style='#c0c0c0')

def addblankrules():
    for object in objects:
        for item in objects[object]:
            foundpositive = False
            for rule in rules:
                if item in rule:
                    foundpositive = True
                    break
            foundnegative = False
            for rulepair in rulesnegative:
                if item in rulepair:
                    foundnegative = True
                    break
            if not foundpositive and not foundnegative:
                manualinput(object, item, 99)

def addtherest():
    for object in objects:
        for eachobject in objects[object]:
            found = False
            for i, place in enumerate(placeholder):
                value = placeholder[i].get(object)
                if value == eachobject:
                    found = True
                    break
            if not found:
                manualinput(object, eachobject, 99)

def showhistory():
    for i, his in enumerate(history):
        print(f'{i} {his}')

def fillallup():
    for i in range(lenpersons):
        myatt = {}
        for att in attributes:
            myatt[att]=''
        person.append(myatt)

    for rule in rules:
        myatt = {}
        for item in rule:
            att = getattitem(item)
            if(att == None):
                print(item + ' [#ff0000]Whatt?![/#ff0000]')
            myatt[att] = item
        placeholder.append(myatt)

def movenormal(tfrom, tto):
    if safetomove(tfrom, tto):
        print(f' {tfrom} {tto} ')
        placeholder[tto] = placeholder[tfrom] | placeholder[tto]
        placeholder.pop(tfrom)
        history.append([tfrom,tto])
        return True
    else:
        #error=('[red]Not allowed![/red]')
        return False

def manualinput(manual, item, mycol):
    if mycol > len(placeholder):
        placeholder.append(
            {manual:item}
        )
        history.append(['i', manual, item, mycol])
    elif safetoinput(mycol, manual, item):
        placeholder[mycol][manual]=item
        history.append(['i', manual, item, mycol])
    else:
        global error
        error=('[red]Not allowed![/red]')

os.system('cls')
console = Console()

person = []
placeholder = []
fillallup()

if(len(sys.argv)>1):
    x='auto'
else:
    x=''
highlight=-1
colhighlight=-1
tposs = []
possobject=[]
history=[]
runonce=1
while(x != 'x'):
    error=''
    if(x!=''):
        if(x=='h'):
            highlight = input('Which row to highlight? ')
        elif(x=='c'):
            colhighlight = input('Which row to highlight? ')
        elif(x=='cl'):
            colhighlight=-1
        elif(x=='u'):
            print('Select from history:')
            showhistory()
            his = input(' Enter -1 to reset, "x" to cancel ==> ')
            if(his=='x'):
                x = 'x'
            else:
                try:
                    his = int(his)
                    if his > len(history)-1:
                        error = '[red]Out of range![/red]'
                    else:
                        placeholder.clear()
                        fillallup()
                        temphistory = history.copy()
                        history.clear()
                        for i, myhis in enumerate(temphistory):
                            if i==his:
                                break
                            if(myhis[0]=='i'):
                                manualinput(myhis[1], myhis[2], int(myhis[3]))
                            elif(myhis[0]=='s'):
                                placeholder[myhis[1]], placeholder[myhis[2]] = placeholder[myhis[2]], placeholder[myhis[1]]
                                history.append(['s',myhis[1],myhis[2]])
                            else:
                                movenormal(int(myhis[0]), int(myhis[1]))
                except:
                    error = '[red]Invalid input![/red]'
        elif(x=='auto'):
            for arg in sys.argv[1:]:
                if arg.startswith('i,'):
                    op, mycat, myitem, tocol = arg.split(',')
                    if int(tocol) > len(placeholder):
                        placeholder.append(
                            {mycat:myitem}
                        )
                    elif safetoinput(int(tocol), mycat, myitem):
                        placeholder[int(tocol)][mycat]=myitem
                    else:
                        sys.exit('Invalid input!')
                else:
                    tfrom, tto = map(int, arg.split(','))
                    placeholder[tto] = placeholder[tfrom] | placeholder[tto]
                    placeholder.pop(tfrom)
        elif(x=='i'):
            manual = input('What to input? (category)? ')
            try:
                print(objects[manual])
                item = input('What item to input? ')
                mycol = input('To which column? ')
                mycol = int(mycol)
                manualinput(manual, item, mycol)
            except:
                pass
        elif(x=='p'):
            possibilities = input('Which column and attribute to check possibilities? (col,att) ')
            printposs(possibilities, possobject, tposs)
        elif(x=='pr'):
            att = input('Which attribute? ')
            for i, place in enumerate(placeholder):
                value = place.get(att)
                print(f' {i} ', end='')
                if value is None:
                    temp = str(i)+','+att
                    printposs(temp, possobject, tposs)
                else:
                    print(value, end='')
                print(tposs)
                tposs=[]
            temp = input('Press enter to continue or to input, start with 0 or i (0 for moving, i for input)...')
            if temp.startswith('0'):
                try:
                    tem2, tfrom, tto = map(int, temp.split(','))
                    if not movenormal(tfrom, tto):
                        error = '[red]Invalid input![/red]'
                    else:
                        error = f'[green]Done moving {tfrom} to {tto}[/green]'
                except:
                    error = f'[red]Invalid input![/red]'
            elif temp.startswith('i'):
                toinput = temp.split(',')
                try:
                    manualinput(toinput[1], toinput[2], int(toinput[3]))
                except:
                    error = f'[red]Invalid input![/red]'
        elif(x=='n'):
            negative = input('What to check negative? (att) ')
            for rulepair in rulesnegative:
                if negative in rulepair:
                    tposs.append(rulepair)
        elif(x=='s'):
            swap = input('Which columns to swap (col1,col2)? ')
            try:
                tfrom, tto = map(int, swap.split(','))
                placeholder[tfrom], placeholder[tto] = placeholder[tto], placeholder[tfrom]
                history.append(['s', tfrom, tto])
            except:
                error='[red]Invalid input![/red]'
        else:
            try:
                tfrom, tto = map(int, x.split(','))
                if not movenormal(tfrom, tto):
                    error = '[red]Invalid input or not allowed![/red]'
                else:
                    error = f'[green]Done moving {tfrom} to {tto} [/green]'
            except:
                pass
    os.system('clear')
    if(runonce==1):
        addblankrules()
        addtherest()
        runonce=0
    printrules(highlight, colhighlight)
    print(tposs)
    tposs = []
    print("\n\n")
    print(error)
    x = input('To move input "from,to" (e.g. 1,3). Enter x to quit ')