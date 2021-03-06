#
#    Copyright (c) 2010 Brian E. Granger
#
#    This file is part of pyzmq.
#
#    pyzmq is free software; you can redistribute it and/or modify it under
#    the terms of the Lesser GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    pyzmq is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    Lesser GNU General Public License for more details.
#
#    You should have received a copy of the Lesser GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from unittest import TestCase

import zmq
from zmq.tests import BaseZMQTestCase

#-----------------------------------------------------------------------------
# Tests
#-----------------------------------------------------------------------------

class TestReqRep(BaseZMQTestCase):

    def test_basic(self):
        s1, s2 = self.create_bound_pair(zmq.REQ, zmq.REP)

        msg1 = 'message 1'
        msg2 = self.ping_pong(s1, s2, msg1)
        self.assertEquals(msg1, msg2)

    def test_multiple(self):
        s1, s2 = self.create_bound_pair(zmq.REQ, zmq.REP)

        for i in range(10):
            msg1 = i*' '
            msg2 = self.ping_pong(s1, s2, msg1)
            self.assertEquals(msg1, msg2)

    def test_bad_send_recv(self):
        s1, s2 = self.create_bound_pair(zmq.REQ, zmq.REP)
        self.assertRaises(zmq.ZMQError, s1.recv)
        self.assertRaises(zmq.ZMQError, s2.send, 'asdf')

        # I have to have this or we die on an Abort trap.
        msg1 = 'asdf'
        msg2 = self.ping_pong(s1, s2, msg1)
        self.assertEquals(msg1, msg2)

