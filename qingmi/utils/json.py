# coding: utf-8
from __future__ import unicode_literals
from flask import jsonify


def success(code=0, msg='SUCCESS', _data=None, **kwargs):
    res = dict(code=code, msg=msg)
    if _data is not None:
        res['data'] = _data
    elif kwargs:
        res['data'] = kwargs
    return jsonify(res)

def error(code=-1, msg='ERROR', _data=None, **kwargs):
    res = dict(code=code, msg=msg)
    if _data is not None:
        res['data'] = _data
    elif kwargs:
        res['data'] = kwargs
    return jsonify(res)