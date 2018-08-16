
import random

first = True

def player_stats():
    global player_hp_defence
    global player_attacks
    global enemy_turn
    global enemy_hp_defence
    hp_defence = []
    player_attacks=[]
    my_level=int(input("which level of difficulty to do you want?\nfor easy type 1\nfor medium type 2\nfor hard type 3\n"))
    #while my_level != type(int):
        #player_stats()
    if my_level == 1:
        hp = 50
        defence = 35
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_1= 10
        attack_2 = 5
        player_attacks.append(attack_1)
        player_attacks.append(attack_2)
        ability_player = 5
        player_attacks.append(ability_player)

    if my_level == 2:
        hp = 30
        defence = 20
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_1 = 7
        attack_2 = 3
        player_attacks.append(attack_1)
        player_attacks.append(attack_2)
        ability_player = 5
        player_attacks.append(ability_player)
    
    if my_level == 3:
        hp = 20
        defence = 10
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_1 = 4
        attack_2 = 1
        player_attacks.append(attack_1)
        player_attacks.append(attack_2)
        ability_player = 5
        player_attacks.append(ability_player)
    return player_attacks, hp_defence

def enemy_stats():
    global player_hp_defence
    global player_attacks
    global enemy_turn
    global enemy_hp_defence
    hp_defence = []
    enemy_attacks=[]
    his_level=int(input("which level of difficulty do you want your enemy to be?\nfor easy type 1\nfor medium type 2\nfor hard type 3\n"))
    #while his_level != type(int):
        #player_stats()
    if his_level == 1:
        hp = 15
        defence = 8
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 3
        attack_two = 1
        enemy_attacks.append(attack_one)
        enemy_attacks.append(attack_two)
        ability_enemy = 4
        enemy_attacks.append(ability_enemy)

    if his_level == 2:
        hp = 25
        defence = 18
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 7
        attack_two = 3
        enemy_attacks.append(attack_one)
        enemy_attacks.append(attack_two)
        ability_enemy = 4
        enemy_attacks.append(ability_enemy)
    
    if his_level == 3:
        hp = 45
        defence = 30
        hp_defence.append(hp)
        hp_defence.append(defence)
        attack_one = 12
        attack_two = 8
        enemy_attacks.append(attack_one)
        enemy_attacks.append(attack_two)
        ability_enemy = 4
        enemy_attacks.append(ability_enemy)
    return enemy_attacks, hp_defence

def player_game(enemy_turn):
    global player_hp_defence
    global player_attacks
    global enemy_hp_defence
    global enemy_attacks
##    turn=( , )
    global first
    if not first:
        if enemy_turn[0] == 'ability':
            player_hp_defence[1] -= enemy_turn[1]
            print(player_hp_defence[1])
        elif enemy_turn[0] == 'attack less power':
            player_hp_defence[0] -= enemy_turn[1]
            print('The enemy took you down to '+str(player_hp_defence[0])+' health')
        elif enemy_turn[0] == 'attack power':
            player_hp_defence[0] -= enemy_turn[1] - (enemy_turn[1]/100)*15
            print(player_hp_defence[0])
        else:
            print('ass')
            quit()
            
    choice = input("What Would you like to do?\nTo choose attack type'attack'\nTo use ability type'ability'\nTo run type'run'\n")
    choice.lower()
    while choice != 'attack' and choice != 'ability' and choice != 'run':
        print('Try again')
        choice =input("What Would you like to do?\nTo choose attack type'attack'\nTo use ability type'ability'\nTo run type'run'\n")
        choice.lower()
        
    if(choice == 'attack'):
        attack_choice = input("To choose a powerfull attack that is affected by defence type'power'\nTo choose a less is not affected by defence type'less power'\n")
        attack_choice.lower()
        while attack_choice != 'less power' and attack_choice != 'power' :
            print('Try again')
            attack_choice =input("To choose a powerfull attack that is affected by defence type'power'\nTo choose a less is not affected by defence type'less power'\n")
            attack_choice.lower()
        print(attack_choice)
        if attack_choice == 'power':
            player_turn = "attack power",player_attacks[0]
        elif(attack_choice =='less power'):
            player_turn = "attack less power" , player_attacks[1]
    elif choice == 'ability':
        player_turn = "ability" , player_attacks[2]
    elif(choice == 'run'):
        print('2ass')
        exit()
    first = False
    return player_turn



def enemy_game(player_turn):
    global player_hp_defence
    global player_attacks
    global enemy_hp_defence
    global enemy_attacks
    ran = random.randint(1,3)

    if ran == 1 or ran == 2:
        if player_turn[0] == 'ability':
            enemy_hp_defence[1] -= player_turn[1]
            print(enemy_hp_defence[1])
        elif player_turn[0] == 'attack less power':
            enemy_hp_defence[0] -= player_turn[1]
            print(enemy_hp_defence[0])
        elif player_turn[0] == 'attack power':
            enemy_hp_defence[0] -= player_turn[1]
            print('You took the enemy dow to '+str(enemy_hp_defence[0])+' health')
        else:
            print(player_turn)
            #its qutting it here
            print('1ass')
            quit()
    else:
        print('The enemy has doged you attack')
    if (changing_def >=  player_hp_defence[1]/2):
        rand_abi_latt = random.randint(1,4)
        if rand_abi_latt == 1:
            enemy_turn_be = 'ability', enemy_attacks[2]
        elif rand_abi_latt == 2 or rand_abi_latt == 3:
            enemy_turn_be = 'attack less power', enemy_attacks[1]
        elif rand_abi_latt == 4:
            enemy_turn_be = 'power attack' , enemy_attacks[0]
    else:
        enemy_turn_be = 'power attack' , enemy_attacks[0]
    print(enemy_turn_be)
    return enemy_turn_be
        

#print(enemy_game((10, 10), (10, 10), (5, 5, 5), ('attack power', 5)))       
    
#1/3 chance that the same move will not work for player

def main():
    global player_hp_defence
    global player_attacks
    global enemy_hp_defence
    global enemy_attacks
    enemy_turn  = []
    enemy_attacks, enemy_hp_defence  =  enemy_stats()
    player_attacks,player_hp_defence = player_stats()
    print(player_attacks)

    player_turn = player_game(enemy_turn)
    global changing_def
    changing_def = player_hp_defence[1]
    while player_hp_defence[0] >0 or enemy_hp_defence[0]:
        enemy_turn = enemy_game(player_turn)
        player_turn = player_game(enemy_turn)
        

            
            

main()
        
        
