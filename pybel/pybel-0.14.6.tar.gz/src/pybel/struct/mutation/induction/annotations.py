# -*- coding: utf-8 -*-

"""Functions for inducing graphs based on edge annotations."""

import logging

from .utils import get_subgraph_by_edge_filter
from ...filters import build_annotation_dict_all_filter, build_annotation_dict_any_filter
from ...pipeline import transformation

__all__ = [
    'get_subgraph_by_annotation_value',
    'get_subgraph_by_annotations',
]

logger = logging.getLogger(__name__)


@transformation
def get_subgraph_by_annotations(graph, annotations, or_=None):
    """Induce a sub-graph given an annotations filter.

    :param graph: pybel.BELGraph graph: A BEL graph
    :param dict[str,iter[str]] annotations: Annotation filters (match all with :func:`pybel.utils.subdict_matches`)
    :param boolean or_: if True any annotation should be present, if False all annotations should be present in the
                        edge. Defaults to True.
    :return: A subgraph of the original BEL graph
    :rtype: pybel.BELGraph
    """
    edge_filter_builder = (
        build_annotation_dict_any_filter
        if (or_ is None or or_) else
        build_annotation_dict_all_filter
    )

    return get_subgraph_by_edge_filter(graph, edge_filter_builder(annotations))


@transformation
def get_subgraph_by_annotation_value(graph, annotation, values):
    """Induce a sub-graph over all edges whose annotations match the given key and value.

    :param pybel.BELGraph graph: A BEL graph
    :param str annotation: The annotation to group by
    :param values: The value(s) for the annotation
    :type values: str or iter[str]
    :return: A subgraph of the original BEL graph
    :rtype: pybel.BELGraph
    """
    if isinstance(values, str):
        values = {values}

    return get_subgraph_by_annotations(graph, {annotation: values})
