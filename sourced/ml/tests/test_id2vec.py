import argparse
import logging
import unittest

import numpy

from sourced.ml.cmd import id2vec_project
from sourced.ml.models import Id2Vec
import sourced.ml.tests.models as paths
from sourced.ml.utils import projector


class Id2VecTests(unittest.TestCase):
    def setUp(self):
        self.model = Id2Vec().load(source=paths.ID2VEC)

    def test_embeddings(self):
        embeddings = self.model.embeddings
        self.assertIsInstance(embeddings, numpy.ndarray)
        self.assertEqual(embeddings.shape, (1000, 300))

    def test_tokens(self):
        tokens = self.model.tokens
        self.assertIsInstance(tokens, list)
        self.assertEqual(len(tokens), 1000)
        self.assertIsInstance(tokens[0], str)

    def test_token2index(self):
        self.assertEqual(self.model["get"], 0)
        with self.assertRaises(KeyError):
            print(self.model["xxx"])

    def test_len(self):
        self.assertEqual(len(self.model), 1000)

    def test_items(self):
        key, val = next(iter(self.model.items()))
        self.assertEqual(self.model[key], val)

    def test_id2vec_project1(self):
        present_embeddings = projector.present_embeddings
        wait = projector.wait

        presented = False
        waited = False

        def fake_present(*args, **kwargs):
            nonlocal presented
            presented = True

        def fake_wait():
            nonlocal waited
            waited = True

        projector.present_embeddings = fake_present
        projector.wait = fake_wait
        args = argparse.Namespace(
            input=paths.ID2VEC, output="fake", docfreq_in=paths.DOCFREQ,
            no_browser=False, log_level=logging.DEBUG)
        try:
            id2vec_project(args)
        finally:
            projector.present_embeddings = present_embeddings
            projector.wait = wait

        self.assertTrue(presented)
        self.assertTrue(waited)

    def test_id2vec_project2(self):
        present_embeddings = projector.present_embeddings
        wait = projector.wait

        presented = False
        waited = False

        def fake_present(*args, **kwargs):
            nonlocal presented
            presented = True

        def fake_wait():
            nonlocal waited
            waited = True

        projector.present_embeddings = fake_present
        projector.wait = fake_wait
        args = argparse.Namespace(
            input=paths.ID2VEC, output="fake", docfreq_in=None,
            no_browser=False, log_level=logging.DEBUG)
        try:
            id2vec_project(args)
        finally:
            projector.present_embeddings = present_embeddings
            projector.wait = wait

        self.assertTrue(presented)
        self.assertTrue(waited)


if __name__ == "__main__":
    unittest.main()
