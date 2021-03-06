# -*- coding: utf-8 -*-
#
# Blip! (http://blip.pl) communication library.
# Author: Marcin Sztolcman <marcin /at/ urzenia /dot/ net>
# Version: 0.02.11
# Copyright: (r) 2009 Marcin Sztolcman
# License: http://opensource.org/licenses/lgpl-3.0.html The GNU Lesser General Public License, version 3.0 (LGPLv3)

import os.path

from _utils import encode_multipart

def create (**args):
    """ Create new directed message. """

    if not args.get ('body') or not args.get ('user'):
        raise ValueError ('Directed_message body or recipient is missing.')

    fields = {
        'directed_message[body]':      args['body'],
        'directed_message[recipient]': args['user'],
    }
    if args.get ('image') and os.path.isfile (args['image']):
        fields['directed_message[picture]'] = (args['image'], args['image'], )

    data, boundary = encode_multipart (fields)

    return dict (
        url         = '/directed_messages',
        method      = 'post',
        data        = data,
        boundary    = boundary,
    )

def read (**args):
    """ Read directed messages to specified or logged user, or by ID. """

    if args.get ('user'):
        if args['user'] == '__ALL__':
            if args.get ('since_id'):
                url = '/directed_messages/' + str (args['since_id']) + '/all_since'
            else:
                url = '/directed_messages/all'
        else:
            if args.get ('since_id'):
                url = '/users/' + args['user'] + '/directed_messages/' + str (args['since_id']) + '/since'
            else:
                url = '/users/' + args['user'] + '/directed_messages'
    elif args.get ('id'):
        url = '/directed_messages/' + str (args['id'])

    else:
        url = '/directed_messages'
        if args.get ('since_id'):
            url += str (args['since_id']) + '/since'

    params = dict ()
    params['limit']     = args.get ('limit', 10)
    params['offset']    = args.get ('offset', 0)
    params['include']   = ','.join (args.get ('include', ''))

    return dict (
        url     = url,
        method  = 'get',
        params  = params,
    )

def delete (**args):
    """ Delete directed message. """

    if not args.get ('id'):
        raise ValueError ('Directed_message ID is missing.')

    return dict (
        url     = '/directed_messages/' + str (args['id']),
        method  = 'delete',
    )

