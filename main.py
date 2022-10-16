import sys
import os
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5.QtGui import QPainter

import WebServer
from FinebitOperator import LeverageType, SeedType, FinebitStatus, PayMethod
import FinebitOperator

class FlaskThread(QThread):
    positionSignal = pyqtSignal(bool)
    statusSignal = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)

    def run(self):
        WebServer.fbo.setStatusCallback(self.__statusCallback)
        # WebServer.app.run(host='192.168.0.2', port=3004)
        WebServer.app.run(host='0.0.0.0', port=3004)

    def __statusCallback(self, status):
        self.statusSignal.emit(status)

    def setStop(self):
        WebServer.fbo.setStop()

    def setStart(self, id, pw):
        WebServer.fbo.setStart(id, pw)

    def setLeverage(self, leverage):
        WebServer.fbo.setLeverage(leverage)

    def setSeedPoint(self, seed):
        WebServer.fbo.setSeedPoint(seed)

    def setLogin(self, id, pw):
        WebServer.fbo.setLogin(id, pw)

    def setAmount(self, amount):
        WebServer.fbo.setAmount(amount)

    def setSelectSeed(self, status):
        WebServer.fbo.setSelectSeed(status)
        

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 

class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # uic.loadUi('MainWidget.ui', self)
        uic.loadUi(BASE_DIR + r'\MainWidget.ui', self)

        self.ft = FlaskThread(self)
        self.__initSignals()
        self.ft.start()

    def __initSignals(self):
        # Status notify
        self.ft.statusSignal.connect(self.statusSlot)
        # SeedPosition Buttons
        self.seed10Button.toggled.connect(self.onSeed10ButtonToggled)
        self.seed25Button.toggled.connect(self.onSeed25ButtonToggled)
        self.seed50Button.toggled.connect(self.onSeed50ButtonToggled)
        self.seed75Button.toggled.connect(self.onSeed75ButtonToggled)
        self.seed100Button.toggled.connect(self.onSeed100ButtonToggled)
        # Leverage Buttons
        self.lev1Button.toggled.connect(self.onLev1ButtonToggled)
        self.lev25Button.toggled.connect(self.onLev25ButtonToggled)
        self.lev35Button.toggled.connect(self.onLev35ButtonToggled)
        self.lev50Button.toggled.connect(self.onLev50ButtonToggled)
        self.lev75Button.toggled.connect(self.onLev75ButtonToggled)
        self.lev100Button.toggled.connect(self.onLev100ButtonToggled)
        self.lev125Button.toggled.connect(self.onLev125ButtonToggled)
        # Start / Stop Buttons
        self.startButton.clicked.connect(self.onStartButtonClicked)
        self.stopButton.clicked.connect(self.onStopButtonClicked)
        # Amount Change
        self.amountSpin.valueChanged.connect(self.onAmountChanged)
        # Select Persentage or Seed
        self.selectSeed.currentTextChanged.connect(self.onSelectSeedChanged)

    @pyqtSlot(str)
    def onSelectSeedChanged(self, value) :
        if value == 'Seed Amount' :
            self.ft.setSelectSeed(PayMethod.AMOUNT)
        elif value == 'Seed Persentage':
            self.ft.setSelectSeed(PayMethod.PERCENTAGE)

    @pyqtSlot(bool)
    def onSeed10ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setSeedPoint(SeedType.SEED_PERCENT_10)

    @pyqtSlot(bool)            
    def onSeed25ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setSeedPoint(SeedType.SEED_PERCENT_25)

    @pyqtSlot(bool)            
    def onSeed50ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setSeedPoint(SeedType.SEED_PERCENT_50)

    @pyqtSlot(bool)            
    def onSeed75ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setSeedPoint(SeedType.SEED_PERCENT_75)

    @pyqtSlot(bool)            
    def onSeed100ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setSeedPoint(SeedType.SEED_PERCENT_100)

    @pyqtSlot(bool)            
    def onLev1ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setLeverage(LeverageType.LEVERAGE_1)

    @pyqtSlot(bool)            
    def onLev25ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setLeverage(LeverageType.LEVERAGE_25)

    @pyqtSlot(bool)            
    def onLev35ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setLeverage(LeverageType.LEVERAGE_35)

    @pyqtSlot(bool)            
    def onLev50ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setLeverage(LeverageType.LEVERAGE_50)

    @pyqtSlot(bool)            
    def onLev75ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setLeverage(LeverageType.LEVERAGE_75)

    @pyqtSlot(bool)            
    def onLev100ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setLeverage(LeverageType.LEVERAGE_100)

    @pyqtSlot(bool)            
    def onLev125ButtonToggled(self, isToggled):
        if isToggled:
            self.ft.setLeverage(LeverageType.LEVERAGE_125)

    @pyqtSlot(float)
    def onAmountChanged(self, amount):
        self.ft.setAmount(round(amount, 5))

    @pyqtSlot(int)
    def statusSlot(self, status):
        self.statusLabel.setText(FinebitOperator.FinebitStatusDescriptionList[status])
        if status == FinebitStatus.SHORT_DONE or status == FinebitStatus.LONG_DONE:
            self.inposButton.setChecked(True)

        if status == FinebitStatus.CLEAR_DONE:
            self.noposButton.setChecked(True)

        if status == FinebitStatus.STOP:
            self.stopButton.setEnabled(False)
            self.startButton.setEnabled(True)
        else:
            self.stopButton.setEnabled(True)
            self.startButton.setEnabled(False)

    @pyqtSlot()
    def onStartButtonClicked(self):
        if self.idEdit.text() != '' and self.pwEdit.text() != '':
            self.ft.setStart(str(self.idEdit.text()), str(self.pwEdit.text()))

    @pyqtSlot()
    def onStopButtonClicked(self):
        self.ft.setStop()


if __name__ == '__main__':
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    # w.showFullScreen()
    sys.exit(app.exec())
