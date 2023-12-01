import pandas as pd

def save_JSON(json_data):
    with open ("target.json","w") as json_file:
        json_file.write(json_data)


def convert_to_JSON(excel_file):
    return excel_file.to_json(orient='records')

def read_file(target):
    file =  pd.ExcelFile(target)
    out = pd.read_excel(file)
    return out


out = read_file("./target.xlsx")
json_data = convert_to_JSON(out)
save_JSON(json_data)

