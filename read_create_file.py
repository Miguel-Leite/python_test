import csv

file = open('data.csv', 'w')

if file:
    file.write('nome,email, contacto, empresa')
else:
    print("Não foi possível criado o arquivo.")

file.close()

changes = [                                                                
        'Miguel',                                      
        'miguel@gmail.com',                                      
        '945633425',                                      
        'SNIR',                                      
    ]      
with open(file.name, 'w+') as f:                                    
    writer = csv.writer(f)                                                       
    writer.writerow(changes)

    reader = csv.reader(open(file.name,'r'))

    for row in reader:
        print(row)

    f.close()

