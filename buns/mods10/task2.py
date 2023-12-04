import re
import requests

url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)                     
content = response.text                          

captions = re.findall(r'<h3 id=".*?">(.*?)</h3>', content)

print(captions)
