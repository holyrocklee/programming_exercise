# -*- coding: utf-8 -*-
# Author  ：Rocklee
# Time  ：2019/9/19  15:18 

import six

# print(json_tools.diff(dict1,dict2))
def diff(local, other):
    """ 计算两个JSON数据之间的差异。
    """
    def _recursive_diff(l, r, res, path='/'):
        if type(l) != type(r):
            res.append({
                'replace': path,
                'value': r,
                'details': 'type',
                'prev': l
            })
            return

        delim = '/' if path != '/' else ''

        if isinstance(l, dict):
            for k, v in six.iteritems(l):
                new_path = delim.join([path, k])
                if k not in r:
                    res.append({'remove': new_path, 'prev': v})
                else:
                    _recursive_diff(v, r[k], res, new_path)
            for k, v in six.iteritems(r):
                if k in l:
                    continue
                res.append({
                    'add': delim.join([path, k]),
                    'value': v
                })
        elif isinstance(l, list):
            ll = len(l)
            lr = len(r)
            if ll > lr:
                for i, item in enumerate(l[lr:], start=lr):
                    res.append({
                        'remove': delim.join([path, str(i)]),
                        'prev': item,
                        'details': 'array-item'
                    })
            elif lr > ll:
                for i, item in enumerate(r[ll:], start=ll):
                    res.append({
                        'add': delim.join([path, str(i)]),
                        'value': item,
                        'details': 'array-item'
                    })
            minl = min(ll, lr)
            if minl > 0:
                for i, item in enumerate(l[:minl]):
                    _recursive_diff(item, r[i], res, delim.join([path, str(i)]))
        else:  # both items are atomic
            if l != r:
                res.append({
                    'replace': path,
                    'value': r,
                    'prev': l
                })

    result = []
    _recursive_diff(local, other, result)
    return result

dict1 = {
    "HeWeather6": [
        {
            "status": "ok",
            "now": {
                "wind_dir": "东北风",
                "wind_spd": "11",
                "wind_sc": "2",
                # "sun":[123,456]
            }
        }
    ]
}

dict2 = {
    "HeWeather6": [
        {
            "status": "ok",
            "now": {
                "wind_dir": "东北风",
                "wind_sc": "2",
                "wind_spd": "11",
                # "sun":[456,123]
            }
        }
    ]
}
#输出的结果如果是[]，则表示两个json字符串相等；如果不同，则输出一个包含两个元素（对比显示出不同之处）的列表
print(diff(dict1,dict2))