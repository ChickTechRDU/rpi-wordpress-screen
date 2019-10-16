# Get latest post

```python
import requests
response = requests.get('http://demo.wp-api.org/wp-json/wp/v2/posts?per_page=1')
post = response.json()[0]
print('{0}: {1}'.format(post['date'], post['title']['rendered']))
```

On localhost will be something like http://blog.example.com/index.php/wp-json/wp/v2/posts?per_page=1

# OLED

How to guide: http://codelectron.com/setup-oled-display-raspberry-pi-python/

Pinout reference: https://pinout.xyz/

## Enable i2c module

1. `$ raspi-config`
2. In menus: 5 -> P5 -> Yes
3. And restart
4. Should see file at `/dev/i2c-1`

`modinfo i2c_dev` shows some more interesting information

`raspi-gpio get` lists all the pins

`i2cdetect -r 1` probes for address

## python oled/ssd1306 bindings

ssd1306 spec: https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf

Requires libjpeg62-turbo-dev to be installed

```
sudo apt-get install python-dev python-pip libfreetype6-dev libjpeg-dev build-essential
```

Example:

```python
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

# Box and text rendered in portrait mode
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((10, 40), "WWW.CODELECTRON.COM", fill="white")
```

### Font support

```python
from PIL import ImageFont, ImageDraw

# Snip....

with canvas(device) as draw:
    font = ImageFont.truetype('/usr/share/fonts/opentype/linux-libertine/LinLibertine_M.otf',20)
    draw.text((0, 0), "Hello World", font=font, fill=255)
```

### Polling

```python
#!/usr/bin/env python
import os
import sys
import time
import random
import requests
from luma.core.interface.serial import i2c
from luma.core.render import canvas 
from luma.oled.device import ssd1306

def fetch_latest_post():
    try: 
        response = requests.get('http://blog.example.com/wp-json/wp/v2/posts?per_page=1')
        # TODO: Detect if no posts
        return response.json()[0]
    except:
        print("Error fetching latest post")

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

while True:
    post = fetch_latest_post()
    title = post['title']['rendered']
    with canvas(device) as draw:
        x = random.randint(0,60)
        y = random.randint(0,40)
        draw.text((x, y), title, fill="white")
    time.sleep(3)
```

Attempting to render content

```python
#!/usr/bin/env python
import os
import sys
import time
import random
import requests
import imgkit
import io
from luma.core.interface.serial import i2c
from luma.core.render import canvas 
from luma.oled.device import ssd1306
from PIL import Image

def fetch_latest_post():
    try: 
        response = requests.get('http://blog.example.com/wp-json/wp/v2/posts?per_page=1')
        # TODO: Detect if no posts
        return response.json()[0]
    except:
        print("Error fetching latest post")

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

while True:
    post = fetch_latest_post()
    content = post['content']['rendered']
    as_binary = imgkit.from_string(content, False, options={'format': 'jpg', 'xvfb': ''})
    bytesio = io.BytesIO(as_binary)
    bytesio.seek(0)
    as_image = Image.open(bytesio)
    fff = Image.new(as_image.mode, as_image.size, (255,) * 4)
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - as_image.width) // 2, 0)
    title = post['title']['rendered']
    with canvas(device) as draw:
        #x = random.randint(0,60)
        #y = random.randint(0,40)
        #draw.text((x, y), title, fill="white")
        background.paste(img, posn)
        device.display(background.convert(device.mode))
    time.sleep(10)
```
