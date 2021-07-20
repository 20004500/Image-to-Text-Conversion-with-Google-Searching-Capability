#Modified by Usama Khawar 2K18/ELE/119 , Dua Asif 2K18/ELE/25
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract  #these libraries for OCR

#these are for google related
import webbrowser
from search_engine_parser import GoogleSearch
from urllib.parse import quote

print("please wait...")
#from here
pytesseract.pytesseract.tesseract_cmd = r'F:\PYthon\tesseract.exe' #tessarct path here

text_from_image = pytesseract.image_to_string(Image.open('FET.png'))
#to here we copied from net


#this code we added to search detected text on google
def openInBrowser():
    url = "https://www.google.com.tr/search?q={}".format(quote(text_from_image, safe='')) 
    webbrowser.open(url)

def showInConsole():
    search_args = (text_from_image, 1)
    gsearch = GoogleSearch()
    gresults = gsearch.search(*search_args)
    for r in gresults:
        print("Title = " + r['titles'], end="\n")
        print("Links = " + r['links'], end="\n\n\n")

print("\t\tText Detected from Image\n\n")        
print(text_from_image)

print("\t\tImage to Google Search\n\n")
promtText = "Press 1 for open result in browser\nPress 2 to show result in console\nEnter> "
num1 = int(input(promtText))

if num1 == 1:
    openInBrowser()
else:
    showInConsole()
