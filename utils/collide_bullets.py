from constants.dimensions import height
from constants.sounds import sounds

def collide_player_bullets(player, enemy_ship):
    for bullet in player.bullets:
        if enemy_ship.colliderect(bullet):
            player.bullets.remove(bullet)
        elif bullet.y < 0:
            player.bullets.remove(bullet)

def collide_enemy_bullets(player, enemy):
    for bullet in enemy.bullets:
        if player.colliderect(bullet):
            sounds['hit_sound'].play()
            player.health -= 1
            enemy.bullets.remove(bullet)
        elif bullet.y > height.get("screen"):
            enemy.bullets.remove(bullet)