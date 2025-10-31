#task1
import csv

count = 0
with open("C:/Users/超级飞龙/Desktop/books-en.csv", encoding="latin-1") as file:
    reader = csv.DictReader(file, delimiter = ";")
    for row in reader:
        if len(row["Book-Title"]) > 30:
            count+=1
print(count)

#task2
import csv

with open("C:/Users/超级飞龙/Desktop/books-en.csv", encoding="latin-1") as file:
    reader = csv.DictReader(file, delimiter=";")
    Author = input("Author:")
    newreader = []
    for row in reader:
        try:
            year = int(row["Year-Of-Publication"])
            if year <= 1990 and row["Book-Author"] == Author:
                newreader.append(row)
        except KeyError:
            print("error")
    for i in newreader:
       print(i["Book-Title"],i["Book-Author"],i["Year-Of-Publication"])

#task3
import csv
import random

with open("C:/Users/超级飞龙/Desktop/books-en.csv", encoding="latin-1") as file:
    reader = list(csv.DictReader(file,delimiter=";"))
    books = random.sample(reader,20)
with open("Books.txt","w",encoding="latin-1") as f:
    for index,book in enumerate(books,start=1):
        f.write(f"{index}.{book["Book-Author"]}.{book["Book-Title"]}-{book["Year-Of-Publication"]}\n")
    print("Generation complete")

#task4
import xml.etree.ElementTree as ET

tree = ET.parse('currency.xml')
root = tree.getroot()
for child in root.findall('.//Valute'):
    if int(child.find("Nominal").text) == 1:
        print(child.find("Name").text)

#task5
import csv

with open("C:/Users/超级飞龙/Desktop/books-en.csv",encoding="latin-1") as file:
    reader = list(csv.DictReader(file,delimiter=";"))
list_Publish = []
for row in reader:
    if row["Publisher"] not in list_Publish:
        list_Publish.append(row["Publisher"])
for i in list_Publish:
    print(i)
  
#task6
import csv

with open("C:/Users/超级飞龙/Desktop/books-en.csv",encoding="latin-1") as file:
    reader = list(csv.DictReader(file,delimiter=";"))
reader.sort(key=lambda x:int(x['Downloads']))
list_popular_books = reader[-20:]
for index, book in enumerate(list_popular_books, start=1):
    print(f"{index}. {book["Book-Title"]}")
