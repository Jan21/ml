from sourced.ml.algorithms import UastGraph2Bag
from sourced.ml.extractors import BagsExtractor, register_extractor, get_names_from_kwargs,\
    filter_kwargs


@register_extractor
class GraphletBagExtractor(BagsExtractor):
    NAME = "graphlet"
    NAMESPACE = "g."
    OPTS = dict(get_names_from_kwargs(UastGraph2Bag.__init__))
    OPTS.update(BagsExtractor.OPTS)

    def __init__(self, docfreq_threshold=None, **kwargs):
        super().__init__(docfreq_threshold)
        self._log.debug("__init__ %s", kwargs)
        uast2bag_kwargs = filter_kwargs(kwargs, UastGraph2Bag.__init__)
        self.uast2bag = UastGraph2Bag(**uast2bag_kwargs)

    def uast_to_bag(self, uast):
        return self.uast2bag(uast)
