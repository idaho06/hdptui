import logging
import unittest
import util.config
import services.solr

loglevel = logging.DEBUG
logging.basicConfig(level=loglevel,
                    format="%(asctime)s %(levelname)s: %(funcName)s: %(message)s")


class TestAmbariInfraSolr(unittest.TestCase):
    def setUp(self):
        self.config = util.config.ConfigClass('test/testconfig.ini')
        solrconfig = self.config.parser['SOLR']
        self.solr = services.solr.SolrClass(solrconfig)

    def tearDown(self):
        pass

    def test_config_class_section_is_present(self):
        self.assertTrue('SOLR' in self.config.parser)
        logging.debug("END test_config_class_section_is_present")
        logging.debug("..............................................")

    def test_solr_connect(self):
        self.assertTrue(self.solr._isconnected, "Could not connect to Solr service.")
        logging.debug("END test_solr_connect")
        logging.debug("..............................................")

    def test_get_collections(self):
        collections = self.solr.getCollections()
        self.assertIsInstance(collections, list, "Response is not a list")
        logging.debug("END test_get_collections")
        logging.debug("..............................................")


if __name__ == '__main__':
    unittest.main()