# cia-server
the backend of cia-collectd

    # '''
    # 基础参数部分：
    #     chrome:cli＝10&ver＝alxg-3.3&dat=ns
    #     firefox:cli＝10&ver＝alxg-3.3&dat=ns
    # cdt参数部分
    #     rq: 同一个tab页打开本页面的次数
    #     wid: 打开当前页面的tabId
    #     t: 0|1 根据referer决定 payload.referer ? "1" : "0"
    #     ss：屏幕分辨率
    #     bw：窗口宽度
    #     winid：这个是tabId所在的windowId
    #     cttl: 页面load时间 window.performance.timing.domContentLoadedEventEnd-window.performance.timing.navigationStart,
    #     m: 可选 打开网站的方法 method 填GET即可
    #     s: http状态码 200 即可
    # 待更新的url
    #     ref= payload.referer ? encodeURIComponent( payload.referer )
    #     url＝inurl ? encodeURIComponent( inurl )
    # '''