# -*- coding: utf-8 -*-
from collective.azipfele.interfaces import IZipState
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse
import json


@implementer(IPublishTraverse)
class ZipperStateView(BrowserView):

    def __call__(self):
        self.request.response.setHeader('Content-Type', 'application/json')
        state = IZipState(self.uid)
        result = {
            'task': state['task'],
            'queued': state['queued'],
            'started': state['started'],
            'ended': state['ended'],
        }
        return json.dumps(result)

    def publishTraverse(self, request, name):
        self.uid = name
        return self