#!/usr/bin/env python3
import logging
import os
import platform
import resource

if platform.system() == 'Darwin':
    # Raise the rather small default 256-open-files-only limit to 1024
    no_files = 1024
    resource.setrlimit(resource.RLIMIT_NOFILE, (no_files, no_files))

from nbpages import make_parser, run_parsed, make_html_index

args = make_parser()
args.add_argument("--notebook-path", default='.', dest='nb_path',
                  help="A relative path to notebooks you wish to execute.")
args = args.parse_args()

if args.template_file is None and os.path.exists('nb_html.tpl'):
    args.template_file = 'nb_html.tpl'

if args.exclude is None:
    # If there is an "exclude_notebooks" file, use that to find which ones to
    # skip.  Format is one pattern per line, "#" for comments.
    # note that this will be ignored if exclude is given at the command line.
    to_exclude = []
    if os.path.isfile('exclude_notebooks'):
        with open('exclude_notebooks') as f:
            for line in f:
                if line.strip() != '':
                    to_exclude.append(line.strip().split('#')[0])
    if to_exclude:
        args.exclude = ','.join(to_exclude)

if args.report_file is None:
    args.report_file = "junit_report.xml"

try:
    converted = run_parsed(args.nb_path, output_type='HTML', args=args, timeout=36000)
except Exception as e:
    print("ERROR: {}".format(e))
    print("args={}".format(args))
    raise e

logging.getLogger('nbpages').info('Generating index.html')
make_html_index(converted, './index.tpl')
