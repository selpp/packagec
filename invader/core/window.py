import ctypes

from invader.core.utils import Color

bdl                      = ctypes.cdll.LoadLibrary( 'packagepython/res/bdl.so' )
bdl.createWindow.restype = ctypes.c_void_p

class _Mode( ctypes.Structure ):
   _fields_ = [ ( 'w', ctypes.c_int ), ( 'h', ctypes.c_int ), ( 'bpp', ctypes.c_int ) ]

class Mode:
    def __init__( self: 'Mode', w: int, h: int, bpp: int ) -> None:
        self.w   = w
        self.h   = h
        self.bpp = bpp

    def to_c( self: 'Mode' ) -> '_Mode':
        return _Mode( ctypes.c_int( self.w ), ctypes.c_int( self.h ), ctypes.c_int( self.bpp ) )

class Window:
    def __init__( self: 'Window', mode: 'Mode', title: str, flag: int, fps_cap: int = None ) -> None:
        self.mode    = mode
        self.title   = title
        self.flag    = flag
        self.fps_cap = fps_cap
        self.window  =  self._create_window( )

        if fps_cap is not None:
            self._set_fps_cap( )

    def _create_window( self: 'Window' ) -> ctypes.c_void_p:
        window = bdl.createWindow( self.mode.to_c( ), ctypes.c_char_p( self.title.encode( ) ), ctypes.c_int( self.flag ), ctypes.c_void_p( 0 ) )
        return ctypes.c_void_p( window )

    def _set_fps_cap( self: 'Window' ) -> None:
         bdl.setFPSCapWindow( self.window, self.fps_cap )

    def is_open( self: 'Window' ) -> bool:
        return bdl.isOpenWindow( self.window )

    def clear( self: 'Window', color: 'Color' ) -> None:
        return bdl.clearWindow( self.window, color.to_c( ) )

    def display( self: 'Window' ) -> None:
        bdl.displayWindow( self.window )

    def handle_events( self: 'Window' ) -> None:
        bdl.handleDefaultEvents( self.window )
