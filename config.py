#!/usr/bin/env python3
# Copyright (C) @CVOOZ
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6785417702:AAHXTfPdboBOW6ITv2QBxftMDDOXHb6t9g8")

    APP_ID = int(os.environ.get("APP_ID", "16240771"))

    API_HASH = os.environ.get("API_HASH", "e8717d3a9601531928f27590fb41c44d")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
