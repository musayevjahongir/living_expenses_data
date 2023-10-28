import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    import json
    s=0
    f=open(file_path).read()
    f=json.loads(f)
    for i in f:
        s+=f[i]
    return s


# test
file_path = "data.json"
total = total_expenses(file_path)
print(total)
