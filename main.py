import random
import csv
import re

forecast = "FORECAST_VALUE"  # header option 1
measured = "MEASURED_VALUE"  # header option 2
timestamp = "TIME_STAMP"  # header


class File:
    def __init__(self, value, timestamp_start):
        self.value = value
        self.timestamp = timestamp_start
def validate_date(start_date):
    validate = re.search("[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2} [0]:[0]{2,2}", start_date)
    if validate != None:
        return start_date
    else:
        return ""
def generate_values_forecast(min,max,count):
    values = list()
    for i in range(0,count):
        value = random.uniform(min,max)
        values.append(value)
    return values
def round_values(values):
    rounded = list()
    for i in range(0,len(values)):
        rounded.append(round(values[i],4))
    return rounded
def replace_date_hour(hour,date):
    splited = date.split(' ')
    split_hour= splited[1].split(':')
    split_hour[0]=hour
    return str(splited[0])+" "+str(split_hour[0])+":"+split_hour[1]
def create_dic_for_csv(start_date,values,count):
    dic = {}
    for i in range(0,count):
        obj = File(values[i],replace_date_hour(str(i),start_date))
        dic[obj.timestamp] = obj.value
    return dic
def get_single(date):
    split = date.split(" ")
    date_split = split[0].split("-")
    y = date_split[0]
    m = date_split[1]
    d = date_split[2]
    return y,m,d
def create_file_name(date,name="forecast"):
    y,m,d = get_single(date)
    return name+"_"+y+"_"+m+"_"+d+".csv"
def create_dic_with_custom_name(start_date_val,generated_values,count):
    values_csv = {}
    if start_date_val!="":
        values_csv = create_dic_for_csv(start_date_val,generated_values,count)
    return values_csv
def create_and_write_file(filename,header1,header2,dic):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([header1,header2])
        for key,value in dic.items():
            writer.writerow([key,value])

forecast_values = [6044.094996, 5661.121702, 5279.72392, 5046.107824, 4974.1855, 5171.577852, 5833.84025,6338.345902,6524.451696,6599.523452,6555.162898,6548.337902,6463.81625,6410.0058,6323.908952,6391.106648,6837.076902,7017.407404,6996.67095,6905.849154,6820.80265,6644.409498,6510.014746,6400.293798]
min = min(forecast_values)
max = max(forecast_values)
count = len(forecast_values)

generated_values = generate_values_forecast(min,max,count)
#print(generated_values)
rounded_values = round_values(generated_values)
#print(rounded_values)


filename = create_file_name("1970-01-01 0:00")
#print(filename)


start_date = input("Type date like: 1970-01-01 0:00\n")
start_date_val = validate_date(start_date)
if start_date_val!="":
    filename = create_file_name(start_date_val)
    print(f"Filename:{filename}")
else:
    print("Date is not in valid format")


dic = create_dic_with_custom_name(start_date_val,generated_values,count)

print(dic)

create_and_write_file(filename,timestamp,forecast,dic)