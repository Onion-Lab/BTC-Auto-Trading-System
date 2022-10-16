from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FinebitStatus:
    STOP = 0
    STARTED = 1
    LOGIN_PROCEESS = 2
    LOGIN_DONE = 3
    LOGIN_FAIL = 4
    LONG_PROCESS = 5
    LONG_DONE = 6
    SHORT_PROCESS = 7
    SHORT_DONE = 8
    STOPLOSS_PROCESS = 9
    STOPLOSS_DONE = 10
    CLEAR_PROCESS = 11
    CLEAR_DONE = 12
    SET_LEVERAGE_PROCESS = 13
    SET_LEVERAGE_DONE = 14

FinebitStatusDescriptionList = [
    '정지',
    '시작',
    '로그인중...',
    '로그인 완료',
    '로그인 실패',
    'Long 진행중...',
    'Long 완료',
    'Short 진행중...',
    'Short 완료',
    '손절가 설정중...',
    '손절가 설정 완료',
    '청산중...',
    '청산 완료',
    '레버리지 설정중...',
    '레버리지 설정완료'
]

class LeverageType:
    LEVERAGE_1 = 0
    LEVERAGE_25 = 1
    LEVERAGE_35 = 2
    LEVERAGE_50 = 3
    LEVERAGE_75 = 4
    LEVERAGE_100 = 5
    LEVERAGE_125 = 6

LeverageXPathList = [
    '//*[@id="modal_leverage_exchange_buttons"]/div[1]',
    '//*[@id="modal_leverage_exchange_buttons"]/div[2]',
    '',
    '//*[@id="modal_leverage_exchange_buttons"]/div[3]',
    '//*[@id="modal_leverage_exchange_buttons"]/div[4]',
    '//*[@id="modal_leverage_exchange_buttons"]/div[5]',
    '//*[@id="modal_leverage_exchange_buttons"]/div[6]'
]

class SeedType:
    SEED_PERCENT_10 = 0
    SEED_PERCENT_25 = 1
    SEED_PERCENT_50 = 2
    SEED_PERCENT_75 = 3
    SEED_PERCENT_100 = 4

class PayMethod:
    PERCENTAGE = 0
    AMOUNT = 1

SeedXPathList = [
    '//*[@id="exchange_input_range_box"]/div[1]/span',
    '//*[@id="exchange_input_range_box"]/div[2]/span',
    '//*[@id="exchange_input_range_box"]/div[3]/span',
    '//*[@id="exchange_input_range_box"]/div[4]/span',
    '//*[@id="exchange_input_range_box"]/div[5]/span'
]

class FinebitOperator:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.status = FinebitStatus.STOP
        self.statusCallback = None
        self.leverage = LeverageType.LEVERAGE_35
        self.isLeverageUpdated = True
        self.positionStatus = FinebitStatus.CLEAR_DONE
        self.seed = SeedType.SEED_PERCENT_10
        self.amount = 0.00001
        self.id = ''
        self.pw = ''
        self.isStarted = False
        self.selectSeed = PayMethod.PERCENTAGE

    def setSelectSeed(self, status) :
        self.selectSeed = status

    def getSelectSeed(self) :
        return self.selectSeed

    def setStatusCallback(self, callback):
        self.statusCallback = callback

    def __setStatus(self, status):
        self.status = status
        if self.statusCallback != None:
            self.statusCallback(self.status)

    def setLeverage(self, leverage):
        print('lev setting!', leverage)
        self.isLeverageUpdated = True
        self.leverage = leverage

    def setSeedPoint(self, seed):
        self.seed = seed

    def setAmount(self, amount):
        print('Amount setting!', amount)
        self.amount = amount

    def setStop(self):
        self.__setStatus(FinebitStatus.STOP)

    def setStart(self, id, pw):
        self.__setStatus(FinebitStatus.STARTED)
        self.id = id
        self.pw = pw
        self.actionLogin()

    def actionLogin(self):
        self.__setStatus(FinebitStatus.LOGIN_PROCEESS)
        self.driver.get('https://fine-bit.com/signin')
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, 'email').send_keys(self.id)
        self.driver.find_element(By.NAME, 'password').send_keys(self.pw)
        self.driver.find_element(By.ID, 'kt_sign_in_submit').click()

        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID , 'kt_header_user_menu_toggle'))
            )

        except Exception as e:
            print(e)
            return False
        else:
            self.driver.get('https://fine-bit.com/exchange/btc')
            time.sleep(3) # TODO: 거래 창 진입까지 대기
            self.__setStatus(FinebitStatus.LOGIN_DONE)

    def actionSetLeverage(self):
        if self.status == FinebitStatus.STOP:
            return False
        self.__setStatus(FinebitStatus.SET_LEVERAGE_PROCESS)
        self.driver.find_element(By.ID, 'exchange_action_leverage').click() # 레버리지 설정 클릭
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'modal_leverage_submit')) # 레버리지 확인버튼 대기
            )
        except Exception as e:
            print(e)
            return False
        time.sleep(0.3)
        if self.leverage == LeverageType.LEVERAGE_35:
            self.driver.find_element(By.XPATH, LeverageXPathList[1]).click() # 레버리지 설정
            for i in range(10):
                self.driver.find_element(By.XPATH, '//*[@id="modal_leverage_bar_right"]').click()
        else:
            self.driver.find_element(By.XPATH, LeverageXPathList[self.leverage]).click() # 레버리지 설정
        time.sleep(0.3)
        self.driver.find_element(By.ID, 'modal_leverage_submit').click() # 레버리지 확인버튼
        time.sleep(0.3)
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'swal2-confirm.btn.btn-primary')) # Alert창 대기
            )
        except Exception as e:
            print(e)
            return False
        else:
            time.sleep(0.3)
            self.driver.find_element(By.CLASS_NAME, 'swal2-confirm.btn.btn-primary').click() # Alert 창 확인버튼 클릭
            self.__setStatus(FinebitStatus.SET_LEVERAGE_DONE)
            self.isLeverageUpdated = False
            return True


    def actionLong(self):
        if self.status == FinebitStatus.STOP:
            return False
        if self.isLeverageUpdated:
            self.actionSetLeverage()
            time.sleep(1)
        if self.positionStatus == FinebitStatus.SHORT_DONE:
            self.actionClear()
            time.sleep(3)

        if self.selectSeed == PayMethod.AMOUNT :
            self.__setStatus(FinebitStatus.LONG_PROCESS)
            self.driver.find_element(By.ID, 'exchange_input_amount').clear()
            time.sleep(0.3)
            maxSell = round(float(self.driver.find_element(By.ID, 'exchange_max_sell').text[:-3]), 5)
            if maxSell >= self.amount:
                self.driver.find_element(By.ID, 'exchange_input_amount').send_keys(format(self.amount, ".5f"))
            else:
                return False

            self.driver.find_element(By.XPATH, '//*[@id="exchange_order_button_wrapper"]/div[1]').click() # Long 버튼
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'swal2-confirm.btn.btn-primary'))
                )
            except Exception as e:
                print(e)
                return False
            else:
                self.driver.find_element(By.CLASS_NAME, 'swal2-confirm.btn.btn-primary').click()
                self.__setStatus(FinebitStatus.LONG_DONE)
                self.positionStatus = FinebitStatus.LONG_DONE
                return True
        elif self.selectSeed == PayMethod.PERCENTAGE :
            self.__setStatus(FinebitStatus.LONG_PROCESS)
            self.driver.find_element(By.XPATH, SeedXPathList[self.seed]).click() # 포지션 설정(몇퍼센트?)
            self.driver.find_element(By.XPATH, '//*[@id="exchange_order_button_wrapper"]/div[1]').click() # Long 버튼
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'swal2-confirm.btn.btn-primary'))
                )
            except Exception as e:
                print(e)
                return False
            else:
                self.driver.find_element(By.CLASS_NAME, 'swal2-confirm.btn.btn-primary').click()
                self.__setStatus(FinebitStatus.LONG_DONE)
                self.positionStatus = FinebitStatus.LONG_DONE
                return True


    def actionShort(self):
        if self.status == FinebitStatus.STOP:
            return False
        if self.isLeverageUpdated:
            self.actionSetLeverage()
            time.sleep(1)
        if self.positionStatus == FinebitStatus.LONG_DONE:
            self.actionClear()
            time.sleep(3)

        if self.selectSeed == PayMethod.AMOUNT :
            self.__setStatus(FinebitStatus.SHORT_PROCESS)
            # self.driver.find_element(By.XPATH, SeedXPathList[self.seed]).click() # 포지션 설정(몇퍼센트?)
            self.driver.find_element(By.ID, 'exchange_input_amount').clear()
            time.sleep(0.3)
            maxSell = round(float(self.driver.find_element(By.ID, 'exchange_max_sell').text[:-3]), 5)
            if maxSell >= self.amount:
                self.driver.find_element(By.ID, 'exchange_input_amount').send_keys(format(self.amount, ".5f"))
            else:
                return False

            self.driver.find_element(By.XPATH, '//*[@id="exchange_order_button_wrapper"]/div[2]').click() # Short 버튼
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'swal2-confirm.btn.btn-primary'))
                )
            except Exception as e:
                print(e)
                return False
            else:
                self.driver.find_element(By.CLASS_NAME, 'swal2-confirm.btn.btn-primary').click()
                self.__setStatus(FinebitStatus.SHORT_DONE)
                self.positionStatus = FinebitStatus.SHORT_DONE
                return True
        elif self.selectSeed == PayMethod.PERCENTAGE :
            self.__setStatus(FinebitStatus.SHORT_PROCESS)
            self.driver.find_element(By.XPATH, SeedXPathList[self.seed]).click() # 포지션 설정(몇퍼센트?)
            self.driver.find_element(By.XPATH, '//*[@id="exchange_order_button_wrapper"]/div[2]').click() # Short 버튼
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'swal2-confirm.btn.btn-primary'))
                )
            except Exception as e:
                print(e)
                return False
            else:
                self.driver.find_element(By.CLASS_NAME, 'swal2-confirm.btn.btn-primary').click()
                self.__setStatus(FinebitStatus.SHORT_DONE)
                self.positionStatus = FinebitStatus.SHORT_DONE
                return True

                
    def actionStopLoss(self, stopLoss):
        if self.status == FinebitStatus.STOP:
            return False
        if self.positionStatus == FinebitStatus.CLEAR_DONE:
            return False
        if self.positionStatus == FinebitStatus.STOPLOSS_DONE:
            return False

        self.__setStatus(FinebitStatus.STOPLOSS_PROCESS)

        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'exchange-order-row-tpsl'))
            )
        except Exception as e:
            print('Stop Loss Button Not found!')
            self.__setStatus(FinebitStatus.STOPLOSS_DONE)
            self.positionStatus = FinebitStatus.CLEAR_DONE
            return False

        self.driver.find_element(By.CLASS_NAME, 'exchange-order-row-tpsl').click()
        time.sleep(0.3)
        self.driver.find_element(By.ID, 'modal_tpsl_sl').clear()
        time.sleep(0.3)
        self.driver.find_element(By.ID, 'modal_tpsl_sl').send_keys(int(stopLoss))
        time.sleep(0.3)
        self.driver.find_element(By.ID, 'modal_tpsl_submit').click()
        time.sleep(0.3)
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'swal2-confirm.btn.btn-primary'))
            )
        except Exception as e:
            print(e)
            return False
        else:
            self.driver.find_element(By.CLASS_NAME, 'swal2-confirm.btn.btn-primary').click()
            self.__setStatus(FinebitStatus.STOPLOSS_DONE)
            return True
        # swal2-confirm btn btn-danger # Error

    def actionClear(self):
        if self.status == FinebitStatus.STOP:
            return False
        if self.positionStatus == FinebitStatus.CLEAR_DONE:
            return False
        self.__setStatus(FinebitStatus.CLEAR_PROCESS)

        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'exchange-order-row-market'))
            )
        except Exception as e:
            print('Market Button Not found! Not in position')
            self.__setStatus(FinebitStatus.CLEAR_DONE)
            self.positionStatus = FinebitStatus.CLEAR_DONE
            return False

        # Market 버튼
        self.driver.find_element(By.CLASS_NAME, 'exchange-order-row-market').click()
        time.sleep(0.3)
        #100% 버튼
        self.driver.find_element(By.XPATH, '//*[@id="modal_market_buttons"]/div[4]').click()
        time.sleep(0.3)
        # submit 버튼
        self.driver.find_element(By.XPATH, '//*[@id="modal_market_submit"]').click()
        time.sleep(0.3)
        # 확인 버튼
        self.driver.find_element(By.CLASS_NAME, 'swal2-confirm.btn.btn-primary').click()
        self.__setStatus(FinebitStatus.CLEAR_DONE)
        self.positionStatus = FinebitStatus.CLEAR_DONE
        return True


if __name__ == "__main__":
    fbo = FinebitOperator()
    fbo.actionLogin()
    fbo.actionLong()
    time.sleep(3)
    fbo.actionStopLoss(20000)
    time.sleep(3)
    fbo.actionClear()
    time.sleep(9999)
