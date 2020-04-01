#!/usr/bin/env python
# -*- coding:utf-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Authors:
# - Brian Bockelman, <bbockelm@cse.unl.edu>, 2017-2018
# - James Alexander Clark, <james.clark@ligo.org>, 2018-2019
"""
lfn2pfn.py

Legacy LFN-to-path algorithms for LIGO
"""
from __future__ import absolute_import
import re
from rucio.rse.protocols.protocol import RSEDeterministicTranslation

_GWF_RE = re.compile(r'([A-Z]+)-([A-Za-z0-9_]+)-([0-9]{5,5})(.*)')
_LV_DATASET_RE = re.compile(r'([A-Z0-9]+)_([A-Z0-9]+)_([A-Za-z0-9_]+)')
_K_DATASET_RE = re.compile(r'([A-Z0-9]+)_([A-Z0-9]+)')
_TESTS_RE = re.compile(r'^[A-Z]+\.[a-z0-9]+$')

# pylint: disable=fixme
# TODO: overhaul these functions into a class with shared methods as in
# lib/rucio/rse/protocols/protocol.py
# TODO: Remove duplicated name matching code


def kagra_offline(scope, name, rse, rse_attrs, proto_attrs):
    """
    Map the GWF files according to the KAGRA aggregated offline schema.

    Low-latency frames at ICRR are aggregated into 4096 frame files and placed
    in a directory named for the detector:

    O3:K-K1_C10-1268645888-4096.gwf ->
    <prefix>/C10/O3/K1/K-K1_C10-1268645888-4096.gwf

    This function maps the scope:LFN to the PFN.

    Parameters:

    :param scope: Scope of the LFN.
    :param name: File name of the LFN.
    :param rse: RSE for PFN (ignored)
    :param rse_attrs: RSE attributes for PFN (ignored)
    :param protocol_attrs: RSE protocol attributes for PFN (ignored)
    :returns: Path for use in the PFN generation.
    """
    # Prevents unused argument warnings in pylint
    del rse
    del rse_attrs
    del proto_attrs

    # Exception for automatix test data. E.g.,
    # test.61f182e47315405ebc029599672199f2
    match = _TESTS_RE.match(name)
    if match:
        return "%s/%s" % (scope, name)

    # Parse LFN
    match = _GWF_RE.match(name)
    if not match:
        raise ValueError("Invalid LIGO filename")
    detector, dataset, _, _ = match.groups()

    detector = detector[0] + '1'

    # Parse frame type
    match = _K_DATASET_RE.match(dataset)
    _, calib = match.groups()

    pfn = "%s/%s/%s/%s" % (calib, scope, detector, name)

    return pfn


RSEDeterministicTranslation.register(kagra_offline)


def ligo_legacy(scope, name, rse, rse_attrs, proto_attrs):
    """
    Map the GWF files according to the Caltech schema.

    ER8:H-H1_HOFT_C02-1126256640-4096 ->
    ER8/hoft_C02/H1/H-H1_HOFT_C02-11262/H-H1_HOFT_C02-1126256640-4096
    """
    # pylint: disable=too-many-return-statements
    # pylint: disable=too-many-branches

    # Prevents unused argument warnings in pylint
    del rse
    del rse_attrs
    del proto_attrs

    # Exception for automatix test data. E.g.,
    # test.61f182e47315405ebc029599672199f2
    match = _TESTS_RE.match(name)
    if match:
        return "%s/%s" % (scope, name)

    match = _GWF_RE.match(name)
    if not match:
        raise ValueError("Invalid LIGO filename")
    detector, dataset, gps_prefix, _ = match.groups()
    dir_hash = "%s-%s-%s" % (detector, dataset, gps_prefix)

    # Virgo

    # In O1: all Virgo data went to /archive/frames/AdVirgo

    # In O2:
    #       - V1Online went to /archive/frames/AdVirgo
    #       - raw V1O2Repro1A and V1O2Repro2A lived in /archive/frames/O2

    # In O3: raw, V1Online live in /archive/frames/O3

    if dataset == 'V1Online' and scope != 'O3':
        detector = 'AdVirgo'
        dataset = 'HrecOnline'
        pfn = '%s/%s/%s/%s' % (detector, dataset, dir_hash,
                               name)

    elif detector == 'V' and dataset == 'raw' and scope in ['O2', 'O3']:
        detector = detector[0] + '1'
        pfn = "%s/%s/%s/%s/%s" % (scope, dataset, detector, dir_hash,
                                  name)

    elif dataset == 'V1Online' and scope == 'O3':
        pfn = "%s/%s/%s/%s" % (scope, dataset, dir_hash, name)

    elif detector == 'V' and dataset == 'raw':
        detector = 'AdVirgo'
        pfn = "%s/%s/%s/%s" % (detector, dataset, dir_hash, name)

    elif dataset in ['V1O2Repro1A', 'V1O2Repro2A']:
        pfn = '%s/%s/%s/%s' % (scope, dataset, dir_hash, name)

    # KAGRA
    elif dataset in ['K1_C10']:
        pfn = "%s/%s/%s/%s/%s" % (scope, detector, dataset, dir_hash, name)

    else:

        # LIGO
        detector = detector[0] + '1'
        match = _LV_DATASET_RE.match(dataset)
        if match:
            _, kind, calib = match.groups()

            if calib == 'C00':
                dataset = kind.lower()
            else:
                dataset = '%s_%s' % (kind.lower(), calib)

        # LIGO Exceptions
        if dataset in ['H1_R', 'L1_R']:
            dataset = 'raw'
        elif dataset in ['hoft_CLEAN_SUB60HZ_C01']:
            dataset = 'hoft_C01_clean_sub60Hz'

        pfn = "%s/%s/%s/%s/%s" % (scope, dataset, detector, dir_hash, name)

    return pfn


RSEDeterministicTranslation.register(ligo_legacy)

if __name__ == '__main__':

    def test_mapping(algorithm, scope, name, pfn):
        """Demonstrate the LFN->PFN mapping"""
        if algorithm.__name__ not in ['ligo_legacy', 'kagra_offline']:
            raise ValueError("Invalid algorithm name")
        mapped_pfn = algorithm(scope, name, None, None, None)
        assert mapped_pfn == pfn, "{0} should be {1}".format(mapped_pfn, pfn)

    test_mapping(
        ligo_legacy, "postO1", "H-H1_HOFT_C00-1163149312-4096.gwf",
        "postO1/hoft/H1/H-H1_HOFT_C00-11631/H-H1_HOFT_C00-1163149312-4096.gwf")

    test_mapping(
        ligo_legacy, "postO1", "L-L1_HOFT_C00-1158533120-4096.gwf",
        "postO1/hoft/L1/L-L1_HOFT_C00-11585/L-L1_HOFT_C00-1158533120-4096.gwf")

    test_mapping(
        ligo_legacy, "O2", "H-H1_HOFT_C01-1188003840-4096.gwf",
        "O2/hoft_C01/H1/H-H1_HOFT_C01-11880/H-H1_HOFT_C01-1188003840-4096.gwf")

    test_mapping(
        ligo_legacy, "O1", "L-L1_HOFT_C01_4kHz-1137250304-4096.gwf",
        "O1/hoft_C01_4kHz/L1/L-L1_HOFT_C01_4kHz-11372/"
        "L-L1_HOFT_C01_4kHz-1137250304-4096.gwf")

    test_mapping(
        ligo_legacy, "AdVirgo", "V-V1Online-1192294000-2000.gwf",
        "AdVirgo/HrecOnline/V-V1Online-11922/V-V1Online-1192294000-2000.gwf")

    test_mapping(
        ligo_legacy, "O2", "V-V1O2Repro1A-1187990000-5000.gwf",
        "O2/V1O2Repro1A/V-V1O2Repro1A-11879/V-V1O2Repro1A-1187990000-5000.gwf")

    test_mapping(ligo_legacy, "O1", "H-H1_R-1126631040-64.gwf",
                 "O1/raw/H1/H-H1_R-11266/H-H1_R-1126631040-64.gwf")

    test_mapping(ligo_legacy, "O3", "K-K1_C10-1268715520-4096.gwf",
                 "O3/K/K1_C10/K-K1_C10-12687/K-K1_C10-1268715520-4096.gwf")

    test_mapping(kagra_offline, "O3", "K-K1_C10-1268604928-4096.gwf",
                 "C10/O3/K1/K-K1_C10-1268604928-4096.gwf")
