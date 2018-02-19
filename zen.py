import requests
import re

content = requests.get('http://maoyan.com/board/4').text
# if content.encoding == 'ISO-8859-1':
#     encodings = requests.utils.get_encodings_from_content(content.text)
#     if encodings:
#         encoding = encodings[0]
#     else:
#         encoding = content.apparent_encoding
#
#     # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
#     global encode_content
#     encode_content = content.content.decode(encoding, 'replace') #如果设置为replace，则会用?取代非法字符；

# print(encode_content)
print(content)

pattern  = re.compile('<dd>.*?-index-.*?">(.*?)</i>.*?data-src="(.*?)".*?"name">.*?>(.*?)</a>.*?"star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i>.*?</dd>', re.S)
items = re.findall(pattern, content)
print(items)