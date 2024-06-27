import requests
import base64  
import json

CHANNEL_LIST = {
    
    
    'J': {
        'name': '翡翠台',
        'nameTC': '翡翠台',
        'license': '0958b9c657622c465a6205eb2252b8ed:2d2fd7b1661b1e28de38268872b48480',
        'logo': 'https://assets.livednow.com/logo/翡翠台.png'
    },
   'C': {
        'name': '无线新闻台',
        'nameTC': '無綫新聞台',
        'license': '90a0bd01d9f6cbb39839cd9b68fc26bc:51546d1f2af0547f0e961995b60a32a1',
        'logo': 'https://assets.livednow.com/logo/無線新聞台.png'
    },
    'P': {
        'name': '明珠台',
        'nameTC': '明珠台',
        'license': 'e04facdd91354deee318c674993b74c1:8f97a629de680af93a652c3102b65898',
        'logo': 'https://assets.livednow.com/logo/明珠台.png'
    },
    'B': {
        'name': 'TVB plus',
        'nameTC': 'TVB plus',
        'license': '56603b65fa1d7383b6ef0e73b9ae69fa:5d9d8e957d2e45d8189a56fe8665aaaa',
        'logo': 'https://img.sky4k.top/TVB_Plus_CheerVisionTV.png'
    },
    
   'JUHD': {
        'name': '翡翠台 4K',
        'nameTC': '翡翠台(超高清)',
        'license': '2c045f5adb26d391cc41cd01f00416fa:fc146771a9b096fc4cb57ffe769861be',
        'logo': 'https://assets.livednow.com/logo/翡翠台.png'
    },
    'CWIN': {
        'name': 'Super Free',
        'nameTC': 'Super Free',
        'license': '0737b75ee8906c00bb7bb8f666da72a0:15f515458cdb5107452f943a111cbe89',
        'logo': 'https://xiaotan.860775.xyz/mytvsuper.png'
    },
    'TVG': {
        'name': '黃金翡翠台',
        'nameTC': '黃金翡翠台',
        'license': '8fe3db1a24969694ae3447f26473eb9f:5cce95833568b9e322f17c61387b306f',
        'logo': 'https://xiaotan.860775.xyz/mytvsuper.png'
    },
    
    'CTVE': {
        'name': '娱乐新闻台',
        'nameTC': '娛樂新聞台',
        'license': '6fa0e47750b5e2fb6adf9b9a0ac431a3:a256220e6c2beaa82f4ca5fba4ec1f95',
        'logo': 'https://gitjs.wokaotianshi123.cloudns.org/https://raw.githubusercontent.com/sparkssssssssss/epg/main/logo/%E5%A8%B1%E4%B9%90%E6%96%B0%E9%97%BB%E5%8F%B0.png',
    },
    'PCC': {
        'name': '凤凰卫视中文台',
        'nameTC': '鳳凰衛視中文台',
        'license': '7bca0771ba9205edb5d467ce2fdf0162:eb19c7e3cea34dc90645e33f983b15ab',
        'logo': 'https://assets.livednow.com/logo/鳳凰中文.png'
    },
    'PIN': {
        'name': '凤凰卫视资讯台',
        'nameTC': '鳳凰衛視資訊台',
        'license': '83f7d313adfc0a5b978b9efa0421ce25:ecdc8065a46287bfb58e9f765e4eec2b',
        'logo': 'https://assets.livednow.com/logo/鳳凰資訊.png'
    },
    'PHK': {
        'name': '凤凰卫视香港台',
        'nameTC': '鳳凰衛視香港台',
        'license': 'cde62e1056eb3615dab7a3efd83f5eb4:b8685fbecf772e64154630829cf330a3',
        'logo': 'https://assets.livednow.com/logo/鳳凰香港.png'
    },
    'CC1': {
        'name': 'cctv-1 (港澳版)',
        'nameTC': '中央電視台綜合頻道 (港澳版)',
        'license': 'e50b18fee7cab76b9f2822e2ade8773a:2e2e8602b6d835ccf10ee56a9a7d91a2',
        'logo': 'https://assets.livednow.com/logo/CCTV1.png'
    },
    'CRE': {
        'name': '创世电视',
        'nameTC': '創世電視',
        'license': 'adef00c5ba927d01642b1e6f3cedc9fb:b45d912fec43b5bbd418ea7ea1fbcb60',
        'logo': 'https://xiaotan.860775.xyz/%E5%89%B5%E4%B8%96%E9%9B%BB%E8%A6%96.png'
    }
        
}

def get_mytvsuper(channel):
    if channel not in CHANNEL_LIST:
        return '频道代号错误'

    api_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJib3NzX2lkIjoiODUwNDY0NTgwIiwiZGV2aWNlX3Rva2VuIjoiWHp6anMzYTVKTms2TFpnZmJQeFZHR2QzIiwiZGV2aWNlX2lkIjoiTldGalptSmxNREF0TkRJNU5TMDBaakV3TFRrNFl6QXRNbUkwT0RCbFpXRTJaVEV3IiwiZGV2aWNlX3R5cGUiOiJ3ZWIiLCJkZXZpY2Vfb3MiOiJicm93c2VyIiwiZHJtX2lkIjoiTldGalptSmxNREF0TkRJNU5TMDBaakV3TFRrNFl6QXRNbUkwT0RCbFpXRTJaVEV3IiwiZXh0cmEiOnsicHJvZmlsZV9pZCI6MX0sImlhdCI6MTcwOTgwNTA3NywiZXhwIjoxNzA5ODA4Njc3fQ.XG-C6gWxLgbBRQ3ttKn68AKMQLOg6SxTpbmHxXl_qI2dbjd1eFFmwB9kD1yd2N_X8HxLPBwJukD4lygIKxbBGrQQDY_1vNd76TldllaeE2BC3fUtc-kAFOU4JwbUkfFYsWVm3v2JP-YGM2GGlhFqN_3170WDAi2Gq-R0tZckeFNWk7jOSShqkE0E7L3eqJ09sDG76R-PCbdpnCIxaY_NXtoYRfIoVQZA9QysExUyO6hQGUxLaTvJDtflX_ZM3OiqTMndHp1p0cDsINnpFokD6Yby5XS18RjQ-Dn1XJznj7-sRjlaGgyIIBoJjxsR2oD5S8teA5S6x7w3Dv6uTO3bWVV9J60E6jguGVqKnSYJ4Rx8A1TgyUTT_g57key6UFIiEhkHYqk7s3H01V-lHffNp5zDo9UrCdaO6maW_ZeA85ohR6P1PMh9EakQ5A-vok60s2oqyokKHfyrQvcodsI-MTC9mKegjJzgV2-HBgyylyj6B2ewvE4icDD25UdspWgbc33NrRpe_kgPxgVKF4cgKCD-S1AT3WrOaqKnPfPvhqmlciwlpZrUqZg09BqcazWPoyWAp2nqf93H6tlDqMrtAQgvft3Nd8-cM7jYx-WvzqRrCRpZ8vRSv11UdezKzR2Jm4H64KTWbs3GxB5vboZaeypdEzQW6PipPpftqRnNMQU'  # Replace with your actual API token
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Host': 'user-api.mytvsuper.com',
        'Origin': 'https://www.mytvsuper.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15',
        'Referer': 'https://www.mytvsuper.com/',
        'X-Forwarded-For': '210.6.4.148'  # 香港原生IP  210.6.4.148
    }

    params = {
        'platform': 'android_tv',
        'network_code': channel
    }

    url = 'https://user-api.mytvsuper.com/v1/channel/checkout'
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"请求失败:{CHANNEL_LIST[channel]['name']}")
        return ''#请求失败

    response_json = response.json()




    


    
    profiles = response_json.get('profiles', [])

    play_url = ''
    for profile in profiles:
        if profile.get('quality') == 'high':
            play_url = profile.get('streaming_path', '')
            break

    if not play_url:
        return '未找到播放地址'

    play_url = play_url.split('&p=')[0]


    license_key = CHANNEL_LIST[channel]['license']
    license_data = encode_keys(license_key)  
    print(f"hexTOBase64：{license_data}")

    channel_name = CHANNEL_LIST[channel]['name']
    channel_logo = CHANNEL_LIST[channel]['logo']
    m3u_content = f"#EXTINF:-1 tvg-id=\"{channel_name}\" tvg-name=\"{channel_name}\" tvg-logo=\"{channel_logo}\",{channel_name}\n"
    m3u_content += "#KODIPROP:inputstream.adaptive.manifest_type=mpd\n"
    m3u_content += "#KODIPROP:inputstream.adaptive.license_type=clearkey\n"
    m3u_content += f"#KODIPROP:inputstream.adaptive.license_key={license_data}\n"
    m3u_content += f"{play_url}\n"

    return m3u_content


def encode_keys(hex_keyi_key):  
    hex_keyid, hex_key = hex_keyi_key.split(':')  
    bin_keyid = bytes.fromhex(hex_keyid)  
    keyid64 = base64.b64encode(bin_keyid).decode('utf-8').rstrip('=')  
    bin_key = bytes.fromhex(hex_key)  
    key64 = base64.b64encode(bin_key).decode('utf-8').rstrip('=')  
  
    
    keys = [{"kty": "oct", "k": key64, "kid": keyid64}]  
  
    
    license = {"keys": keys, "type": "temporary"}  
  
    
    return json.dumps(license)  



# 创建或打开文件用于写入
with open('mytvsuper.m3u', 'w', encoding='utf-8') as m3u_file:
    # 写入 M3U 文件的头部 http://epg.51zmt.top:8000/e.xml,xmltv.bph.workers.dev这个需要翻墙不用了
    #m3u_file.write("#EXTM3U url-tvg=\"https://xmltv.bph.workers.dev\"\n")
    #m3u_file.write("#EXTM3U url-tvg=\"http://epg.51zmt.top:8000/e.xml\"\n")
    #2.tvb的,3.tvb的,4.xmltv.bph.workers.dev要科学,1:全局的,
    #url_tvg = "http://zzqwe.giize.com:12228/epgmysuper.xml,http://zzqwe.giize.com:12228/epganywhere.xml,http://epg.51zmt.top:8000/e.xml"
    catchup = "append"
    catchup_source = "?playseek=${(b)yyyyMMddHHmmss}-${(e)yyyyMMddHHmmss}"

    #m3u_file.write('#EXTM3U url-tvg=\"{url_tvg}\" catchup="{catchup}" catchup-source="{catchup_source}"\n')
    m3u_file.write(f'#EXTM3U url-tvg=\"http://epg.51zmt.top:8000/e.xml\" catchup=\"{catchup}\" catchup-source=\"{catchup_source}\"\n')
    # 遍历所有频道并写入每个频道的 M3U 内容
    for channel_code in CHANNEL_LIST.keys():
        m3u_content = get_mytvsuper(channel_code)
        m3u_file.write(m3u_content)


print("所有频道的 M3U 播放列表已生成并保存为 'mytvsuper.m3u'。")
