print("Mohd.Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")
def print_table(data):
    if not data:
        print("No data to display.")
        return
    num_columns = len(data[0])
    col_widths = [max(len(str(row[i])) for row in data) for i in range(num_columns)]
    for row in data:
        for i in range(num_columns):
            print(str(row[i]).ljust(col_widths[i] + 2), end='')
        print()  
table_data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "San Francisco"],
    ["Charlie", 35, "London"]
]
print_table(table_data)
