import argparse
import datetime
import os

def prepend_date_to_report(reportfile):
    """Add date to filename
    
    Parameters
    ----------
    reportfile : str
        name of report to add date to
    """

    now = datetime.datetime.now()

    if os.path.exists(reportfile):
        dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")   
        os.replace(reportfile, 'report-' + dt_string + '.xml') 
    else:
        print("Path not provided, continuing")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--reportfile', default=None, dest='report',
                        help='Path to report file')
    args = parser.parse_args()

    prepend_date_to_report(args.report)

if __name__ == '__main__':
    main()