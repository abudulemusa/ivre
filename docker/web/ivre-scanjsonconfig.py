# This file is part of IVRE.
# Copyright 2011 - 2014 Pierre LALET <pierre.lalet@cea.fr>
#
# IVRE is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IVRE is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with IVRE. If not, see <http://www.gnu.org/licenses/>.

import ivre.utils
import re
import os
ipaddr = re.compile('^\d+\.\d+\.\d+\.\d+$')
get_notepad_pages = lambda: [
    ivre.utils.ip2int(x[:-4])
    for x in os.listdir("/var/lib/dokuwiki/data/pages")
    if x.endswith('.txt') and ipaddr.match(x[:-4])
]