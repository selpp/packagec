#include "resources.h"
#include <stdlib.h>
#include <string.h>

sfTexture* createTexture( char* path ) {
  return sfTexture_createFromFile( path, NULL );
}

sfTexture** createTextureManager( int size ) {
  sfTexture** manager = ( sfTexture** ) malloc( sizeof( sfTexture* ) * size );
  return memset( manager, 0, sizeof( sfTexture* ) * size );
}

int addTexture( sfTexture** manager, int size, sfTexture* texture ) {
  int        idx     = 0;
  sfTexture* current = manager[ idx ];

  while( current != 0 ) {
    if( idx > size - 1 ) FAILURE( "addTexture" );
    current = manager[ ++idx ];
  }

  manager[ idx ] = texture;
  return idx;
}
