import random

# English Translate: EPLSOFF, CumMaster2006
# Translation may contain spellings errors

print('\nWelcome to DUNGEON MASTER!')
print('Your goal is complete 100 leves and find Dungeon Master')
print('Each level can have 9 rooms')
print('Beware of SLAVE, they can kill you\n')

dif = ''
while not dif.isdigit() or not 1 <= int(dif) <= 3:
    print('>/=\\-------------------/=\\<')
    print('Choose the difficulty level')
    print('1. Slave')
    print('2. Performance Artist')
    print('3. Dungeon Master')
    dif = input(': ')
    print('>/=\\-------------------/=\\<\n')

    if not dif.isdigit() or not 1 <= int(dif) <= 3:
        print('#*@>>>-<<<#*@')
        print("Boy next door")
        print('#*@>>>-<<<#*@\n')
    else:
        if int(dif) == 1:
            hero_max_hp, hero_hp, hero_damage = 600, 600, 54
            slave, slave_hp, slave_damage = 0.06, 295, 11
        elif int(dif) == 2:
            hero_max_hp, hero_hp, hero_damage = 500, 500, 48
            slave, slave_hp, slave_damage = 0.08, 320, 15
        else:
            hero_max_hp, hero_hp, hero_damage = 400, 400, 40
            slave, slave_hp, slave_damage = 0.11, 350, 20
        slave_counter = 0

# Game settings
level = 1
room = 1
dif = int(dif)

# Food
food = 0
food_up_hp = 75

def battle(): # Battle
    global hero_hp
    global slave_hp
    slave_hpb = slave_hp
    while hero_hp > 0 and slave_hpb > 0:
        # Your attack
        hero_damageb = random.randint(int(hero_damage*0.8),int(hero_damage*1.2))
        slave_hpb -= hero_damageb
        print(f'===----------{di(hero_damageb)}===')
        print(f'You deal {hero_damageb} damage')
        print(f'===----------{di(hero_damageb)}===')
        input()

        # Slave attack
        if slave_hpb > 0:
            slave_damageb = random.randint(int(slave_damage*0.8),int(slave_damage* 1.2))
            hero_hp -= slave_damageb
            print(f'===---------{di(slave_damageb)}===')
            print(f'It deal {slave_damageb} damage')
            print(f'===---------{di(slave_damageb)}===')
            input()

def di(a): # Sticks are doing wee wee
    return len(str(a)) * '-'

while level != 100:
    print(f'<-----{di(level)}>')
    print(f'Level: {level}')
    print(f'<-----{di(level)}>\n')
    if level % 30 == 0:
        food_up_hp += 25
        print(f'-=1#@^------------------{di(food_up_hp - 25) + di(food_up_hp)}^@#1=-')
        print('Health recovery from food increased')
        print(f'Health recovery from food: {food_up_hp - 25} > {food_up_hp}')
        print(f'-=1#@^------------------{di(food_up_hp - 25) + di(food_up_hp)}^@#1=-\n')
    while room != 10:
        a = random.randrange(1, 10)
        if a == 1:
            print('*&^#----------#^&*')
            print('Slave attacked you')
            input('*&^#----------#^&*\n')
            slave_hpb = random.randint(slave_hp, slave_hp)
            battle()

            # End battle
            if hero_hp > 0: # Win
                slave_counter += 1

                # Up damage
                if dif == 1:
                    a = random.randint(3,9)
                elif dif == 2:
                    a = random.randint(3,10)
                else:
                    a = random.randint(4,12)
                hero_damage += a

                print(f'^&-------------{di(hero_damage - a) + di(hero_damage)}&^')
                print('YOU WON!\n')

                # Up HP
                if dif == 1:
                    hp = random.randint(10,24)
                elif dif == 2:
                    hp = random.randint(10,30)
                else:
                    hp = random.randint(10,36)
                hero_max_hp += hp

                print(f'Max. HP: {hero_max_hp - hp} > {hero_max_hp}')
                print(f'HP: {hero_hp}\n')

                print(f'Aver. damage: {hero_damage - a} > {hero_damage}') # Aver. damage
                print(f'^&-------------{di(hero_damage - a) + di(hero_damage)}&^')
                input()
            
            else: # Lose
                print('Death by slave...')
                exit()
        
        a = random.randint(1,20) # Maybe chest
        if a <= 3:
            foodr = random.randint(1,3) 
            a = random.randint(1,4) # Maybe +HP
            print('$#$-----------------------$#$')
            print('You found deep dark fantasies')
            print(f'+FOOD: {foodr}')
            food += foodr
            if a == 1:
                a = random.randint(80,150)
                print(f'+HP: {a}')
                if hero_hp + a > hero_max_hp:
                    hero_hp = hero_max_hp
                else:
                    hero_hp += a
            print('$#$-----------------------$#$\n')

        passages = random.randint(1,4)
        a = ''
        while not str(a).isdigit() or int(a) > passages:
            if room != 9: # Door
                print(f'You have only {passages} DOOR') 
                a = input(': ')
                print()

            else: # Pass down
                print(f'You have only {passages} ANAL')
                a = input(': ')
                print()

            if not a.isdigit() or int(a) > passages and not 5 <= int(a) <= 7: # Boy next door
                print('#*@>>>-<<<#*@')
                print("Boy next door")
                print('#*@>>>-<<<#*@\n')

            else:
                a = int(a)

            if a == 5: # Food
                if food == 0:
                    print('@=^----------@-^')
                    print('You have no food')
                    print('@=^----------@-^\n')
                elif hero_hp != hero_max_hp:
                    food -= 1
                    if hero_hp + food_up_hp > hero_max_hp: # You ate food, but HP + food > max. HP
                        print(f'&^*----------------------{di(hero_hp) + di(hero_max_hp)}&^*')
                        print(f'SUCK SOME DICK. Your HP: {hero_hp} > {hero_max_hp}')
                        print(f'&^*----------------------{di(hero_hp) + di(hero_max_hp)}&^*\n')
                        hero_hp = hero_max_hp
                    else: # You ate food 
                        hero_hp += food_up_hp
                        print(f'&^*----------------------{di(hero_hp - food_up_hp) + di(hero_hp)}&^*')
                        print(f'SUCK SOME DICK. Your HP: {hero_hp - food_up_hp} > {hero_hp}')
                        print(f'&^*----------------------{di(hero_hp - food_up_hp) + di(hero_hp)}&^*\n')
                else: # HP is full
                    print('^^#--------------#^^')
                    print('Wee wee already full')
                    print('^^#--------------#^^\n')

            elif a == 6: # Information and characteristics
                print(f'#^&*=--------------{di(slave_counter)}=&^#')
                print('Level:', level)
                print(f'{room} room from 9')
                print(f'HP: {hero_hp}')
                print(f'Max. HP: {hero_max_hp}')
                print(f'aver. damage: {hero_damage}')
                print(f"Total defeated '{slave_counter}' slave")
                print(f'#^&*=--------------{di(slave_counter)}=&^#\n')

            elif a == 7: # Inventory
                if food != 0:
                    print(f'<^--{di(food)}^>')
                    print(f'Food: {food}')
                    print(f'<^--{di(food)}^>\n')
                else: # Inventory is empty
                    print('^*><-----------------------------------><*^')
                    print('There is not even a cum in the inventory...')
                    print('^*><-----------------------------------><*^\n')
    
        room += 1
    level += 1
    room = 1

    # Up damage and HP
    if dif == 1:
        slave_hp = int(295 * (1 + level * slave))
        slave_damage = int(11 * (1 + level * slave))
    elif dif == 2:
        slave_hp = int(320 * (1 + level * slave))
        slave_damage = int(15 * (1 + level * slave))
    else:
        slave_hp = int(350 * (1 + level * slave))
        slave_damage = int(20 * (1 + level * slave))

if level == 100:
    print('It seeems like you lost food...')
    for i in range(15): # Corridor
        a = input(f'{i+1}:')
    input('Dungeon master...')
    if dif == 1:
        slave_hp = 5500
        slave_damage = 180
    elif dif == 2:
        slave_hp = 7500
        slave_damage = 220
    else:
        slave_hp = 9000
        slave_damage = 260

    battle()
    if hero_hp <= 0: # Lose
        print('Master is dead...')
        exit()

    print('#-----------------------#')
    print("You beat 'dungeon master'")
    print('#-----------------------#')
    input()
    print('*---------------*')
    print('+pass for fisting') 
    print('*---------------*')
    input()
    print('()<>===========================================<>()')
    print("Footage of fight: 'youtube.com/watch?v=s5NDqiCGqy8'")
    print('()<>===========================================<>()\n')