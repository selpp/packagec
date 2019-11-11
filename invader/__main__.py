from invader.core.shapes import Rectangle
from invader.core.shapes import Polygone
from invader.core.window import Window
from invader.core.shapes import Circle
from invader.core.window import Mode
from invader.core.utils import BLACK
from invader.core.maths import Vec2f
from invader.core.utils import GREEN
from invader.core.utils import BLUE
from invader.core.utils import RED

WIDTH         = 800
HEIGHT        = 600
BIT_PER_PIXEL = 32
TITLE         = "test"
WINDOW_FLAG   = 6
FPS_CAP       = 60

mode          = Mode( WIDTH, HEIGHT, BIT_PER_PIXEL )
window        = Window( mode, TITLE, WINDOW_FLAG, FPS_CAP )

circle        = Circle( Vec2f( 0, 0 ), 50, RED, 0, BLACK )
rectangle     = Rectangle( Vec2f( 50, 50 ), Vec2f( 50, 50 ), BLUE, 0, BLACK )
polygone      = Polygone( [ Vec2f( 150, 150 ), Vec2f( 150, 200 ), Vec2f( 200, 150 ) ], GREEN, 0, BLACK )

while( window.is_open( ) ):
    window.handle_events( )
    window.clear( BLACK )

    circle( window )
    rectangle( window )
    polygone( window )

    window.display( )
