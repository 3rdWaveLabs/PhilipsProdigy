from statistics import mean

# function for linear regression
def linear_regression(x, y):     
    N = len(x)
    x_mean = mean(x)
    y_mean = mean(y)
    
    B1_num = 0
    B1_den = 0
    for xi, yi in zip(x, y):
        B1_num = B1_num + ((xi - x_mean) * (yi - y_mean))
        B1_den = B1_den + ((xi - x_mean)**2)

    # calculate M    
    M = B1_num / B1_den
    
    # calculate B
    B = y_mean - (M*x_mean)
    
    # create formatted equation
    EQU = f'y = {M:.3f}X + {B:.1f}'
    
    return (M, B, EQU)

# PT100 Cal Data
PT100T = [0, 1.85, 6.85,11.85,16.85,21.85,26.85,31.85,36.85,41.85,46.85,51.85,56.85,61.85,66.85,71.85,76.85,86.85,91.85,96.85,101.85,106.85,111.85,116.85,121.85,126.85,131.85,136.85,141.85,146.85,151.85,156.85,161.85,166.85,171.85,176.85,181.85,186.85,191.85,196.85,201.85,206.85,211.85,216.85,221.85,226.85,231.85,236.85,241.85,246.85,251.85,256.85,261.85,266.85]
PT100R = [100,100.7228,102.6745,104.6232,106.5691,108.5121,110.4522,112.3894,114.3237,116.2551,118.1836,120.1093,122.032,123.9519,125.8689,127.783,129.6942,133.508,135.4105,137.3102,139.207,141.1009,142.9919,144.88,146.7652,148.6475,150.527,152.4035,154.2772,156.148,158.0159,159.8809,161.743,163.6023,165.4586,167.3121,169.1627,171.0104,172.8552,174.6971,176.5361,178.3722,180.2055,182.0359,183.8633,185.6879,187.5096,189.3284,191.1444,192.9574,194.7675,196.5748,198.3792,200.1807]


heater1T = []
heater1R = []
heater2T = []
heater2R = []

data = open('./heaterdata_16.csv', 'r').read().splitlines()
# data format is: timestamp, RTD0, Resistance0, RTD1, Resistance1
for line in data:
    # split each line into data entries
    entries = line.split(',')
    # ignore timestamp field (start at 1)
    # place entries in lists
    try:
        Time = float(entries[0])
        Setpoint = float(entries[9])
        if ((Time > 0 and Time < 26) 
        or (Time > 70 and Time < 87) 
        or (Time > 124 and Time < 146) 
        or (Time > 175 and Time < 179) 
        or (Time > 230 and Time < 360)
        and (Setpoint != 0.0)):
            heater1T.append(float(entries[1]))
            heater1R.append(float(entries[2]))
            heater2T.append(float(entries[3]))
            heater2R.append(float(entries[4]))
    except Exception as e:
        pass

# Use Linear regression function to get M and B

M, B, EQU = linear_regression(heater1R, heater1T)
print(f'Heater 0:\nM = {M*20:.3f}\nB = {B:.1f}\n')


M, B, EQU = linear_regression(heater2R, heater2T)
print(f'Heater 1:\nM = {M*20:.3f}\nB = {B:.1f}\n')