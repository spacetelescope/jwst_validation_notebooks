import os

from pathlib import Path

if __name__ == "__main__":
    for path in Path('jwst_validation_notebooks').rglob('exec*.ipynb'):
        print("Removing {}".format(path))
        os.remove(path)
    for path in Path('jwst_validation_notebooks').rglob('*.html'):
        print(path)
        os.remove(path)
    if os.path.exists("index.html"):
        print("Removing index.html")
        os.remove("index.html")
    if os.path.exists("junit_report.xml"):
        print("Removing junit_report.xml")
        os.remove("junit_report.xml")
