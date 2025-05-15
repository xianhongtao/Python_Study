from datetime import datetime
input_str = input("请输入年月日（示例格式: 2025-5-15）: ")
input_list = input_str.split('-')
year = int(input_list[0])
month = int(input_list[1])
day = int(input_list[2])
days_since_start_of_year = datetime(year, month, day) - datetime(year, 1, 1)
print("这是该年的第{}天".format(days_since_start_of_year.days + 1))
