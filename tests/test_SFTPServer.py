#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from unittest import TestCase

from psftp import SFTPServer

__author__ = 'Marco Bartel'

LOG = logging.getLogger()
logging.basicConfig(format='%(levelname)8s: %(message)s [%(name)s]',level=logging.DEBUG)

class TestSFTPServer(TestCase):
    def test_SFTPServer(self):

        server = SFTPServer()
        server.start()
