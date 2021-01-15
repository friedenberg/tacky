
import sys
import os
import objc

import argparse

from Foundation import NSString, NSUTF8StringEncoding, NSBundle
from AppKit import NSPasteboard, NSPasteboardItem

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
            '-i','--item',
            action = 'append',
            nargs = 2,
            metavar = ('uti_type', 'file'),
            help = 'help:')

    args = parser.parse_args()

    copy([(uti_from_argument(e[0]), e[1]) for e in args.item])

def uti_from_argument(uti_type):
    uti_value = uti_type

    if uti_type.startswith('kUTType'):
        bundle = NSBundle.bundleWithIdentifier_("com.apple.AppKit")
        objc.loadBundleVariables(bundle, globals(), [(uti_type, b'@')])
        uti_value = globals()[uti_type]

    return uti_value


def copy(entries):
    pb = NSPasteboard.generalPasteboard()
    types = [e[0] for e in entries]
    pb.declareTypes_owner_(types, None)

    pb_item = NSPasteboardItem.alloc().init()

    used_stdin = False

    for (uti, path) in entries:
        if path == '-' and not used_stdin:
            path = '/dev/stdin/'
            used_stdin = True
        elif used_stdin:
            #todo throw error
            pass

        with open(path, 'r') as f:
            value = f.read()
            new_str = NSString.stringWithString_(value).nsstring()
            new_data = new_str.dataUsingEncoding_(NSUTF8StringEncoding)
            pb_item.setData_forType_(new_data, uti)

    pb.writeObjects_([pb_item])

if __name__ == "__main__":
    main()

