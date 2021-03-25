from python.ADS.testing.pyadstest import DRIVETIME
import pyads
import logging
from time import sleep

class MotorController(object):
    AMS_ADDRESS :str    = '5.46.12.154.1.1'
    PORT        :int    = pyads.PORT_TC3PLC1
    WAITTIME    :float  = 0.5
    DRIVETIME   :float  = 1
    CMDDELAY    :float  = 0.2
    
    def __init__(self):
        self.plc = pyads.Connection(self.AMS_ADDRESS, self.PORT)
        self.logging.info('Connected established.')
    
    def start(self):
        self.plc.start()
        self.logging.info('Started')
    
    def stop(self):
        self.plc.stop()
        self.logging.info('Stopped')
    
    def getSymbols(self):
        ################################################################
        # Horizontal Axis 
        self.hEnable      = self.plc.get_symbol('HAVL.enable')
        self.hForward     = self.plc.get_symbol('HAVL.forward')
        self.hBackward    = self.plc.get_symbol('HAVL.backwards')
        self.hResetError  = self.plc.get_symbol('HAVL.resetError')
        
        ###############################################################
        # Rotational Axis 
        self.hEnable      = self.plc.get_symbol('RAVL.enable')
        self.hForward     = self.plc.get_symbol('RAVL.forward')
        self.hBackward    = self.plc.get_symbol('RAVL.backwards')
        self.hResetError  = self.plc.get_symbol('RAVL.resetError')
    
    def readHorizontalAxis(self):
        self.logging.info('Hor. enable\t',       self.hEnable.read())  
        self.logging.info('Hor. forward\t',      self.hForward.read())
        self.logging.info('Hor. backward\t',     self.hBackward.read())
        self.logging.info('Hor. reseterror\t',   self.hResetError.read())
    
    def readRotationalAxis(self):
        self.logging.info('Rot. enable\t',       self.rEnable.read())  
        self.logging.info('Rot. forward\t',      self.rForward.read())
        self.logging.info('Rot. backward\t',     self.rBackward.read())
        self.logging.info('Rot. reseterror\t',   self.rResetError.read()) 
    
    def resetHorizontalAxis(self):
        self.hResetError.write(True)
        sleep(self.CMDDELAY)
        self.hResetError.write(False)
        
    def resetRotationalAxis(self):
        self.rResetError.write(True)
        sleep(self.CMDDELAY)
        self.rResetError.write(False)
        
    def enableHorizontalAxis(self):
        self.hEnable(True)
        self.logging.info("Horizontal Axis:\t ENABLED")
    
    def disableHorizontalAxis(self):
        self.hEnable(False)
        self.logging.info("Horizontal Axis:\t DISABLED")
        
    def enableRotationalAxis(self):
        self.rEnable(True)
        self.logging.info("Rotational Axis:\t ENABLED")
    
    def disableRotationalAxis(self):
        self.rEnable(False)
        self.logging.info("Rotational Axis:\t DISABLED")
    
    def moveHorizontalForward(self):
        self.hForward(True)
        self.logging.info("Horizontal Moving:\t FORWARD")
        
    def stopHorizontalForward(self):
        self.hForward(False)
        self.logging.info("Horizontal Stopped")
        
    def moveHorizontalBackward(self):
        self.hBackward(True)
        self.logging.info("Horizontal Moving:\t BACKWARD")
        
    def stopHorizontalBackward(self): 
        self.hBackward(False)
        self.logging.info("Horizontal Stopped")
        
    def moveRotationClockwise(self):
        self.rForward(True)
        self.logging.info("Rotation Moving:\t CLOCKWISE")
        
    def stopRotationClockwise(self):
        self.rForward(False)
        self.logging.info("Rotation Stopped")
        
    def moveRotationCounterClockwise(self):
        self.rBackward(True)
        self.logging.info("Rotation Moving:\t COUNTER CLOCKWISE")
        
    def stopRotationCounterClockwise(self): 
        self.rBackward(False)
        self.logging.info("Rotation Stopped")
    
    def stopHorizontal(self):
        self.hForward(False)
        self.hBackward(False)
        self.logging.info("Horizontal Stopped")
        
    def stopRotation(self):
        self.rforward(False)
        self.rBackward(False)
        self.logging.info("Rotation Stopped")
        