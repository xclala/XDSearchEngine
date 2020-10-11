def info(keywd):
    from requests import get
    req = get(f'https://www.baidu.com/s?ie=UTF-8&wd={keywd}', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}).text
    req = req.replace(
        '<img class="index-logo-src" src="" alt="到百度首页" title="到百度首页">', '')
    req = req.replace(
        '<a href="https://passport.baidu.com/v2/?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2F" name="tj_login" class="lb" onclick="return false;">登录</a>', '<a href="localhost">')
    req = req.replace('百度', '邢栋的搜索引擎')
    req = req.replace(
        '<input type="submit" id="su" value="百度一下" class="bg s_btn">', '')
    req = req.replace('<span class="bg s_ipt_wr quickdelete-wrap"><span class="soutu-btn"></span><input id="kw" name="wd" class="s_ipt" value="hi" maxlength="255" autocomplete="off"><a href="javascript:;" id="quickdelete" title="清空" class="quickdelete" style="top: 0px; right: 0px; display: block;"></a><span class="soutu-hover-tip" style="display: none;">按图片搜索</span></span>', '')
    return req.replace('//www.baidu.com/img/flexible/logo/pc/result.png', '')
