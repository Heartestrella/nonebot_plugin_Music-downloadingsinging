import httpx
from nonebot.matcher import Matcher
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.params import CommandArg, ArgPlainText, Arg, EventPlainText
import base64
import binascii
import json
import random
import string
from urllib import parse
from Crypto.Cipher import AES
import requests
hand = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
p = '唱歌'
hello = on_command(p)


@hello.handle()
async def _(matcher: Matcher, foo: Message = CommandArg()):
    plain_text = foo.extract_plain_text()
    if plain_text:
        matcher.set_arg("city", foo)


@hello.got(key='city', prompt='输入歌名')
async def _(mucis: Matcher, city: Message = Arg(), city_name: str = ArgPlainText("city")):
    global resp
    
    resp = await mucis_name_get(nameis=city_name)
    mucis_name_0 = '0:'+resp['result']['songs'][0]['name']
    mucis_name_1 = '1:'+resp['result']['songs'][1]['name']
    mucis_name_2 = '2:'+resp['result']['songs'][2]['name']
    mucis_name_3 = '3:'+resp['result']['songs'][3]['name']
    mucis_name_4 = '4:'+resp['result']['songs'][4]['name']
    mucis_name_5 = '5:'+resp['result']['songs'][5]['name']
    mucis_name_6 = '6:'+resp['result']['songs'][6]['name']
    mucis_name_7 = '7:'+resp['result']['songs'][7]['name']
    mucis_name_8 = '8:'+resp['result']['songs'][8]['name']
    mucis_name_9 = '9:'+resp['result']['songs'][9]['name']
    mucis_name = f'''
{mucis_name_0}
{mucis_name_1}
{mucis_name_2}
{mucis_name_3}
{mucis_name_4}
{mucis_name_5}
{mucis_name_6}
{mucis_name_7}
{mucis_name_8}
{mucis_name_9}
                '''
    
    mucis_name = mucis_name.strip()
    await hello.send(mucis_name)


@hello.got(key='mucis', prompt='请输入序号')
async def a(xuhao: str = EventPlainText()):
    ids = resp['result']['songs'][int(xuhao)]['id']

    url = await mucis_url(ids=ids)
    await hello.send(await hello.send(MessageSegment.record(url)))


async def mucis_name_get(nameis):

    def get_random():
        random_str = ''.join(random.sample(
            string.ascii_letters + string.digits, 16))
        return random_str

    def len_change(text):
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        text = text.encode("utf-8")
        return text

    def aes(text, key):
        # 首先对加密的内容进行位数补全，然后使用 CBC 模式进行加密
        iv = b'0102030405060708'
        text = len_change(text)
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(text)
        encrypt = base64.b64encode(encrypted).decode()
        return encrypt

    def b(text, str):
        first_data = aes(text, '0CoJUm6Qyw8W8jud')
        second_data = aes(first_data, str)
        return second_data

    def c(text):
        e = '010001'
        f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        text = text[::-1]
        result = pow(int(binascii.hexlify(text.encode()), 16),
                     int(e, 16), int(f, 16))
        return format(result, 'x').zfill(131)

    def get_final_param(text, str):
        params = b(text, str)
        encSecKey = c(str)
        return {'params': params, 'encSecKey': encSecKey}


    d = {"hlpretag": "<span class=\"s-fc7\">", "hlposttag": "</span>", "s": nameis, "type": "1", "offset": "0",
            "total": "true", "limit": "30", "csrf_token": ""}
    d = json.dumps(d)
    random_param = get_random()
    param = get_final_param(d, random_param)
    data1 = {
            'params':param['params'],
            'encSecKey':param['encSecKey']
        }
    url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='

    resp = httpx.post(url, headers=hand, data=data1).json()

    return resp
    

async def mucis_url(ids):
    def get_random():
        random_str = ''.join(random.sample(
            string.ascii_letters + string.digits, 16))
        return random_str

    def len_change(text):
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        text = text.encode("utf-8")
        return text

    def aes(text, key):
        # 首先对加密的内容进行位数补全，然后使用 CBC 模式进行加密
        iv = b'0102030405060708'
        text = len_change(text)
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(text)
        encrypt = base64.b64encode(encrypted).decode()
        return encrypt

    def b(text, str):
        first_data = aes(text, '0CoJUm6Qyw8W8jud')
        second_data = aes(first_data, str)
        return second_data

    def c(text):
        e = '010001'
        f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        text = text[::-1]
        result = pow(int(binascii.hexlify(text.encode()), 16),
                     int(e, 16), int(f, 16))
        return format(result, 'x').zfill(131)

    def get_final_param(text, str):
        params = b(text, str)
        encSecKey = c(str)
        return {'params': params, 'encSecKey': encSecKey}
    
    random_param = get_random()
    d = {"ids": "[" + str(ids) + "]", "level": "standard", "encodeType": "",
            "csrf_token": ""}
    d = json.dumps(d)

    param = get_final_param(d, random_param)
    data = {
        'params':param['params'],
        'encSecKey':param['encSecKey']
    }
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='

    resp = httpx.post(url, headers=hand, data=data).json()
    url = resp['data'][0]['url']
    return url
    
