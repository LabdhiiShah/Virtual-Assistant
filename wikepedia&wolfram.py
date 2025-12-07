import requests
import xml.etree.ElementTree as ET
import wikipedia

while(True):
    question = input("Question: ")

    try:
        # wolfram
        app_id = "R6UV22GKVQ"
        url = "https://api.wolframalpha.com/v2/query"

        params = {
            "input": question,
            "appid": app_id,
            "format": "image,plaintext",
            "output": "XML"
        }

        response = requests.get(url, params=params)

        # Parse XML from the API
        root = ET.fromstring(response.text)

        # Find all pods
        pods = root.findall(".//pod")

        if not pods:
            print("No pods found.")
        else:
            for pod in pods:
                title = pod.attrib.get("title", "No Title")
                
                subpods = pod.findall("subpod")
                for sub in subpods:
                    plaintext = sub.findtext("plaintext")
                    if plaintext:
                        print(plaintext)


    except:
        # wikipeida
        print(wikipedia.summary(question, sentences = 2, auto_suggest=False))