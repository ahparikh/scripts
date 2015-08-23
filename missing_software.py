#!/usr/bin/python

# TODO:
# have flag for required vs optional
# have additional app details (links, etc)

import os

required_apps = [
  # (AppName, AppPath)
  ('Alfred 2', None),
  ('Iterm', None),
  ('TaskPaper', None),
  ('Rdio', None),
  ('Sublime Text 2', None),
  ('Aperture', None),
  ('Dropbox', None),
  ('Google Drive', None),
  ('1Password', None),
]

optional_apps = [
  # (AppName, AppPath)
  ('FluidApp', None),
  ('Hulu Desktop', None),
  ('GitHub', None),
  ('Twitter', None),
  ('GeekTool', None),
  ('Picasa', None),
  ('Skype', None),
]


def is_installed(app_name, app_path=None, is_required=False):
  # if not app_path, then take a guess
  if not app_path:
    app_path = "/Applications/%s.app" % app_name

  if is_required:
    prefix = 'Required'
  else:
    prefix = 'Optional'

  if not os.path.isdir(app_path):
    print '%s app missing: %s (checked %s)' % (prefix, app_name, app_path)


def main():
  for required_app in required_apps:
    is_installed(required_app[0],
                 required_app[1],
                 True)

  for optional_app in optional_apps:
    is_installed(optional_app[0],
                 optional_app[1],
                 False)

if __name__ == "__main__":
    main()
