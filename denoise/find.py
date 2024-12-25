from complete_examples import examples
from openai import OpenAI
from copy import copy

Nodes = []
import json


api_key = "sk-LnRR7GEjgsWNP8lJ6hS51XPjTbqZL4IDPsvGhDc3g46p8dft"
base_url = "https://api.closeai-proxy.xyz/v1"
client = OpenAI(base_url=base_url, api_key=api_key,)

def find_node(nodes):
    if nodes["children"] != []:
        for node in nodes["children"]:
            find_node(node)
    else:
        if nodes["info"]["sample_code"] == "None" or nodes["info"]["handle_code"] == "None":
            if nodes["info"]["sample_code"] == "None":
                pyload = {
                    "model": "gpt-3.5-turbo-0125",
                }
                question = f"{nodes["info"]} \n\n***question***\ncomplete the None place in Context"
                context = copy.deepcopy(examples)
                context.append({"role": "user", "content": question})
                pyload.update({"messages": context})
                response = client.chat.completions.create(**pyload).choices[0].message.content
                nodes["info"]["sample_code"] = response
            if node["info"]["handle_code"] == "None":
                pyload = {
                    "model": "gpt-3.5-turbo-0125",
                }
                question = f"{nodes["info"]} \n\n***question***\ncomplete the None place in Context"
                context = copy.deepcopy(examples)
                context.append({"role": "user", "content": question})
                pyload.update({"messages": context})
                response = client.chat.completions.create(**pyload).choices[0].message.content
                nodes["info"]["handle_code"] = response
        
            
            
with open("/home/zym/projects/CEE/cee_data_java.json", "r") as f:
    data = json.load(f)
    find_node(data)

with open("./test.json", "w") as w:
    json.dump(data, w, ensure_ascii=False, indent=4) 
