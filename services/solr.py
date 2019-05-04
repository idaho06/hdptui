import logging
import configparser
import requests
from util.krb import krbauth
from requests_kerberos import HTTPKerberosAuth, REQUIRED


class SolrClass:
    _url = None
    _auth = None
    _requests_auth = None
    _user = None
    _password = None
    _principal = None
    _keytab = None
    _isconnected = False

    def __init__(self, solrconfig):
        logging.debug("Received configuration: " + solrconfig.name)
        # TODO: check proper configuration is coming
        if not solrconfig.get('solr_url'):
            raise ValueError("There is no solr_url in the configuration parameter")
        self._url = solrconfig['solr_url']

        self._auth = solrconfig['auth']

        if self._auth == 'kerberos':
            self._principal = solrconfig['principal']
            self._keytab = solrconfig['keytab']
            self._requests_auth = HTTPKerberosAuth(mutual_authentication=REQUIRED, force_preemptive=True)
            krbauth(self._principal, self._keytab)
        else:
            self._user = solrconfig['user']
            self._password = solrconfig['password']
            self._requests_auth = (self._user, self._password)

        try:
            r = requests.get(self._url, auth=self._requests_auth)
        except ConnectionError:
            logging.critical("Error connecting to " + self._url)
            raise
        if r.status_code is not 200:
            logging.critical("Error connecting to " + self._url + " Status code is " + str(r.status_code))
            raise ConnectionError
        self._isconnected = True
        r.close()

    def _getDataFromSolr(self, path, payload):
        if not type(path) is str:
            raise ValueError("Argument path must be a string: " + str(path))
        if not type(payload) is dict:
            raise ValueError("Argument payload must be a dict" + str(payload))
        payload["wt"]="json"
        logging.debug("Connecting to " + self._url + path)
        if 'kerberos' in self._auth:
            krbauth(self._principal, self._keytab)
        r = requests.get(self._url + path, params=payload, auth=self._requests_auth)
        logging.debug("GET to " + r.url)
        logging.debug(r.text)
        rjson = r.json()
        r.close()
        return rjson

    def getCollections(self):
        payload = {'action': 'LIST'}
        path = "admin/collections"
        responsejson = self._getDataFromSolr(path, payload)
        collections = responsejson["collections"]
        logging.debug("Returning LIST: " + str(collections))
        return collections

    def getCollectionDetails(self, collection=None):
        if type(collection) is not str:
            raise ValueError("Collection argument must be a string")
        logging.debug("Going to get collection: " + collection)
        payload = {'action': 'CLUSTERSTATUS'}
        path = 'admin/collections'
        responsejson = self._getDataFromSolr(path, payload)
        collectionjson = responsejson['cluster']['collections'][collection]
        logging.debug("Returning json: " + str(collectionjson))
        return collectionjson
