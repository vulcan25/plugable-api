# -*- coding: utf-8 -*-

from .base import APIEndpoint
from .exceptions import BadRequest
from ..repositories import bananas
from flask import request


class Bananas(APIEndpoint):

    def get(self, farm_id=None):
        if farm:
            return bananas.all(farm_id=farm_id)
        else:
            return bananas.all()

    def post(self, farm_id=None):
        '''Create new banana.'''
        payload = request.json or {}
        banana_type, name = payload.get('type'), payload.get('name')
        farm_id = payload.get('farm') or farm_id
        if not banana_type or not name or not farm_id:
            raise BadRequest('"type", "farm" and "name" are required.')

        return bananas.new(banana_type=banana_type, name=name, farm_id=farm_id)