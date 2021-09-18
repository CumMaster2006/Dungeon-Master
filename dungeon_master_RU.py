import random

print('\nДобро пожалывать в DUNGEON MASTER!')
print('Суть игры пройти 100 уровней и попасть к dungeon master')
print('На одном уровне могут быть 9 комнат')
print('Опасайтесь SLAVE они могут вас убить, и вы потеряете свои 300$')

dif = ''
while not dif.isdigit() or not 1 <= int(dif) <= 3:
    print('>/=\\------------------/=\\<')
    print('Выберети уровень сложности')
    print('1. Slave')
    print('2. Performance Artist')
    print('3. Dungeon Master')
    dif = input(': ')
    print('>/=\\------------------/=\\<\n')

    if not dif.isdigit() or not 1 <= int(dif) <= 3:
        print('#*@>>>----------------------------------------<<<#*@')
        print('Эй, дружок пирожок, тобою выбрана неправильная дверь')
        print('#*@>>>----------------------------------------<<<#*@\n')
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

# Настройки игры
level = 1
room = 1
dif = int(dif)

# Еда
food = 0
food_up_hp = 75

def battle(): # Битва
    global hero_hp
    global slave_hp
    slave_hpb = slave_hp
    while hero_hp > 0 and slave_hpb > 0:
        # Твоя атака
        hero_damageb = random.randint(int(hero_damage*0.8),int(hero_damage*1.2)) # генерация значение урона
        slave_hpb -= hero_damageb
        print(f'===-----------{di(hero_damageb)}===')
        print(f'Вы нанесли {hero_damageb} урона')
        print(f'===-----------{di(hero_damageb)}===')
        input()

        # Атака врага
        if slave_hpb > 0:
            slave_damageb = random.randint(int(slave_damage*0.8),int(slave_damage* 1.2)) # генерация значение урона (У врага)
            hero_hp -= slave_damageb
            print(f'===------------{di(slave_damageb)}===')
            print(f'Вам нанесли {slave_damageb} урона')
            print(f'===------------{di(slave_damageb)}===')
            input()

def di(a): # Палочки делают wee wee
    return len(str(a)) * '-'

while level != 100:
    print(f'<-------{di(level)}>')
    print(f'Уровень: {level}')
    print(f'<-------{di(level)}>\n')
    if level % 30 == 0:
        food_up_hp += 25
        print(f'-=1#@^------------------------------^@#1=-')
        print('Восстановления здоровье от еды увеличилось')
        print(f'Здоровье от еды: {food_up_hp - 25} > {food_up_hp}')
        print(f'-=1#@^------------------------------^@#1=-\n')
    while room != 10:
        a = random.randrange(1, 10)
        if a == 1:
            print('*&^#----------#^&*')
            print('Slave напал на вас')
            input('*&^#----------#^&*\n')
            slave_hpb = random.randint(int(slave_hp*0.80),int(slave_hp*1.2))
            battle()

            # Конец битвы
            if hero_hp > 0: # Выигрыш
                slave_counter += 1

                # Прокачка здоровье
                if dif == 1:
                    hp = random.randint(10,24)
                elif dif == 2:
                    hp = random.randint(10,30)
                else:
                    hp = random.randint(10,36)
                hero_max_hp += hp
                print(f'^&---------------{di(hero_max_hp - hp) + di(hero_max_hp)}&^')
                print('Вы победили!\n')
                print(f'Макс. здоровье: {hero_max_hp - hp} > {hero_max_hp}') # Макс. здоровье
                print(f'Здоровье: {hero_hp}\n')

                # Прокачка урона
                if dif == 1:
                    a = random.randint(3,9)
                elif dif == 2:
                    a = random.randint(3,10)
                else:
                    a = random.randint(4,12)
                hero_damage += a
                print(f'Сред. урон: {hero_damage - a} > {hero_damage}') # Сред. урон
                print(f'^&---------------{di(hero_max_hp - hp) + di(hero_max_hp)}&^')
                input()
            
            else: # Проигрыш
                print('Умер от slave...\n')
                exit()
        
        a = random.randint(1,20) # Шансы на сундук
        if a <= 3:
            foodr = random.randint(1,3) 
            a = random.randint(1,4) # Шансы на +здоровье
            print('$#$----------------------$#$')
            print('Вы нашли deep dark fantasies')
            print(f'+еда: {foodr}')
            food += foodr
            if a == 1:
                a = random.randint(80,150)
                print(f'+здоровье: {a}')
                if hero_hp + a >= hero_max_hp:
                    hero_hp = hero_max_hp
                else:
                    hero_hp += a
            print('$#$----------------------$#$\n')

        passages = random.randint(1,4) # сколько всего будет дверей в комнате
        a = ''
        while not str(a).isdigit() or int(a) > passages:
            if room != 9: # Дверь
                print(f'У вас всего {passages} DOOR') 
                a = input(': ')
                print()

            else: # Проход вниз
                print(f'У вас всего {passages} ANAL')
                a = input(': ')
                print()

            if not a.isdigit() or int(a) > passages and not 5 <= int(a) <= 7: # Защита от дурака
                print('#*@>>>----------------------------------------<<<#*@')
                print('Эй, дружок пирожок, тобою выбрана неправильная дверь')
                print('#*@>>>----------------------------------------<<<#*@\n')

            else:
                a = int(a)

            if a == 5: # Есть еду
                if food == 0: # Нет еды
                    print('@=^-------@-^')
                    print('У вас нет еды')
                    print('@=^-------@-^\n')
                elif hero_hp != hero_max_hp:
                    food -= 1
                    if hero_hp + food_up_hp >= hero_max_hp: # Вы съели еду, но hero_hp + food_up_hp >= hero_max_hp
                        print(f'&^*----------------------------{di(hero_hp) + di(hero_max_hp)}&^*')
                        print(f'SUCK SOME DICK. Ваше здоровье: {hero_hp} > {hero_max_hp}')
                        print(f'&^*----------------------------{di(hero_hp) + di(hero_max_hp)}&^*\n')
                        hero_hp = hero_max_hp
                    else: # Вы съели еду
                        hero_hp += food_up_hp
                        print(f'&^*----------------------------{di(hero_hp - food_up_hp) + di(hero_hp)}&^*')
                        print(f'SUCK SOME DICK. Ваше здоровье: {hero_hp - food_up_hp} > {hero_hp}')
                        print(f'&^*----------------------------{di(hero_hp - food_up_hp) + di(hero_hp)}&^*\n')
                else: # Здоровье заполнено
                    print('^^#------------------#^^')
                    print('Wee wee и так достаточно')
                    print('^^#------------------#^^\n')

            elif a == 6: # Информация и статистика
                print(f'#^&*=-------------{di(slave_counter)}=&^#')
                print('Уровень:', level)
                print(f'{room}-ая комната из 9')
                print(f'Здоровье: {hero_hp}')
                print(f'Макс. здоровье: {hero_max_hp}')
                print(f'Сред. урон: {hero_damage}')
                print(f"Всего одолено '{slave_counter}' slave")
                print(f'#^&*=-------------{di(slave_counter)}=&^#\n')

            elif a == 7: # Инвентарь
                if food != 0: # Ну хотя бы инвентарь не пустой 
                    print(f'<^-{di(food)}^>')
                    print(f'Еда: {food}')
                    print(f'<^-{di(food)}^>\n')
                else: # Инвентарь пуст
                    print('^*><--------------------><*^')
                    print('В инвентаре даже cum нету...')
                    print('^*><--------------------><*^\n')

        room += 1
    level += 1
    room = 1

    # Прокачка врагов
    if dif == 1:
        slave_hp = int(295 * (1 + level * slave))
        slave_damage = int(11 * (1 + level * slave))
    elif dif == 2:
        slave_hp = int(330 * (1 + level * slave))
        slave_damage = int(15 * (1 + level * slave))
    else:
        slave_hp = int(350 * (1 + level * slave))
        slave_damage = int(20 * (1 + level * slave))

if level == 100:
    print('похоже вы петеряли еду...')
    for i in range(15): # Коридор
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
    if hero_hp <= 0: # Ну идиот, здохнуть в конце это надо уметь
        print('Master умер...')
        exit()

    print('#-------------------------#')
    print('Вы одалели dungeon master-а')
    print('#-------------------------#')
    input()
    print('*-----------------*')
    print('+пропуск на fisting') 
    print('*-----------------*')
    input()
    print('()====================------------------------------------===================()')
    print("Один из FUCKING SLAVE записал начало битвы: youtube.com/watch?v=johcE5s525M")
    print('()====================------------------------------------===================()\n')