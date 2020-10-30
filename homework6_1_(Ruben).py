def possible_turns(cell):
    cell=list(cell)
    letter = ['','A','B','C','D','E','F','G','H']
    number = ['', 1,2,3,4,5,6,7,8]
    for i in range(1,len(letter),1):
        if letter.index(cell[0])- i == 2 or i - letter.index(cell[0]) ==2:
            print(letter[i] + str(number[int(cell[1])-1]),letter[i] + str(number[int(cell[1])+1]))
        if letter.index(cell[0])-i == 1 or i - letter.index(cell[0]) ==1:
            print(letter[i] + str(number[int(cell[1])-2]),letter[i] + str(number[int(cell[1])+2]))
        
            
possible_turns('B1')
                                                                             