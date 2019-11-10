#ifndef _lcsfml
#define _lcsfml
#include <SFML/Graphics.h>
#include <SFML/System.h>
#endif

// ========= MACROS =============
#define FAILURE( info ) ( { perror( info ); return EXIT_FAILURE; } )

// ========= RENAME =============
#define createWindow( ... ) sfRenderWindow_create( __VA_ARGS__ )
#define setFPSCapWindow( ... ) sfWindow_setFramerateLimit( __VA_ARGS__ )
#define isOpenWindow( ... ) sfRenderWindow_isOpen( __VA_ARGS__ )
#define pollEventWindow( ... ) sfRenderWindow_pollEvent( __VA_ARGS__ )
#define closeWindow( ... ) sfRenderWindow_close( __VA_ARGS__ )
#define clearWindow( ... ) sfRenderWindow_clear( __VA_ARGS__ )
#define displayWindow( ... ) sfRenderWindow_display( __VA_ARGS__ )
#define destroyWindow( ... ) sfRenderWindow_destroy( __VA_ARGS__ )

// ========= CLASSES ============
#define Mode( w, h, bpp ) ( ( sfVideoMode ) { w, h, bpp } )
#define Vec2f( x, y ) ( ( sfVector2f ) { x, y } )
#define RGBA( r, g, b, a ) ( ( sfColor ) { r, g, b, a } )
#define RGB( r, g, b ) ( ( sfColor ) { r, g, b, 255 } )

// ========= COLORS =============
#define BLACK RGB( 0, 0, 0 )
#define WHITE RGB( 255, 255, 255 )
