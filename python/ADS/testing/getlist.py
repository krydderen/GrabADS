import pyads
from time import sleep

plc = pyads.Connection('5.46.12.154.1.1',pyads.PORT_TC3PLC1)
plc.open()
print('open')
sleep(1)
################################


x = plc.get_all_symbols()
print(x)
print('\n'.join("%s: %s" % item for item in vars(x[0]).items()))



################################
plc.close()