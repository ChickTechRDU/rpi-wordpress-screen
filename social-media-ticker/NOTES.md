# Get latest post

```python
import requests
response = requests.get('http://demo.wp-api.org/wp-json/wp/v2/posts?per_page=1')
post = response.json()[0]
print('{0}: {1}'.format(post['date'], post['title']['rendered'])
```

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

## python oled bindings

Requires libjpeg62-turbo-dev to be installed

```
sudo apt-get install python-dev python-pip libfreetype6-dev libjpeg-dev build-essential
```




