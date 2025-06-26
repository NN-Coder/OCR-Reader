import requests
import json
import os

def ocr_space_file(filename, overlay=False, api_key="K87947986188957", language='eng'):
    #OCR API specs
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    #driver code
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    #driver code: opening each image.png
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    #decoding JSON format into Parsed Text
    y = json.loads(r.content.decode())
    print(y)
    
    #printing parsed text
    print(y['ParsedResults'][0]['ParsedText'])

    #opening a .txt file and writing the parsed text in it
    file = open("OCR_Text.txt", "a")
    file.write(curfile)
    file.write(y['ParsedResults'][0]['ParsedText'])
    file.write('\n')
    file.close()

    #returning decoded content
    return r.content.decode()

#running driver code using function mechanics and folder iteration
path = "_____" #my data redacted
os.chdir(path)
for curfile in os.listdir():
    if curfile.endswith(".jpg"):
        ocr_space_file(curfile)
