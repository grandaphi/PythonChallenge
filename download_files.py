#  download sequential files from a given server. The sequence of files should be found through searching through the text of the file name and/or address

#  inputs: URL for first item, output directory
#  outputs: files should be downloaded to the given directory

#  sample URL: https://699340.youcanlearnit.net/image001.jpg

import requests, re, os

newUrl = url = 'https://699340.youcanlearnit.net/image001.jpg'
folder = './DL_files/'
inc = '001'


def url_ok(url):
    try:
        response = requests.head(url)

        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError as e:
        return e


while url_ok(newUrl):
    r = requests.get(newUrl, allow_redirects=True)

    #   use OS to easily get file extension
    filename, file_extension = os.path.splitext(newUrl)
    lastinc = inc

    #  assuming last match is correct one, allow to run through matches and use last one only
    for match in re.finditer("[0-9]+", newUrl):

        inc = (newUrl[match.start():match.end()])

    #  update image path to save to 
    imagepath = folder + 'image' + inc + file_extension

    with open(imagepath, 'wb+') as f:
        f.write(r.content)

    # increment sequence number in string
    inc = str(int(inc) + 1).zfill(len(inc))

    #  update URL with next number in sequence
    newUrl = newUrl.replace(lastinc,inc)
    


print("no response from:", newUrl)
