from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
import os

"""
단일 품목, 카카오페이 결제
"""

driver = webdriver.Chrome(os.getcwd() + '/chromedriver/chromedriver.exe')

driver.get("https://my.musinsa.com/login/v1/login?referer=https%3A%2F%2Fstore.musinsa.com%2Fapp%2Fgoods%2F" + "상품 번호") # 상품번호 입력
driver.implicitly_wait(1000)
driver.find_element_by_name('id').send_keys('ID') #아이디
driver.find_element_by_name('pw').send_keys('PWD')#패스워드
driver.find_element_by_xpath("//input[@type='submit']").click()

print("아무키 입력 -> 상품 결제")
start = input()

#장바구니클릭
driver.refresh()
driver.implicitly_wait(1000)
while True:
    try:
        driver.execute_script("addCartToast('1','상품번호','0','1'); return false;") #단일 품복 상품번호
        driver.find_element_by_id('left_cart_btn').click()
        break
    except UnexpectedAlertPresentException as e:
        driver.refresh()

#장바구니
driver.implicitly_wait(1000)
print('장바구니')
#driver.find_element_by_xpath('/html/body/div[7]/div[4]/form[1]/div[2]/div[1]/div[3]/button').click()
driver.execute_script("sel_goods_order(); return false;")

#결제창
driver.implicitly_wait(1000)
print('결제창 접속')
driver.find_element_by_xpath('/html/body/div[12]/div[4]/form/div[6]/div[1]/div/div[1]/ul[5]/li[1]/label/input').click()
#driver.find_element_by_id('btn_pay').click()
while True:
    driver.execute_script("Order.payment();")
    if len(driver.window_handles) == 2:
        break


#카카오 결제창 변경
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1])
print('카카오창 접속')
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/li[2]/a').click()
driver.implicitly_wait(1000)
driver.find_element_by_id('userPhone').send_keys('핸드폰 번호')
driver.find_element_by_id('userBirth').send_keys('생년월일')
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/form/fieldset/button').click()
print('결제')
