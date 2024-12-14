import copy
from openai import OpenAI
import json
from examples import history as examples
from tqdm import tqdm

Nodes = []

def find_node(nodes):
    if nodes["children"] != []:
        for node in nodes["children"]:
            find_node(node)
    else:
        Nodes.append(nodes)

def denoise(noised_code, client):
    pyload = {
        "model": "gpt-3.5-turbo-0125",
    }
    question = f"{noised_code} \n\n Extract and format the code in Context, if not code is found, please respond with 'None'"
    context = copy.deepcopy(examples)
    context.append({"role": "user", "content": question})
    pyload.update({"messages": context})
    response = client.chat.completions.create(**pyload).choices[0].message.content
    return response

        
if __name__ == "__main__":
    api_key = ""
    base_url = "https://api.closeai-proxy.xyz/v1"
    client = OpenAI(base_url=base_url, api_key=api_key,)
    with open("../data.json", "r") as f:
        data = json.load(f)
        
    # with open("./examples.txt", "r") as f:
    #     examples = f.read()
        
    find_node(data)
    for node in tqdm(Nodes):
        print(node["name"])
        sample_code = node["info"]["sample_code"]
        handle_code = node["info"]["handle_code"]
        denoised_sim_code = denoise(sample_code, client)
        denoised_handle_code = denoise(handle_code, client)
        node["info"]["sample_code"] = denoised_sim_code
        node["info"]["handle_code"] = denoised_handle_code
        tqdm.write(f"Sample Code: {denoised_sim_code}")
        tqdm.write(f"Handle Code: {denoised_handle_code}")

    with open("./denoised_data.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

