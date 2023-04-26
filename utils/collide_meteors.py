from constants.dimensions import height
from constants.images import meteors_img
from constants.sounds import sounds

def collide_meteors(meteors, player, score_list):
    for meteor in meteors:
        meteor.y += meteor.vel
        if player.colliderect(meteor):
            sounds['hit_sound'].play()
            player.health -= 3
            meteors.remove(meteor)
        elif meteor.y > height.get("screen"):
            meteors.remove(meteor)
        for bullet in player.bullets:
            if bullet.colliderect(meteor):
                if meteor.type == 'brown':
                    meteors.remove(meteor)
                    score[0] += 100
                else:
                    meteor.type = 'brown'
                    meteor.image = meteors_img.get("brown1")
                    score[0] += 100
                player.bullets.remove(bullet)