"""Extra Credit: What titles were most browsed?

This program takes a CSV data file and outputs a new CSV data file with the title from A line to V line.
Run like so:

    python combine_extracredit_title_vline.py mrjob/anonymous-msweb.data > extacredit_title_vline.data
"""
    
import csv
import fileinput
from sys import stdout


def csv_readline(line):
    """Given a string CSV line, return a list of strings."""
    for row in csv.reader([line]):
        return row


def main():


    csv_writer = csv.writer(stdout)

    titles = {}

    for line in fileinput.input():
        cell = csv_readline(line)
        if cell[0] == 'A':
            titles[cell[1]] = cell[3]
        elif cell[0] == 'V':
            cell[2] = titles[cell[1]]

        csv_writer.writerow(cell)


if __name__ == '__main__':
    main()
