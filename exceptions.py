# -*- coding: utf-8 -*-
'''
Wrapper classes to return JSON exception, not HTML exception as werkzeug does.
'''
from flask.exceptions import JSONHTTPException
from werkzeug import exceptions


class BadRequest(JSONHTTPException, exceptions.BadRequest):
    pass


class Unauthorized(JSONHTTPException, exceptions.Unauthorized):
    pass


class Forbidden(JSONHTTPException, exceptions.Forbidden):
    pass
