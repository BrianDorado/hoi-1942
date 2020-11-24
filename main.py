import csv


def main():
    '''Imports Data from spredsheets and creates unit class based on data. Outputs .txt file formatted to conform with HOI IV unit files'''
    csvToOpen = 'HOI IV Divisions.csv'

    with open(csvToOpen, 'r' ) as csvFile:
        csvReader = csv.reader(csvFile)

        for row in csvReader:
            print(row)

main()