with open('./../Data BMI.csv') as file:
    counter = 1;
    for line in file:
        sistol = 0;
        try:
            sistol = round(int(line.rstrip().split(',')[6]), -1)
        except:
            sistol = 0;

        if sistol > 0:
            f = open("input/file" + f'{counter:02d}', 'w+')
            f.write(str(sistol))
            f.close()
            counter += 1
