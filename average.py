import json

def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    import json
    s=0
    f=open(file_path).read()
    f=json.loads(f)
    for i in f:
        s+=f[i]
    return s/len(f)


# test
file_path = "data.json"
average = average_expenses(file_path)
print(average)
