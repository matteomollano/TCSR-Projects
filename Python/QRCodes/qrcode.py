# basic_qrcode.py

import segno

# scale = controls the size of each pixel in the qr code
# border = controls how much white space surrounds the qr code
# light = background color of qrcode
# dark = color of qrcode
# quiet_zone = controls the color of the surrounding white space

# basic qr code
qrcode = segno.make_qr("www.nike.com")
qrcode.save("images/qrcode.png", scale=25, border=3, dark="#d974e8", light="#4fcfe8", quiet_zone="#d1f0d1")

# rotated qr code
qrcode = segno.make("www.google.com", error="h")
img = qrcode.to_pil(scale=25, border=3, dark="#d974e8", light="#4fcfe8", quiet_zone="#d1f0d1").rotate(45, expand=True)
img.save("images/qrcode.png")

# qr code with gif
qrcode = segno.make("www.apple.com", error="h")
qrcode.to_artistic(
    background="gifs/husky.gif", 
    target="gifs/husky_qrcode.gif",
    scale=10,
    dark="#d974e8", 
    light="#4fcfe8", 
    #quiet_zone="#d1f0d1"
)

# qrcode.save(
    # "images/qrcode.png", 
    # scale=15, dark="#004499", 
    # light="#CCEEFF", b
    # order=10, 
    # quiet_zone="#00BBFF"
# )

# qrcode.save(
#     "images/nike_qrcode.png", 
#     scale=10,  
#     light="lightblue",
#     dark="darkblue"
# )

# qrcode = segno.make("scratch.mit.edu", error="h")
# qrcode.to_artistic(background="gifs/rainbow cat.gif", target="gifs/angrypancake.gif", scale=10, dark="#004499")