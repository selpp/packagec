import ctypes
import os

bdl = ctypes.cdll.LoadLibrary( os.environ[ 'BDL' ] )
