import csv

with open('c:/Users/Natalia/Desktop/CourseraPython/2/csv_example.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))

with open('c:/Users/Natalia/Desktop/CourseraPython/2/csvparaescribir.csv','a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Pedro','Gant','43575664','pgant@gmail.com'])


