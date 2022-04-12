from lutris.database import schema
from lutris import startup
import os

import gi

gi.require_version('Gtk', '3.0')


def setup_test_environment():
    """Sets up a system to be able to run tests"""
    os.environ["LUTRIS_SKIP_INIT"] = "1"
    schema.syncdb()
    startup.init_lutris()
