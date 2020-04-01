""""

    RemoteDataAsset:  DataAsset that has only a URL for assigned in the metadada

"""

from mimetypes import MimeTypes
from urllib.parse import urlparse

from starfish.asset.asset_base import AssetBase
from starfish.asset.data_asset import DataAsset


class RemoteDataAsset(DataAsset):

    @staticmethod
    def create_with_url(name, url, metadata=None, did=None):
        """

        Create a new RemoteDataAsset using a url.

        :param str name: Name of the asset to create
        :param str url: URL to assign to the asset
        :param dict metadata: Optional metadata to add to the assets metadata
        :param str did: Option DID to assign to this asset

        :return: a new DataAsset
        :type: :class:`.DataAsset`

        """

        metadata = AssetBase.generateMetadata(name, 'dataset', metadata)
        metadata['url'] = url
        if urlparse(url):
            metadata['contentType'] = 'application/octet-stream'
            mime = MimeTypes()
            mime_type = mime.guess_type(url)
            if mime_type and mime_type[0]:
                metadata['contentType'] = mime_type[0]

        return RemoteDataAsset(metadata, did)

    @property
    def url(self):
        if 'url' in self._metadata:
            return self._metadata['url']
        return None
