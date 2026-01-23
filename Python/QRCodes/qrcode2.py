import segno 

# basic qrcode
qrcode = segno.make_qr("golden retriever")
qrcode.save(
    "images/myqrcode.png",
    scale=10,
    dark="#D2042D",
    light="#ADD8E6",
    border=3,
    quiet_zone="#e09443"
)

# rotated qrcode
rotated_qrcode = segno.make("bing.com", error="h")
img = rotated_qrcode.to_pil(scale=10).rotate(45, expand=True)
img.save("images/myrotatedqrcode.png")

# gif qrcode
gif_qrcode = segno.make("wikipedia.org", error="h")
gif_qrcode.to_artistic(
    background="gifs/cute-cat.gif", 
    target="gifs/cat_qrcode.gif", 
    scale=10
)