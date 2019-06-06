from enum import Enum

# this will keep track of values that need to stay immutable
class GameStates(Enum):
	PLAYERS_TURN = 1
	ENEMY_TURN = 2