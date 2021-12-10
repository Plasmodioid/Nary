import math


def calc():
    numbersys = int(input('Please enter the number system you are trying to convert (Binary = 2, Decimal = 10, etc.)'))
    numberend = int(input('What numeric system would you like to convert to?'))
    numbe = (input('What is your number?'))

    savednumber = numbe
    print('')

    extranums = []
    for t in range(64):
        extranums.append(t + 10)

    extraextranums = []
    for e in range(64):
        extraextranums.append(e)

    if numberend == 64 or numbersys == 64: 
        extranums = extraextranums
    
    extras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    finalstring = []
    string = ''
    numlist = []
    summer = 0

    counter = 0

    if numbe.isdigit():
        number = []
        for s in range(len(numbe)):
            number.append(numbe[s])
            startingnumber = int(numbe)
    else:
        number = []
        for y in range(len(numbe)):
            number.append(numbe[y])
        for p in number:
            if p in extras:
                #print(p)
                number[number.index(p)] = extranums[extras.index(p)]
        THING = 0
        length = len(number)
                    
        #print(number, 'aisdufhidusahf')
        startingnumber = number
                
    if numbersys != -10:
        for t in range(len(number)):
            numlist.append(numbersys**t)
        numlist = numlist[::-1]
        for t in range(len(numlist)):
            summer += numlist[t]*int(number[t])

        numlist = []
        number = summer
        if numberend == 10:
            print('ur mom likes reverse osmosis')

    startingnumber = number

    numlist = []

    print(number)
    for i in range(len(str(number))+3):
        numlist.append(numberend**i)

    numlist = numlist[::-1]

    print(number)

    for ii in numlist:
        if ii > startingnumber:
            continue
        if ii <= number:
            thing = numlist.index(ii)
            while ii <= number:
                ii+=numlist[thing]
                counter += 1
            ii -= numlist[thing]
            number -= ii
        else:
            finalstring.append(0)
            continue
        
        finalstring.append(counter)
        #print(finalstring)
        counter = 0

        while finalstring[0] == 0:        
            finalstring = finalstring[1:]

        if numberend > 10:
            for iiii in range(len(extranums[0:numberend])):
                for iiiii in range(len(str(number))):
                    if int(extranums[iiii]) in finalstring:
                        l = finalstring.index(extranums[iiii])
                        finalstring[l] = extras[iiii]
                
    for num in finalstring:
        string += str(num)
    print('Base ' + str(numbersys) + ': [' + str(savednumber) + ']')
    print('Base ' + str(numberend) + ': [' + str(string) + ']')
    print('')

calc()

def againlol():
    again = input('Again? y/n')
    if again != 'n':
        print('')
        calc()
        againlol()

againlol()

