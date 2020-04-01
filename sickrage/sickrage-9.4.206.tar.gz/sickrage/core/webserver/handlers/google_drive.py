# ##############################################################################
#  Author: echel0n <echel0n@sickrage.ca>
#  URL: https://sickrage.ca/
#  Git: https://git.sickrage.ca/SiCKRAGE/sickrage.git
#  -
#  This file is part of SiCKRAGE.
#  -
#  SiCKRAGE is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  -
#  SiCKRAGE is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  -
#  You should have received a copy of the GNU General Public License
#  along with SiCKRAGE.  If not, see <http://www.gnu.org/licenses/>.
# ##############################################################################

from sickrage.core.webserver.handlers.base import BaseHandler


@Route('/googleDrive(/?.*)')
class GoogleDriveHandler(BaseHandler):
    def __init__(self, *args, **kwargs):
        super(GoogleDriveHandler, self).__init__(*args, **kwargs)

    def getProgress(self):
        return google_drive.GoogleDrive.get_progress()

    def syncRemote(self):
        self._genericMessage(_("Google Drive Sync"), _("Syncing app data to Google Drive"))
        google_drive.GoogleDrive().sync_remote()

    def syncLocal(self):
        self._genericMessage(_("Google Drive Sync"), _("Syncing app data from Google Drive"))
        google_drive.GoogleDrive().sync_local()