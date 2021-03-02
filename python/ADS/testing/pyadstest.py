import pyads
from time import sleep

plc = pyads.Connection('5.46.12.154.1.1',pyads.PORT_TC3PLC1)
plc.open()
print('open')
sleep(1)
print(plc.read_state())
# input('Enter to continue..')
################################################################
# Setup symbols
################################################################
# Horizontal Axis 
################################################################
hEnable      = plc.get_symbol('HAVL.enable')
hForward     = plc.get_symbol('HAVL.forward')
hBackward    = plc.get_symbol('HAVL.backwards')
hResetError  = plc.get_symbol('HAVL.resetError')
################################################################
# Rotational Axis 
################################################################
rEnable      = plc.get_symbol('RAVL.enable')
rForward     = plc.get_symbol('RAVL.forward')
rBackward    = plc.get_symbol('RAVL.backwards')
rResetError  = plc.get_symbol('RAVL.resetError')

################################################################
# Testing symbols
################################################################
hEnable.write(False)
hForward.write(False)
hBackward.write(False)

rEnable.write(False)
rForward.write(False)
rBackward.write(False)

print('Hor enable\t',hEnable.read())  
print('Hor forward\t',hForward.read())
print('Hor backward\t',hBackward.read())
print('Hor reseterror\t',hResetError.read())

print('\n')

print('Rot enable\t',rEnable.read())  
print('Rot forward\t',rForward.read())
print('Rot backward\t',rBackward.read())
print('Rot reseterror\t',rResetError.read())

input('Enter to continue..')

################################################################
# Resetting eventual error codes
################################################################
print('resetting')
hResetError.write(True)
sleep(1)
hResetError.write(False)
sleep(1)
print('Hor Error\t',hResetError.read())

print('\n')

rResetError.write(True)
sleep(1)
rResetError.write(False)
sleep(1)
print('Rot Error\t', rResetError.read())

input('Enter to continue..')


################################################################
# Driving Horizontal Axis 
################################################################
sleep(1)
hEnable.write(True)
# rEnable.write(True)
print('enable \t', hEnable.read())
sleep(2)
hForward.write(True)
# rForward.write(True)
print('forward \t', hForward.read())
sleep(4)
hForward.write(False)
# rForward.write(False)
print('forward \t', hForward.read())
sleep(2)
hBackward.write(True)
#rBackward.write(True)
print('backward \t', hBackward.read())
sleep(4)
hBackward.write(False)
#rBackward.write(False)
print('backward \t', hBackward.read())
sleep(2)
hEnable.write(False)
#rEnable.write(False)
print('enabled \t', hEnable.read())
sleep(1)

################################################################
# Driving Rotational Axis 
################################################################
sleep(1)
# hEnable.write(True)
rEnable.write(True)
print('enable \t', rEnable.read())
sleep(2)
# hForward.write(True)
rForward.write(True)
print('forward \t', rForward.read())
sleep(4)
# hForward.write(False)
rForward.write(False)
print('forward \t', rForward.read())
sleep(2)
# hBackward.write(True)
rBackward.write(True)
print('backward \t', rBackward.read())
sleep(4)
# hBackward.write(False)
rBackward.write(False)
print('backward \t', rBackward.read())
sleep(2)
# hEnable.write(False)
rEnable.write(False)
print('enabled \t', rEnable.read())
sleep(1)


##############################################################
# Close the connection 
##############################################################
plc.close()
print('closed')
