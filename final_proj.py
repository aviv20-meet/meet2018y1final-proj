import turtle
import time
turtle.tracer(1,0)
turtle.register_shape('bg.gif')
turtle.bgpic("bg.gif")
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

enemy_health.penup()
enemy_health.color('white')
enemy_health.goto(180,25)
enemy_health.pendown()
enemy_health.write("hp", font= ("impact" ,20))
enemy_health.hideturtle()


enemy_defence.penup()
enemy_defence.color('white')
enemy_defence.goto(180,-5)
enemy_defence.pendown()
enemy_defence.write("defence", font= ("impact" ,20))
enemy_defence.hideturtle()



player_health.penup()
player_health.color('white')
player_health.goto(-230,160)
player_health.pendown()
player_health.write("hp", font= ("impact" ,20))
player_health.hideturtle()


player_defence.penup()
player_defence.color('white')
player_defence.goto(-230,130)
player_defence.pendown()
player_defence.write("defence", font= ("impact" ,20))
player_defence.hideturtle()




def power_attack(x,y):
    player_des = ('Power Attack')
    print('power attack')

def lesser_attack(x,y):
    player_des = ('Lesser Attack')

def ability_f(x,y):
    player_des = ('Ability')

def run_f(x,y):
    player_des = ('Run')
    lines.write('You are a COWARD!!!',font = ('impact',100, 'normal'))
    time.sleep(3)
    
    quit()



pattack.onclick(power_attack)
lattack.onclick(lesser_attack)
ability.onclick(ability_f)
run.onclick(run_f)











