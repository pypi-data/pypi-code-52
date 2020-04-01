# Licensed under a 3-clause BSD style license - see LICENSE.rst
import pytest
import numpy as np
from numpy.testing import assert_allclose
from gammapy.stats import CashCountsStatistic, WStatCountsStatistic

ref_array = np.ones((3, 2, 4))

values = [
    (1, 2, [-1.0, -0.78339367, 0.433396]),
    (5, 1, [4.0, 2.84506224, 4.4402745934e-3]),
    (10, 5, [5.0, 1.96543726, 0.049363650550]),
    (100, 23, [77.0, 11.8294207, 2.75033324833345e-32]),
    (1, 20, [-19, -5.65760863, 1.534966634510499e-08]),
    (5 * ref_array, 1 * ref_array, [4.0, 2.84506224, 4.4402745934e-3]),
]


@pytest.mark.parametrize(("n_on", "mu_bkg", "result"), values)
def test_cash_basic(n_on, mu_bkg, result):
    stat = CashCountsStatistic(n_on, mu_bkg)
    excess = stat.excess
    significance = stat.significance
    p_value = stat.p_value

    assert_allclose(excess, result[0])
    assert_allclose(significance, result[1], atol=1e-5)
    assert_allclose(p_value, result[2], atol=1e-5)


values = [
    (1, 2, [-1.0, 1.35767667]),
    (5, 1, [-1.915916, 2.581106]),
    (10, 5, [-2.838105, 3.504033]),
    (100, 23, [-9.669482, 10.336074]),
    (1, 20, [-1, 1.357677]),
    (5 * ref_array, 1 * ref_array, [-1.915916, 2.581106]),
]


@pytest.mark.parametrize(("n_on", "mu_bkg", "result"), values)
def test_cash_errors(n_on, mu_bkg, result):
    stat = CashCountsStatistic(n_on, mu_bkg)
    errn = stat.compute_errn()
    errp = stat.compute_errp()

    assert_allclose(errn, result[0], atol=1e-5)
    assert_allclose(errp, result[1], atol=1e-5)


values = [
    (1, 2, [5.869898]),
    (5, 1, [13.98959]),
    (10, 5, [17.696064]),
    (100, 23, [110.07206]),
    (1, 20, [4.711538]),
    (5 * ref_array, 1 * ref_array, [13.98959]),
]


@pytest.mark.parametrize(("n_on", "mu_bkg", "result"), values)
def test_cash_ul(n_on, mu_bkg, result):
    stat = CashCountsStatistic(n_on, mu_bkg)
    ul = stat.compute_upper_limit()

    assert_allclose(ul, result[0], atol=1e-5)


values = [
    (100, 5, 54.012755),
    (100, -5, -45.631273),
    (1, -2, np.nan),
    ([1, 2], 5, [8.327276, 10.550546]),
]


@pytest.mark.parametrize(("mu_bkg", "significance", "result"), values)
def test_cash_excess_matching_significance(mu_bkg, significance, result):
    stat = CashCountsStatistic(1, mu_bkg)
    excess = stat.excess_matching_significance(significance)

    assert_allclose(excess, result, atol=1e-3)


values = [
    (1, 2, 1, [-1.0, -0.5829220133009171, 0.55994580085]),
    (5, 1, 1, [4.0, 1.7061745691234782, 0.087975582112]),
    (10, 5, 0.3, [8.5, 3.5853812867949024, 3.365860865528742e-4]),
    (10, 23, 0.1, [7.7, 3.443415522820395, 5.74416016688779e-4]),
    (1, 20, 1.0, [-19, -4.590373638528086, 4.424532535784618e-06]),
    (
        5 * ref_array,
        1 * ref_array,
        1 * ref_array,
        [4.0, 1.7061745691234782, 0.087975582112],
    ),
]


@pytest.mark.parametrize(("n_on", "n_off", "alpha", "result"), values)
def test_wstat_basic(n_on, n_off, alpha, result):
    stat = WStatCountsStatistic(n_on, n_off, alpha)
    excess = stat.excess
    significance = stat.significance
    p_value = stat.p_value

    assert_allclose(excess, result[0])
    assert_allclose(significance, result[1], atol=1e-5)
    assert_allclose(p_value, result[2], atol=1e-5)


values = [
    (1, 2, 1, [-1.942465, 1.762589]),
    (5, 1, 1, [-2.310459, 2.718807]),
    (10, 5, 0.3, [-2.932472, 3.55926]),
    (10, 23, 0.1, [-2.884366, 3.533279]),
    (1, 20, 1.0, [-4.897018, 4.299083]),
    (5 * ref_array, 1 * ref_array, 1 * ref_array, [-2.310459, 2.718807]),
]


@pytest.mark.parametrize(("n_on", "n_off", "alpha", "result"), values)
def test_wstat_errors(n_on, n_off, alpha, result):
    stat = WStatCountsStatistic(n_on, n_off, alpha)
    errn = stat.compute_errn()
    errp = stat.compute_errp()

    assert_allclose(errn, result[0], atol=1e-5)
    assert_allclose(errp, result[1], atol=1e-5)


values = [
    (1, 2, 1, [6.272627]),
    (5, 1, 1, [14.222831]),
    (10, 5, 0.3, [21.309229]),
    (10, 23, 0.1, [20.45803]),
    (1, 20, 1.0, [4.884418]),
    (5 * ref_array, 1 * ref_array, 1 * ref_array, [14.222831]),
]


@pytest.mark.parametrize(("n_on", "n_off", "alpha", "result"), values)
def test_wstat_ul(n_on, n_off, alpha, result):
    stat = WStatCountsStatistic(n_on, n_off, alpha)
    ul = stat.compute_upper_limit()

    assert_allclose(ul, result[0], atol=1e-5)


values = [
    ([10, 20], [0.1, 0.1], 5, [9.82966, 12.038423]),
    ([10, 10], [0.1, 0.3], 5, [9.82966, 16.664516]),
    ([10], [0.1], 3, [4.818497]),
    (
        [[10, 20], [10, 20]],
        [[0.1, 0.1], [0.1, 0.1]],
        5,
        [[9.82966, 12.038423], [9.82966, 12.038423]],
    ),
]


@pytest.mark.parametrize(("n_off", "alpha", "significance", "result"), values)
def test_wstat_excess_matching_significance(n_off, alpha, significance, result):
    stat = WStatCountsStatistic(1, n_off, alpha)
    excess = stat.excess_matching_significance(significance)

    assert_allclose(excess, result, atol=1e-3)
