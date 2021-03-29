from re import S
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
    
    def start(self) -> None:
        self.plc.start()
        self.logging.info('Started')
    
    def stop(self) -> None:
        self.plc.stop()
        self.logging.info('Stopped')
    
    def getSymbols(self) -> None:
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
    
    def readHorizontalAxis(self) -> None:
        self.logging.info('Hor. enable\t',       self.hEnable.read())  
        self.logging.info('Hor. forward\t',      self.hForward.read())
        self.logging.info('Hor. backward\t',     self.hBackward.read())
        self.logging.info('Hor. reseterror\t',   self.hResetError.read())
    
    def readRotationalAxis(self) -> None:
        self.logging.info('Rot. enable\t',       self.rEnable.read())  
        self.logging.info('Rot. forward\t',      self.rForward.read())
        self.logging.info('Rot. backward\t',     self.rBackward.read())
        self.logging.info('Rot. reseterror\t',   self.rResetError.read()) 
    
    def resetHorizontalAxis(self) -> None:
        self.hResetError.write(True)
        sleep(self.CMDDELAY)
        self.hResetError.write(False)
        
    def resetRotationalAxis(self) -> None:
        self.rResetError.write(True)
        sleep(self.CMDDELAY)
        self.rResetError.write(False)
        
    def enableHorizontalAxis(self) -> None:
        self.hEnable(True)
        self.logging.info("Horizontal Axis:\t ENABLED")
    
    def disableHorizontalAxis(self) -> None:
        self.hEnable(False)
        self.logging.info("Horizontal Axis:\t DISABLED")
        
    def enableRotationalAxis(self) -> None:
        self.rEnable(True)
        self.logging.info("Rotational Axis:\t ENABLED")
    
    def disableRotationalAxis(self) -> None:
        self.rEnable(False)
        self.logging.info("Rotational Axis:\t DISABLED")
    
    def startExtendSnake(self) -> None:
        self.hForward(True)
        self.logging.info("Horizontal Moving:\t FORWARD")
        
    def stopExtendSnake(self) -> None:
        self.hForward(False)
        self.logging.info("Horizontal Stopped")
        
    def startRetractSnake(self) -> None:
        self.hBackward(True)
        self.logging.info("Horizontal Moving:\t BACKWARD")
        
    def stopRetractSnake(self) -> None:
        self.hBackward(False)
        self.logging.info("Horizontal Stopped")
        
    def moveRotationClockwise(self) -> None:
        self.rForward(True)
        self.logging.info("Rotation Moving:\t CLOCKWISE")
        
    def stopRotationClockwise(self) -> None:
        self.rForward(False)
        self.logging.info("Rotation Stopped")
        
    def moveRotationCounterClockwise(self) -> None:
        self.rBackward(True)
        self.logging.info("Rotation Moving:\t COUNTER CLOCKWISE")
        
    def stopRotationCounterClockwise(self) -> None:
        self.rBackward(False)
        self.logging.info("Rotation Stopped")
    
    def stopHorizontal(self) -> None:
        self.hForward(False)
        self.hBackward(False)
        self.logging.info("Horizontal Stopped")
        
    def stopRotation(self) -> None:
        self.rforward(False)
        self.rBackward(False)
        self.logging.info("Rotation Stopped")
    
    def runTest(self) -> None:
        self.start()
        self.getSymbols()
        self.readHorizontalAxis()
        self.readRotationalAxis()
        self.resetHorizontalAxis()
        self.resetRotationalAxis()
        self.enableHorizontalAxis()
        self.enableRotationalAxis()
        self.startExtendSnake()
        sleep(1)
        self.stopExtendSnake()
        sleep(0.5)
        self.startRetractSnake()
        sleep(1)
        self.stopRetractSnake()
        sleep(0.5)
        self.moveRotationCounterClockwise()
        sleep(1)
        self.stopRotationCounterClockwise()
        sleep(0.5)
        self.moveRotationClockwise()
        sleep(1)
        self.stopRotationClockwise()
        sleep(0.5)
        self.disableHorizontalAxis()
        self.disableRotationalAxis()
        self.stop()
        