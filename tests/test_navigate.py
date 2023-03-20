import sys
from types import ModuleType

from unittest import TestCase
from unittest.mock import MagicMock

from mock_module import MockModule

MockModule('pynvim')
MockModule('kitty.boss')
MockModule('kittens.tui.handler')

import navigate
