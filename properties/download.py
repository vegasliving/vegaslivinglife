import requests
from requests.auth import HTTPDigestAuth
import shutil
from django.contrib.staticfiles.templatetags.staticfiles import static

def downloadImage(matrixUniqueID,i):
	print(i)
	for count in range(0,int(i)):
		print(count)
		url = 'http://rets.las.mlsmatrix.com/rets/GetObject.ashx?Type=LargePhoto&Resource=Property&ID=%s:%s'%(matrixUniqueID, count)
		path = 'static/properties/images/%s:%s.jpg'%(matrixUniqueID,count)
		gpath = path[7:32]
		r = requests.get(url, auth=HTTPDigestAuth('tinoco', 'lv360'), stream=True)
		print(r.headers, r.status_code, r.raw)
		if r.status_code == 200:
		    with open(path, 'wb') as f:
		        r.raw.decode_content = True
		        shutil.copyfileobj(r.raw, f) 
	return(gpath)


