from .utils import NamespacedClient, query_params, _make_path


class NodesClient(NamespacedClient):
    @query_params("timeout")
    def reload_secure_settings(self, node_id=None, params=None, headers=None):
        """
        Reloads secure settings.
        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/secure-settings.html#reloadable-secure-settings>`_

        :arg node_id: A comma-separated list of node IDs to span the
            reload/reinit call. Should stay empty because reloading usually involves
            all cluster nodes.
        :arg timeout: Explicit operation timeout
        """
        return self.transport.perform_request(
            "POST",
            _make_path("_nodes", node_id, "reload_secure_settings"),
            params=params,
            headers=headers,
        )

    @query_params("flat_settings", "timeout")
    def info(self, node_id=None, metric=None, params=None, headers=None):
        """
        Returns information about nodes in the cluster.
        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cluster-nodes-info.html>`_

        :arg node_id: A comma-separated list of node IDs or names to
            limit the returned information; use `_local` to return information from
            the node you're connecting to, leave empty to get information from all
            nodes
        :arg metric: A comma-separated list of metrics you wish
            returned. Leave empty to return all.  Valid choices: settings, os,
            process, jvm, thread_pool, transport, http, plugins, ingest
        :arg flat_settings: Return settings in flat format (default:
            false)
        :arg timeout: Explicit operation timeout
        """
        return self.transport.perform_request(
            "GET", _make_path("_nodes", node_id, metric), params=params, headers=headers
        )

    @query_params(
        "completion_fields",
        "fielddata_fields",
        "fields",
        "groups",
        "include_segment_file_sizes",
        "level",
        "timeout",
        "types",
    )
    def stats(
        self, node_id=None, metric=None, index_metric=None, params=None, headers=None
    ):
        """
        Returns statistical information about nodes in the cluster.
        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cluster-nodes-stats.html>`_

        :arg node_id: A comma-separated list of node IDs or names to
            limit the returned information; use `_local` to return information from
            the node you're connecting to, leave empty to get information from all
            nodes
        :arg metric: Limit the information returned to the specified
            metrics  Valid choices: _all, breaker, fs, http, indices, jvm, os,
            process, thread_pool, transport, discovery
        :arg index_metric: Limit the information returned for `indices`
            metric to the specific index metrics. Isn't used if `indices` (or `all`)
            metric isn't specified.  Valid choices: _all, completion, docs,
            fielddata, query_cache, flush, get, indexing, merge, request_cache,
            refresh, search, segments, store, warmer, suggest
        :arg completion_fields: A comma-separated list of fields for
            `fielddata` and `suggest` index metric (supports wildcards)
        :arg fielddata_fields: A comma-separated list of fields for
            `fielddata` index metric (supports wildcards)
        :arg fields: A comma-separated list of fields for `fielddata`
            and `completion` index metric (supports wildcards)
        :arg groups: A comma-separated list of search groups for
            `search` index metric
        :arg include_segment_file_sizes: Whether to report the
            aggregated disk usage of each one of the Lucene index files (only
            applies if segment stats are requested)
        :arg level: Return indices stats aggregated at index, node or
            shard level  Valid choices: indices, node, shards  Default: node
        :arg timeout: Explicit operation timeout
        :arg types: A comma-separated list of document types for the
            `indexing` index metric
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_nodes", node_id, "stats", metric, index_metric),
            params=params,
            headers=headers,
        )

    @query_params(
        "doc_type", "ignore_idle_threads", "interval", "snapshots", "threads", "timeout"
    )
    def hot_threads(self, node_id=None, params=None, headers=None):
        """
        Returns information about hot threads on each node in the cluster.
        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cluster-nodes-hot-threads.html>`_

        :arg node_id: A comma-separated list of node IDs or names to
            limit the returned information; use `_local` to return information from
            the node you're connecting to, leave empty to get information from all
            nodes
        :arg doc_type: The type to sample (default: cpu)  Valid choices:
            cpu, wait, block
        :arg ignore_idle_threads: Don't show threads that are in known-
            idle places, such as waiting on a socket select or pulling from an empty
            task queue (default: true)
        :arg interval: The interval for the second sampling of threads
        :arg snapshots: Number of samples of thread stacktrace (default:
            10)
        :arg threads: Specify the number of threads to provide
            information for (default: 3)
        :arg timeout: Explicit operation timeout
        """
        # type is a reserved word so it cannot be used, use doc_type instead
        if "doc_type" in params:
            params["type"] = params.pop("doc_type")

        return self.transport.perform_request(
            "GET",
            _make_path("_nodes", node_id, "hot_threads"),
            params=params,
            headers=headers,
        )

    @query_params("timeout")
    def usage(self, node_id=None, metric=None, params=None, headers=None):
        """
        Returns low-level information about REST actions usage on nodes.
        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cluster-nodes-usage.html>`_

        :arg node_id: A comma-separated list of node IDs or names to
            limit the returned information; use `_local` to return information from
            the node you're connecting to, leave empty to get information from all
            nodes
        :arg metric: Limit the information returned to the specified
            metrics  Valid choices: _all, rest_actions
        :arg timeout: Explicit operation timeout
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_nodes", node_id, "usage", metric),
            params=params,
            headers=headers,
        )
