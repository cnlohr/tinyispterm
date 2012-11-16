/*
 * avrdude - A Downloader/Uploader for AVR device programmers
 * Copyright (C) 2007 Limor Fried
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */


#ifndef usbtiny_h
#define usbtiny_h

//#include "avrpart.h"

// these are specifically assigned to USBtiny,
// if you need your own VID and PIDs you can get them for cheap from
// www.mecanique.co.uk so please don't reuse these. Thanks!
#define USBTINY_VENDOR  0x1781
#define USBTINY_PRODUCT 0x0C9F

#define TINYISP_VENDORID USBTINY_VENDOR
#define TINYISP_PRODUCTID USBTINY_PRODUCT

// Generic requests to the USBtiny
#define	USBTINY_ECHO 	     0      // echo test
#define	USBTINY_READ         1	    // read byte (wIndex:address)
#define	USBTINY_WRITE 	     2	    // write byte (wIndex:address, wValue:value)
#define	USBTINY_CLR          3	    // clear bit (wIndex:address, wValue:bitno)
#define	USBTINY_SET          4	    // set bit (wIndex:address, wValue:bitno)

// Programming requests
#define	USBTINY_POWERUP      5	    // apply power (wValue:SCK-period, wIndex:RESET)
#define	USBTINY_POWERDOWN    6	    // remove power from chip
#define	USBTINY_SPI          7	    // issue SPI command (wValue:c1c0, wIndex:c3c2)
#define	USBTINY_POLL_BYTES   8	    // set poll bytes for write (wValue:p1p2)
#define	USBTINY_FLASH_READ   9	    // read flash (wIndex:address)
#define	USBTINY_FLASH_WRITE  10	    // write flash (wIndex:address, wValue:timeout)
#define	USBTINY_EEPROM_READ  11	    // read eeprom (wIndex:address)
#define	USBTINY_EEPROM_WRITE 12	    // write eeprom (wIndex:address, wValue:timeout)
#define USBTINY_DDRWRITE     13
#define USBTINY_SPI1         14


// Flags to indicate how to set RESET on power up
#define	RESET_LOW	0
#define	RESET_HIGH	1

// The SCK speed can be set by avrdude, to allow programming of slow-clocked parts
#define	SCK_MIN		1	// usec delay (target clock >= 4 MHz)
#define	SCK_MAX		250	// usec (target clock >= 16 KHz)
#define	SCK_DEFAULT	10	// usec (target clock >= 0.4 MHz)

// How much data, max, do we want to send in one USB packet?
#define	CHUNK_SIZE	128	// must be power of 2 less than 256

// The default USB Timeout
#define	USB_TIMEOUT	500	// msec

#ifdef __cplusplus
extern "C" {
#endif

#ifdef __cplusplus
}
#endif

#endif /* usbtiny_h */
