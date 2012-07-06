print "a"
from pygcm.client import GcmClient as _GcmClient
from pygcm.client import HTTPClient
from twisted.web.client import getPage


class TwistedHttpClient(HTTPClient):
    def send(self, api_key, registration_ids, send_data): 
        def cb(result):
            return self._handler.load(result)

        def eb(failure):
            return

        d = getPage(
                self.url,
                method='POST',
                postdata=self._handler.dump(registration_ids, send_data),
                headers={
                    'Content-Type': self._handler.content_type,
                    'Authorization': 'key=%s' % api_key,
                })
        d.addCallbacks(cb, eb)
        return d


class GcmClient(_GcmClient):
    def __init__(self, api_key, mode='json', client=TwistedHttpClient):
        super(GcmClient, self).__init__(api_key, client=client)
