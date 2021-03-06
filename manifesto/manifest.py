# -*- coding: utf-8 -*-
from bencode import bencode

from django.utils.hashcompat import sha_constructor


class Manifest(object):
    def fallback(self):
        return []

    def network(self):
        return ['*']

    def cache(self):
        return []

    def revision(self):
        revision = self.fallback() + self.network() + self.cache()
        return sha_constructor(bencode(revision)).hexdigest()[:7]
