#name: malachi
#russian roulette

import random
bullet = int(input("how many bullets:"))
bullet1, bullet2, bullet3, bullet4, bullet5, bullet6 = random.sample(range(1, 7), 6)
Bullet_placement = random.randint(1, 6)
if bullet == 1:
    print(Bullet_placement)
    print(bullet1)
    if Bullet_placement == bullet1:
        print("you died")
    else:
        print("you survived")
elif bullet == 2:
    print(Bullet_placement)
    print(bullet1,bullet2)
    if Bullet_placement in (bullet1, bullet2):
        print("you died")
    else:
        print("you survived")
elif bullet == 3:
    print(Bullet_placement)
    print(bullet1,bullet2,bullet3)
    if Bullet_placement in (bullet1, bullet2, bullet3):
        print("you died")
    else:
        print("you survived")
elif bullet == 4:
    print(Bullet_placement)
    print(bullet1,bullet2,bullet3,bullet4)
    if Bullet_placement in (bullet1, bullet2, bullet3, bullet4):
        print("you died")
    else:
        print("you survived")
elif bullet == 5:
    print(Bullet_placement)
    print(bullet1,bullet2,bullet3,bullet4,bullet5)
    if Bullet_placement in (bullet1, bullet2, bullet3, bullet4, bullet5):
        print("you died")
    else:
        print("you survived")
elif bullet == 6:
    print(Bullet_placement)
    print(bullet1,bullet2,bullet3,bullet4,bullet5,bullet6)
    if Bullet_placement in (bullet1, bullet2, bullet3, bullet4, bullet5, bullet6):
        print("you died")
