Nodes = []
import json

def find_node(nodes):
    if nodes["children"] != []:
        for node in nodes["children"]:
            find_node(node)
    else:
        if nodes["info"]["sample_code"] == "None" or nodes["info"]["handle_code"] == "None":
            print(nodes["name"])
            
            
with open("./denoised_data.json", "r") as f:
    data = json.load(f)
    find_node(data)
