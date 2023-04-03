from constants.velocities import velocities
from constants.dimensions import height

def handle_meteors(meteors, player):
    for meteor in meteors:
        meteor.y += velocities.get("meteor")
        if player.colliderect(meteor):
            player.health -= 3
            meteors.remove(meteor)
        elif meteor.y > height.get("screen"):
            meteors.remove(meteor)
        for bullet in player.bullets:
            if bullet.colliderect(meteor):
                meteors.remove(meteor)
                player.bullets.remove(bullet)