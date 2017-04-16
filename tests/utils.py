# -*- coding: utf-8 -*-


class AttributeContainer(object):
    def __init__(self, **attrs):
        for name, value in attrs.items():
            setattr(self, name, value)
