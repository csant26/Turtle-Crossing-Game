"""Constants"""
# screen specs
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BACKGROUND_COLOR = "antiquewhite"
MAX_SCREEN_YCOOR = SCREEN_HEIGHT // 2
MIN_SCREEN_YCOOR = - (MAX_SCREEN_YCOOR)

# player specs
PLAYER_COLOUR = "black"
INITIAL_PLAYER_XCOOR = 0
INITIAL_PLAYER_YCOOR = - (MAX_SCREEN_YCOOR - 20)
PLAYER_PACE = 15
PLAYER_MAX_XCOOR = SCREEN_WIDTH // 2 - 20
PLAYER_MIN_XCOOR = -PLAYER_MAX_XCOOR
PLAYER_MAX_YCOOR = SCREEN_HEIGHT // 2 - 30
PLAYER_MIN_YCOOR = INITIAL_PLAYER_YCOOR + 20

# scoreboard specs
SCORE_XCOOR = -(SCREEN_WIDTH // 2 - 10)
SCORE_YCOOR = SCREEN_HEIGHT // 2 - 35
SCORE_COLOUR = "black"

# car colors
CAR_COLORS = [
    "lightsteelblue",  
    "cadetblue",       
    "darkseagreen",    
    "lightcoral",      
    "lightskyblue",    
    "khaki",           
    "plum",            
    "powderblue",      
    "palevioletred",   
    "mediumaquamarine" 
]
CAR_MAX_XCOOR = SCREEN_WIDTH // 2 + 50
CAR_MIN_XCOOR = - (CAR_MAX_XCOOR)
CAR_MAX_YCOOR = SCORE_YCOOR - 50
CAR_MIN_YCOOR = INITIAL_PLAYER_YCOOR + 50
INITIAL_CAR_COUNT = 5


# file for saving players
FILE_NAME = "players.txt"
