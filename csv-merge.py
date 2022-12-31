#  input: two csv files
#  out: a single csv file of the two files merged, allowing for mismatched columns etc 
import csv, subprocess

with open('list1.csv', 'r') as csv1, open('list2.csv', 'r') as csv2:
    readCsv1 = csv.DictReader(csv1)
    readCsv2 = csv.DictReader(csv2)


    with open('newcsv.csv', 'w',newline='') as newcsv:
        headers = readCsv1.fieldnames
        headers.extend(x for x in readCsv2.fieldnames if x not in headers)

        writer = csv.DictWriter(newcsv, fieldnames = headers)
        writer.writeheader()
        writer.writerows(readCsv1)
        writer.writerows(readCsv2)

print(subprocess.run(['cat newcsv.csv'], shell = True, capture_output=True))
        
        # csvDict.update(line[i for i in range(len(line))])

    

    