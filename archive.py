import argparse
import datetime
import os
import shutil

from pathlib import Path, PurePosixPath

archive_dir = os.path.join(os.getcwd(), "html_archive")
nb_dir = os.path.join(os.getcwd(), "jwst_validation_notebooks")
out_base = "/grp/jwst/wit/jwst_validation_notebooks"
date_dir = datetime.datetime.now().strftime("%Y-%m-%d")
out_dir = os.path.join(out_base, date_dir)
do_zip = True
verbose = False

archive_help = "Base directory for local HTML archive. Default is {}".format(archive_dir)
out_help = "Directory to copy the archive to. Default is {}".format(out_dir)
nb_help = "Directory to search for notebook HTML files. Default is {}".format(nb_dir)
verbose_help = "Print diagnostic information while running."
zip_help = "Should the central storage archive be zipped. Default is {}".format(do_zip)

parser = argparse.ArgumentParser(description=description)
parser.add_argument('-i', '--input', dest='nb_dir', help=nb_help,
                    default=nb_dir)
parser.add_argument('-o', '--output', dest='out_dir', help=out_help,
                    default=out_dir)
parser.add_argument('-a', '--archive_dir', dest='archive_dir', help=archive_help,
                    default=archive_dir)
parser.add_argument('-z', '--zip', dest="zip", action='store_false', default=do_zip, 
                    help=zip_help)
parser.add_argument('-v', '--verbose', dest="verbose", 
                    action='store_true', default=verbose, help=verbose_help)
res = parser.parse_args()


if __name__ == "__main__":
    archive_dir = res.archive_dir
    nb_dir = res.nb_dir
    out_dir = res.out_dir
    do_zip = res.zip
    verbose = res.verbose

    if os.path.exists(archive_dir):
        shutil.rmtree(archive_dir)
    os.path.makedirs(archive_dir)

    for path in Path(nb_dir).rglob('*.html'):
        if verbose:
            print("Archiving {}".format(path))
        pure_path = PurePosixPath(path)
        rel_path = pure_path.relative_to(nb_dir)
        archive_path = os.path.join(archive_dir, rel_path)
        if verbose:
            print("\tCopying to {}".format(archive_path))
        shutil.copy(path, archive_path)
        central_path = os.path.join(out_dir, rel_path)
        if verbose:
            print("\tCopying to {}".format(central_path))
        shutil.copy(path, central_path)
    if os.path.isfile("index.html"):
        shutil.copy("index.html", os.path.join(archive_dir, "index.html"))
        shutil.copy("index.html", os.path.join(out_dir, "index.html"))
    
    if do_zip:
        shutil.make_archive(date_dir, 'zip', archive_dir)
