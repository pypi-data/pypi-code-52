# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['cloud'] = """
type: group
short-summary: Manage registered Azure clouds.
"""

helps['cloud list'] = """
type: command
short-summary: List registered clouds.
"""

helps['cloud list-profiles'] = """
type: command
short-summary: List the supported profiles for a cloud.
"""

helps['cloud register'] = """
type: command
short-summary: Register a cloud.
long-summary: When registering a cloud, specify only the resource manager endpoint for the autodetection of other endpoints.
"""

helps['cloud set'] = """
type: command
short-summary: Set the active cloud.
examples:
  - name: Set the active cloud. (autogenerated)
    text: |
        az cloud set --name MyRegisteredCloud
    crafted: true
"""

helps['cloud show'] = """
type: command
short-summary: Get the details of a registered cloud.
"""

helps['cloud unregister'] = """
type: command
short-summary: Unregister a cloud.
examples:
  - name: Unregister a cloud. (autogenerated)
    text: |
        az cloud unregister --name MyRegisteredCloud
    crafted: true
"""

helps['cloud update'] = """
type: command
short-summary: Update the configuration of a cloud.
examples:
  - name: Update the configuration of a cloud. (autogenerated)
    text: |
        az cloud update --profile latest
    crafted: true
"""
