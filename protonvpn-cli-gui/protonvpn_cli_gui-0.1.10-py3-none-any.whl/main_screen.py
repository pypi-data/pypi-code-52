#    This file is part of ProtonVPN-CLI-GUI for Linux.

#    Copyright (C) <year>  <name of author>
#
#    ProtonVPN-CLI-GUI is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Kivy Libraries
from kivy.uix.screenmanager import Screen

# Local
from .widgets import (  # noqa # pylint: disable=import-error
    PvpnDropDown,
)


class MainScreen(Screen):
    """Primary screen where most app usage takes place."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_dropdown = PvpnDropDown()

    def open_dropdown_menu(self):
        self.menu_dropdown.open(self.ids.menu_button_icon)
