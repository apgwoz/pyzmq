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

import zmq

from zmq.tests import BaseZMQTestCase

#-----------------------------------------------------------------------------
# Tests
#-----------------------------------------------------------------------------

class TestP2p(BaseZMQTestCase):

    def test_basic(self):
        s1, s2 = self.create_bound_pair(zmq.P2P, zmq.P2P)

        msg1 = 'message1'
        msg2 = self.ping_pong(s1, s2, msg1)
        self.assertEquals(msg1, msg2)

    def test_multiple(self):
        s1, s2 = self.create_bound_pair(zmq.P2P, zmq.P2P)

        for i in range(10):
            msg = i*' '
            s1.send(msg)

        for i in range(10):
            msg = i*' '
            s2.send(msg)

        for i in range(10):
            msg = s1.recv()
            self.assertEquals(msg, i*' ')

        for i in range(10):
            msg = s2.recv()
            self.assertEquals(msg, i*' ')

