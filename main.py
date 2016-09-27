# main program to run USBB

import os, shutil, sys, time
# from datetime import date, timedelta

class getconnection:
    def drivedata(self):
        pass

    def isempty(self):
        os.chdir('/Volumes')    # jumping to Drives List in MBP
        emptyMountedList = ['Macintosh HD']  # Only for MBP
        mountedList = os.listdir()
        if emptyMountedList == mountedList :
            return True  # method was well done
        else:
            del mountedList[mountedList.index('Macintosh HD')]
            return mountedList  # method must be reruned

    def firstdevice(self):
        while True:
            mountedlist = os.listdir()
            if 'Macintosh HD' != mountedlist:
                del mountedlist[mountedlist.index('Macintosh HD')]
                # print('Was plugged: ', mountedList )
                firstusb = mountedlist
                return firstusb

    def seconddevice(self, usb1):
        inserted = os.listdir()
        while True:
            if os.listdir() == inserted:
                pass
            else:
                inserted = os.listdir()
                print("Flash 2 was inserted", os.listdir())
                inserted.remove('Macintosh HD')
                usbtwoo = set(inserted).difference(usb1)

                return usbtwoo

            #print(mountedlist, "-----", usb1)
            '''if 'Macintosh HD' != mountedlist:
                del mountedlist[mountedlist.index('Macintosh HD')]
                # print('Was plugged: ', mountedList )
                firstusb = mountedlist
                return firstusb'''

    def comparison(self):  # we are need to compare size of copyed data
        pass

    def backup(self):
        substring = '/Volumes/'

        pass


# print("Plugged device is:", usbPlug())
connection = getconnection()  # creating example of class connection
if True == connection.isempty(): # test for usb ports: there must be empty
    print('* Drive initialization is correct')
else:
    print('***** USB ports must be free of flash in the start of backup\n'
          'Please unmount following devices: ', connection.isempty())
if True == connection.isempty():
    print('Please insert first USB drive:')
while True == connection.isempty():
    pass
else:
    usb1 = connection.firstdevice()
    print("First USB was: ", usb1, "\n"
          "* All data will be copied to this drive","\n"
          "Please insert second USB for Backup: ")
    usb2 = connection.seconddevice(usb1)
    print('Second USB is: ', usb2
          "* Now we are ready to copy files")
    # connection.drivedata()  # data about size of usb, name and other


# print(connection.firstDevice())
