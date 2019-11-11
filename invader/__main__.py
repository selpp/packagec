import argparse
import os

from invader.core.sprite import TextureManager
from invader.core.shapes import Rectangle
from invader.core.shapes import Polygone
from invader.core.window import Window
from invader.core.shapes import Circle
from invader.core.sprite import Sprite
from invader.core.window import Mode
from invader.core.utils import BLACK
from invader.core.maths import Vec2f
from invader.core.utils import GREEN
from invader.core.utils import BLUE
from invader.core.utils import RED

parser          = argparse.ArgumentParser( )
parser.add_argument(
    '-r', '--res',
    help     = 'Resources folder',
    type     = str,
    required = True
)
args            = parser.parse_args( )

WIDTH           = 800
HEIGHT          = 600
BIT_PER_PIXEL   = 32
TITLE           = "test"
WINDOW_FLAG     = 6
FPS_CAP         = 60
MAX_TEXTURES    = 10

mode            = Mode( WIDTH, HEIGHT, BIT_PER_PIXEL )
window          = Window( mode, TITLE, WINDOW_FLAG, FPS_CAP )

texture_manager = TextureManager( MAX_TEXTURES )
sprite_id       = texture_manager + os.path.join( args.res, 'sprites/sprite.png' )

circle          = Circle( Vec2f( 0, 0 ), 50, RED, 0, BLACK )
rectangle       = Rectangle( Vec2f( 50, 50 ), Vec2f( 50, 50 ), BLUE, 0, BLACK )
polygone        = Polygone( [ Vec2f( 150, 150 ), Vec2f( 150, 200 ), Vec2f( 200, 150 ) ], GREEN, 0, BLACK )
sprite          = Sprite( Vec2f( 200, 200 ), Vec2f( .5, .5 ), texture_manager, sprite_id )

while( window.is_open( ) ):
    window.handle_events( )
    window.clear( BLACK )

    circle( window )
    rectangle( window )
    polygone( window )
    sprite( window )

    window.display( )
