from Fuzzification import Fuzzification
from Inference import Inference
from Defuzzufucation import  Defuzzification
import csv

with open('DataTugas2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    no = []
    penghasilan = []
    hutang = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            no.append(int(row[0]))
            penghasilan.append(float(row[1]))
            hutang.append(float(row[2]))
        # endif
    # endfor

data = []
for i in range(0,len(penghasilan)):
    data.append([no[i],penghasilan[i],hutang[i]])
# endfor

for x in range(0,len(data)):
    crisp = Fuzzification(data[x][1], data[x][2])
    crisp.triangularPenghasilan()
    crisp.trapezoidalHutang()
    inf = Inference(crisp.getMyuKecil(), crisp.getMyuBiasa(), crisp.getMyuGede(), crisp.getMKecil(), crisp.getMBiasa(),
                    crisp.getMGede())
    inf.fuzRules()
    dfuzz = Defuzzification(inf.getATidak(),inf.getACons(),inf.getAYa(),x,data)
    dfuzz.sugeno()
# endfor



try:
    fix = []
    for y in range(0, len(dfuzz.getBlt()[0:20])):
        fix.append(['keluarga', dfuzz.getBlt()[y][0]])
    # endfor

    with open('TebakanTugas2.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')
        for line in fix:
            csv_writer.writerow(line)

    print("'TebakanTugas2.csv' successfully created")
except ValueError:
    print("'TebakanTugas2.csv' can't be create")