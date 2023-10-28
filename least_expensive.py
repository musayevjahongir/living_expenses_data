import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    import json
    s=[]
    f=open(file_path).read()
    f=json.loads(f)
    for i in f:
        s.append(f[i])
    return min(s)
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
