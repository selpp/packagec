import ctypes
bdl = ctypes.cdll.LoadLibrary( './build/bdl.so' )

class Mode( ctypes.Structure ):
   _fields_ = [ ( 'w', ctypes.c_int ), ( 'h', ctypes.c_int ), ( 'bpp', ctypes.c_int ) ]

class RGBA( ctypes.Structure ):
   _fields_ = [ ( 'r', ctypes.c_char ), ( 'g', ctypes.c_char ), ( 'b', ctypes.c_char ), ( 'a', ctypes.c_char ) ]

class Vec2f( ctypes.Structure ):
    _fields_ = [ ( 'x', ctypes.c_float ), ( 'y', ctypes.c_float ) ]

WIDTH                    = ctypes.c_int( 800 )
HEIGHT                   = ctypes.c_int( 600 )
BIT_PER_PIXEL            = ctypes.c_int( 32 )
TITLE                    = ctypes.c_char_p( b"test" )
WINDOW_FLAG              = ctypes.c_int( 6 )

BLACK                    = RGBA( ctypes.c_char( 0 ), ctypes.c_char( 0 ), ctypes.c_char( 0 ), ctypes.c_char( 255 ) )
RED                      = RGBA( ctypes.c_char( 255 ), ctypes.c_char( 0 ), ctypes.c_char( 0 ), ctypes.c_char( 255 ) )
FPS_CAP                  = 60

bdl.createWindow.restype = ctypes.c_void_p

mode                     = Mode( WIDTH, HEIGHT, BIT_PER_PIXEL )
window                   = bdl.createWindow( mode, TITLE, WINDOW_FLAG, ctypes.c_void_p( 0 ) )
window                   = ctypes.c_void_p( window )

bdl.setFPSCapWindow( window, FPS_CAP );

while( bdl.isOpenWindow(window) ):
    bdl.handleDefaultEvents( window )
    bdl.clearWindow( window, BLACK );
    bdl.drawCircle( window, Vec2f( 0.0, 0.0 ), ctypes.c_float( 50 ), RED, ctypes.c_int( 1 ), BLACK );
    bdl.displayWindow( window );
