# -*- coding: utf-8 -*-

from .bananas import Bananas
from .base import bmi_api


the_api.add_url_rule('/bananas', view_func=Bananas.as_view('bananas'))

__all__ = [
    'the_api'
]