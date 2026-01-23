import segno

# rotated qrcode
qrcode = segno.make('Hello, World!', error='h')
img = qrcode.to_pil(scale=10, dark="blue", light="lightblue").rotate(45, expand=True)
img.save("images/rotated_qrcode.png")

# with gif
qrcode = segno.make('dog gif', error='h')
qrcode.to_artistic(background='dog.gif', target='dog_qrcode.gif', scale=10)

# from gif link
import io
from urllib.request import urlopen

qrcode = segno.make('dog gif from link', error='h')
url = 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjJhYmJ4OGxmOXBnamJ2bWMwdzQ4NmVmejIzN2NsbjNkbjN2ZDNleCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hSoFXPq2J3PWvYKyUn/giphy.gif'

# open the gif into a background image
bg_file = urlopen(url)

# create a BytesIO object to store the artistic qrcode
out = io.BytesIO()
qrcode.to_artistic(background=bg_file, target=out, scale=10, kind='gif')

# write the qrcode byte data to a file using the BytesIO object
with open('dog_qrcode_from_link.gif', 'wb') as file:
    file.write(out.getvalue())