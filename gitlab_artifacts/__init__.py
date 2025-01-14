# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Efrain Calderon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Gitlab artifacts downloader using python-gitlab."""

import warnings

from gitlab_artifacts._version import (  # noqa: F401
    __author__,
    __copyright__,
    __email__,
    __license__,
    __title__,
    __version__,
)
from gitlab_artifacts.client import GitlabClient  # noqa: F401
from gitlab_artifacts.downloader import ArtifactDownloader  # noqa: F401
from gitlab_artifacts.exceptions import *  # noqa: F401,F403


__all__ = [
    "__author__",
    "__copyright__",
    "__email__",
    "__license__",
    "__title__",
    "__version__",
    "GitlabClient",
    "ArtifactDownloader",
]
