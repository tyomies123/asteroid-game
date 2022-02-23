# Asteroid Game by tyomies123

### Info
A simple pygame project from 2019. You control a rocket in an arcade style game dodging and shooting at asteroids, using powerups and defeating enemy UFOs. 

On the right side of the screen, you can see your current health points, score and powerup ammo. Additionally when an enemy UFO appears, you can see its remaining health points. 

#### Controls
Move left and right with the corresponding arrow keys.
Shoot with the Up or Space key.
Quit the game with the Esc key.

#### Health
You start the game with 3 health points. Getting hit by asteroids or enemy shots will decrease your hp by 1 point. The game ends if your hp drops to 0. Occasionally extra health pickups will appear falling from the top of the screen. Picking these up will add 1 point to your health, capping at 6 max. 

#### Score
Your score increases by 1 point for every asteroid destroyed, powerup picked up, extra health picked up and UFO destroyed. 

#### Powerups
Your basic green weapon has infinite uses. Occasionally powerups will appear falling from the top of the screen. Collecting the pickups will grant you 5 ammo of the corresponding powerup type. Collecting another pickup of the same type will also add 5 ammo, capping at 10 max. However, picking up a different powerup will instead empty your current ammo and switch to the new powerup type. 

###### Blue weapon - Piercing Shot
Shots will pierce multiple targets, while traveling slower than normal. NOTE: it is possible to defeat a UFO with only one Piercing Shot.

###### Yellow weapon - Wide Shot
Shots will become wider and shorter, making it easier to hit targets. The shots will also have a slight speed reduction compared to normal. 

###### Purple weapon - Rapid Shot
Shots will travel at super high speeds! NOTE: sometimes collision registering will not work, because the projectile bypasses the object it was supposed to hit (?).

###### Orange weapon - Bomb Shot
Shots will travel super slowly, but upon collision will explode and destroy all targets within a sizable radius. NOTE: if a bomb shot hits an object at the very top of the screen, it will cause an infinite loop of collision registering and completely jam up the game. 

#### Enemy UFOs
Sometimes enemy UFOs will appear at the top of the screen. They will move sideways and attempt to shoot you down. Avoid their shots and destroy them by hitting them 3 times. LOOK OUT: UFOs will also target and destroy powerup and extra health pickups!

#### Tools used
Python code with IDLE and Visual Studio Code
Pygame library
All sprite assets made with Piskel (https://www.piskelapp.com)