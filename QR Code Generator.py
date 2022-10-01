
import pyqrcode 
from pyqrcode import QRCode 

print( "QR Code Genrator")
link  = str(input("Enter the link:"))  

s = (link) 
url = pyqrcode.create(s) 
   
url.svg("Your QR", scale = 8) 