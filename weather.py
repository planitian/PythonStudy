import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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

    def __del__(self):
        print("本身销毁")

    def info(self):
        self.driver.get(self.base_url)
        time.sleep(10)
        html = self.driver.page_source
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
    t = threading.Timer(20, run)
    t.start()


def test():
    print(">>>>")
    global t
    t = threading.Timer(2, test)
    t.start()


if __name__ == '__main__':
    t = threading.Timer(20, run)
    t.start()
