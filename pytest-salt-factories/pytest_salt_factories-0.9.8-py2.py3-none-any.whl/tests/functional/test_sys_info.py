# -*- coding: utf-8 -*-
"""
    tests.functional.test_sys_info
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests related to system information reports enabled by the `--sys-info` flag.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pytest


@pytest.mark.parametrize("flag", ["--sysinfo", "--sys-info"])
def test_sysinfo(testdir, flag):
    p = testdir.makepyfile(
        """
        def test_one():
            assert True
        """
    )
    res = testdir.runpytest("-vv", flag)
    res.assert_outcomes(passed=1)
    res.stdout.fnmatch_lines(
        [
            "*>> System Information >>*",
            "*-- Salt Versions Report --*",
            "*-- System Grains Report --*",
            "*<< System Information <<*",
            "collect*",
            "* PASSED*",
            "* 1 passed in *",
        ]
    )


def test_no_sysinfo(testdir):
    p = testdir.makepyfile(
        """
        def test_one():
            assert True
        """
    )
    res = testdir.runpytest("-vv")
    res.assert_outcomes(passed=1)
    try:
        res.stdout.no_fnmatch_line("*>> System Information >>*")
    except AttributeError:
        # PyTest 4.6.x
        from _pytest.outcomes import Failed

        with pytest.raises(Failed):
            res.stdout.fnmatch_lines(
                ["*>> System Information >>*",]
            )
    res.stdout.fnmatch_lines(
        ["collect*", "* PASSED*", "* 1 passed in *",]
    )
