import pyads
from time import sleep

plc = pyads.Connection('5.46.12.154.1.1',pyads.PORT_TC3PLC1)
plc.open()

plc.write_by_name('HAVL.enable', True)
print('enabled')
sleep(1)
plc.write_by_name('HAVL.forward',True)
print('forward true')
sleep(4)
plc.write_by_name('HAVL.forward',False)
print('forward false')
sleep(2)
plc.write_by_name('HAVL.backwards',True)
print('backward true')
sleep(4)
plc.write_by_name('HAVL.backwards',False)
print('backward false')
sleep(1)
plc.write_by_name('HAVL.enable', False)
print('disabled')

plc.close()