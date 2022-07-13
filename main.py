import random
import sys
import copy
from weapons import *
from enemies import *
from map import *
from sql_functions import *
from items import *
from story import *

class Player:
    name = ''
    level = 0
    exp = 0
    BodyPoint = 0
    DexterityPoint = 0
    HP = 0
    Weapon = None
    invertory = []

def inputCheck(n):
    while True:
        input_data = input("Введите число: ")
        if not input_data.isnumeric():
            print("Вы ввели не число. Попробуйте снова: ")
        elif not 1 <= int(input_data) <= n:
            print("Ваше ответ не в диапазоне. Попробуйте снова")
        else:
            break
    return int(input_data)

def inputCheckString(n):
    forbidden = [';', ',', ':', '"', "'"]
    while True:
        input_data = input('Введите текст: ')
        isExit = True
        for letter in input_data:
            if (letter in forbidden):
                print('Использованы запрещенные символы при вводе!')
                isExit = False
                break
        if not len(input_data) <= n:
            print('Введенный текст более', n, 'символов. Попробуйте снова')
            isExit = False
        if isExit == True:
            break
    return input_data
            
def heroCreator():
    print('Для начала Вам необходимо создать персонажа.')
    print('Введите имя вашего Героя.')
    player = Player()
    player.name = inputCheckString(16)
    player.BodyPoint = 1
    player.DexterityPoint = 1
    player.StrengthPoint = 1
    player.HP = 10 + player.BodyPoint
    print('\nВыберите тип оружия(введите цифру как ответ)\n 1. Кинжал\n 2. Меч\n 3. Топор')
    inputChoice = inputCheck(3)
    if inputChoice == 1:
        player.Weapon = copy.copy(dagger)
    elif inputChoice == 2:
        player.Weapon = copy.copy(sword)
    elif inputChoice == 3:
        player.Weapon = copy.copy(axe)
    print('\nВведите название вашего оружия.')
    player.Weapon.name = inputCheckString(32)
    print('\nВаш Герой:', player.name)
    print(' Телосложение:', player.BodyPoint, 'из 10.')
    print(' Ловкость:', player.DexterityPoint, 'из 10.')
    print(' Сила:', player.StrengthPoint, 'из 10.')
    print('\nВаше оружие', player.Weapon.weaponType, player.Weapon.name)
    print(' Урон:', player.Weapon.damage, 'очков')
    print(' Скорость атаки:', player.Weapon.speed, 'очков')
    return player

def battle(player, isBoss, floor):
    global currentEnemies
    if isBoss == False:
        enemy = copy.copy(random.choice(currentEnemies))
    elif isBoss == True:
        enemy = copy.copy(SQL_loadBoss())
    print('На вас напал', enemy.name)
    if player.DexterityPoint >= enemy.DexterityPoint:
        print('Вы быстрее противника')
        yourTurn = True
    else:
        print('Вы медленнее противника')
        yourTurn = False
    pattern_counter = 0
    defence = 0
    while True:
        if yourTurn == True:
            print('Твой ход:')
            print('Здоровье', player.name+':', player.HP)
            print('Здоровье', enemy.name+':', enemy.HP)
            print('Действие(введите цифру как ответ)\n 1. Атака\n 2. Защита\n 3. Анализ')
            inputChoice = inputCheck(3)
            if inputChoice == 1:
                damage = int(player.Weapon.damage * (player.Weapon.speed / 2))
                enemy.HP -= damage
                print('Вы нанесли врагу', int(player.Weapon.speed / 2), 'удара оружием', player.Weapon.weaponType, player.Weapon.name+'.', 'Итого урона:', int(damage))
                if enemy.HP <= 0:
                    print('Вы убили врага!')
                    player.exp += 1
                    print('Вы получили опыта: 1')
                    if player.exp == 3:
                        player = levelUP(player)
                        player.exp = 0
                    print('')
                    break
            elif inputChoice == 2:
                defence += int(player.BodyPoint/2)
                print('В следующем ходу противника Вам нанесут меньше урона:', -defence)
            elif inputChoice == 3:
                print('Урон противника:', enemy.Damage)
                print('Ловкость противника:', enemy.DexterityPoint)
                print('Описание противника:', enemy.Descryption)
            print('')
            yourTurn = False
        else:
            print('Ход противника:')
            print('Здоровье', player.name+':', player.HP)
            print('Здоровье', enemy.name+':', enemy.HP)
            if enemy.Attack_Pattern[pattern_counter] == 1:
                total_damage = int((enemy.Damage * (enemy.speed / 2)) - defence)
                defence = 0
                if total_damage < 0:
                    total_damage = 0
                print('Враг нанес вам', int(enemy.speed / 2), 'удара оружием', enemy.Weapon_type, enemy.Weapon_name+'.', 'Итого урона:', total_damage)
                player.HP -= total_damage
                defence = 0
                if player.HP <= 0:
                    SQL_insertDead(player, floor)
                    tellAStory(ending_loose)
                    print('Герой умер. Нажмите Enter, чтобы завершить программу.')
                    input('')
                    sys.exit(0)
            elif enemy.Attack_Pattern[pattern_counter] == 0:
                print(enemy.name, 'не атакует')
            pattern_counter += 1
            if pattern_counter == 3:
                pattern_counter = 0
            print('')
            yourTurn = True
    return player

def workbench(player):
    print('Здесь вы можете улучшить один из параметров своего оружия на 1 очко.')
    print('Выберите параметр:\n 1. Урон\n 2. Скорость атаки')
    inputChoice = inputCheck(2)
    if inputChoice == 1:
        player.Weapon.damage += 1
        print('Урон вашего оружия '+player.Weapon.name+' улучшен на 1 очко. Итого: '+str(player.Weapon.damage))
    if inputChoice == 2:
        player.Weapon.speed += 1
        print('Скорость атаки вашего оружия '+player.Weapon.name+' улучшена на 1 очко. Итого: '+str(player.Weapon.speed))
    input('Нажмите Enter, чтобы продолжить')
    return player

def chest(player):
    print('В попали в комнату с сундуком.')
    random_number = random.randint(0, 2)
    if random_number == 0:
        item = random.choice(items)
        print('В сундуке вы нашли', item.name)
        if len(player.invertory) > 6:
            print('В инвентаре Вы не можете носить более 6 предметов. Использовать сейчас или выкинуть?\n 1.Использовать сейчас\n 2. Выкинуть')
            inputChoice = inputCheck(2)
            if inputChoice == 1:
                player.HP += item.recovery
                if player.HP > player.BodyPoint + 10:
                    player.HP = player.BodyPoint + 10
                print('Ваше Здоровье:', player.HP)   
        else:
            player.invertory.append(item) 
            print('Предмет добавлен в инвентарь.')
    elif random_number == 1:
        print('В сундуке вы нашли Зелье Опыта(+1 к Опыту)')
        player.exp += 1
        if player.exp == 3:
            player = levelUP(player)
            player.exp = 0
    elif random_number == 2:
        global currentWeapons
        random_weapon = random.choice(currentWeapons)
        print('В сундуке лежит оружие', random_weapon.weaponType, random_weapon.name)
        print(' Урон:', random_weapon.damage)
        print(' Скорость:', random_weapon.speed)
        print('Вы готовы взять оружие?')
        print('Ответ:\n 1. Да\n 2. Нет')
        inputChoice = inputCheck(2)
        if inputChoice == 1:
            player.Weapon = random_weapon
            print('Вы взяли оружие')
        if inputChoice == 2:
            return player
    print('Нажмите Enter, чтобы продолжить')
    input('')
    print('')
    return player

def levelUP(player):
    player.level += 1
    print('Ваш уровень:', player.level, '!!!')
    print('Вы сможете улучшить один из своих параметров.')
    print('Выберите параметр:\n 1. Телосложение\n 2. Ловкость')
    inputChoice = inputCheck(2)
    if inputChoice == 1:
        player.BodyPoint += 1
        if player.BodyPoint > 10:
            player.BodyPoint = 10
        print('Добавлено 1 очка к Телосложению. Итог:', player.BodyPoint)
    elif inputChoice == 2:
        player.DexterityPoint += 1
        if player.DexterityPoint > 10:
            player.DexterityPoint = 10
        print('Добавлено 1 очка к Ловкости. Итог:', player.DexterityPoint)
    player.HP = 10 + player.BodyPoint
    print('Восполнено здоровье')
    print('')
    return player

def enviromentCheck(x, y):
    global currentFloor
    print('1. Север: ', end='')
    if currentFloor[x-1][y] == 0:
        print('пустая клетка')
    elif currentFloor[x-1][y] == 1:
        print('стена')
    elif currentFloor[x-1][y] == 2:
        print('верстак')
    elif currentFloor[x-1][y] == 3:
        print('сундук')
    elif currentFloor[x-1][y] == 4:
        print('лестница наверх')
    elif currentFloor[x-1][y] == 5:
        print('босс')
    print('2. Юг: ', end='')
    if currentFloor[x+1][y] == 0:
        print('пустая клетка')
    elif currentFloor[x+1][y] == 1:
        print('стена')
    elif currentFloor[x+1][y] == 2:
        print('верстак')
    elif currentFloor[x+1][y] == 3:
        print('сундук')
    elif currentFloor[x+1][y] == 4:
        print('лестница наверх')
    elif currentFloor[x+1][y] == 5:
        print('босс')
    print('3. Запад: ', end='')
    if currentFloor[x][y-1] == 0:
        print('пустая клетка')
    elif currentFloor[x][y-1] == 1:
        print('стена')
    elif currentFloor[x][y-1] == 2:
        print('верстак')
    elif currentFloor[x][y-1] == 3:
        print('сундук')
    elif currentFloor[x][y-1] == 4:
        print('лестница наверх')
    elif currentFloor[x][y-1] == 5:
        print('босс')
    print('4. Восток: ', end='')
    if currentFloor[x][y+1] == 0:
        print('пустая клетка')
    elif currentFloor[x][y+1] == 1:
        print('стена')
    elif currentFloor[x][y+1] == 2:
        print('верстак')
    elif currentFloor[x][y+1] == 3:
        print('сундук')
    elif currentFloor[x][y+1] == 4:
        print('лестница наверх')
    elif currentFloor[x][y+1] == 5:
        print('босс')

def playerMove(coordinates, direction):
    global currentFloor
    if direction == 1:
        if currentFloor[coordinates[0]-1][coordinates[1]] == 1:
            print('Вы не можете ходить в стену!')
            return False, coordinates
        coordinates[0] -= 1
    elif direction == 2:
        if currentFloor[coordinates[0]+1][coordinates[1]] == 1:
            print('Вы не можете ходить в стену!')
            return False, coordinates
        coordinates[0] += 1
    elif direction == 3:
        if currentFloor[coordinates[0]][coordinates[1]-1] == 1:
            print('Вы не можете ходить в стену!')
            return False, coordinates
        coordinates[1] -= 1
    elif direction == 4:
        if currentFloor[coordinates[0]][coordinates[1]+1] == 1:
            print('Вы не можете ходить в стену!')
            return False, coordinates
        coordinates[1] += 1
    return True, coordinates

def printMap():
    global currentFloor, playerCoordinates
    print('На карте отображено Ваше положение и расположение стен:')
    for i in range(len(currentFloor)):
        for j in range(len(currentFloor[0])):
            if currentFloor[i][j] == 1:
                print('■', end='')
            elif i == playerCoordinates[0] and j == playerCoordinates[1]:
                print('P', end='')
            else:
                print('□', end='')
        print('')
    print('Нажмите Enter, чтобы продолжить')
    input()

def invertory(player):
    print('Ваш инвентарь:')
    if player.invertory == []:
        print(' Пусто')
        return player
    else:
        for i in range(len(player.invertory)):
            print(' '+str(i+1)+'. '+player.invertory[i].name)
        print(' '+str(len(player.invertory)+1)+'. Выход')
        print('Выберите, что хотите использовать или выход')
        inputChoice = inputCheck(len(player.invertory)+1)
        if inputChoice == len(player.invertory)+1:
            return player
        else:
            print('Вы использовали', player.invertory[inputChoice-1].name)
            player.HP += player.invertory[inputChoice-1].recovery
            if player.HP > player.BodyPoint + 10:
                player.HP = player.BodyPoint + 10
            print('Ваше Здоровье:', player.HP)
            del player.invertory[inputChoice-1]
    return player

def playerActions(player):
    isExit = False
    while isExit == False:
        print("\nВы желаете сделать что-то перед тем, как продолжить ваш путь?")
        print('Выберите действие:\n 1. Посмотреть карту\n 2. Посмотреть инвентарь\n 3. Посмотреть характеристики\n 4. Ничего (продолжить движение)')
        inputChoice = inputCheck(4)
        if inputChoice == 1:
            printMap()
        elif inputChoice == 2:
            player = invertory(player)
        elif inputChoice == 3:
            print(player.name)
            print('Телосложение:', player.BodyPoint, 'из 10')
            print('Ловкость:', player.DexterityPoint, 'из 10')
            print('Здоровье:', player.HP, 'из', player.BodyPoint+10)
            print('Уровень:', player.level)
            print('Количество опыта на этом уровне:', player.exp, 'из 3\n')
            print(player.Weapon.weaponType, player.Weapon.name)
            print('Урон:', player.Weapon.damage)
            print('Скорость атаки:', player.Weapon.speed)
            input('\nНажмите Enter, чтобы продолжить')
        elif inputChoice == 4:
            isExit = True
    return player

print('Simple Dungeon Crawler v2.0')
tellAStory(starting)
print('Просмотреть обучение? \n 1. Да \n 2. Нет')
inputChoice = inputCheck(2)
if inputChoice == 1:
    tellAStory(tutorial)
player = heroCreator()
currentFloor = tower[0]
floorCounter = 1
currentRandom = random_events[0]
currentWeapons = SQL_loadWeapons(floorCounter)
currentEnemies = SQL_loadEnemies(floorCounter)
playerCoordinates = [8, 1]
while True:
    if currentFloor[playerCoordinates[0]][playerCoordinates[1]] == 0:
        event = random.choice(currentRandom)
        if event == 0:
            print('\n!Пустая клетка!')
        if event == 1:
            print('\n!Битва!')
            player = battle(player, False, floorCounter)
        if event == 2:
            print('\n!Находка!')
            player = chest(player)
    elif currentFloor[playerCoordinates[0]][playerCoordinates[1]] == 2:
        print('\n!Верстак!')
        player = workbench(player)
        currentFloor[playerCoordinates[0]][playerCoordinates[1]] = 0
    elif currentFloor[playerCoordinates[0]][playerCoordinates[1]] == 3:
        print('\n!Сундук!')
        player = chest(player)
        currentFloor[playerCoordinates[0]][playerCoordinates[1]] = 0
    elif currentFloor[playerCoordinates[0]][playerCoordinates[1]] == 4:
        print('\n!Лестница!')
        print('\nВы поднимаетесь на этаж выше...')
        currentRandom = random_events[floorCounter]
        currentFloor = tower[floorCounter]
        floorCounter += 1
        currentWeapons = SQL_loadWeapons(floorCounter)
        currentEnemies = SQL_loadEnemies(floorCounter)
        print('Вы на', floorCounter, 'этаже')
    elif currentFloor[playerCoordinates[0]][playerCoordinates[1]] == 5:
        print('\n!Финал!')
        player = battle(player, True, floorCounter)
        SQL_updateBoss(player, floorCounter)
        tellAStory(ending_win)
        break
    player = playerActions(player)
    print(playerCoordinates)
    enviromentCheck(playerCoordinates[0], playerCoordinates[1])
    isMoveMade = False
    while isMoveMade == False:
        print('Выберите путь')
        inputChoice = inputCheck(4)
        isMoveMade, playerCoordinates = playerMove(playerCoordinates, inputChoice)
print('Вы прошли игру! Нажмите Enter, чтобы завершить программу')
input('')
