#  download sequential files from a given server. The sequence of files should be found through searching through the text of the file name and/or address

#  inputs: URL for first item, output directory
#  outputs: files should be downloaded to the given directory

#  sample URL: https://699340.youcanlearnit.net/image001.jpg

import requests

url = 'https://699340.youcanlearnit.net/image001.jpg' 

r = requests.get(url, allow_redirects=True)
with open('./DL_files/image001.jpg', 'wb+') as f:
    f.write(r.content)

