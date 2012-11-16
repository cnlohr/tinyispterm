#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <string.h>

extern "C"
{
#include <usb.h>
}

#include "tinyispterm.h"

using namespace std;
#define USB_TIMEOUT 500

usb_dev_handle * hTinyISP;

#define GETBYTE(x) usb_control(USBTINY_SPI1, x,  1)
#define GETBYTE4(x) usb_control(USBTINY_SPI, x,  1)

usb_dev_handle * acquireTinyISP(void)
{
  struct usb_bus * thisBus;
  struct usb_device * thisDevice = NULL;

  usb_init();
  usb_find_busses();
  usb_find_devices();

  for (int retry = 0; retry < 1 && NULL == thisDevice; retry++)
    {

      for (thisBus = usb_get_busses(); NULL != thisBus; thisBus = thisBus->next)
	{
	  
	  for (thisDevice = thisBus->devices; NULL != thisDevice; thisDevice = thisDevice->next)
	    {
	      usb_dev_handle * device;
	      device = usb_open(thisDevice);
//	      cout << "Vendor " << hex << setw(4) << setfill('0')
//		   << thisDevice->descriptor.idVendor
//		   << " Product " << thisDevice->descriptor.idProduct
//		   << endl;
  

	      if (TINYISP_VENDORID == thisDevice->descriptor.idVendor &&
		  TINYISP_PRODUCTID == thisDevice->descriptor.idProduct)
		{
//		  cout << "Acquired device" << endl;
	 return device;
		}
	      usb_close(device);
	    }
	}
      cerr << "No device found, sleeping..." << endl;
      sleep(1);
    }
}

int usb_control ( int req, unsigned int val, int size )
{
	unsigned char ret[4];
	int r = usb_control_msg( hTinyISP,
		   USB_ENDPOINT_IN | USB_TYPE_VENDOR | USB_RECIP_DEVICE,
		   req, val, size,(char*) ret, 4, USB_TIMEOUT );
	if( r<0 )
	{
		fprintf( stderr, "Error: Could not read char (%d).\n", r );
		exit( -1 );
	}

	return (r<4)?ret[0]:(*(int*)ret);
}

int main(int argc, char ** argv)
{
	bool bUseSTDIN = false;
	bool bRebootOnly = false;

	if( argc != 1 )
	{
		bool bShowHelp = false;
		for( int i = 1; i < argc; i++ )
		{
			const char * ar = argv[i];
			if( strcmp( ar, "-h" ) == 0 || strcmp( ar, "--help" ) == 0 )
			{
				bShowHelp = true;
			}
			else if( strcmp( ar, "-v" ) == 0 || strcmp( ar, "--version" ) == 0 )
			{
				printf( "0.1cnl\n" );
				return 0;
			}
			else if( strcmp( ar, "-s" ) == 0 || strcmp( ar, "--stdin" ) == 0 )
			{
				bUseSTDIN = true;
			}
			else if( strcmp( ar, "-r" ) == 0 || strcmp( ar, "--reboot-only" ) == 0 )
			{
				bRebootOnly = true;
			}
		}

		if( bShowHelp )
		{
			printf( "TinyISPTerm v0.1cnl - Copyright 2011 Charles Lohr\n" );
			printf( "  usage: tinyispterm [-h|--help|-v|--version]|[-s|--stdin]\n" );
			printf( "  -h or --help: print this message.\n" );
			printf( "  -v or --version: print version of software.\n" );
			printf( "  -r or --reboot-only: reboot chip and exit\n" );
			printf( "  -s or --stdin: only request bytes from device when stdin\n" );
			printf( "       present.  Also, only pass those devices as output.\n" );
			return 0;
		}
	}

	unsigned i = 0;
	hTinyISP = acquireTinyISP();

	if (NULL == hTinyISP)
	{
		cerr << "Could not acquire device" << endl;
		exit(1);
	}

//   usb_control( USBTINY_POWERUP, USB_TIMEOUT, RESET_HIGH );
	usb_control( USBTINY_POWERUP, USB_TIMEOUT, RESET_LOW );
	usleep(200000);
	usb_control( USBTINY_POWERUP, USB_TIMEOUT, RESET_HIGH );
	usleep(200000);

//Alternative: 1011 1101  (SLAVE MODE

	usb_control(USBTINY_SET, 1, 1); // /SS high (NOT /ss high???) (this doesn't seem to affect anythign)
//This actually causes big problems for the micro version
	usb_control(USBTINY_DDRWRITE, 0xbd, 1);

	if( bRebootOnly ) goto end;

	while(1)
	{
		unsigned char c;
		if( bUseSTDIN )
		{
			c = GETBYTE( getchar() );
			if( c != 0x00 )
				printf( "%c", c );
			fflush( stdout );
		}
		else
		{
			unsigned int r = GETBYTE4( 0 );
//			printf( "%d", r );
			while( r )
			{
				if( r & 0xFF )
//					printf( ":%d", r & 0xff );
					printf( "%c", r & 0xff );
				r >>= 8;
			}
//			printf( "\n");
			fflush( stdout );
		}

	}

end:
	usb_close(hTinyISP);
}
