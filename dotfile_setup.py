#!/usr/bin/python

import os

DOTFILE_DIR='~/Google Drive/config/dotfiles/'

links = [
  ('~/Google Drive/secure/ssh/', '~/.ssh'),
  ('~/Google Drive/config/sublime/Packages/', '~/Library/Application Support/Sublime Text 2/Packages/'),
]

def symlink(source, link):
  link = os.path.expanduser(link)
  source = os.path.expanduser(source)

  if os.path.exists(link):
    print '%s exists' % link
  else:
    print '%s missing, creating' % link
    os.symlink(source, link)

def unwrap_dotfiles():
  expanded_dir = os.path.expanduser(DOTFILE_DIR)
  for dotfile in os.listdir(expanded_dir):
    link_path = '~/.' + dotfile
    src_path = expanded_dir + dotfile
    links.append((src_path, link_path))

unwrap_dotfiles()
for link in links:
  symlink(link[0], link[1])
