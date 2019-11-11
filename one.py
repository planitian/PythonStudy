import re

# 正则表达式
pattern = "www"
content = "wWw.baidu.com.www.baidu.com"
# re.I 忽略大小写
m_list = re.findall(pattern, content, re.I)
# 对列表 进行 遍历  带 位置的
for i, val in enumerate(m_list, 0):
    # 格式化输出一下
    print("第 %d 行 数据是 %s" % (i, val))
# 返回的是 迭代器
it = re.finditer(pattern=pattern, string=content, flags=re.I)
# 输出迭代器的下一个元素
print(next(it))  # <re.Match object; span=(0, 3), match='wWw'>
for e in it:
    print(str(e.start()) + "--->" + e.group())
# 替换 .  为 /  ，note  .  需要 转义 \.
print(re.sub(r'\.', "/", content))  # wWw/baidu/com/www/baidu/com


