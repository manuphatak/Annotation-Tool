# -*- coding: utf-8 -*-
__version__ = '0.5.1'
__version_info__ = tuple(  # :off
    [
        int(num) if num.isdigit() else num
        for num in __version__.replace('-', '.', 1).split('.')
    ]
)  # :on

from . import users, contrib
