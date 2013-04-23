# -*- coding: utf-8 -*-

from .base import APIEndpoint
from .exceptions import BadRequest
from ..repositories import bananas
from flask import request


class Bananas(APIEndpoint):

    def get(self):
        return bananas.all()

    def post(self):
        '''Create new banana.'''
        payload = request.json or {}
        banana_type, name = payload.get('type'), payload.get('name')
        if not banana_type or not name:
            raise BadRequest('Both "type" and "name" are required.')

        return bananas.new(banana_type=banana_type, name=name)