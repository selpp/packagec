import ctypes

class _RGBA( ctypes.Structure ):
   _fields_ = [ ( 'r', ctypes.c_char ), ( 'g', ctypes.c_char ), ( 'b', ctypes.c_char ), ( 'a', ctypes.c_char ) ]

class Color:
    def __init__( self: 'Color', r: int, g: int, b: int, a: int = 255 ) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def to_c( self: 'Color' ) -> '_RGBA':
         return _RGBA( ctypes.c_char( self.r ), ctypes.c_char( self.g ), ctypes.c_char( self.b ), ctypes.c_char( self.a ) )

    def lerp( self: 'Color', other: 'Color', t: float ) -> 'Color':
        t = min( max( t, 0 ), 1 )
        return Color(
            self.r + ( other.r - self.r ) * t,
            self.g + ( other.g - self.g ) * t,
            self.b + ( other.b - self.b ) * t,
            self.a + ( other.a - self.a ) * t
        )

BLACK = Color(   0,   0,   0 )
WHITE = Color( 255, 255, 255 )
GREY  = Color( 128, 128, 128 )
RED   = Color( 255,   0,   0 )
GREEN = Color(   0, 255,   0 )
BLUE  = Color(   0,   0, 255 )
