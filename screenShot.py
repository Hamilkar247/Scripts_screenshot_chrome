#!/bin/python3
import time
import datetime
from datetime import datetime
from requests import Session
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
import logging
import traceback

#logi
logging.basicConfig(level=logging.DEBUG)

display = Display(visible=0, size=(1920, 1200))
display.start()


#Driver = 'chromedriver'
#driver = webdriver.Chrome(Driver)
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("--kiosk")
chrome_options.add_argument("--disable-application-cache")

#kusy modyfikacja -bez tego w blad >selenium.common.exceptions.WebDriverException: Message: unknown error: DevToolsActivePort file doesn'
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")


driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)

driver.set_window_size(1920,1316)

driver.set_script_timeout(30)
driver.set_page_load_timeout(30) # seconds

while True:
    try:
        milli_sec = int(round(time.time()*1000))
        now = datetime.now()
        t = now.strftime("[%Y/%m/%d-%H:%M:%S]")
        driver.get('https://czujnikimiejskie.pl/public/kolno/?url_node_id=281&a='+str(milli_sec))
        time.sleep(20)
        screenshot = driver.save_screenshot('/home/devel/kolno_map.png')
        print(t, " ScreenShoot: Mapa Kolno")
        
        now = datetime.now()	
        t = now.strftime("[%Y/%m/%d-%H:%M:%S]")
        driver.get('https://czujnikimiejskie.pl/public/kozienice/?url_node_id=196&kml=false&a='+str(milli_sec))
        time.sleep(20)
        screenshot = driver.save_screenshot('/home/devel/kozienice_map.png')
        print(t, " ScreenShoot: Mapa Kozienice")
        
        now = datetime.now()
        t = now.strftime("[%Y/%m/%d-%H:%M:%S]")
        driver.get('https://czujnikimiejskie.pl/public/piaseczno/?url_node_id=205&a='+str(milli_sec))
        time.sleep(20)
        screenshot = driver.save_screenshot('/home/devel/piaseczno_map.png')
        print(t, " ScreenShoot: Mapa Piasecnzo")
        
        now = datetime.now()
        t = now.strftime("[%Y/%m/%d-%H:%M:%S]")
        driver.get('https://czujnikimiejskie.pl/public/widgety/widget_kolno.html?id=281&a='+str(milli_sec))
        time.sleep(20)
        screenshot = driver.save_screenshot('/home/devel/widget_kolno.png')
        print(t, " ScreenShoot: Widget Kolno")
        
        now = datetime.now()
        t = now.strftime("[%Y/%m/%d-%H:%M:%S]")
        driver.get('https://czujnikimiejskie.pl/public/widgety/widget_kozienice.html?id=196&a='+str(milli_sec))
        time.sleep(20)
        screenshot = driver.save_screenshot('/home/devel/widget_kozienice.png')
        print(t, " ScreenShoot: Widget Kozienice")
        
        now = datetime.now()
        t = now.strftime("[%Y/%m/%d-%H:%M:%S]")
        driver.get('https://czujnikimiejskie.pl/public/widgety/widget.html?id=205&a='+str(milli_sec))
        time.sleep(20)
        screenshot = driver.save_screenshot('/home/devel/widget_piaseczno.png')
        print(t , " ScreenShoot: Widget Piaseczno")
        
        session = Session()
        response = session.post(
            url='http://czujnikimiejskie.pl/apipost/add/measurement',
        data={"sn":"3000","a":"1","w":"0","z":"0"},
                headers={'Connection':'close'}
             )
        print("Wyslano")
        time.sleep(600)
    except TimeoutException as e:
        print("Wystepuje problem związany z TimeoutException")
        logging.debug("Wystepuje problem związany z TimeoutException")
        traceback.print_exc()  

driver.quit()
display.stop() 
