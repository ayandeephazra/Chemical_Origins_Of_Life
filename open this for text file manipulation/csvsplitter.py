import os
import csv

list = []

# This is the path where all the files are stored.

folder_path = "C:\\Users\\Ayan Deep Hazra\\PycharmProjects\\pythonProject1\\open this for text file " \
              "manipulation\\filtered_test_scibert.csv"

# try multiple encodings if one fails
file = open(folder_path, encoding="utf-8")
csvreader = csv.reader(file)
rows = []

for row in csvreader:
    rows.append(row[0])
i = 0

for sentence in rows:
    f2 = open("C:\\Users\\Ayan Deep Hazra\\PycharmProjects\\pythonProject1\\open this for text file " \
              "manipulation\\output\\FILE" + str(i) + ".txt", "w+", encoding="utf-8-sig")
    i = i + 1
    f2.write(sentence)
    f2.close()
