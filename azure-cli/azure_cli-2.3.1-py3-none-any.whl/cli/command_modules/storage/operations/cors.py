# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def list_cors(client, timeout=None):
    results = {}
    for s in client:
        results[s.name] = s.get_cors(timeout)
    return results


def add_cors(client, origins, methods, max_age=0, exposed_headers=None, allowed_headers=None, timeout=None):
    for s in client:
        s.add_cors(origins, methods, max_age, exposed_headers, allowed_headers, timeout)


def clear_cors(client, timeout=None):
    for s in client:
        s.clear_cors(timeout)
