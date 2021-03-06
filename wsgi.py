import sys
from pprint import pformat

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    return [pformat([environ, vars(sys)]).encode('utf-8')]
