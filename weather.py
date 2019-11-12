import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import threading
import sched


class Weatherinfo:

    def __init__(self, url) -> None:
        """
        url string
        :param url:
        """
        self.base_url = url
        # 浏览器选项
        driver_options = webdriver.ChromeOptions()
        # 设定不打开 浏览器界面，下面两种方式 都可以
        driver_options.headless = True
        # driver_options.add_argument('--headless')
        # 创建驱动，记得参数
        driver = webdriver.Chrome(options=driver_options)
        driver.maximize_window()
        self.driver = driver
        # 设置 隐式等待 秒为单位  这个并不会得到完全的页面
        # self.driver.implicitly_wait(100)

    def __del__(self):
        print("本身销毁")

    def info(self):
        self.driver.get(self.base_url)
        try:
            # 显示等待
            element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located((By.ID, 'pl_unlogin_home_hots')))  # 通过id 来查找
        except Exception as ex:
            print(ex)
            return
        html = self.driver.page_source
        # print(html)
        bs4 = BeautifulSoup(html, "html.parser")
        # print(bs4.prettify())
        ug = bs4.find('div', attrs={'class': 'WB_main_r'})
        content = ug.find_all('div', class_='UG_contents')
        content = content[1]
        content = content.find_all('div', class_='UG_list_c')
        # print(str(content))
        print("微博实时热点")
        with open("re.txt", 'a+', encoding='utf-8') as f:
            now = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime())
            f.writelines(str(now) + '  微博实时热点')
            for i in content:
                temp_url = self.base_url + i.get('href')
                temp_name = i.find('a', class_='S_txt1').string
                print(temp_name + "     " + temp_url)
                f.writelines(temp_name + "\n")
                f.writelines(temp_url + "\n")

        print("微博热门话题")
        ht = bs4.find('h2', text='微博热门话题')
        ht_content = ht.next_sibling.next_sibling
        ht_content = ht_content.find_all('div', class_='UG_list_c')
        with open("re.txt", 'a+', encoding='utf-8') as f:
            now = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime())
            f.writelines(str(now) + '  微博热门话题')
            for i in ht_content:
                # print(i)
                temp_url = i['href']
                temp_name = i.find('a', class_='S_txt1').string
                print(temp_name + "        " + temp_url)
                f.writelines(temp_name + "\n")
                f.writelines(temp_url + "\n")
        self.driver.quit()


def run():
    weather = Weatherinfo("https://weibo.com")
    weather.info()
    t = threading.Timer(10, run)
    t.start()


def test():
    print(">>>>")
    global t
    t = threading.Timer(2, test)
    t.start()


if __name__ == '__main__':
    t = threading.Timer(0, run)
    t.start()
