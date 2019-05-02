import logging
import configparser
import requests


class SolrClass:
    _url = ''
    _isconnected = False

    def __init__(self, solrconfig):
        logging.debug("Received configuration: " + solrconfig.name)
        # TODO: check proper configuration is coming
        if not solrconfig.get('solr_url'):
            raise EnvironmentError
        self._url = solrconfig['solr_url']
        try:
            r = requests.get(self._url)
        except ConnectionError:
            logging.critical("Error connecting to " + self._url)
            raise
        if r.status_code is not 200:
            logging.critical("Error connecting to" + self._url + " Status code is " + r.status_code)
            raise ConnectionError
        self._isconnected = True
        r.close()

    def getCollections(self):
        payload = {'action': 'LIST'}
        path = "admin/collections"
        logging.debug("Connecting to "+ self._url + path )
        r = requests.get(self._url + path, params=payload)
        logging.debug("GET to "+ r.url)
        logging.debug(r.text)
        rjson = r.json()
        r.close()
        collections = rjson["collections"]
        logging.debug("Returning LIST: " + str(collections))
        return collections
