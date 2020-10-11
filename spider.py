def info(keywd):
    from requests import get
    req = get(f'https://m.sm.cn/s?q={keywd}', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}).text
    return req


