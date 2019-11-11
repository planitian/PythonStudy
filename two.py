from bs4 import BeautifulSoup
import requests
import re

html = """
<html>
<head><title>标题</title></head>
<body>
 <p class="title" name="dromouse"><b>标题</b></p>
 <div name="divlink">
  <p>
   <text href="http://example.com/1" class="sister" id="link1">链接1</text>
   <a href="http://example.com/2" class="sister" id="link2">链接2</a>
   <a href="http://example.com/3" class="sister" id="link3">链接3</a>
  </p>
 </div>
 <p></p>
 <div name='dv2'></div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup.find("div", {"name": "divlink"}).find_all("text"))
print(soup.select("title "))
print(soup.select("html head title"))
print(soup.select('.sister'))
print(soup.select('#link1'))


class bs:

    def __init__(self, url) -> None:
        super().__init__()
        self.url = url
        self.response = ""

    def _req(self):
        if len(self.url) == 0:
            raise NameError
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/69.0.3497.100 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Cookie": "BIDUPSID=2B6CFFA59C2AAF505BE7B4E564B11571; PSTM=1564450027; "
                      "BAIDUID=25FBFD5331FCF9867828313B719A5D1C:FG=1; "
                      "BDUSS=mF"
                      "-aUVBZng3OGktQzhCSzZIWmQ3MlNNNVU4eGhMUm01REFXQk5BN09hckpXTXRkRVFBQUFBJCQAAAAAAAAAAAEAAAA5"
                      "~VM7zOy1wNexAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMnLo13Jy6NdM;"
                      " BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; BDRCVFR[C0p6oIjvx-c]=I67x6TjHwwYf0; H_PS_PSSID=; "
                      "pgv_pvi=9912030208; pgv_si=s6412033024; BDRCVFR[DM1GxVpU1K0]=mbxnW11j9Dfmh7GuZR8mvqV; BDRCVFR[WAwq7VO8WyY]=mbxnW11j9Dfmh7GuZR8mvqV "
        }
        response = requests.get(self.url, header)
        if response.status_code != 200:
            raise IOError
        html = response.text
        return html

    def deal(self):
        html = self._req()
        # print(html)
        bs4 = BeautifulSoup(html, "html.parser")
        # 加入 类型提示
        a_list = bs4.find_all(href="ss")  # type:bs4.element.ResultSet

        for i in a_list:  # type:bs4.element.Tag
            print(i.next_sibling)
            print(" %s :链接地址 %s" % (i.string, i.get("href")))
            if i.has_attr("class_"):
                print(i["class_"])


bs = bs("http://site.baidu.com")
bs.deal()
