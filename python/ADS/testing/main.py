import pyads
import logging
from time import sleep

class GRAB(object):
    AMS_ADDRESS :str    = '5.46.12.154.1.1'
    PORT        :int    = pyads.PORT_TC3PLC1
    WAITTIME    :float  = 0.5
    DRIVETIME   :float  = 1
    CMDDELAY    :float  = 0.2
    CONNECTION  :bool   = False
    
    def __init__(self):
        self.plc = pyads.Connection(self.AMS_ADDRESS, self.PORT)
        logging.basicConfig(format='%(asctime)s | %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
        logging.info('Connected ready.')
        
    def getSymbols(self) -> None:
        ################################################################
        # Grab State
        self.grabState          = self.plc.get_symbol('GVL.grabState')
        
        ################################################################
        # Horizontal Axis 
        self.hEnable            = self.plc.get_symbol('HAVL.enable')
        self.hExtend            = self.plc.get_symbol('HAVL.extend')
        self.hRetract           = self.plc.get_symbol('HAVL.retract')
        self.hResetError        = self.plc.get_symbol('HAVL.resetError')
        
        ###############################################################
        # Rotational Axis 
        self.rEnable            = self.plc.get_symbol('RAVL.enable')
        self.rClockwise         = self.plc.get_symbol('RAVL.clockwise')
        self.rCounterClockwise  = self.plc.get_symbol('RAVL.counterClockwise')
        self.rResetError        = self.plc.get_symbol('RAVL.resetError')
        
        ###############################################################
        # Vertical Axis 
        self.vEnable            = self.plc.get_symbol('VAVL.enable')
        self.vAscend            = self.plc.get_symbol('VAVL.ascend')
        self.vDescend           = self.plc.get_symbol('VAVL.descend')
        self.vResetError        = self.plc.get_symbol('VAVL.resetError')
        
    def open(self) -> None:
        try:
            self.plc.open()
            self.CONNECTION = True
            logging.info('Started')
            self.plc.getSymbols()
        except Exception:
            logging.exception('Shit Broke bro')
    
    def getState(self):
        if self.CONNECTION: logging.info(self.plc.read_state())
    
    def close(self) -> None:
        if self.CONNECTION:
            self.plc.stop()
            self.CONNECTION = False
        logging.info('Stopped')
    
    ######################################################################
    # Reading the different axis
    def readHorizontalAxis(self) -> None:
        if self.CONNECTION:
            logging.info('Horizontal Axis: ENABLED\t|'          ,   self.hEnable.read())  
            logging.info('Horizontal Axis: EXTEND\t|'           ,   self.hExtend.read())
            logging.info('Horizontal Axis: RETRACT\t|'          ,   self.hRetract.read())
            logging.info('Horizontal Axis: RESETERROR\t|'       ,   self.hResetError.read())
    
    def readRotationalAxis(self) -> None:
        if self.CONNECTION:
            logging.info('Rotational Axis: ENABLED\t|'          ,   self.rEnable.read())  
            logging.info('Rotational Axis: Clockwise\t|'        ,   self.rClockwise.read())
            logging.info('Rotational Axis: CounterClockwise\t|' ,   self.rCounterClockwise.read())
            logging.info('Rotational Axis: RESETERROR\t|'       ,   self.rResetError.read()) 
    
    def readVerticalAxis(self) -> None:
        if self.CONNECTION:
            logging.info('Vertical Axis: ENABLED\t|'            ,   self.vEnable.read())  
            logging.info('Vertical Axis: ASCEND\t|'             ,   self.vExtend.read())
            logging.info('Vertical Axis: DESCEND\t|'            ,   self.vRetract.read())
            logging.info('Vertical Axis: RESETERROR\t|'         ,   self.vResetError.read())
    
    def readAllAxis(self) -> None:
        self.readHorizontalAxis()
        self.readRotationalAxis()
        self.readVerticalAxis()
    
    ######################################################################
    # Resetting different axis
    def resetHorizontalAxis(self) -> None:
        if self.CONNECTION:
            self.hResetError.write(True)
            sleep(self.CMDDELAY)
            self.hResetError.write(False)
        logging.info("Horizontal Axis:\t RESET")
        
    def resetRotationalAxis(self) -> None:
        if self.CONNECTION:
            self.rResetError.write(True)
            sleep(self.CMDDELAY)
            self.rResetError.write(False)
        logging.info("Rotation Axis:\t RESET")
    
    def resetVerticalAxis(self) -> None:
        if self.CONNECTION:
            self.vResetError.write(True)
            sleep(self.CMDDELAY)
            self.vResetError.write(False)
        logging.info("Vertical Axis:\t RESET")
    
    def resetAllAxis(self) -> None:
        logging.info("ALL AXIS:\t RESETTING...")
        if self.CONNECTION:
            self.resetHorizontalAxis()
            self.readRotationalAxis()
            self.resetVerticalAxis()
    ######################################################################
    # Enable or disable
    def enableHorizontalAxis(self):
        if self.CONNECTION: self.hEnable.write(True)
        logging.info("Horizontal Axis:\t ENABLED")
    
    def disableHorizontalAxis(self):
        if self.CONNECTION: self.hEnable.write(False)
        logging.info("Horizontal Axis:\t DISABLED")
        
    def enableRotationalAxis(self) -> None:
        if self.CONNECTION: self.rEnable.write(True)
        logging.info("Rotational Axis:\t ENABLED")
    
    def disableRotationalAxis(self) -> None:
        if self.CONNECTION: self.rEnable.write(False)
        logging.info("Rotational Axis:\t DISABLED")

    def enableVerticalAxis(self) -> None:
        if self.CONNECTION: self.vEnable.write(True)
        logging.info("Vertical Axis:\t ENABLED")
    
    def disableVerticalAxis(self) -> None:
        if self.CONNECTION: self.vEnable.write(False)
        logging.info("Vertical Axis:\t DISABLED")
    
    ######################################################################
    # Operation for horizontal axis
    def startExtendSnake(self):
        if self.CONNECTION: self.hExtend.write(True)
        logging.info("Horizontal Axis |\t EXTENDING")
        
    def stopExtendSnake(self):
        if self.CONNECTION: self.hExtend.write(False)
        logging.info("Horizontal Axis |\t STOPPED")
        
    def startRetractSnake(self):
        if self.CONNECTION: self.hRetract.write(True)
        logging.info("Horizontal Axis |\t RETRACTING")
        
    def stopRetractSnake(self):
        if self.CONNECTION: self.hRetract.write(False)
        logging.info("Horizontal Axis |\t STOPPED")
        
    def stopHorizontal(self) -> None:
        if self.CONNECTION: self.hExtend.write(False)
        if self.CONNECTION: self.hRetract.write(False)
        logging.info("Horizontal Axis |\t STOPPED")
    
    ######################################################################
    # Operation for rotation axis
    def moveRotationClockwise(self) -> None:
        if self.CONNECTION: self.rClockwise.write(True)
        logging.info("Rotation Axis |\t CLOCKWISE")
        
    def stopRotationClockwise(self) -> None:
        if self.CONNECTION: self.rClockwise.write(False)
        logging.info("Rotation Axis |\t STOPPED")
        
    def moveRotationCounterClockwise(self) -> None:
        if self.CONNECTION: self.rCounterClockwise.write(True)
        logging.info("Rotation Axis |\t COUNTERCLOCKWISE")
        
    def stopRotationCounterClockwise(self) -> None:
        if self.CONNECTION: self.rCounterClockwise.write(False)
        logging.info("Rotation Axis |\t STOPPED")
    
    def stopRotation(self) -> None:
        if self.CONNECTION: self.rClockwise.write(False)
        if self.CONNECTION: self.rCounterClockwise.write(False)
        logging.info("Rotation Axis |\t STOPPED")
    
    ######################################################################
    # Operation for vertical axis
    def ascendVerticalAxis(self) -> None:
        if self.CONNECTION: self.vAscend.write(True)
        logging.info("Vertical Axis |\t ASCENDING")
        
    def descendVerticalAxis(self) -> None:
        if self.CONNECTION: self.vDescend.write(True)
        logging.info("Vertical Axis |\t DESCENDING")
        
    def stopVerticalAxis(self) -> None:
        if self.CONNECTION: self.vAscend.write(False)
        if self.CONNECTION: self.vDescend.write(False)
        logging.info("Vertical Axis |\t STOPPED")
    
    ######################################################################
    # Testing functions
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
        