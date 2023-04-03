from constants.dimensions import height

def handle_player_bullets(player, enemy_ship):
    for bullet in player.bullets:
        if enemy_ship.colliderect(bullet):
            player.bullets.remove(bullet)
        elif bullet.y < 0:
            player.bullets.remove(bullet)

def handle_enemy_bullets(player, enemy):
    for bullet in enemy.bullets:
        if player.colliderect(bullet):
            player.health -= 1
            enemy.bullets.remove(bullet)
        elif bullet.y > height.get("screen"):
            enemy.bullets.remove(bullet)