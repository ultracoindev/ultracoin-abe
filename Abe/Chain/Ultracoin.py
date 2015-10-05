# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.


from .ScryptJaneChain import ScryptJaneChain
from .PpcPosChain import PpcPosChain

class Ultracoin(ScryptJaneChain, PpcPosChain):
    def __init__(chain, **kwargs):
        chain.name = 'Ultracoin'
        chain.code3 = 'UTC'
        chain.address_version = "\x44"
        chain.script_addr_vers = '\x06'
        chain.magic = "\xd9\xe6\xe7\xf5"
        chain.decimals = 6
        super(Ultracoin, chain).__init__(**kwargs)

    datadir_conf_file_name = "ultracoin.conf"
    datadir_rpcport = 44201
    start_time = 1388361600

