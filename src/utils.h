#ifndef _lcsfml
#define _lcsfml
#include <SFML/Graphics.h>
#include <SFML/System.h>
#endif

#include <stdio.h>
#include <stdlib.h>

// ========= MACROS =============
#define FAILURE( info ) ( { perror( info ); return EXIT_FAILURE; } )

// ========= RENAME =============
#define _createWindow( ... ) sfRenderWindow_create( __VA_ARGS__ )
#define _setFPSCapWindow( ... ) sfWindow_setFramerateLimit( __VA_ARGS__ )
#define _isOpenWindow( ... ) sfRenderWindow_isOpen( __VA_ARGS__ )
#define _pollEventWindow( ... ) sfRenderWindow_pollEvent( __VA_ARGS__ )
#define _closeWindow( ... ) sfRenderWindow_close( __VA_ARGS__ )
#define _clearWindow( ... ) sfRenderWindow_clear( __VA_ARGS__ )
#define _displayWindow( ... ) sfRenderWindow_display( __VA_ARGS__ )
#define _destroyWindow( ... ) sfRenderWindow_destroy( __VA_ARGS__ )

sfRenderWindow* createWindow( sfVideoMode mode, char* title, char style, void* settings );
void setFPSCapWindow( sfWindow* window, int cap );
char isOpenWindow( sfRenderWindow* window );
char pollEventWindow( sfRenderWindow* window, sfEvent* event );
void closeWindow( sfRenderWindow* window );
void clearWindow( sfRenderWindow* window, sfColor color );
void displayWindow( sfRenderWindow* window );
void destroyWindow( sfRenderWindow* window );
void handleDefaultEvents( sfRenderWindow* window );

// ========= CLASSES ============
#define Mode( w, h, bpp ) ( ( sfVideoMode ) { w, h, bpp } )
#define Vec2f( x, y ) ( ( sfVector2f ) { x, y } )
#define RGBA( r, g, b, a ) ( ( sfColor ) { r, g, b, a } )
#define RGB( r, g, b ) ( ( sfColor ) { r, g, b, 255 } )

// ========= COLORS =============
#define BLACK RGB( 0, 0, 0 )
#define WHITE RGB( 255, 255, 255 )
