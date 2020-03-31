"""
Tests for functions that calibrate/prep AIA image data
"""
import tempfile

import numpy as np
import pytest
import astropy.time
import astropy.units as u
from astropy.io.fits.verify import VerifyWarning
import sunpy.data.test
from sunpy.map import Map

from aiapy.calibrate import (register, correct_degradation,
                             degradation)
from aiapy.calibrate.util import get_correction_table
from aiapy.tests.data import get_test_filepath


@pytest.fixture
def lvl_15_map(aia_171_map):
    # Use scipy set to True as skimage can cause CI test failures
    return register(aia_171_map, use_scipy=True)


def test_register(aia_171_map, lvl_15_map):
    """
    Test that header info for the map has been correctly updated after the
    map has been scaled to 0.6 arcsec / pixel and aligned with solar north
    """
    # Check all of these for Map attributes and .meta values?
    # Check array shape
    assert lvl_15_map.data.shape == aia_171_map.data.shape
    # Check crpix values
    assert lvl_15_map.meta['crpix1'] == lvl_15_map.data.shape[1] / 2.0 + 0.5
    assert lvl_15_map.meta['crpix2'] == lvl_15_map.data.shape[0] / 2.0 + 0.5
    # Check cdelt values
    assert lvl_15_map.meta['cdelt1'] / 0.6 == int(lvl_15_map.meta['cdelt1'] / 0.6)
    assert lvl_15_map.meta['cdelt2'] / 0.6 == int(lvl_15_map.meta['cdelt2'] / 0.6)
    # Check rotation value, I am assuming that the inaccuracy in
    # the CROTA -> PCi_j matrix is causing the inaccuracy here
    np.testing.assert_allclose(
        lvl_15_map.rotation_matrix, np.identity(2), rtol=1e-5, atol=1e-8)
    # Check level number
    assert lvl_15_map.meta['lvl_num'] == 1.5


def test_register_filesave(lvl_15_map):
    """
    Test that adjusted header values are still correct after saving the map
    and reloading it.
    """
    afilename = tempfile.NamedTemporaryFile(suffix='.fits').name
    with pytest.warns(
            VerifyWarning,
            match="The 'BLANK' keyword is only applicable to integer data"):
        lvl_15_map.save(afilename, overwrite=True)
    load_map = Map(afilename)
    # Check crpix values
    assert load_map.meta['crpix1'] == lvl_15_map.data.shape[1] / 2.0 + 0.5
    assert load_map.meta['crpix2'] == lvl_15_map.data.shape[0] / 2.0 + 0.5
    # Check cdelt values
    assert load_map.meta['cdelt1'] / 0.6 == int(load_map.meta['cdelt1'] / 0.6)
    assert load_map.meta['cdelt2'] / 0.6 == int(load_map.meta['cdelt2'] / 0.6)
    # Check rotation value
    np.testing.assert_allclose(
        lvl_15_map.rotation_matrix, np.identity(2), rtol=1e-5, atol=1e-8)
    # Check level number
    assert load_map.meta['lvl_num'] == 1.5


def test_register_unsupported_maps(aia_171_map):
    """
    Make sure we raise an error when an unsupported map is passed in
    """
    # A submap
    original_cutout = aia_171_map.submap(aia_171_map.center,
                                         aia_171_map.top_right_coord)
    with pytest.raises(ValueError):
        _ = register(original_cutout)
    # A Map besides AIA or HMI
    non_sdo_map = Map(sunpy.data.test.get_test_filepath(
        'mdi_fd_Ic_6h_01d.5871.0000_s.fits'))
    with pytest.raises(ValueError):
        _ = register(non_sdo_map)


@pytest.mark.parametrize('correction_table', [
    pytest.param(None, marks=pytest.mark.remote_data),
    get_correction_table(correction_table=get_test_filepath(
        'aia_V8_20171210_050627_response_table.txt')),
])
def test_correct_degradation(aia_171_map, correction_table):
    original_corrected = correct_degradation(
        aia_171_map, correction_table=correction_table)
    d = degradation(aia_171_map.wavelength, aia_171_map.date,
                    correction_table=correction_table)
    uncorrected_over_corrected = aia_171_map.data / original_corrected.data
    # If intensity is zero, ratio will be NaN/infinite
    i_valid = aia_171_map.data > 0.
    assert np.allclose(uncorrected_over_corrected[i_valid], d)


@pytest.mark.parametrize('correction_table,time_correction_truth', [
    pytest.param(None, 0.7667012041798814 * u.dimensionless_unscaled,
                 marks=pytest.mark.remote_data),
    (get_test_filepath('aia_V8_20171210_050627_response_table.txt'),
     0.7667108920899671 * u.dimensionless_unscaled),
    (get_correction_table(correction_table=get_test_filepath(
        'aia_V8_20171210_050627_response_table.txt')),
     0.7667108920899671 * u.dimensionless_unscaled),
])
def test_degradation(correction_table, time_correction_truth):
    # NOTE: this just tests an expected result from aiapy, not necessarily an
    # absolutely correct result. It was calculated for the above time and
    # the specific correction table file.
    # NOTE: If the first test starts failing, it may be because the correction
    # table parameters have been updated in JSOC.
    obstime = astropy.time.Time('2015-01-01T00:00:00', scale='utc')
    time_correction = degradation(94*u.angstrom, obstime,
                                  correction_table=correction_table)
    assert u.allclose(time_correction, time_correction_truth,
                      rtol=1e-10, atol=0.)
