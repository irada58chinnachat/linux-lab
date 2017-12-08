import sys
import click
import requests
import json
import re

from bs4 import BeautifulSoup
from PIL import Image
try:
    from StringIO import StringIO
except: # when using python3.x
    from io import BytesIO, StringIO



#url = 'https://www.toonzaa.com/?s={}'


@click.command()
@click.option('--as-author', '-c', is_flag=True, help='Computer Science at UBU')
@click.argument('name', default='wichit2s', required=False)
def main(name, as_author):
    """Get Github Avatar"""
    #greet = 'Howdy' if as_cowboy else 'Hello'
    #click.echo('{0}, {1}.'.format(greet, name))
    url = 'https://www.toonzaa.com/?s={}'.format(name)
    r=requests.get(url.format(name))
    b = BeautifulSoup(r.text, 'lxml')
    images = b.find_all('img')

    imgurl = images[-1]['src']
 
    req = requests.get(imgurl)
    if sys.version_info >= (3,0):
        img = Image.open(BytesIO(req.content))
        img.show()
    else:
        img = Image.open(StringIO(req.content))
        img.show()
