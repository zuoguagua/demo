#!/usr/bin/env python


import os
import sys

shared_dir = os.path.dirname(sys.modules[__name__].__file__)

print shared_dir

client_dir = os.path.dirname(shared_dir)

print client_dir

root_dir = os.path.dirname(client_dir)

print root_dir

setting_path_client = os.path.join(client_dir,'global_config.ini')

print setting_path_client

settings_path_root = os.path.join(root_dir,'global_config.ini')


print settings_path_root

config_in_root = os.path.exists(settings_path_root)

print config_in_root
