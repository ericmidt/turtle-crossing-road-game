# turtle-crossing-road-game
Turtle crossing the road game made in Python using the Turtle module.

## How the game works
The player's goal is to reach the other side of the road without getting hit by the cars.
If the player, represented by a turtle, colides with a car, the game is over.
Each time the player manages to reach the other side of the road, the level is incremented.
At each new level, the player character respawns back to their inital position and the speed of the cars increases.

## OOP
This program was made following OOP concepts. Three new classes were created, the Player, the CarManager and the Scoreboard.
The Player, CarManager and Scoreboard classes derive from the Turtle class provided by the turtle module.
Apart from initialization, new methods were created to add movement to the player, update the scoreboard and generate new Turtle objects to populate CarManager's all_cars list. 
