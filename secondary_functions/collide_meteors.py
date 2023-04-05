from constants.dimensions import height
from constants.images import meteors_img

def collide_meteors(meteors, player):
    for meteor in meteors:
        meteor.y += meteor.vel
        if player.colliderect(meteor):
            player.health -= 3
            meteors.remove(meteor)
        elif meteor.y > height.get("screen"):
            meteors.remove(meteor)
        for bullet in player.bullets:
            if bullet.colliderect(meteor):
                if meteor.type == 'brown':
                    meteors.remove(meteor)
                else:
                    meteor.type = 'brown'
                    meteor.image = meteors_img.get("brown1")
                player.bullets.remove(bullet)