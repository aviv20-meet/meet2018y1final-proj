import turtle
import time
import random
turtle.tracer(1,0)
turtle.register_shape('bg.gif')
turtle.bgpic("bg.gif")
you_won = turtle.clone()
you_won.color('orange')
lines = turtle.clone()
lines.penup()
lines.hideturtle()
##turtle.hideturtle()
lines.goto(0,300)
lines.pendown()
lines.color('white')
lines.write("Clairdan Saving The Environment!" , align = 'center', font= ('impact', 30, "normal"))
lines.penup()
lines.goto(0,350)
lines.pendown()
lines.goto(470,350)
lines.goto(470,-350)
lines.goto(-470,-350)
lines.goto(-470,350)
lines.goto(0,350)


SIZE_X=700
SIZE_Y=400
turtle.setup(1000, 1000)
turtle.register_shape("clairdan.gif")
turtle.register_shape("clairdan_back.gif")
turtle.register_shape("enemy.gif")



clairdan = turtle.clone()
enemy = turtle.clone()
run = turtle.clone()
ability = turtle.clone()
lattack = turtle.clone()
pattack = turtle.clone()
turtle.register_shape("pattack.gif")
turtle.register_shape("lattack.gif")
turtle.register_shape("ability.gif")
turtle.register_shape("run.gif")
enemy.shape("enemy.gif")
clairdan.shape("clairdan.gif")
run.shape("run.gif")
ability.shape("ability.gif")
lattack.shape("lattack.gif")
pattack.shape("pattack.gif")
run.penup()
pattack.penup()
lattack.penup()
ability.penup()
clairdan.penup()
enemy.penup()

clairdan.goto(-200,40)
enemy.goto(200,-80)
pattack.goto(-365,-250)
ability.goto(120,-250)
lattack.goto(-120,-250)
run.goto(365,-250)
enemy_health = turtle.clone()
player_health = turtle.clone()
enemy_defence = turtle.clone()
player_defence = turtle.clone()

##enemy_health.penup()
##enemy_health.color('white')
##enemy_health.goto(180,25)
##enemy_health.pendown()
##enemy_health.write('hp', font= ("impact" ,20))
##enemy_health.hideturtle()
##
##
##enemy_defence.penup()
##enemy_defence.color('white')
##enemy_defence.goto(180,-5)
##enemy_defence.pendown()
##enemy_defence.write("defence", font= ("impact" ,20))
##enemy_defence.hideturtle()


##
##player_health.penup()
##player_health.color('white')
##player_health.goto(-230,160)
##player_health.pendown()
##player_health.write("hp", font= ("impact" ,20))
##player_health.hideturtle()
##
##
##player_defence.penup()
##player_defence.color('white')
##player_defence.goto(-230,130)
##player_defence.pendown()
##player_defence.write("defence", font= ("impact" ,20))
##player_defence.hideturtle()



###################################################################################
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
    player_health.clear()
    enemy_health.clear()
    #enemy_deffence.clear()
    global player_hp_defence
    global player_attacks
    global enemy_hp_defence
    global enemy_attacks
    global first
    global choice
    enemy_health.penup()
    enemy_health.color('white')
    enemy_health.goto(180,25)
    enemy_health.pendown()
    enemy_health.write("hp "+str(enemy_hp_defence[0]), align = "center", font= ("impact" ,20))
    enemy_health.hideturtle()
    
    ##enemy_deffence.penup()
    #enemy_deffence.color('white')
    #enemy_deffence.goto(180,10)
    #enemy_deffence.pendown()
    #enemy_deffence.write("deffence "+str(enemy_hp_defence[1]), align = "center", font= ("impact" ,20))
    #enemy_deffence.hideturtle()
    

    player_health.penup()
    player_health.color('white')
    player_health.goto(-230,160)
    player_health.pendown()
    player_health.write("hp "+str(player_hp_defence[0]), font= ("impact" ,20))
    player_health.hideturtle()
    
    if not first:
        print(enemy_turn[0])
        if 'ability' in enemy_turn[0]:
            player_hp_defence[1] -= enemy_turn[1]
            print(player_hp_defence[1])
        elif  'less' in enemy_turn[0]:
            player_hp_defence[0] -= enemy_turn[1]
            print('The enemy took you down to '+str(player_hp_defence[0])+' health')
        elif 'power' in enemy_turn[0]:
            player_hp_defence[0] -= enemy_turn[1] - (enemy_turn[1]/100)*15
            print(player_hp_defence[0])
        elif 'run' in enemy_turn[0]:
            print('You quite and ran away')
            quit()
            
##    choice = input('what would toy like to do?\nto choose attack type "attack"\nto choose ability type "ability"\nto choose run type "run"')
##    choice.lower()
##    while choice != 'attack' and choice != 'ability' and choice != 'run':
##        print('Try again')
##        choice =input("What Would you like to do?\nTo choose attack type'attack'\nTo use ability type'ability'\nTo run type'run'\n")
##        choice.lower()
    choice_bool = False
    choice = None
    while choice == None:
        if pattack.onclick(power_attack):
                choice_bool = True
                print("hhhh")
                power_attack()
        if lattack.onclick(lesser_attack):
                choice_bool = True
                lesser_attack()
        if ability.onclick(ability_f):
                choice_bool = True
                ability_f()
        if run.onclick(run_f):
                choice_bool = True
                run_f()
    #choice = ''
    if ('attack' in choice):
##        attack_choice = input("To choose a powerfull attack that is affected by defence type'power'\nTo choose a less is not affected by defence type'less power'\n")
##        attack_choice.lower()
##        
##        while attack_choice != 'less power' and attack_choice != 'power' :
##            print('Try again')
##            attack_choice =input("To choose a powerfull attack that is affected by defence type'power'\nTo choose a less is not affected by defence type'less power'\n")
##            attack_choice.lower()
##        print('pow'+attack_choice)
        if  'power' in choice:
            player_turn = "attack power",player_attacks[0]
        elif('less' in choice):
            player_turn = "attack less power" , player_attacks[1]
    elif choice == 'ability':
        player_turn = "ability" , player_attacks[2]
    elif(choice == 'run'):
        print('2ass')
        exit()
    #print('this is the player turn var'+str(player_turn))
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
        elif player_turn[0] == 'attack less':
            enemy_hp_defence[0] -= player_turn[1]
            print(enemy_hp_defence[0])
        elif player_turn[0] == 'attack power':
            enemy_hp_defence[0] -= player_turn[1]
            print('You took the enemy dow to '+str(enemy_hp_defence[0])+' health')
        else:
            print('yo'+str(player_turn))
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
    print('what'+str(enemy_turn_be))
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
    print('ssssssssssssssssssss'+str(player_attacks))
    player_turn = player_game(enemy_turn)
    global changing_def
    changing_def = player_hp_defence[1]
    while player_hp_defence[0] !=0 and enemy_hp_defence[0] != 0:
        enemy_turn = enemy_game(player_turn)
        player_turn = player_game(enemy_turn)
        if(enemy_hp_defence[0] <0):
            you_won.write("YOU WON!" , align = 'center', font= ('impact', 180, "normal"))
            time.sleep(2)
            quit()

        if(player_hp_defence[0] < 0):
            you_won.write("YOU lost!" , align = 'center', font= ('impact', 50, "normal"))
            time.sleep(2)
            quit()
   
    
    

def power_attack(x,y):
    global choice
    choice = 'power attack'
    print("power attack")
def lesser_attack(x,y):
    global choice
    choice = 'less power attack'
    print('less power')

def ability_f(x,y):
    global choice
    choice = 'ability'
    print("ability")

def run_f(x,y):
    global choice
    chocie = 'run'
##     player_des = ('Run')
##     print('Run')
##     lines.write('You are a COWARD!!!',font = ('impact',100, 'normal'))
##     time.sleep(3)
##     return player_des
    quit()
    

def print_pattack(x,y):
    print('pattack')
    


#
##pattack.onclick(print_pattack)
##lattack.onclick(lesser_attack)
##ability.onclick(ability_f)
##run.onclick(run_f)
##




main()







