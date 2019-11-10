#ifndef _lcsfml
#define _lcsfml
#include <SFML/Graphics.h>
#include <SFML/System.h>
#include "utils.h"
#endif

sfTexture* createTexture( char* path );

sfTexture** createTextureManager( int size );

int addTexture( sfTexture** manager, int size, sfTexture* texture );
