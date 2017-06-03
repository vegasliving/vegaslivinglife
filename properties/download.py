import requests
from requests.auth import HTTPDigestAuth
import shutil

url = 'http://rets.las.mlsmatrix.com/rets/GetObject.ashx?Type=LargePhoto&Resource=Property&ID=128665674:0'
path = 'properties/128665674.jpg'

# r = requests.get(url, auth=HTTPBasicAuth('tinoco', 'lv360'))
r = requests.get(url, auth=HTTPDigestAuth('tinoco', 'lv360'), stream=True)
print(r.headers, r.status_code, r.raw)
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f) 