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
    STANDBY     :int    = 0
    HOMINGMODE  :int    = 1
    MANUALMODE  :int    = 2
    
    def __init__(self):
        self.plc = pyads.Connection(self.AMS_ADDRESS, self.PORT)
        logging.basicConfig(format='%(asctime)s | %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
        logging.info('Connected ready.')
        
    def getSymbols(self) -> None:
        ################################################################
        # Global Variable List
        self.grabState          :int    = self.plc.get_symbol('GVL.stateGRAB')
        self.homingDone         :bool   = self.plc.get_symbol('GVL.homingDone')
        
        ################################################################
        # Horizontal Axis 
        self.hEnable            :bool   = self.plc.get_symbol('HAVL.enable')
        self.hEnableMove        :bool   = self.plc.get_symbol('HAVL.enableMove')
        self.hExtend            :bool   = self.plc.get_symbol('HAVL.extend')
        self.hRetract           :bool   = self.plc.get_symbol('HAVL.retract')
        self.hResetError        :bool   = self.plc.get_symbol('HAVL.resetError')
        
        self.hBusy              :bool   = self.plc.get_symbol('HAVL.busy')
        self.hRunning           :bool   = self.plc.get_symbol('HAVL.running')
        self.hDone              :bool   = self.plc.get_symbol('HAVL.done')
        
        self.hTargetPosition    :float  = self.plc.get_symbol('HAVL.targetPosition')
        self.hActualPosition    :float  = self.plc.get_symbol('HAVL.actualPosition')
        self.hActialPositionInt :float  = self.plc.get_symbol('HAVL.actualPositionInt')
        
        ###############################################################
        # Rotational Axis 
        self.rEnable            :bool   = self.plc.get_symbol('RAVL.enable')
        self.hEnableMove        :bool   = self.plc.get_symbol('HAVL.enableMove')
        self.rClockwise         :bool   = self.plc.get_symbol('RAVL.clockwise')
        self.rCounterClockwise  :bool   = self.plc.get_symbol('RAVL.counterClockwise')
        self.rResetError        :bool   = self.plc.get_symbol('RAVL.resetError')
        
        self.rBusy              :bool   = self.plc.get_symbol('RAVL.busy')
        self.rRunning           :bool   = self.plc.get_symbol('RAVL.running')
        self.rDone              :bool   = self.plc.get_symbol('RAVL.done')
        
        self.rTargetPosition    :float  = self.plc.get_symbol('RAVL.targetPosition')
        self.rActualPosition    :float  = self.plc.get_symbol('RAVL.actualPosition')
        self.rActialPositionInt :float  = self.plc.get_symbol('RAVL.actualPositionInt')
        ###############################################################
        # Vertical Axis 
        self.vEnable            :bool   = self.plc.get_symbol('VAVL.enable')
        self.hEnableMove        :bool   = self.plc.get_symbol('HAVL.enableMove')
        self.vAscend            :bool   = self.plc.get_symbol('VAVL.ascend')
        self.vDescend           :bool   = self.plc.get_symbol('VAVL.descend')
        self.vResetError        :bool   = self.plc.get_symbol('VAVL.resetError')
        
    def open(self) -> None:
        try:
            self.plc.open()
            self.CONNECTION = True
            sleep(0.2)
            logging.info('Started')
            self.getSymbols()
        except Exception:
            logging.exception('Shit Broke bro')
    
    def getState(self):
        if self.CONNECTION: logging.info(self.plc.read_state())
    
    def close(self) -> None:
        if self.CONNECTION:
            self.grabState.write(STANDBY)
            self.plc.close()
            self.CONNECTION = False
        logging.info('Stopped')
    
    ######################################################################
    # Global Variable changes
    def standbyMode(self) -> None:
        if self.CONNECTION: grabState.write(STANDBY)
        logging.info('Current State: \t  STANDBY')
        
    def homingMode(self) -> None:
        if self.CONNECTION: grabState.write(HOMINGMODE)
        logging.info('Current State: \t  HOMINGMODE')
        
    def manualMode(self) -> None:
        if self.CONNECTION: grabState.write(MANUALMODE)
        logging.info('Current State: \t  MANUALMODE')
    
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
    
    def resetAllErrors(self):
        if self.CONNECTION:
            self.vResetError.write(True)
            self.rResetError.write(True)
            self.hResetError.write(True)
            
    def startHoming(self):
        if self.CONNECTION:
            # self.grabState.write(1)
            self.homingMode()
            logging.info("ALL Axis:\t HOMING....")
            sleep(0.2)
            print(self.homingDone.read())
            while(not self.homingDone.read()):
                print(self.homingDone.read())
                sleep(0.5)
            self.homingDone.write(False)
            logging.info("ALL Axis:\t HOMING DONE")
            sleep(0.2)
            # Testing GUI
            # self.grabState.write(2)
        else:
            logging.info("ALL Axis:\t HOMING")
            sleep(1)
            logging.info("ALL Axis:\t HOMING DONE")
        
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
        logging.info("Horizontal Axis \t|\t ENABLED")
    
    def disableHorizontalAxis(self):
        if self.CONNECTION: self.hEnable.write(False)
        logging.info("Horizontal Axis \t|\t DISABLED")
        
    def enableRotationalAxis(self) -> None:
        if self.CONNECTION: self.rEnable.write(True)
        logging.info("Rotational Axis \t|\t ENABLED")
    
    def disableRotationalAxis(self) -> None:
        if self.CONNECTION: self.rEnable.write(False)
        logging.info("Rotational Axis \t|\t DISABLED")

    def enableVerticalAxis(self) -> None:
        if self.CONNECTION: self.vEnable.write(True)
        logging.info("Vertical Axis \t|\t ENABLED")
    
    def disableVerticalAxis(self) -> None:
        if self.CONNECTION: self.vEnable.write(False)
        logging.info("Vertical Axis \t|\t DISABLED")
    
    def disableAllAxis(self) -> None:
        if self.CONNECTION: 
            self.disableHorizontalAxis()
            self.disableRotationalAxis()
            self.disableVerticalAxis()
        logging.info('All Axis \t|\t  DISABLED')
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
        
    def stopVertical(self) -> None:
        if self.CONNECTION: self.vAscend.write(False)
        if self.CONNECTION: self.vDescend.write(False)
        logging.info("Vertical Axis |\t STOPPED")
    
    ######################################################################
    # Stop all 
    def stopAllAxis(self) -> None:
        if self.CONNECTION: self.stopVertical();self.stopRotation();self.stopHorizontal()
        logging.info("All Axis |\t STOPPED")
    
    # def disableAllAxis(self) -> None:
        # if self.CONNECTION: self.disableVerticalAxis();self.disableRotation
        
        
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
        