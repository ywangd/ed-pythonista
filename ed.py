# coding: utf-8

import os
import sys
import argparse
import inspect

import ui
import console

ap = argparse.ArgumentParser()
ap.add_argument('filename', help='file to edit')
ns = ap.parse_args()

def set_text(sender):
    try:
        with open(ns.filename) as ins:
            lines = ins.read()
    except IOError as e:
        lines = ''

    sender.text = lines

def save_action(sender):
    with open(ns.filename, 'w') as outs:
        v = sender.superview
        outs.write(v['tv'].text)
        console.hud_alert('Saved!')

class Ed (ui.View):
    def keyboard_frame_did_change(self, frame):
        if ui.get_screen_size()[1] < 768:
            self.frame = (self.frame[0], self.frame[1], self.frame[2], self.frame[3]-frame[3])

pyui_file = os.path.abspath(inspect.getfile(inspect.currentframe())) + 'ui'

v = ui.load_view(os.path.expanduser(pyui_file))
set_text(v['tv'])

if ui.get_screen_size()[1] >= 768:
    # iPad
    v.present()
else:
    # iPhone
    v.present(orientations=['portrait'])



