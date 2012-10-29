import math

daten = open('daten.txt')
#gibt die erste zeiele aus
#print(daten.readline())

#classvars
mean_sum = 0.0
stand_sum =0.0
outputFileName = "result.txt"

#formatiere datenset in liste
valueList = []
for zeile in daten:
    #print(zeile)
    valueList.extend(zeile.split(' '))

#berechne median
for value in  valueList:
    val_num = float(value)
    #median
    mean_sum += val_num

median = mean_sum / len(valueList)

#berechne deviation
for value in  valueList:
    val_num = float(value)
    #median
    stand_sum += (val_num - median)**2

standart_deviation = math.sqrt(stand_sum/len(valueList))
    
print "mean:               " + str(median)
print "standard deviation: " + str(standart_deviation)

outputFile = open(outputFileName, 'w')
outputFile.write("mean:               " + str(median) + "\n" + "standard deviation: " + str(standart_deviation) )
outputFile.close()
daten.close()
