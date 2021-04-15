import pyads
import logging
from time import sleep

class GRAB(object):
    AMS_ADDRESS :str    = '5.46.12.154.1.1'
    PORT        :int    = pyads.PORT_TC3PLC1
    WAITTIME    :float  = 0.5
    DRIVETIME   :float  = 1
    CMDDELAY    :float  = 0.5
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
        
        self.hEnableMove        :bool   = self.plc.get_symbol('HAVL.enableMove')
        self.hTargetPosition    :float  = self.plc.get_symbol('HAVL.targetPosition')
        self.hActualPosition    :float  = self.plc.get_symbol('HAVL.actualPosition')
        self.hActualPositionInt :int    = self.plc.get_symbol('HAVL.actualPositionInt')
        
        self.hCurrentErrorPower     = self.plc.get_symbol('HAVL.currentErrorPower')
        self.hCurrentErrorCmd       = self.plc.get_symbol('HAVL.currentErrorCommand') 
        
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
        
        self.rEnableMove        :bool   = self.plc.get_symbol('RAVL.enableMove')
        self.rTargetPosition    :float  = self.plc.get_symbol('RAVL.targetPosition')
        self.rActualPosition    :float  = self.plc.get_symbol('RAVL.actualPosition')
        self.rActualPositionInt :int    = self.plc.get_symbol('RAVL.actualPositionInt')
        
        self.rCurrentErrorPower     = self.plc.get_symbol('RAVL.currentErrorPower')
        self.rCurrentErrorCmd       = self.plc.get_symbol('RAVL.currentErrorCommand') 
        ###############################################################
        # Vertical Axis 
        self.vEnable            :bool   = self.plc.get_symbol('VAVL.enable')
        self.hEnableMove        :bool   = self.plc.get_symbol('HAVL.enableMove')
        self.vAscend            :bool   = self.plc.get_symbol('VAVL.ascend')
        self.vDescend           :bool   = self.plc.get_symbol('VAVL.descend')
        self.vResetError        :bool   = self.plc.get_symbol('VAVL.resetError')
        
        self.vBusy              :bool   = self.plc.get_symbol('VAVL.busy')
        self.vRunning           :bool   = self.plc.get_symbol('VAVL.running')
        self.vDone              :bool   = self.plc.get_symbol('VAVL.done')
        
        self.vEnableMove        :bool   = self.plc.get_symbol('VAVL.enableMove')
        self.vTargetPosition    :float  = self.plc.get_symbol('VAVL.targetPosition')
        self.vActualPosition    :float  = self.plc.get_symbol('VAVL.actualPosition')
        self.vActualPositionInt :int    = self.plc.get_symbol('VAVL.actualPositionInt')
        
        self.vCurrentErrorPower     = self.plc.get_symbol('VAVL.currentErrorPower')
        self.vCurrentErrorCmd       = self.plc.get_symbol('VAVL.currentErrorCommand') 
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
            self.grabState.write(0)
            self.plc.close()
            self.CONNECTION = False
        logging.info('Stopped')
    
    ######################################################################
    # Global Variable changes
    def standbyMode(self) -> None:
        if self.CONNECTION: self.grabState.write(0)
        logging.info('Current State \t|\t STANDBY')
        
    def homingMode(self) -> None:
        if self.CONNECTION: self.grabState.write(1)
        logging.info('Current State \t|\t HOMINGMODE')
        
    def manualMode(self) -> None:
        if self.CONNECTION: self.grabState.write(2)
        logging.info('Current State \t|\t MANUALMODE')
    
    def positionMode(self) -> None:
        if self.CONNECTION: self.grabState.write(3)
        logging.info('Currentstate \t|\t POSITIONMODE')
    
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
    
    def startHoming(self):
        if self.CONNECTION:
            # self.grabState.write(1)
            self.homingMode()
            logging.info("ALL Axis \t|\t HOMING....")
            sleep(0.2)
            print(self.homingDone.read())
            while(not self.homingDone.read()):
                print(self.homingDone.read())
                sleep(0.5)
            self.homingDone.write(False)
            logging.info("ALL Axis \t|\t HOMING DONE")
            sleep(0.2)
            # Testing GUI
            # self.grabState.write(2)
        else:
            logging.info("ALL Axis \t|\t HOMING")
            sleep(1)
            logging.info("ALL Axis \t|\t HOMING DONE")
        
    ######################################################################
    # Resetting different axis
    def resetHorizontalAxis(self) -> None:
        if self.CONNECTION:
            self.hResetError.write(True)
            sleep(self.CMDDELAY)
            self.hResetError.write(False)
        logging.debug("Horizontal Axis \t|\t RESET")
        
    def resetRotationalAxis(self) -> None:
        if self.CONNECTION:
            self.rResetError.write(True)
            sleep(self.CMDDELAY)
            self.rResetError.write(False)
        logging.debug("Rotation Axis: \t|\t RESET")
    
    def resetVerticalAxis(self) -> None:
        if self.CONNECTION:
            self.vResetError.write(True)
            sleep(self.CMDDELAY)
            self.vResetError.write(False)
        logging.debug("Vertical Axis \t|\t RESET")
    
    def resetAllAxis(self) -> None:
        logging.info("ALL AXIS \t|\t RESETTING...")
        if self.CONNECTION:
            self.resetHorizontalAxis()
            self.resetRotationalAxis()
            self.resetVerticalAxis()
        logging.info("ALL AXIS \t|\t RESET")
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
    
    def enableAllAxis(self) -> None:
        if self.CONNECTION: 
            self.enableHorizontalAxis()
            self.enableRotationalAxis()
            self.enableVerticalAxis()
        logging.info('All Axis \t|\t  ENABLED')
    
    def disableAllAxis(self) -> None:
        if self.CONNECTION: 
            self.disableHorizontalAxis()
            self.disableRotationalAxis()
            self.disableVerticalAxis()
        logging.info('All Axis \t|\t DISABLED')
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
        logging.info("All Axis \t|\t STOPPED")
    
    # def disableAllAxis(self) -> None:
        # if self.CONNECTION: self.disableVerticalAxis();self.disableRotation
        
    
    
    ######################################################################
    # Position mode, change this to take in args to decide manual or standby.
    
    def zeroManualHorizontal(self):
        self.positionMode()
        sleep(self.CMDDELAY)
        self.hTargetPosition.write(0)
        sleep(self.CMDDELAY)
        self.hEnableMove.write(True)
        sleep(self.CMDDELAY)
        self.hEnableMove.write(False)
        while(self.hBusy.read()):
            logging.info('Moving Horizontal to zero...')
            sleep(0.5)
        logging.info('Moving done...')
        self.manualMode()
    
    def zeroManualRotational(self):
        self.positionMode()
        sleep(self.CMDDELAY)
        self.rTargetPosition.write(0)
        sleep(self.CMDDELAY)
        self.rEnableMove.write(True)
        sleep(self.CMDDELAY)
        self.rEnableMove.write(False)
        while(self.rBusy.read()):
            logging.info('Moving Horizontal to zero...')
            sleep(0.5)
        logging.info('Moving done...')
        self.manualMode()
    
    def zeroManualVertical(self):
        self.positionMode()
        sleep(self.CMDDELAY)
        self.vTargetPosition.write(0)
        sleep(self.CMDDELAY)
        self.vEnableMove.write(True)
        sleep(self.CMDDELAY)
        self.vEnableMove.write(False)
        while(self.vBusy.read()):
            logging.info('Moving Horizontal to zero...')
            sleep(0.5)
        logging.info('Moving done...')
        self.manualMode()
        
    # PickBox Position method
    def movePosHorizontal(self, pos):
        sleep(self.CMDDELAY)
        self.hTargetPosition.write(pos)
        
        sleep(self.CMDDELAY)
        self.hEnableMove.write(True)
        sleep(self.CMDDELAY)
        self.hEnableMove.write(False)
        
        while(self.hBusy.read()):
            logging.info('Moving Horizontal to zero...')
            sleep(0.5)
        logging.info('Moving done...')
    
    def movePosRotational(self, pos):
        sleep(self.CMDDELAY)
        self.rTargetPosition.write(pos)
        
        sleep(self.CMDDELAY)
        self.rEnableMove.write(True)
        sleep(self.CMDDELAY)
        self.rEnableMove.write(False)
        
        while(self.rBusy.read()):
            logging.info('Moving Horizontal to zero...')
            sleep(0.5)
        logging.info('Moving done...')
    
    # Checks CMD or POWER error from given AXIS
    def checkError(self, currentErrorPower, currentCmdError):
        if currentErrorPower.read() != 0:
            raise Exception('Power Error: \t'+ str(currentErrorPower.read()))
        elif currentCmdError.read() != 0:
            raise Exception('Cmd Error: \t'+ str(currentCmdError.read()))
        else:
            pass
    
    # Universal MovePos method using given axis parameters.
    def movePosTarget(self, pos : int, targetPos, currentPos, enableMove, currentErrorPower, currentCmdError, busy):
        self.checkError(currentErrorPower, currentCmdError)
        sleep(self.CMDDELAY)
        targetPos.write(pos)
        sleep(self.CMDDELAY)
        enableMove.write(True)
        sleep(self.CMDDELAY)
        enableMove.write(False)
        sleep(self.CMDDELAY)
        self.checkError(currentErrorPower, currentCmdError)
        sleep(self.CMDDELAY)
        
        logging.info('Moving...')
        while(busy.read()):
            logging.debug('Moving..')
            logging.info('Position \t|\t' + str(currentPos.read()))
            sleep(0.1)
            self.checkError(currentErrorPower, currentCmdError)
        logging.info('Moving done...')
        
        
    ######################################################################
    # Testing functions
    
    ################################################################
    # New Pickbox method 
    def newPickBox(self) -> None:
        try:
            self.positionMode()
            sleep(self.CMDDELAY)
            self.enableAllAxis()
            sleep(1)
            
            # Start movement 
            # Start by moving everyone to ZERO.
            self.movePosTarget(0,
                                self.hTargetPosition,
                                self.hActualPositionInt,
                                self.hEnableMove,
                                self.hCurrentErrorPower,
                                self.hCurrentErrorCmd,
                                self.hBusy)
            self.movePosTarget(0,
                                self.rTargetPosition,
                                self.rActualPositionInt,
                                self.rEnableMove,
                                self.rCurrentErrorPower,
                                self.rCurrentErrorCmd,
                                self.rBusy)
            self.movePosTarget(0,
                                self.vTargetPosition,
                                self.vActualPositionInt,
                                self.vEnableMove,
                                self.vCurrentErrorPower,
                                self.vCurrentErrorCmd,
                                self.vBusy)
            
            #Ascend to given position before reaching for box
            self.movePosTarget(730,
                                self.vTargetPosition,
                                self.vActualPositionInt,
                                self.vEnableMove,
                                self.vCurrentErrorPower,
                                self.vCurrentErrorCmd,
                                self.vBusy)
            # Rotate towards table
            self.movePosTarget(90,
                                self.rTargetPosition,
                                self.rActualPositionInt,
                                self.rEnableMove,
                                self.rCurrentErrorPower,
                                self.rCurrentErrorCmd,
                                self.rBusy)
            # Reach out for box
            self.movePosTarget(500,
                                self.hTargetPosition,
                                self.hActualPositionInt,
                                self.hEnableMove,
                                self.hCurrentErrorPower,
                                self.hCurrentErrorCmd,
                                self.hBusy)
            # Lift the box
            self.movePosTarget(900,
                                self.vTargetPosition,
                                self.vActualPositionInt,
                                self.vEnableMove,
                                self.vCurrentErrorPower,
                                self.vCurrentErrorCmd,
                                self.vBusy)
            # Pull the box in
            self.movePosTarget(0,
                                self.hTargetPosition,
                                self.hActualPositionInt,
                                self.hEnableMove,
                                self.hCurrentErrorPower,
                                self.hCurrentErrorCmd,
                                self.hBusy)
            # Rotate to zero, before lowering
            self.movePosTarget(0,
                                self.rTargetPosition,
                                self.rActualPositionInt,
                                self.rEnableMove,
                                self.rCurrentErrorPower,
                                self.rCurrentErrorCmd,
                                self.rBusy)
            # Descend down to pallet
            self.movePosTarget(269,
                                self.vTargetPosition,
                                self.vActualPositionInt,
                                self.vEnableMove,
                                self.vCurrentErrorPower,
                                self.vCurrentErrorCmd,
                                self.vBusy)
            # Extend snake to position box on pallet.
            self.movePosTarget(500,
                                self.hTargetPosition,
                                self.hActualPositionInt,
                                self.hEnableMove,
                                self.hCurrentErrorPower,
                                self.hCurrentErrorCmd,
                                self.hBusy)
            # Descend to let go of box
            self.movePosTarget(145,
                                self.vTargetPosition,
                                self.vActualPositionInt,
                                self.vEnableMove,
                                self.vCurrentErrorPower,
                                self.vCurrentErrorCmd,
                                self.vBusy)
            # Retract snake to zero
            self.movePosTarget(0,
                                self.hTargetPosition,
                                self.hActualPositionInt,
                                self.hEnableMove,
                                self.hCurrentErrorPower,
                                self.hCurrentErrorCmd,
                                self.hBusy)
            # Extend snake to position box on pallet.
            self.movePosTarget(500,
                                self.hTargetPosition,
                                self.hActualPositionInt,
                                self.hEnableMove,
                                self.hCurrentErrorPower,
                                self.hCurrentErrorCmd,
                                self.hBusy)
            # Ascend box up from pallet
            self.movePosTarget(260,
                                self.vTargetPosition,
                                self.vActualPositionInt,
                                self.vEnableMove,
                                self.vCurrentErrorPower,
                                self.vCurrentErrorCmd,
                                self.vBusy)
            # Retract snake to zero
            self.movePosTarget(0,
                                self.hTargetPosition,
                                self.hActualPositionInt,
                                self.hEnableMove,
                                self.hCurrentErrorPower,
                                self.hCurrentErrorCmd,
                                self.hBusy)
            # Lift the box
            self.movePosTarget(900,
                                self.vTargetPosition,
                                self.vActualPositionInt,
                                self.vEnableMove,
                                self.vCurrentErrorPower,
                                self.vCurrentErrorCmd,
                                self.vBusy)
            # Rotate towards table
            self.movePosTarget(90,
                                self.rTargetPosition,
                                self.rActualPositionInt,
                                self.rEnableMove,
                                self.rCurrentErrorPower,
                                self.rCurrentErrorCmd,
                                self.rBusy)
            # Extend snake to position box on pallet.
            self.movePosTarget(500,
                                self.hTargetPosition,
                                self.hActualPositionInt,
                                self.hEnableMove,
                                self.hCurrentErrorPower,
                                self.hCurrentErrorCmd,
                                self.hBusy)
            #Ascend to given position before reaching for box
            self.movePosTarget(730,
                                self.vTargetPosition,
                                self.vActualPositionInt,
                                self.vEnableMove,
                                self.vCurrentErrorPower,
                                self.vCurrentErrorCmd,
                                self.vBusy)
            # Retract snake to zero
            self.movePosTarget(0,
                                self.hTargetPosition,
                                self.hActualPositionInt,
                                self.hEnableMove,
                                self.hCurrentErrorPower,
                                self.hCurrentErrorCmd,
                                self.hBusy)
            
        except Exception as e:
            logging.exception("Exception flew by! \t|\t "+e.__str__())
        finally:
            self.stopAllAxis()
            sleep(self.CMDDELAY)
            self.disableAllAxis()
            sleep(self.CMDDELAY)
            self.standbyMode()