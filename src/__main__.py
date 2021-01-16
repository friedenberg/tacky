
import sys
import os
import objc

import argparse

from Foundation import NSString, NSUTF8StringEncoding, NSBundle
from AppKit import NSPasteboard, NSPasteboardItem

def main():
    parser = argparse.ArgumentParser(prog = "tacky")
    subparsers = parser.add_subparsers()

    copy_parser = subparsers.add_parser("copy")
    copy_parser.set_defaults(func = cli_copy)
    copy_parser.add_argument(
            '-i','--item',
            action = 'append',
            nargs = 2,
            metavar = ('uti_type', 'file'),
            help = 'help:')

    paste_parser = subparsers.add_parser("paste")
    paste_parser.set_defaults(func = cli_paste)
    paste_parser.add_argument(
            '-u','--uti',
            action = 'store',
            help = 'help:')

    paste_parser.add_argument(
            '-l','--list',
            action = 'store_true',
            help = 'help:')

    args = parser.parse_args()
    args.func(args)

def uti_from_argument(uti_type):
    uti_value = uti_type

    if uti_type.startswith('kUTType'):
        bundle = NSBundle.bundleWithIdentifier_("com.apple.AppKit")
        objc.loadBundleVariables(bundle, globals(), [(uti_type, b'@')])
        uti_value = globals()[uti_type]

    return uti_value

def cli_copy(args):
    copy([(uti_from_argument(e[0]), e[1]) for e in args.item])

def cli_paste(args):
    if args.list:
        list_uti()
    elif args.uti:
        paste(args.uti)

def copy(entries):
    pb = NSPasteboard.generalPasteboard()
    types = [e[0] for e in entries]
    pb.declareTypes_owner_(types, None)

    stdin_data = None

    for (uti, path) in entries:
        if path == '-':
            if stdin_data is None:
                stdin_data = sys.stdin.read()

            write_pasteboard(pb, stdin_data, uti)
        else:
            with open(path, 'r') as f:
                value = f.read()
                write_pasteboard(pb, value, uti)

def write_pasteboard(pb, value, uti):
    new_str = NSString.stringWithString_(value).nsstring()
    new_data = new_str.dataUsingEncoding_(NSUTF8StringEncoding)
    pb.setData_forType_(new_data, uti)

def list_uti():
    pb = NSPasteboard.generalPasteboard()
    for p in pb.pasteboardItems():
        for t in p.types():
            print(NSString.stringWithString_(t).nsstring())

def paste(uti):
    pb = NSPasteboard.generalPasteboard()
    for p in pb.pasteboardItems():
        for t in p.types():
            if t == uti:
                print(p.stringForType_(uti))
                return

if __name__ == "__main__":
    main()

