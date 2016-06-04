#include "avr_print.h"
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>

static void setup_clock( void )
{
	CLKPR = 0x80;	/*Setup CLKPCE to be receptive*/
	CLKPR = 0x00;	/*No scalar*/

	/*OSCCAL = 0x7F;*/
}



int main( void )
{
	unsigned char i;
	cli();

	setup_clock( );
	setup_spi( );

	sei();

//	DDRA &= 0xFF;
//	PORTA &= 0xF0;

	while( 1 )
	{
		printf( "Hello, World!\n" );
	}

	return 0;
} 
