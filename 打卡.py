from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import json
import msvcrt

def open_Chrome():
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    option.add_argument("--headless")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=option)
    return driver

def find(str):
    try:
        driver.find_element_by_xpath(str)
    except:
        return False
    else:
        return True

def dk_operate():
    while True:
        driver = open_Chrome()
        driver.set_page_load_timeout(10)
        try:
            driver.get(url)
        except:
            print('网页超时，重新加载')
            driver.quit()
            #driver.refresh()
            continue
        #time.sleep(1)
        #开始寻找输入框输入账号密码
        driver.find_element_by_name('IDToken1').send_keys(config["用户名/学号"])
        driver.find_element_by_name('IDToken2').send_keys(config["密码"])
        #登录提交表单
        time.sleep(1)
        try:
            driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/th/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[6]/td/img[1]").click()
        except:
            try:
                driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[6]/td/img[1]").click()
            except:
                print('登录失败')
                driver.quit()
                #driver.refresh()
                continue
        else:
            print('登录成功')


        time.sleep(1)
        #看看是否成功登录网页
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/h3")
        except:
            print('登录失败或者服务器卡了')
            driver.quit()
            #driver.refresh()
            continue
        else:
            print('已进入健康打卡选择页面，准备开始打卡')


        #点击次页面的研究生健康打卡按钮
        try:
            # while 1:
            driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/section/section/div/a').click()
            time.sleep(2)
                # if find('/html/body/div[1]/div[4]/div/section/section/div/a'):
                #     time.sleep(3)
                #     driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/section/section/div/a').click()
                #     break
                # time.sleep(2)
            # driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/section/section/div/a').click()
            # time.sleep(2)
            # driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/section/section/div/a').click()
        except:
            print('网页超时，重新加载')
            driver.quit()
            #driver.refresh()
            continue
        else:       
            print('开始打卡')

        #等待1秒
        time.sleep(1)
        try:
            #输入身份证号
            # driver.find_element_by_xpath('//*[@id="SFZJH_402404"]').clear()
            # driver.find_element_by_xpath('//*[@id="SFZJH_402404"]').send_keys(config["身份证号"])
            # #输入攻读学位名称
            # driver.find_element_by_xpath('//*[@id="GDXW_926421"]').clear()
            # driver.find_element_by_xpath('//*[@id="GDXW_926421"]').send_keys(config["攻读学位"])
            #输入导师名字
            driver.find_element_by_xpath('//*[@id="DSNAME_606453"]').clear()
            driver.find_element_by_xpath('//*[@id="DSNAME_606453"]').send_keys(config["导师名字"])
            #培养类别
            driver.find_element_by_xpath('//*[@id="PYLB_253720"]').clear()
            driver.find_element_by_xpath('//*[@id="PYLB_253720"]').send_keys(config["培养类别"])
            #选择宿舍楼
            Select(driver.find_element_by_xpath('//*[@id="SELECT_172548"]')).select_by_value(config["宿舍楼"])
            #输入宿舍号
            driver.find_element_by_xpath('//*[@id="TEXT_91454"]').clear()
            driver.find_element_by_xpath('//*[@id="TEXT_91454"]').send_keys(config["宿舍号"])
            #输入手机号和紧急联系号码
            driver.find_element_by_xpath('//*[@id="TEXT_24613"]').clear()
            driver.find_element_by_xpath('//*[@id="TEXT_24613"]').send_keys(config["电话"])
            driver.find_element_by_xpath('//*[@id="TEXT_826040"]').clear()
            driver.find_element_by_xpath('//*[@id="TEXT_826040"]').send_keys(config["紧急联系电话"])
            #体温状况正常？-》正常
            driver.find_element_by_xpath('//*[@id="d-RADIO_799044"]/div/label[1]/input').click()
            #是否在校内？-》在
            driver.find_element_by_xpath('//*[@id="d-RADIO_384811"]/div/label[1]/input').click()
            #driver.find_element_by_xpath('//*[@id="d-RADIO_384811"]/div/label[2]/input').click()
            #本人症状？-》健康
            driver.find_element_by_xpath('//*[@id="d-RADIO_907280"]/div/label[1]/input').click()
            #同住人员？-》健康
            driver.find_element_by_xpath('//*[@id="d-RADIO_716001"]/div/label[1]/input').click()
            #有无接触？-》无
            driver.find_element_by_xpath('//*[@id="d-RADIO_248990"]/div/label[1]/input').click()
            #print('最后一步')
            #提交
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="saveBtn"]').click()
        except:
            print('打卡出错，开始重新打卡')
            driver.quit()
            continue
        else:
            time.sleep(5)
            print('打卡完成')
            driver.quit()
            break
        # if find('//*[@id="successSubmit"]/div[2]/h5'):
        #     print('打卡成功！')
        #     break
        # else:
        #     print('打卡失败！')
        #     driver.quit()
        #driver.find_element_by_id('panel panel-success')
        #print('daka')
        #driver.find_element('你已成功提交，谢谢参与！')
        # try:
        #     #driver.find_element_by_xpath("/html/body/div[1]/div[3]/h3")
        #     driver.find_element_by_id('panel panel-success')
        # except:
        #     print('打卡失败!')
        #     driver.quit()
        #     continue
        # else:
        #     print('打卡成功!')
        #     driver.quit()
        #     break


url = "http://ids.hhu.edu.cn/amserver/UI/Login?goto=http://form.hhu.edu.cn/pdc/form/list"

try:
    with open("config.json",encoding='utf-8') as f:
        config=json.load(f)
except:
    print("配置文件错误！请检查配置文件是否与py文件放置于同一目录下，或配置文件是否出错! \n 按任意键退出 ")
    msvcrt.getch()
    exit()
print('=======================\n 准备开始打卡,2s后开始！\n=======================')

dk_operate()
#print('打卡成功！按任意键退出')
#msvcrt.getch()
exit()
