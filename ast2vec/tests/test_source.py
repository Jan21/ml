import unittest

from bblfsh.github.com.bblfsh.sdk.uast.generated_pb2 import Node


import ast2vec.tests.models as paths
from ast2vec.source import Source


class SourceTests(unittest.TestCase):
    def setUp(self):
        self.model = Source().load(source=paths.SOURCE)

    def test_dump(self):
        dump = self.model.dump()
        true_dump = "Number of files: 1. First 100 symbols:\n " + \
                    "import os\n\nprint(\"Hello world!\")\n"

        self.assertEqual(dump, true_dump)

    def test_sources(self):
        prop = self.model.sources
        with open(paths.SOURCE_PY) as f:
            true_val = f.read()
        self.assertEqual(len(prop), 1)
        self.assertIsInstance(prop[0], str)
        self.assertEqual(prop[0], true_val)

    def test_uasts(self):
        prop = self.model.uasts
        self.assertEqual(len(prop), 1)
        self.assertIsInstance(prop[0], Node)
        self.assertEqual(len(prop[0].children), 2)

    def test_filenames(self):
        prop = self.model.filenames
        true_val = paths.SOURCE_FILENAME + ".py"
        self.assertEqual(len(prop), 1)
        self.assertEqual(prop[0], true_val)


if __name__ == "__main__":
    unittest.main()
