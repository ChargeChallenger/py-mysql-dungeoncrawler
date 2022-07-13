from mysql.connector import MySQLConnection, Error
from weapons import *
from enemies import *

def SQL_loadWeapons(floor):
    print('Загрузка оружия...')
    current_weapons = []
    if floor == 1:
        quary = 'SELECT * FROM weapons WHERE weapon_floor = 1'
    elif floor == 2:
        quary = 'SELECT * FROM weapons WHERE weapon_floor = 2'
    elif floor == 3:
        quary = 'SELECT * FROM weapons WHERE weapon_floor = 3'
    try:
        conn = MySQLConnection(host='localhost', database='dungeon', user='root', password='root')
        cursor = conn.cursor()
        cursor.execute(quary)
        row = cursor.fetchone()
        iteration = 0
        while row is not None:
            current_weapons.append(Weapon())
            current_weapons[iteration].weaponType = row[1]
            current_weapons[iteration].name = row[2]
            current_weapons[iteration].damage = row[3]
            current_weapons[iteration].speed = row[4]
            iteration += 1
            row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        conn.close()
    print('Оружие загружено!')
    return current_weapons

def SQL_loadEnemies(floor):
    print('Загрузка противников...')
    current_enemies = []
    if floor == 1:
        quary = 'SELECT enemies.enemy_name, enemies.enemy_body, enemies.enemy_dexterity, weapons.weapon_type, weapons.weapon_name, weapons.weapon_damage, weapons.weapon_speed FROM enemies,weapons WHERE enemies.id_weapon=weapons.id_weapon AND floor_number = 1'
    elif floor == 2:
        quary = 'SELECT enemies.enemy_name, enemies.enemy_body, enemies.enemy_dexterity, weapons.weapon_type, weapons.weapon_name, weapons.weapon_damage, weapons.weapon_speed FROM enemies,weapons WHERE enemies.id_weapon=weapons.id_weapon AND floor_number = 2'
    elif floor == 3:
        quary = 'SELECT enemies.enemy_name, enemies.enemy_body, enemies.enemy_dexterity, weapons.weapon_type, weapons.weapon_name, weapons.weapon_damage, weapons.weapon_speed FROM enemies,weapons WHERE enemies.id_weapon=weapons.id_weapon AND floor_number = 3'
    try:
        conn = MySQLConnection(host='localhost', database='dungeon', user='root', password='root')
        cursor = conn.cursor()
        cursor.execute(quary)
        row = cursor.fetchone()
        iteration = 0
        while row is not None:
            current_enemies.append(Enemy())
            current_enemies[iteration].name = row[0]
            current_enemies[iteration].HP = row[1] + 7
            current_enemies[iteration].DexterityPoint = row[2]
            current_enemies[iteration].Weapon_type = row[3]
            current_enemies[iteration].Weapon_name = row[4]
            current_enemies[iteration].Damage = row[5]
            current_enemies[iteration].speed = row[6]
            if current_enemies[iteration].Weapon_type == 'Кинжал':
                current_enemies[iteration].Attack_Pattern = dagger_attack_pattern
                current_enemies[iteration].Descryption = 'Противник первый ход готовится к удару, бьёт и готовится два хода'
            elif current_enemies[iteration].Weapon_type == 'Меч':
                current_enemies[iteration].Attack_Pattern = sword_attack_pattern
                current_enemies[iteration].Descryption = 'Противник дважды атакует, затем отдыхает'
            elif current_enemies[iteration].Weapon_type == 'Топор':
                current_enemies[iteration].Attack_Pattern = axe_attack_pattern
                current_enemies[iteration].Descryption = 'Противник атакует, отдыхает и снова атакует'
            iteration += 1
            row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        conn.close()
    print('Противники загружены!')
    return current_enemies

def SQL_loadBoss():
    print('Загрузка босса...')
    try:
        conn = MySQLConnection(host='localhost', database='dungeon', user='root', password='root')
        cursor = conn.cursor()
        cursor.execute('SELECT bosses.boss_name, bosses.boss_body, bosses.boss_dexterity, weapons.weapon_type, weapons.weapon_name, weapons.weapon_damage, weapons.weapon_speed FROM bosses,weapons WHERE bosses.id_weapon=weapons.id_weapon AND bosses.is_dead = "no"')
        row = cursor.fetchone()
        boss = Enemy()
        boss.name = row[0]
        boss.HP = row[1] + 15
        boss.DexterityPoint = row[2]
        boss.Weapon_type = row[3]
        boss.Weapon_name = row[4]
        boss.Damage = row[5]
        boss.speed = row[6]
        if boss.Weapon_type == 'Кинжал':
            boss.Attack_Pattern = dagger_attack_pattern
            boss.Descryption = 'Противник первый ход готовится к удару, бьёт и готовится два хода'
        elif boss.Weapon_type == 'Меч':
            boss.Attack_Pattern = sword_attack_pattern
            boss.Descryption = 'Противник дважды атакует, затем отдыхает'
        elif boss.Weapon_type == 'Топор':
            boss.Attack_Pattern = axe_attack_pattern
            boss.Descryption = 'Противник атакует, отдыхает и снова атакует'
    except Error as e:
        print(e)
    finally:
        conn.close()
    print('Босс загружен!')
    return boss

def SQL_insertDead(player, floor):
    print('Загрузка души...')
    try:
        conn = MySQLConnection(host='localhost', database='dungeon', user='root', password='root')
        cursor1 = conn.cursor()
        quary = 'insert into weapons(weapon_type, weapon_name, weapon_damage, weapon_speed, weapon_floor) values (%s, %s, %s, %s, %s)'
        values = (player.Weapon.weaponType, player.Weapon.name, player.Weapon.damage, player.Weapon.speed, floor)
        cursor1.execute(quary, values)
        conn.commit()
        quary = 'select id_weapon from weapons where weapon_type = %s and weapon_name = %s and weapon_damage = %s and weapon_speed = %s and weapon_floor = %s'
        cursor1.execute(quary, values)
        row = cursor1.fetchone()
        weapon_id = row[0]
        cursor2 = conn.cursor()
        quary = 'insert into enemies(enemy_name, enemy_body, enemy_dexterity, id_weapon, floor_number) values (%s, %s, %s, %s, %s)'
        values = (player.name, player.BodyPoint, player.DexterityPoint, weapon_id, floor)
        cursor2.execute(quary, values)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()
    print('Душа загружена!')

def SQL_updateBoss(player, floor):
    print('Загрузка души...')
    try:
        conn = MySQLConnection(host='localhost', database='dungeon', user='root', password='root')
        cursor1 = conn.cursor()
        quary = 'update bosses set is_dead = "yes"'
        cursor1.execute(quary)
        conn.commit()
        quary = 'insert into weapons(weapon_type, weapon_name, weapon_damage, weapon_speed, weapon_floor) values (%s, %s, %s, %s, %s)'
        values = (player.Weapon.weaponType, player.Weapon.name, player.Weapon.damage, player.Weapon.speed, floor)
        cursor1.execute(quary, values)
        conn.commit()
        quary = 'select id_weapon from weapons where weapon_type = %s and weapon_name = %s and weapon_damage = %s and weapon_speed = %s and weapon_floor = %s'
        cursor1.execute(quary, values)
        row = cursor1.fetchone()
        weapon_id = row[0]
        cursor2 = conn.cursor()
        quary = 'insert into bosses(boss_name, boss_body, boss_dexterity, id_weapon, is_dead) values (%s, %s, %s, %s, "no")'
        values = (player.name, player.BodyPoint, player.DexterityPoint, weapon_id)
        cursor2.execute(quary, values)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()
    print('Душа загружена!')
