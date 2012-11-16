# This file was created automatically by SWIG 1.3.28.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _libusb
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types



usb_control_in = _libusb.usb_control_in

usb_control_out = _libusb.usb_control_out

usb_string = _libusb.usb_string
USB_CLASS_PER_INTERFACE = _libusb.USB_CLASS_PER_INTERFACE
USB_CLASS_AUDIO = _libusb.USB_CLASS_AUDIO
USB_CLASS_COMM = _libusb.USB_CLASS_COMM
USB_CLASS_HID = _libusb.USB_CLASS_HID
USB_CLASS_PRINTER = _libusb.USB_CLASS_PRINTER
USB_CLASS_PTP = _libusb.USB_CLASS_PTP
USB_CLASS_MASS_STORAGE = _libusb.USB_CLASS_MASS_STORAGE
USB_CLASS_HUB = _libusb.USB_CLASS_HUB
USB_CLASS_DATA = _libusb.USB_CLASS_DATA
USB_CLASS_VENDOR_SPEC = _libusb.USB_CLASS_VENDOR_SPEC
USB_DT_DEVICE = _libusb.USB_DT_DEVICE
USB_DT_CONFIG = _libusb.USB_DT_CONFIG
USB_DT_STRING = _libusb.USB_DT_STRING
USB_DT_INTERFACE = _libusb.USB_DT_INTERFACE
USB_DT_ENDPOINT = _libusb.USB_DT_ENDPOINT
USB_DT_HID = _libusb.USB_DT_HID
USB_DT_REPORT = _libusb.USB_DT_REPORT
USB_DT_PHYSICAL = _libusb.USB_DT_PHYSICAL
USB_DT_HUB = _libusb.USB_DT_HUB
USB_DT_DEVICE_SIZE = _libusb.USB_DT_DEVICE_SIZE
USB_DT_CONFIG_SIZE = _libusb.USB_DT_CONFIG_SIZE
USB_DT_INTERFACE_SIZE = _libusb.USB_DT_INTERFACE_SIZE
USB_DT_ENDPOINT_SIZE = _libusb.USB_DT_ENDPOINT_SIZE
USB_DT_ENDPOINT_AUDIO_SIZE = _libusb.USB_DT_ENDPOINT_AUDIO_SIZE
USB_DT_HUB_NONVAR_SIZE = _libusb.USB_DT_HUB_NONVAR_SIZE
class usb_descriptor_header(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usb_descriptor_header, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usb_descriptor_header, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C usb_descriptor_header instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["bLength"] = _libusb.usb_descriptor_header_bLength_set
    __swig_getmethods__["bLength"] = _libusb.usb_descriptor_header_bLength_get
    if _newclass:bLength = property(_libusb.usb_descriptor_header_bLength_get, _libusb.usb_descriptor_header_bLength_set)
    __swig_setmethods__["bDescriptorType"] = _libusb.usb_descriptor_header_bDescriptorType_set
    __swig_getmethods__["bDescriptorType"] = _libusb.usb_descriptor_header_bDescriptorType_get
    if _newclass:bDescriptorType = property(_libusb.usb_descriptor_header_bDescriptorType_get, _libusb.usb_descriptor_header_bDescriptorType_set)
    def __init__(self, *args):
        this = _libusb.new_usb_descriptor_header(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libusb.delete_usb_descriptor_header
    __del__ = lambda self : None;
_libusb.usb_descriptor_header_swigregister(usb_descriptor_header)

class usb_string_descriptor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usb_string_descriptor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usb_string_descriptor, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C usb_string_descriptor instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["bLength"] = _libusb.usb_string_descriptor_bLength_set
    __swig_getmethods__["bLength"] = _libusb.usb_string_descriptor_bLength_get
    if _newclass:bLength = property(_libusb.usb_string_descriptor_bLength_get, _libusb.usb_string_descriptor_bLength_set)
    __swig_setmethods__["bDescriptorType"] = _libusb.usb_string_descriptor_bDescriptorType_set
    __swig_getmethods__["bDescriptorType"] = _libusb.usb_string_descriptor_bDescriptorType_get
    if _newclass:bDescriptorType = property(_libusb.usb_string_descriptor_bDescriptorType_get, _libusb.usb_string_descriptor_bDescriptorType_set)
    __swig_setmethods__["wData"] = _libusb.usb_string_descriptor_wData_set
    __swig_getmethods__["wData"] = _libusb.usb_string_descriptor_wData_get
    if _newclass:wData = property(_libusb.usb_string_descriptor_wData_get, _libusb.usb_string_descriptor_wData_set)
    def __init__(self, *args):
        this = _libusb.new_usb_string_descriptor(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libusb.delete_usb_string_descriptor
    __del__ = lambda self : None;
_libusb.usb_string_descriptor_swigregister(usb_string_descriptor)

class usb_hid_descriptor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usb_hid_descriptor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usb_hid_descriptor, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C usb_hid_descriptor instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["bLength"] = _libusb.usb_hid_descriptor_bLength_set
    __swig_getmethods__["bLength"] = _libusb.usb_hid_descriptor_bLength_get
    if _newclass:bLength = property(_libusb.usb_hid_descriptor_bLength_get, _libusb.usb_hid_descriptor_bLength_set)
    __swig_setmethods__["bDescriptorType"] = _libusb.usb_hid_descriptor_bDescriptorType_set
    __swig_getmethods__["bDescriptorType"] = _libusb.usb_hid_descriptor_bDescriptorType_get
    if _newclass:bDescriptorType = property(_libusb.usb_hid_descriptor_bDescriptorType_get, _libusb.usb_hid_descriptor_bDescriptorType_set)
    __swig_setmethods__["bcdHID"] = _libusb.usb_hid_descriptor_bcdHID_set
    __swig_getmethods__["bcdHID"] = _libusb.usb_hid_descriptor_bcdHID_get
    if _newclass:bcdHID = property(_libusb.usb_hid_descriptor_bcdHID_get, _libusb.usb_hid_descriptor_bcdHID_set)
    __swig_setmethods__["bCountryCode"] = _libusb.usb_hid_descriptor_bCountryCode_set
    __swig_getmethods__["bCountryCode"] = _libusb.usb_hid_descriptor_bCountryCode_get
    if _newclass:bCountryCode = property(_libusb.usb_hid_descriptor_bCountryCode_get, _libusb.usb_hid_descriptor_bCountryCode_set)
    __swig_setmethods__["bNumDescriptors"] = _libusb.usb_hid_descriptor_bNumDescriptors_set
    __swig_getmethods__["bNumDescriptors"] = _libusb.usb_hid_descriptor_bNumDescriptors_get
    if _newclass:bNumDescriptors = property(_libusb.usb_hid_descriptor_bNumDescriptors_get, _libusb.usb_hid_descriptor_bNumDescriptors_set)
    def __init__(self, *args):
        this = _libusb.new_usb_hid_descriptor(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libusb.delete_usb_hid_descriptor
    __del__ = lambda self : None;
_libusb.usb_hid_descriptor_swigregister(usb_hid_descriptor)

USB_MAXENDPOINTS = _libusb.USB_MAXENDPOINTS
class usb_endpoint_descriptor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usb_endpoint_descriptor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usb_endpoint_descriptor, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C usb_endpoint_descriptor instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["bLength"] = _libusb.usb_endpoint_descriptor_bLength_set
    __swig_getmethods__["bLength"] = _libusb.usb_endpoint_descriptor_bLength_get
    if _newclass:bLength = property(_libusb.usb_endpoint_descriptor_bLength_get, _libusb.usb_endpoint_descriptor_bLength_set)
    __swig_setmethods__["bDescriptorType"] = _libusb.usb_endpoint_descriptor_bDescriptorType_set
    __swig_getmethods__["bDescriptorType"] = _libusb.usb_endpoint_descriptor_bDescriptorType_get
    if _newclass:bDescriptorType = property(_libusb.usb_endpoint_descriptor_bDescriptorType_get, _libusb.usb_endpoint_descriptor_bDescriptorType_set)
    __swig_setmethods__["bEndpointAddress"] = _libusb.usb_endpoint_descriptor_bEndpointAddress_set
    __swig_getmethods__["bEndpointAddress"] = _libusb.usb_endpoint_descriptor_bEndpointAddress_get
    if _newclass:bEndpointAddress = property(_libusb.usb_endpoint_descriptor_bEndpointAddress_get, _libusb.usb_endpoint_descriptor_bEndpointAddress_set)
    __swig_setmethods__["bmAttributes"] = _libusb.usb_endpoint_descriptor_bmAttributes_set
    __swig_getmethods__["bmAttributes"] = _libusb.usb_endpoint_descriptor_bmAttributes_get
    if _newclass:bmAttributes = property(_libusb.usb_endpoint_descriptor_bmAttributes_get, _libusb.usb_endpoint_descriptor_bmAttributes_set)
    __swig_setmethods__["wMaxPacketSize"] = _libusb.usb_endpoint_descriptor_wMaxPacketSize_set
    __swig_getmethods__["wMaxPacketSize"] = _libusb.usb_endpoint_descriptor_wMaxPacketSize_get
    if _newclass:wMaxPacketSize = property(_libusb.usb_endpoint_descriptor_wMaxPacketSize_get, _libusb.usb_endpoint_descriptor_wMaxPacketSize_set)
    __swig_setmethods__["bInterval"] = _libusb.usb_endpoint_descriptor_bInterval_set
    __swig_getmethods__["bInterval"] = _libusb.usb_endpoint_descriptor_bInterval_get
    if _newclass:bInterval = property(_libusb.usb_endpoint_descriptor_bInterval_get, _libusb.usb_endpoint_descriptor_bInterval_set)
    __swig_setmethods__["bRefresh"] = _libusb.usb_endpoint_descriptor_bRefresh_set
    __swig_getmethods__["bRefresh"] = _libusb.usb_endpoint_descriptor_bRefresh_get
    if _newclass:bRefresh = property(_libusb.usb_endpoint_descriptor_bRefresh_get, _libusb.usb_endpoint_descriptor_bRefresh_set)
    __swig_setmethods__["bSynchAddress"] = _libusb.usb_endpoint_descriptor_bSynchAddress_set
    __swig_getmethods__["bSynchAddress"] = _libusb.usb_endpoint_descriptor_bSynchAddress_get
    if _newclass:bSynchAddress = property(_libusb.usb_endpoint_descriptor_bSynchAddress_get, _libusb.usb_endpoint_descriptor_bSynchAddress_set)
    __swig_setmethods__["extra"] = _libusb.usb_endpoint_descriptor_extra_set
    __swig_getmethods__["extra"] = _libusb.usb_endpoint_descriptor_extra_get
    if _newclass:extra = property(_libusb.usb_endpoint_descriptor_extra_get, _libusb.usb_endpoint_descriptor_extra_set)
    __swig_setmethods__["extralen"] = _libusb.usb_endpoint_descriptor_extralen_set
    __swig_getmethods__["extralen"] = _libusb.usb_endpoint_descriptor_extralen_get
    if _newclass:extralen = property(_libusb.usb_endpoint_descriptor_extralen_get, _libusb.usb_endpoint_descriptor_extralen_set)
    def __init__(self, *args):
        this = _libusb.new_usb_endpoint_descriptor(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libusb.delete_usb_endpoint_descriptor
    __del__ = lambda self : None;
_libusb.usb_endpoint_descriptor_swigregister(usb_endpoint_descriptor)

USB_ENDPOINT_ADDRESS_MASK = _libusb.USB_ENDPOINT_ADDRESS_MASK
USB_ENDPOINT_DIR_MASK = _libusb.USB_ENDPOINT_DIR_MASK
USB_ENDPOINT_TYPE_MASK = _libusb.USB_ENDPOINT_TYPE_MASK
USB_ENDPOINT_TYPE_CONTROL = _libusb.USB_ENDPOINT_TYPE_CONTROL
USB_ENDPOINT_TYPE_ISOCHRONOUS = _libusb.USB_ENDPOINT_TYPE_ISOCHRONOUS
USB_ENDPOINT_TYPE_BULK = _libusb.USB_ENDPOINT_TYPE_BULK
USB_ENDPOINT_TYPE_INTERRUPT = _libusb.USB_ENDPOINT_TYPE_INTERRUPT
USB_MAXINTERFACES = _libusb.USB_MAXINTERFACES
class usb_interface_descriptor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usb_interface_descriptor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usb_interface_descriptor, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C usb_interface_descriptor instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["bLength"] = _libusb.usb_interface_descriptor_bLength_set
    __swig_getmethods__["bLength"] = _libusb.usb_interface_descriptor_bLength_get
    if _newclass:bLength = property(_libusb.usb_interface_descriptor_bLength_get, _libusb.usb_interface_descriptor_bLength_set)
    __swig_setmethods__["bDescriptorType"] = _libusb.usb_interface_descriptor_bDescriptorType_set
    __swig_getmethods__["bDescriptorType"] = _libusb.usb_interface_descriptor_bDescriptorType_get
    if _newclass:bDescriptorType = property(_libusb.usb_interface_descriptor_bDescriptorType_get, _libusb.usb_interface_descriptor_bDescriptorType_set)
    __swig_setmethods__["bInterfaceNumber"] = _libusb.usb_interface_descriptor_bInterfaceNumber_set
    __swig_getmethods__["bInterfaceNumber"] = _libusb.usb_interface_descriptor_bInterfaceNumber_get
    if _newclass:bInterfaceNumber = property(_libusb.usb_interface_descriptor_bInterfaceNumber_get, _libusb.usb_interface_descriptor_bInterfaceNumber_set)
    __swig_setmethods__["bAlternateSetting"] = _libusb.usb_interface_descriptor_bAlternateSetting_set
    __swig_getmethods__["bAlternateSetting"] = _libusb.usb_interface_descriptor_bAlternateSetting_get
    if _newclass:bAlternateSetting = property(_libusb.usb_interface_descriptor_bAlternateSetting_get, _libusb.usb_interface_descriptor_bAlternateSetting_set)
    __swig_setmethods__["bNumEndpoints"] = _libusb.usb_interface_descriptor_bNumEndpoints_set
    __swig_getmethods__["bNumEndpoints"] = _libusb.usb_interface_descriptor_bNumEndpoints_get
    if _newclass:bNumEndpoints = property(_libusb.usb_interface_descriptor_bNumEndpoints_get, _libusb.usb_interface_descriptor_bNumEndpoints_set)
    __swig_setmethods__["bInterfaceClass"] = _libusb.usb_interface_descriptor_bInterfaceClass_set
    __swig_getmethods__["bInterfaceClass"] = _libusb.usb_interface_descriptor_bInterfaceClass_get
    if _newclass:bInterfaceClass = property(_libusb.usb_interface_descriptor_bInterfaceClass_get, _libusb.usb_interface_descriptor_bInterfaceClass_set)
    __swig_setmethods__["bInterfaceSubClass"] = _libusb.usb_interface_descriptor_bInterfaceSubClass_set
    __swig_getmethods__["bInterfaceSubClass"] = _libusb.usb_interface_descriptor_bInterfaceSubClass_get
    if _newclass:bInterfaceSubClass = property(_libusb.usb_interface_descriptor_bInterfaceSubClass_get, _libusb.usb_interface_descriptor_bInterfaceSubClass_set)
    __swig_setmethods__["bInterfaceProtocol"] = _libusb.usb_interface_descriptor_bInterfaceProtocol_set
    __swig_getmethods__["bInterfaceProtocol"] = _libusb.usb_interface_descriptor_bInterfaceProtocol_get
    if _newclass:bInterfaceProtocol = property(_libusb.usb_interface_descriptor_bInterfaceProtocol_get, _libusb.usb_interface_descriptor_bInterfaceProtocol_set)
    __swig_setmethods__["iInterface"] = _libusb.usb_interface_descriptor_iInterface_set
    __swig_getmethods__["iInterface"] = _libusb.usb_interface_descriptor_iInterface_get
    if _newclass:iInterface = property(_libusb.usb_interface_descriptor_iInterface_get, _libusb.usb_interface_descriptor_iInterface_set)
    __swig_setmethods__["endpoint"] = _libusb.usb_interface_descriptor_endpoint_set
    __swig_getmethods__["endpoint"] = _libusb.usb_interface_descriptor_endpoint_get
    if _newclass:endpoint = property(_libusb.usb_interface_descriptor_endpoint_get, _libusb.usb_interface_descriptor_endpoint_set)
    __swig_setmethods__["extra"] = _libusb.usb_interface_descriptor_extra_set
    __swig_getmethods__["extra"] = _libusb.usb_interface_descriptor_extra_get
    if _newclass:extra = property(_libusb.usb_interface_descriptor_extra_get, _libusb.usb_interface_descriptor_extra_set)
    __swig_setmethods__["extralen"] = _libusb.usb_interface_descriptor_extralen_set
    __swig_getmethods__["extralen"] = _libusb.usb_interface_descriptor_extralen_get
    if _newclass:extralen = property(_libusb.usb_interface_descriptor_extralen_get, _libusb.usb_interface_descriptor_extralen_set)
    def __init__(self, *args):
        this = _libusb.new_usb_interface_descriptor(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libusb.delete_usb_interface_descriptor
    __del__ = lambda self : None;
_libusb.usb_interface_descriptor_swigregister(usb_interface_descriptor)

USB_MAXALTSETTING = _libusb.USB_MAXALTSETTING
class usb_interface(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usb_interface, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usb_interface, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C usb_interface instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["altsetting"] = _libusb.usb_interface_altsetting_set
    __swig_getmethods__["altsetting"] = _libusb.usb_interface_altsetting_get
    if _newclass:altsetting = property(_libusb.usb_interface_altsetting_get, _libusb.usb_interface_altsetting_set)
    __swig_setmethods__["num_altsetting"] = _libusb.usb_interface_num_altsetting_set
    __swig_getmethods__["num_altsetting"] = _libusb.usb_interface_num_altsetting_get
    if _newclass:num_altsetting = property(_libusb.usb_interface_num_altsetting_get, _libusb.usb_interface_num_altsetting_set)
    def __init__(self, *args):
        this = _libusb.new_usb_interface(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libusb.delete_usb_interface
    __del__ = lambda self : None;
_libusb.usb_interface_swigregister(usb_interface)

USB_MAXCONFIG = _libusb.USB_MAXCONFIG
class usb_config_descriptor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usb_config_descriptor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usb_config_descriptor, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C usb_config_descriptor instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["bLength"] = _libusb.usb_config_descriptor_bLength_set
    __swig_getmethods__["bLength"] = _libusb.usb_config_descriptor_bLength_get
    if _newclass:bLength = property(_libusb.usb_config_descriptor_bLength_get, _libusb.usb_config_descriptor_bLength_set)
    __swig_setmethods__["bDescriptorType"] = _libusb.usb_config_descriptor_bDescriptorType_set
    __swig_getmethods__["bDescriptorType"] = _libusb.usb_config_descriptor_bDescriptorType_get
    if _newclass:bDescriptorType = property(_libusb.usb_config_descriptor_bDescriptorType_get, _libusb.usb_config_descriptor_bDescriptorType_set)
    __swig_setmethods__["wTotalLength"] = _libusb.usb_config_descriptor_wTotalLength_set
    __swig_getmethods__["wTotalLength"] = _libusb.usb_config_descriptor_wTotalLength_get
    if _newclass:wTotalLength = property(_libusb.usb_config_descriptor_wTotalLength_get, _libusb.usb_config_descriptor_wTotalLength_set)
    __swig_setmethods__["bNumInterfaces"] = _libusb.usb_config_descriptor_bNumInterfaces_set
    __swig_getmethods__["bNumInterfaces"] = _libusb.usb_config_descriptor_bNumInterfaces_get
    if _newclass:bNumInterfaces = property(_libusb.usb_config_descriptor_bNumInterfaces_get, _libusb.usb_config_descriptor_bNumInterfaces_set)
    __swig_setmethods__["bConfigurationValue"] = _libusb.usb_config_descriptor_bConfigurationValue_set
    __swig_getmethods__["bConfigurationValue"] = _libusb.usb_config_descriptor_bConfigurationValue_get
    if _newclass:bConfigurationValue = property(_libusb.usb_config_descriptor_bConfigurationValue_get, _libusb.usb_config_descriptor_bConfigurationValue_set)
    __swig_setmethods__["iConfiguration"] = _libusb.usb_config_descriptor_iConfiguration_set
    __swig_getmethods__["iConfiguration"] = _libusb.usb_config_descriptor_iConfiguration_get
    if _newclass:iConfiguration = property(_libusb.usb_config_descriptor_iConfiguration_get, _libusb.usb_config_descriptor_iConfiguration_set)
    __swig_setmethods__["bmAttributes"] = _libusb.usb_config_descriptor_bmAttributes_set
    __swig_getmethods__["bmAttributes"] = _libusb.usb_config_descriptor_bmAttributes_get
    if _newclass:bmAttributes = property(_libusb.usb_config_descriptor_bmAttributes_get, _libusb.usb_config_descriptor_bmAttributes_set)
    __swig_setmethods__["MaxPower"] = _libusb.usb_config_descriptor_MaxPower_set
    __swig_getmethods__["MaxPower"] = _libusb.usb_config_descriptor_MaxPower_get
    if _newclass:MaxPower = property(_libusb.usb_config_descriptor_MaxPower_get, _libusb.usb_config_descriptor_MaxPower_set)
    __swig_setmethods__["interface"] = _libusb.usb_config_descriptor_interface_set
    __swig_getmethods__["interface"] = _libusb.usb_config_descriptor_interface_get
    if _newclass:interface = property(_libusb.usb_config_descriptor_interface_get, _libusb.usb_config_descriptor_interface_set)
    __swig_setmethods__["extra"] = _libusb.usb_config_descriptor_extra_set
    __swig_getmethods__["extra"] = _libusb.usb_config_descriptor_extra_get
    if _newclass:extra = property(_libusb.usb_config_descriptor_extra_get, _libusb.usb_config_descriptor_extra_set)
    __swig_setmethods__["extralen"] = _libusb.usb_config_descriptor_extralen_set
    __swig_getmethods__["extralen"] = _libusb.usb_config_descriptor_extralen_get
    if _newclass:extralen = property(_libusb.usb_config_descriptor_extralen_get, _libusb.usb_config_descriptor_extralen_set)
    def __init__(self, *args):
        this = _libusb.new_usb_config_descriptor(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libusb.delete_usb_config_descriptor
    __del__ = lambda self : None;
_libusb.usb_config_descriptor_swigregister(usb_config_descriptor)

class usb_device_descriptor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usb_device_descriptor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usb_device_descriptor, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C usb_device_descriptor instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["bLength"] = _libusb.usb_device_descriptor_bLength_set
    __swig_getmethods__["bLength"] = _libusb.usb_device_descriptor_bLength_get
    if _newclass:bLength = property(_libusb.usb_device_descriptor_bLength_get, _libusb.usb_device_descriptor_bLength_set)
    __swig_setmethods__["bDescriptorType"] = _libusb.usb_device_descriptor_bDescriptorType_set
    __swig_getmethods__["bDescriptorType"] = _libusb.usb_device_descriptor_bDescriptorType_get
    if _newclass:bDescriptorType = property(_libusb.usb_device_descriptor_bDescriptorType_get, _libusb.usb_device_descriptor_bDescriptorType_set)
    __swig_setmethods__["bcdUSB"] = _libusb.usb_device_descriptor_bcdUSB_set
    __swig_getmethods__["bcdUSB"] = _libusb.usb_device_descriptor_bcdUSB_get
    if _newclass:bcdUSB = property(_libusb.usb_device_descriptor_bcdUSB_get, _libusb.usb_device_descriptor_bcdUSB_set)
    __swig_setmethods__["bDeviceClass"] = _libusb.usb_device_descriptor_bDeviceClass_set
    __swig_getmethods__["bDeviceClass"] = _libusb.usb_device_descriptor_bDeviceClass_get
    if _newclass:bDeviceClass = property(_libusb.usb_device_descriptor_bDeviceClass_get, _libusb.usb_device_descriptor_bDeviceClass_set)
    __swig_setmethods__["bDeviceSubClass"] = _libusb.usb_device_descriptor_bDeviceSubClass_set
    __swig_getmethods__["bDeviceSubClass"] = _libusb.usb_device_descriptor_bDeviceSubClass_get
    if _newclass:bDeviceSubClass = property(_libusb.usb_device_descriptor_bDeviceSubClass_get, _libusb.usb_device_descriptor_bDeviceSubClass_set)
    __swig_setmethods__["bDeviceProtocol"] = _libusb.usb_device_descriptor_bDeviceProtocol_set
    __swig_getmethods__["bDeviceProtocol"] = _libusb.usb_device_descriptor_bDeviceProtocol_get
    if _newclass:bDeviceProtocol = property(_libusb.usb_device_descriptor_bDeviceProtocol_get, _libusb.usb_device_descriptor_bDeviceProtocol_set)
    __swig_setmethods__["bMaxPacketSize0"] = _libusb.usb_device_descriptor_bMaxPacketSize0_set
    __swig_getmethods__["bMaxPacketSize0"] = _libusb.usb_device_descriptor_bMaxPacketSize0_get
    if _newclass:bMaxPacketSize0 = property(_libusb.usb_device_descriptor_bMaxPacketSize0_get, _libusb.usb_device_descriptor_bMaxPacketSize0_set)
    __swig_setmethods__["idVendor"] = _libusb.usb_device_descriptor_idVendor_set
    __swig_getmethods__["idVendor"] = _libusb.usb_device_descriptor_idVendor_get
    if _newclass:idVendor = property(_libusb.usb_device_descriptor_idVendor_get, _libusb.usb_device_descriptor_idVendor_set)
    __swig_setmethods__["idProduct"] = _libusb.usb_device_descriptor_idProduct_set
    __swig_getmethods__["idProduct"] = _libusb.usb_device_descriptor_idProduct_get
    if _newclass:idProduct = property(_libusb.usb_device_descriptor_idProduct_get, _libusb.usb_device_descriptor_idProduct_set)
    __swig_setmethods__["bcdDevice"] = _libusb.usb_device_descriptor_bcdDevice_set
    __swig_getmethods__["bcdDevice"] = _libusb.usb_device_descriptor_bcdDevice_get
    if _newclass:bcdDevice = property(_libusb.usb_device_descriptor_bcdDevice_get, _libusb.usb_device_descriptor_bcdDevice_set)
    __swig_setmethods__["iManufacturer"] = _libusb.usb_device_descriptor_iManufacturer_set
    __swig_getmethods__["iManufacturer"] = _libusb.usb_device_descriptor_iManufacturer_get
    if _newclass:iManufacturer = property(_libusb.usb_device_descriptor_iManufacturer_get, _libusb.usb_device_descriptor_iManufacturer_set)
    __swig_setmethods__["iProduct"] = _libusb.usb_device_descriptor_iProduct_set
    __swig_getmethods__["iProduct"] = _libusb.usb_device_descriptor_iProduct_get
    if _newclass:iProduct = property(_libusb.usb_device_descriptor_iProduct_get, _libusb.usb_device_descriptor_iProduct_set)
    __swig_setmethods__["iSerialNumber"] = _libusb.usb_device_descriptor_iSerialNumber_set
    __swig_getmethods__["iSerialNumber"] = _libusb.usb_device_descriptor_iSerialNumber_get
    if _newclass:iSerialNumber = property(_libusb.usb_device_descriptor_iSerialNumber_get, _libusb.usb_device_descriptor_iSerialNumber_set)
    __swig_setmethods__["bNumConfigurations"] = _libusb.usb_device_descriptor_bNumConfigurations_set
    __swig_getmethods__["bNumConfigurations"] = _libusb.usb_device_descriptor_bNumConfigurations_get
    if _newclass:bNumConfigurations = property(_libusb.usb_device_descriptor_bNumConfigurations_get, _libusb.usb_device_descriptor_bNumConfigurations_set)
    def __init__(self, *args):
        this = _libusb.new_usb_device_descriptor(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libusb.delete_usb_device_descriptor
    __del__ = lambda self : None;
_libusb.usb_device_descriptor_swigregister(usb_device_descriptor)

class usb_ctrl_setup(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usb_ctrl_setup, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usb_ctrl_setup, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C usb_ctrl_setup instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["bRequestType"] = _libusb.usb_ctrl_setup_bRequestType_set
    __swig_getmethods__["bRequestType"] = _libusb.usb_ctrl_setup_bRequestType_get
    if _newclass:bRequestType = property(_libusb.usb_ctrl_setup_bRequestType_get, _libusb.usb_ctrl_setup_bRequestType_set)
    __swig_setmethods__["bRequest"] = _libusb.usb_ctrl_setup_bRequest_set
    __swig_getmethods__["bRequest"] = _libusb.usb_ctrl_setup_bRequest_get
    if _newclass:bRequest = property(_libusb.usb_ctrl_setup_bRequest_get, _libusb.usb_ctrl_setup_bRequest_set)
    __swig_setmethods__["wValue"] = _libusb.usb_ctrl_setup_wValue_set
    __swig_getmethods__["wValue"] = _libusb.usb_ctrl_setup_wValue_get
    if _newclass:wValue = property(_libusb.usb_ctrl_setup_wValue_get, _libusb.usb_ctrl_setup_wValue_set)
    __swig_setmethods__["wIndex"] = _libusb.usb_ctrl_setup_wIndex_set
    __swig_getmethods__["wIndex"] = _libusb.usb_ctrl_setup_wIndex_get
    if _newclass:wIndex = property(_libusb.usb_ctrl_setup_wIndex_get, _libusb.usb_ctrl_setup_wIndex_set)
    __swig_setmethods__["wLength"] = _libusb.usb_ctrl_setup_wLength_set
    __swig_getmethods__["wLength"] = _libusb.usb_ctrl_setup_wLength_get
    if _newclass:wLength = property(_libusb.usb_ctrl_setup_wLength_get, _libusb.usb_ctrl_setup_wLength_set)
    def __init__(self, *args):
        this = _libusb.new_usb_ctrl_setup(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libusb.delete_usb_ctrl_setup
    __del__ = lambda self : None;
_libusb.usb_ctrl_setup_swigregister(usb_ctrl_setup)

USB_REQ_GET_STATUS = _libusb.USB_REQ_GET_STATUS
USB_REQ_CLEAR_FEATURE = _libusb.USB_REQ_CLEAR_FEATURE
USB_REQ_SET_FEATURE = _libusb.USB_REQ_SET_FEATURE
USB_REQ_SET_ADDRESS = _libusb.USB_REQ_SET_ADDRESS
USB_REQ_GET_DESCRIPTOR = _libusb.USB_REQ_GET_DESCRIPTOR
USB_REQ_SET_DESCRIPTOR = _libusb.USB_REQ_SET_DESCRIPTOR
USB_REQ_GET_CONFIGURATION = _libusb.USB_REQ_GET_CONFIGURATION
USB_REQ_SET_CONFIGURATION = _libusb.USB_REQ_SET_CONFIGURATION
USB_REQ_GET_INTERFACE = _libusb.USB_REQ_GET_INTERFACE
USB_REQ_SET_INTERFACE = _libusb.USB_REQ_SET_INTERFACE
USB_REQ_SYNCH_FRAME = _libusb.USB_REQ_SYNCH_FRAME
USB_TYPE_STANDARD = _libusb.USB_TYPE_STANDARD
USB_TYPE_CLASS = _libusb.USB_TYPE_CLASS
USB_TYPE_VENDOR = _libusb.USB_TYPE_VENDOR
USB_TYPE_RESERVED = _libusb.USB_TYPE_RESERVED
USB_RECIP_DEVICE = _libusb.USB_RECIP_DEVICE
USB_RECIP_INTERFACE = _libusb.USB_RECIP_INTERFACE
USB_RECIP_ENDPOINT = _libusb.USB_RECIP_ENDPOINT
USB_RECIP_OTHER = _libusb.USB_RECIP_OTHER
USB_ENDPOINT_IN = _libusb.USB_ENDPOINT_IN
USB_ENDPOINT_OUT = _libusb.USB_ENDPOINT_OUT
USB_ERROR_BEGIN = _libusb.USB_ERROR_BEGIN
class usb_device(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usb_device, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usb_device, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C usb_device instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["next"] = _libusb.usb_device_next_set
    __swig_getmethods__["next"] = _libusb.usb_device_next_get
    if _newclass:next = property(_libusb.usb_device_next_get, _libusb.usb_device_next_set)
    __swig_setmethods__["prev"] = _libusb.usb_device_prev_set
    __swig_getmethods__["prev"] = _libusb.usb_device_prev_get
    if _newclass:prev = property(_libusb.usb_device_prev_get, _libusb.usb_device_prev_set)
    __swig_setmethods__["filename"] = _libusb.usb_device_filename_set
    __swig_getmethods__["filename"] = _libusb.usb_device_filename_get
    if _newclass:filename = property(_libusb.usb_device_filename_get, _libusb.usb_device_filename_set)
    __swig_setmethods__["bus"] = _libusb.usb_device_bus_set
    __swig_getmethods__["bus"] = _libusb.usb_device_bus_get
    if _newclass:bus = property(_libusb.usb_device_bus_get, _libusb.usb_device_bus_set)
    __swig_setmethods__["descriptor"] = _libusb.usb_device_descriptor_set
    __swig_getmethods__["descriptor"] = _libusb.usb_device_descriptor_get
    if _newclass:descriptor = property(_libusb.usb_device_descriptor_get, _libusb.usb_device_descriptor_set)
    __swig_setmethods__["config"] = _libusb.usb_device_config_set
    __swig_getmethods__["config"] = _libusb.usb_device_config_get
    if _newclass:config = property(_libusb.usb_device_config_get, _libusb.usb_device_config_set)
    __swig_setmethods__["dev"] = _libusb.usb_device_dev_set
    __swig_getmethods__["dev"] = _libusb.usb_device_dev_get
    if _newclass:dev = property(_libusb.usb_device_dev_get, _libusb.usb_device_dev_set)
    __swig_setmethods__["devnum"] = _libusb.usb_device_devnum_set
    __swig_getmethods__["devnum"] = _libusb.usb_device_devnum_get
    if _newclass:devnum = property(_libusb.usb_device_devnum_get, _libusb.usb_device_devnum_set)
    __swig_setmethods__["num_children"] = _libusb.usb_device_num_children_set
    __swig_getmethods__["num_children"] = _libusb.usb_device_num_children_get
    if _newclass:num_children = property(_libusb.usb_device_num_children_get, _libusb.usb_device_num_children_set)
    __swig_setmethods__["children"] = _libusb.usb_device_children_set
    __swig_getmethods__["children"] = _libusb.usb_device_children_get
    if _newclass:children = property(_libusb.usb_device_children_get, _libusb.usb_device_children_set)
    def __init__(self, *args):
        this = _libusb.new_usb_device(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libusb.delete_usb_device
    __del__ = lambda self : None;
_libusb.usb_device_swigregister(usb_device)

class usb_bus(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usb_bus, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usb_bus, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C usb_bus instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["next"] = _libusb.usb_bus_next_set
    __swig_getmethods__["next"] = _libusb.usb_bus_next_get
    if _newclass:next = property(_libusb.usb_bus_next_get, _libusb.usb_bus_next_set)
    __swig_setmethods__["prev"] = _libusb.usb_bus_prev_set
    __swig_getmethods__["prev"] = _libusb.usb_bus_prev_get
    if _newclass:prev = property(_libusb.usb_bus_prev_get, _libusb.usb_bus_prev_set)
    __swig_setmethods__["dirname"] = _libusb.usb_bus_dirname_set
    __swig_getmethods__["dirname"] = _libusb.usb_bus_dirname_get
    if _newclass:dirname = property(_libusb.usb_bus_dirname_get, _libusb.usb_bus_dirname_set)
    __swig_setmethods__["devices"] = _libusb.usb_bus_devices_set
    __swig_getmethods__["devices"] = _libusb.usb_bus_devices_get
    if _newclass:devices = property(_libusb.usb_bus_devices_get, _libusb.usb_bus_devices_set)
    __swig_setmethods__["location"] = _libusb.usb_bus_location_set
    __swig_getmethods__["location"] = _libusb.usb_bus_location_get
    if _newclass:location = property(_libusb.usb_bus_location_get, _libusb.usb_bus_location_set)
    __swig_setmethods__["root_dev"] = _libusb.usb_bus_root_dev_set
    __swig_getmethods__["root_dev"] = _libusb.usb_bus_root_dev_get
    if _newclass:root_dev = property(_libusb.usb_bus_root_dev_get, _libusb.usb_bus_root_dev_set)
    def __init__(self, *args):
        this = _libusb.new_usb_bus(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libusb.delete_usb_bus
    __del__ = lambda self : None;
_libusb.usb_bus_swigregister(usb_bus)


usb_open = _libusb.usb_open

usb_close = _libusb.usb_close

usb_get_string = _libusb.usb_get_string

usb_get_string_simple = _libusb.usb_get_string_simple

usb_get_descriptor_by_endpoint = _libusb.usb_get_descriptor_by_endpoint

usb_get_descriptor = _libusb.usb_get_descriptor

usb_bulk_write = _libusb.usb_bulk_write

usb_bulk_read = _libusb.usb_bulk_read

usb_interrupt_write = _libusb.usb_interrupt_write

usb_interrupt_read = _libusb.usb_interrupt_read

usb_control_msg = _libusb.usb_control_msg

usb_set_configuration = _libusb.usb_set_configuration

usb_claim_interface = _libusb.usb_claim_interface

usb_release_interface = _libusb.usb_release_interface

usb_set_altinterface = _libusb.usb_set_altinterface

usb_resetep = _libusb.usb_resetep

usb_clear_halt = _libusb.usb_clear_halt

usb_reset = _libusb.usb_reset
LIBUSB_HAS_GET_DRIVER_NP = _libusb.LIBUSB_HAS_GET_DRIVER_NP

usb_get_driver_np = _libusb.usb_get_driver_np
LIBUSB_HAS_DETACH_KERNEL_DRIVER_NP = _libusb.LIBUSB_HAS_DETACH_KERNEL_DRIVER_NP

usb_detach_kernel_driver_np = _libusb.usb_detach_kernel_driver_np

usb_strerror = _libusb.usb_strerror

usb_init = _libusb.usb_init

usb_set_debug = _libusb.usb_set_debug

usb_find_busses = _libusb.usb_find_busses

usb_find_devices = _libusb.usb_find_devices

usb_get_busses = _libusb.usb_get_busses

cvar = _libusb.cvar

