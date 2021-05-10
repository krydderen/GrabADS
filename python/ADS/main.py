import pyads
import logging
from time import sleep

class GRAB(object):
    """
    A class used to represent the GRAB2.0 Prototype during the bachelor
    thesis.
    ...
    Methods
    -------
    getSymbols(self)
        Fetches all the variables we are interested in from the plc
    open(self)
        Opens communication to PLC
    close(self)
        Closes communication to plc
    ModeSelects
        standby, homing, manual and positionMode changes the state of the robot
    Read functions
        readHorizontalAxis, readVerticalAxis, readRotationalAxis all read the 
        axis values for enable, moving and reset.
    Enable and Disable functions
        Enables and disables the various axis available.
    ...
    """

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
        """ Get symbols from the PLC"""
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
        """Opens communication to the PLC,
        
        Raises
        ------
        Exception
            If no connection is possible.
        """
        try:
            self.plc.open()
            self.CONNECTION = True
            sleep(0.2)
            logging.info('Started')
            self.getSymbols()
        except Exception:
            logging.exception('Error occured whilst opening communication...')
    
    def getState(self):
        """Read the state of the PLC
        """
        if self.CONNECTION: logging.info(self.plc.read_state())
    
    def close(self) -> None:
        """Close the connection to the PLC
        """
        if self.CONNECTION:
            self.grabState.write(0)
            self.plc.close()
            self.CONNECTION = False
        logging.info('Stopped')
    
    ######################################################################
    # Global Variable changes
    def standbyMode(self) -> None:
        """Change the mode of the robot to Standby.
        """
        if self.CONNECTION: self.grabState.write(0)
        logging.info('Current State \t|\t STANDBY')
        
    def homingMode(self) -> None:
        """Change the mode of the robot to Homing.
        """
        if self.CONNECTION: self.grabState.write(1)
        logging.info('Current State \t|\t HOMINGMODE')
        
    def manualMode(self) -> None:
        """Change the mode of the robot to Manual.
        """
        if self.CONNECTION: self.grabState.write(2)
        logging.info('Current State \t|\t MANUALMODE')
    
    def positionMode(self) -> None:
        """Change the mode of the robot to Position.
        """
        if self.CONNECTION: self.grabState.write(3)
        logging.info('Currentstate \t|\t POSITIONMODE')
    
    ######################################################################
    # Reading the different axis
    def readHorizontalAxis(self) -> None:
        """Read enabled, moving and reset error variables from this axis.
        """
        if self.CONNECTION:
            logging.info('Horizontal Axis: ENABLED\t|'          ,   self.hEnable.read())  
            logging.info('Horizontal Axis: EXTEND\t|'           ,   self.hExtend.read())
            logging.info('Horizontal Axis: RETRACT\t|'          ,   self.hRetract.read())
            logging.info('Horizontal Axis: RESETERROR\t|'       ,   self.hResetError.read())
    
    def readRotationalAxis(self) -> None:
        """Read enabled, moving and reset error variables from this axis.
        """
        if self.CONNECTION:
            logging.info('Rotational Axis: ENABLED\t|'          ,   self.rEnable.read())  
            logging.info('Rotational Axis: Clockwise\t|'        ,   self.rClockwise.read())
            logging.info('Rotational Axis: CounterClockwise\t|' ,   self.rCounterClockwise.read())
            logging.info('Rotational Axis: RESETERROR\t|'       ,   self.rResetError.read()) 
    
    def readVerticalAxis(self) -> None:
        """Read enabled, moving and reset error variables from this axis.
        """
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
        """Starts the homing procedure.
        """
        if self.CONNECTION:
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
        else:
            logging.info("ALL Axis \t|\t HOMING")
            sleep(1)
            logging.info("ALL Axis \t|\t HOMING DONE")
        
    ######################################################################
    # Resetting different axis
    def resetHorizontalAxis(self) -> None:
        """Resets the axis.
        """
        if self.CONNECTION:
            self.hResetError.write(True)
            sleep(self.CMDDELAY)
            self.hResetError.write(False)
        logging.debug("Horizontal Axis \t|\t RESET")
        
    def resetRotationalAxis(self) -> None:
        """Resets the axis.
        """
        if self.CONNECTION:
            self.rResetError.write(True)
            sleep(self.CMDDELAY)
            self.rResetError.write(False)
        logging.debug("Rotation Axis: \t|\t RESET")
    
    def resetVerticalAxis(self) -> None:
        """Resets the axis.
        """
        if self.CONNECTION:
            self.vResetError.write(True)
            sleep(self.CMDDELAY)
            self.vResetError.write(False)
        logging.debug("Vertical Axis \t|\t RESET")
    
    def resetAllAxis(self) -> None:
        """Resets all the axis.
        """
        logging.info("ALL AXIS \t|\t RESETTING...")
        if self.CONNECTION:
            self.resetHorizontalAxis()
            self.resetRotationalAxis()
            self.resetVerticalAxis()
        logging.info("ALL AXIS \t|\t RESET")
    ######################################################################
    # Enable or disable
    def enableHorizontalAxis(self):
        """Enables the axis.
        """
        if self.CONNECTION: self.hEnable.write(True)
        logging.info("Horizontal Axis \t|\t ENABLED")
    
    def disableHorizontalAxis(self):
        """Disables the axis.
        """
        if self.CONNECTION: self.hEnable.write(False)
        logging.info("Horizontal Axis \t|\t DISABLED")
        
    def enableRotationalAxis(self) -> None:
        """Enables the axis.
        """
        if self.CONNECTION: self.rEnable.write(True)
        logging.info("Rotational Axis \t|\t ENABLED")
    
    def disableRotationalAxis(self) -> None:
        """Disables the axis.
        """
        if self.CONNECTION: self.rEnable.write(False)
        logging.info("Rotational Axis \t|\t DISABLED")

    def enableVerticalAxis(self) -> None:
        """Enables the axis.
        """
        if self.CONNECTION: self.vEnable.write(True)
        logging.info("Vertical Axis \t|\t ENABLED")
    
    def disableVerticalAxis(self) -> None:
        """Disables the axis.
        """
        if self.CONNECTION: self.vEnable.write(False)
        logging.info("Vertical Axis \t|\t DISABLED")
    
    def enableAllAxis(self) -> None:
        """Enables all axis.
        """
        if self.CONNECTION: 
            self.enableHorizontalAxis()
            self.enableRotationalAxis()
            self.enableVerticalAxis()
        logging.info('All Axis \t|\t  ENABLED')
    
    def disableAllAxis(self) -> None:
        """Disables all axis.
        """
        if self.CONNECTION: 
            self.disableHorizontalAxis()
            self.disableRotationalAxis()
            self.disableVerticalAxis()
        logging.info('All Axis \t|\t DISABLED')
    ######################################################################
    # Operation for horizontal axis
    def startExtendSnake(self):
        """Sends command to extend the SNAKE.
        """
        if self.CONNECTION: self.hExtend.write(True)
        logging.info("Horizontal Axis |\t EXTENDING")
        
    def stopExtendSnake(self):
        """Sends command to stop extending the SNAKE.
        """
        if self.CONNECTION: self.hExtend.write(False)
        logging.info("Horizontal Axis |\t STOPPED")
        
    def startRetractSnake(self):
        """Sends command to retract the SNAKE.
        """
        if self.CONNECTION: self.hRetract.write(True)
        logging.info("Horizontal Axis |\t RETRACTING")
        
    def stopRetractSnake(self):
        """Sends command to stop retracting the SNAKE.
        """
        if self.CONNECTION: self.hRetract.write(False)
        logging.info("Horizontal Axis |\t STOPPED")
        
    def stopHorizontal(self) -> None:
        """Sends command to stop both retracting and extending the SNAKE.
        """
        if self.CONNECTION: self.hExtend.write(False)
        if self.CONNECTION: self.hRetract.write(False)
        logging.info("Horizontal Axis |\t STOPPED")
    
    ######################################################################
    # Operation for rotation axis
    def moveRotationClockwise(self) -> None:
        """Sends command to rotate SNAKEBOX clockwise.
        """
        if self.CONNECTION: self.rClockwise.write(True)
        logging.info("Rotation Axis |\t CLOCKWISE")
        
    def stopRotationClockwise(self) -> None:
        """Sends command to stop rotating the SNAKEBOX.
        """
        if self.CONNECTION: self.rClockwise.write(False)
        logging.info("Rotation Axis |\t STOPPED")
        
    def moveRotationCounterClockwise(self) -> None:
        """Sends comamnd to rotate SNAKEBOX counter-clockwise.
        """
        if self.CONNECTION: self.rCounterClockwise.write(True)
        logging.info("Rotation Axis |\t COUNTERCLOCKWISE")
        
    def stopRotationCounterClockwise(self) -> None:
        """Sends command to stop rotating the SNAKEBOX.
        """
        if self.CONNECTION: self.rCounterClockwise.write(False)
        logging.info("Rotation Axis |\t STOPPED")
    
    def stopRotation(self) -> None:
        """Sends command to stop rotating the SNAKEBOX.
        """
        if self.CONNECTION: self.rClockwise.write(False)
        if self.CONNECTION: self.rCounterClockwise.write(False)
        logging.info("Rotation Axis |\t STOPPED")
    
    ######################################################################
    # Operation for vertical axis
    def ascendVerticalAxis(self) -> None:
        """Sends command to start ascending.
        """
        if self.CONNECTION: self.vAscend.write(True)
        logging.info("Vertical Axis |\t ASCENDING")
        
    def descendVerticalAxis(self) -> None:
        """Sends command to start descending.
        """
        if self.CONNECTION: self.vDescend.write(True)
        logging.info("Vertical Axis |\t DESCENDING")
        
    def stopVertical(self) -> None:
        """Sends command to stop ascending or descending.
        """
        if self.CONNECTION: self.vAscend.write(False)
        if self.CONNECTION: self.vDescend.write(False)
        logging.info("Vertical Axis |\t STOPPED")
    
    ######################################################################
    # Stop all 
    def stopAllAxis(self) -> None:
        """Sends command to stop all axis.
        """
        if self.CONNECTION: self.stopVertical();self.stopRotation();self.stopHorizontal()
        logging.info("All Axis \t|\t STOPPED")
    
    
    ######################################################################
    # Position mode, change this to take in args to decide manual or standby.
    
    # Checks CMD or POWER error from given AXIS
    def checkError(self, currentErrorPower, currentCmdError):
        """Checks whether the given args contain an error or not. 

        Args:
            currentErrorPower (integer): Errors related to power.
            currentCmdError (integer): Errors related to COMMANDS.

        Raises:
            Exception: If error related to POWER.
            Exception: If error related to COMMANDS.
        """
        if currentErrorPower.read() != 0:
            raise Exception('Power Error: \t'+ str(currentErrorPower.read()))
        elif currentCmdError.read() != 0:
            raise Exception('Cmd Error: \t'+ str(currentCmdError.read()))
        else:
            pass
    
    # Universal MovePos method using given axis parameters.
    def movePosTarget(self, pos : int, targetPos, currentPos, enableMove, currentErrorPower, currentCmdError, busy, axis):
        """Sends a position to a given axis with args. 

        Args:
            pos (int): Current wanted position value.
            targetPos ([type]): The symbol used to send pos value.
            currentPos ([type]): The symbol used to read current pos value.
            enableMove ([type]): The symbol used to enable movement on axis.
            currentErrorPower ([type]): The symbol containing error message.
            currentCmdError ([type]): The symbol containing error message.
            busy ([type]): The symbol used to check whether the robot is busy or not.
            axis ([type]): The axis we are going to use. 
        """
        self.checkError(currentErrorPower, currentCmdError)
        sleep(self.CMDDELAY)
        targetPos.write(pos)
        sleep(self.CMDDELAY)
        enableMove.write(True)
        sleep(1)
        enableMove.write(False)
        sleep(self.CMDDELAY)
        self.checkError(currentErrorPower, currentCmdError)
        sleep(self.CMDDELAY)
        
        logging.info('Moving...')
        while(busy.read()):
            logging.debug('Moving..')
            logging.info('Position \t| '+str(axis)+ '\t' + str(currentPos.read()))
            sleep(0.1)
            self.checkError(currentErrorPower, currentCmdError)
        logging.info('Moving done...')
        
        
    ######################################################################
    # Testing functions
    
    ################################################################
    # New Pickbox method 
    def newPickBox(self) -> None:
        """The state machine used to pick a box, and loop X amount of times.
        """
        if self.CONNECTION:
            try:
                self.positionMode()
                sleep(self.CMDDELAY)
                self.enableAllAxis()
                sleep(1)
                loops = 10
                # Start movement 
                # Start by moving everyone to ZERO.
                self.movePosTarget(0,
                                    self.hTargetPosition,
                                    self.hActualPositionInt,
                                    self.hEnableMove,
                                    self.hCurrentErrorPower,
                                    self.hCurrentErrorCmd,
                                    self.hBusy,
                                    "Hor. pos")
                self.movePosTarget(-2,
                                    self.rTargetPosition,
                                    self.rActualPositionInt,
                                    self.rEnableMove,
                                    self.rCurrentErrorPower,
                                    self.rCurrentErrorCmd,
                                    self.rBusy,
                                    "Rot. angle")
                self.movePosTarget(0,
                                    self.vTargetPosition,
                                    self.vActualPositionInt,
                                    self.vEnableMove,
                                    self.vCurrentErrorPower,
                                    self.vCurrentErrorCmd,
                                    self.vBusy,
                                    "X")
                
                #Ascend to given position before reaching for box
                self.movePosTarget(730,
                                    self.vTargetPosition,
                                    self.vActualPositionInt,
                                    self.vEnableMove,
                                    self.vCurrentErrorPower,
                                    self.vCurrentErrorCmd,
                                    self.vBusy,
                                    "X")
                # Rotate towards table
                self.movePosTarget(90,
                                    self.rTargetPosition,
                                    self.rActualPositionInt,
                                    self.rEnableMove,
                                    self.rCurrentErrorPower,
                                    self.rCurrentErrorCmd,
                                    self.rBusy,
                                    "Rot. angle")
                
                
                while loops != 0:
                    # Reach out for box
                    self.movePosTarget(500,
                                        self.hTargetPosition,
                                        self.hActualPositionInt,
                                        self.hEnableMove,
                                        self.hCurrentErrorPower,
                                        self.hCurrentErrorCmd,
                                        self.hBusy,
                                        "Hor. pos")
                    # Lift the box
                    self.movePosTarget(900,
                                        self.vTargetPosition,
                                        self.vActualPositionInt,
                                        self.vEnableMove,
                                        self.vCurrentErrorPower,
                                        self.vCurrentErrorCmd,
                                        self.vBusy,
                                        "Vert. pos")
                    # Pull the box in
                    self.movePosTarget(0,
                                        self.hTargetPosition,
                                        self.hActualPositionInt,
                                        self.hEnableMove,
                                        self.hCurrentErrorPower,
                                        self.hCurrentErrorCmd,
                                        self.hBusy,
                                        "Hor. pos")
                    # Rotate to zero, before lowering
                    self.movePosTarget(-2,
                                        self.rTargetPosition,
                                        self.rActualPositionInt,
                                        self.rEnableMove,
                                        self.rCurrentErrorPower,
                                        self.rCurrentErrorCmd,
                                        self.rBusy,
                                        "X")
                    # Descend down to pallet
                    self.movePosTarget(269,
                                        self.vTargetPosition,
                                        self.vActualPositionInt,
                                        self.vEnableMove,
                                        self.vCurrentErrorPower,
                                        self.vCurrentErrorCmd,
                                        self.vBusy,
                                        "Vert. pos")
                    # Extend snake to position box on pallet.
                    self.movePosTarget(500,
                                        self.hTargetPosition,
                                        self.hActualPositionInt,
                                        self.hEnableMove,
                                        self.hCurrentErrorPower,
                                        self.hCurrentErrorCmd,
                                        self.hBusy,
                                        "Hor. pos")
                    # Descend to let go of box
                    self.movePosTarget(145,
                                        self.vTargetPosition,
                                        self.vActualPositionInt,
                                        self.vEnableMove,
                                        self.vCurrentErrorPower,
                                        self.vCurrentErrorCmd,
                                        self.vBusy,
                                        "Vert. pos")
                    # Retract snake to zero
                    self.movePosTarget(0,
                                        self.hTargetPosition,
                                        self.hActualPositionInt,
                                        self.hEnableMove,
                                        self.hCurrentErrorPower,
                                        self.hCurrentErrorCmd,
                                        self.hBusy,
                                        "Hor. pos")
                    # Extend snake to position box on pallet.
                    self.movePosTarget(500,
                                        self.hTargetPosition,
                                        self.hActualPositionInt,
                                        self.hEnableMove,
                                        self.hCurrentErrorPower,
                                        self.hCurrentErrorCmd,
                                        self.hBusy,
                                        "Hor. pos")
                    # Ascend box up from pallet
                    self.movePosTarget(260,
                                        self.vTargetPosition,
                                        self.vActualPositionInt,
                                        self.vEnableMove,
                                        self.vCurrentErrorPower,
                                        self.vCurrentErrorCmd,
                                        self.vBusy,
                                        "Vert. pos")
                    # Retract snake to zero
                    self.movePosTarget(0,
                                        self.hTargetPosition,
                                        self.hActualPositionInt,
                                        self.hEnableMove,
                                        self.hCurrentErrorPower,
                                        self.hCurrentErrorCmd,
                                        self.hBusy,
                                        "Hor. pos")
                    # Lift the box
                    self.movePosTarget(900,
                                        self.vTargetPosition,
                                        self.vActualPositionInt,
                                        self.vEnableMove,
                                        self.vCurrentErrorPower,
                                        self.vCurrentErrorCmd,
                                        self.vBusy,
                                        "Vert. pos")
                    # Rotate towards table
                    self.movePosTarget(90,
                                        self.rTargetPosition,
                                        self.rActualPositionInt,
                                        self.rEnableMove,
                                        self.rCurrentErrorPower,
                                        self.rCurrentErrorCmd,
                                        self.rBusy,
                                        "X")
                    # Extend snake to position box on pallet.
                    self.movePosTarget(500,
                                        self.hTargetPosition,
                                        self.hActualPositionInt,
                                        self.hEnableMove,
                                        self.hCurrentErrorPower,
                                        self.hCurrentErrorCmd,
                                        self.hBusy,
                                        "Hor. pos")
                    #Ascend to given position before reaching for box
                    self.movePosTarget(730,
                                        self.vTargetPosition,
                                        self.vActualPositionInt,
                                        self.vEnableMove,
                                        self.vCurrentErrorPower,
                                        self.vCurrentErrorCmd,
                                        self.vBusy,
                                        "Vert. pos")
                    # Retract snake to zero
                    self.movePosTarget(0,
                                        self.hTargetPosition,
                                        self.hActualPositionInt,
                                        self.hEnableMove,
                                        self.hCurrentErrorPower,
                                        self.hCurrentErrorCmd,
                                        self.hBusy,
                                        "Hor. pos")
                    loops -= 1
                    
                
            except Exception as e:
                logging.exception("Exception flew by! \t|\t "+e.__str__())
            finally:
                self.stopAllAxis()
                sleep(self.CMDDELAY)
                self.disableAllAxis()
                sleep(self.CMDDELAY)
                self.standbyMode()
        else:
            logging.info('Picking done.')