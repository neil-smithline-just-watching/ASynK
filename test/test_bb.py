##
## Created       : Sat Apr 07 20:03:04 IST 2012
## Last Modified : Tue May 15 17:06:19 IST 2012
##
## Copyright (C) 2012 Sriram Karra <karra.etc@gmail.com>
##
## This file is part of ASynK
##
## ASynK is free software: you can redistribute it and/or modify it under
## the terms of the GNU Affero General Public License as published by the
## Free Software Foundation, version 3 of the License
##
## ASynK is distributed in the hope that it will be useful, but WITHOUT
## ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
## License for more details.
##
## You should have a copy of the license in the doc/ directory of ASynK.  If
## not, see <http://www.gnu.org/licenses/>.
##

import logging, os, os.path, sys, traceback

## Being able to fix the sys.path thusly makes is easy to execute this
## script standalone from IDLE. Hack it is, but what the hell.
DIR_PATH    = os.path.abspath(os.path.dirname(os.path.realpath('../Gout')))
EXTRA_PATHS = [os.path.join(DIR_PATH, 'lib'), os.path.join(DIR_PATH, 'asynk')]
sys.path = EXTRA_PATHS + sys.path

from state         import Config
from pimdb_bb      import BBPIMDB
from folder_bb     import BBContactsFolder
from contact_bb    import BBContact

def main (argv=None):
    print sys.argv

    if len(sys.argv) > 1:
        bbfn = sys.argv[1]
    else:
        bbfn = '/Users/sriramkarra/.bbdb.t'

    tests = TestBBContact(config_fn='../config.json',
                          state_fn='../state.json',
                          bbfn=bbfn)
    if len(sys.argv) > 2:
        name = sys.argv[2]
    else:
        name = 'Amma'

    tests.print_contacts(name=name)
    # tests.write_to_file()

class TestBBContact:
    def __init__ (self, config_fn, state_fn, bbfn):
        logging.debug('Getting started... Reading Config File...')

        self.config = Config(config_fn, state_fn)
        self.bb     = BBPIMDB(self.config, bbfn)
        ms          = self.bb.get_def_msgstore()
        self.deff   = ms.get_folder(ms.get_def_folder_name())

    def print_contacts (self, cnt=0, name=None):
        self.deff.print_contacts(cnt=cnt, name=name)

    def write_to_file (self):
        self.deff.save()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main()
