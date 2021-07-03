def info(keywd):
    from requests import get
    from headers import headers
    r = get(
        f'https://www.baidu.com/s?ie=UTF-8&wd={keywd}', headers=headers())
    r.encoding = 'utf-8'
    req = r.text
    req = req.replace(
        '<img class="index-logo-src" src="" alt="到百度首页" title="到百度首页">', '')
    req = req.replace(
        '<a href="https://passport.baidu.com/v2/?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2F" name="tj_login" class="lb" onclick="return false;">登录</a>', '<a href="localhost">')
    req = req.replace('百度', '邢栋的搜索引擎')
    req = req.replace('<span class="bg s_ipt_wr quickdelete-wrap"><span class="soutu-btn"></span><input id="kw" name="wd" class="s_ipt" value="hi" maxlength="255" autocomplete="off"><a href="javascript:;" id="quickdelete" title="清空" class="quickdelete" style="top: 0px; right: 0px; display: block;"></a><span class="soutu-hover-tip" style="display: none;">按图片搜索</span></span>', '')
    req = req.replace('邢栋的搜索引擎热榜','')
    req = req.replace('换一换','')
    return req.replace('//www.baidu.com/img/flexible/logo/pc/result.png', '')