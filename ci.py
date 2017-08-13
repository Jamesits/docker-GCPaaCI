#!/usr/bin/env python

import argparse
import json
import requests

api_base = 'https://api.github.com'
states = ('pending', 'success', 'error', 'failure')

parser = argparse.ArgumentParser(description='Use Google Cloud Platform as a GitHub CI.\nhttps://github.com/Jamesits/docker-GCPaaCI')
parser.add_argument('-a', '--auth', type=str, help='GitHub access token, usually in the format of username:password or username:personal-access-token')
parser.add_argument('-r', '--repo', type=str, help='repo name like octocat/Hello-World')
parser.add_argument('-c', '--commit-hash', type=str, help='commit hash (usually SHA1)')
parser.add_argument('-s', '--state', type=str, help='CI status \u2208 {"pending", "success", "error", "failure"}')
parser.add_argument('-i', '--context', type=str, nargs='?', default='Jamesits/docker-GCPaaCI', help="a string identifies this CI")
parser.add_argument('-d', '--description', type=str, nargs='?', help="a high-level summary of what happened")
parser.add_argument('-u', '--url', type=str, nargs='?', help="URL to detailed CI status")
parser.add_argument('-v', '--verbose', action='store_true', default=False, help="enable debug output")

if __name__=='__main__':
    args = parser.parse_args()
    if args.verbose:
        import logging
        import http.client as http_client
        http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    # check arguments format
    assert ':' in args.auth
    assert '/' in args.repo
    assert args.state in states

    username, password = args.auth.split(':', 1)
    data = {
            'state': args.state,
            'context': args.context,
        }
    if args.url:
        data['target_url'] = args.url
    if args.description:
        data['description'] = args.description

    r = requests.post(
            '{0}/repos/{1}/statuses/{2}'.format(api_base, args.repo, args.commit_hash), 
            headers = {
                'user-agent': 'GCPaaCI/0.0.0'
            },
            auth = requests.auth.HTTPBasicAuth(username, password),
            data = json.dumps(data)
        )
    print('{0} {1}'.format(r.status_code, r.text))