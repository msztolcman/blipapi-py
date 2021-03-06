# -*- coding: utf-8 -*-
#
# Blip! (http://blip.pl) communication library.
# Author: Marcin Sztolcman <marcin /at/ urzenia /dot/ net>
# Version: 0.02.11
# Copyright: (r) 2009 Marcin Sztolcman
# License: http://opensource.org/licenses/lgpl-3.0.html The GNU Lesser General Public License, version 3.0 (LGPLv3)

def read (**args):
    """ Read movie data from specified update. """

    if not args.get ('id'):
        raise ValueError ('Update ID is missing.')

    return dict (
        url     = '/updates/' + str (args['id']) + '/movie',
        method  = 'get',
    )

