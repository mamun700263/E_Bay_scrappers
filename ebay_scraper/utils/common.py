

def file_formate_checker(file_name:str):
    """
    checks the file formate and returns 
    """
    file_name = file_name.lower()
    if file_name.endswith(".csv"):
        return "csv"
    elif file_name.endswith(".json"):
        return "json"
    elif file_name.endswith(".xlsx"):
        return "xlsx"
    else:
        raise ValueError("Invalid file format. Use .csv, .json, or .xlsx.")

