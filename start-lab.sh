#!/usr/bin/env bash
exec jupyter lab \
  --LabApp.user_settings_dir=.jupyter/lab/user-settings \
  --LabApp.app_settings_dir=.jupyter/lab/app-settings \
  --LabServerApp.workspaces_dir=.jupyter/lab/workspaces \
  $@
