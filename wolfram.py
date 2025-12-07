# import wolframalpha 

# print("heyy")
# question = input("Enter your Question: ")
# app_id = "R6UV22GKVQ"
# client = wolframalpha.Client(app_id)


# res = client.query(question)

# if res['@success'] == 'true':
#     answer = next(res.results).text     # res.pods will return all answers, res.results will only return 1st response
#     print(answer)
# else:
#     print("No results found")




# import wolframalpha
# import xml.etree.ElementTree as ET

# client = wolframalpha.Client("R6UV22GKVQ")  # Full Results AppID

# question = input("Enter your Question: ")

# try:
#     # Query WolframAlpha
#     res = client.query(question, format='plaintext')  # force plaintext format
#     xml_string = res.response  # get raw XML string
    
#     # Parse the XML manually
#     root = ET.fromstring(xml_string)
    
#     # Find the 'Result' pod
#     answer = None
#     for pod in root.findall('.//pod'):
#         if pod.get('title') == 'Result':
#             subpod = pod.find('subpod')
#             answer = subpod.find('plaintext').text
#             break
    
#     if answer:
#         print("Answer:", answer)
#     else:
#         print("No result found in WolframAlpha response.")

# except Exception as e:
#     print("Error:", e)





# import wolframalpha
# import xml.etree.ElementTree as ET

# client = wolframalpha.Client("R6UV22GKVQ")  # your Full Results AppID

# question = input("Enter your Question: ")

# try:
#     res = client.query(question)
#     xml_string = res.response  # raw XML

#     # Parse XML manually
#     root = ET.fromstring(xml_string)
#     answer = None
#     for pod in root.findall(".//pod"):
#         if pod.get("title") == "Result":  # 'Result' pod contains the answer
#             subpod = pod.find("subpod")
#             if subpod is not None:
#                 plaintext = subpod.find("plaintext")
#                 if plaintext is not None and plaintext.text:
#                     answer = plaintext.text
#                     break

#     if answer:
#         print("Answer:", answer)
#     else:
#         print("No result found in WolframAlpha response.")

# except Exception as e:
#     print("Error:", e)





# import requests
# import xml.etree.ElementTree as ET

# APP_ID = "R6UV22GKVQ"  # your Full Results AppID

# question = input("Enter your Question: ")

# url = "http://api.wolframalpha.com/v2/query"
# params = {
#     "input": question,
#     "appid": APP_ID,
#     "format": "plaintext"
# }

# try:
#     response = requests.get(url, params=params)
#     response.raise_for_status()  # raise error if request failed

#     root = ET.fromstring(response.text)
#     answer = None

#     # Look for the 'Result' pod
#     for pod in root.findall(".//pod"):
#         if pod.get("title") == "Result":
#             subpod = pod.find("subpod")
#             if subpod is not None:
#                 plaintext = subpod.find("plaintext")
#                 if plaintext is not None and plaintext.text:
#                     answer = plaintext.text
#                     break

#     if answer:
#         print("Answer:", answer)
#     else:
#         print("No result found.")

# except Exception as e:
#     print("Error:", e)


# import wolframalpha

# client = wolframalpha.Client("R6UV22GKVQ")  # Your Full Results AppID

# question = input("Enter your Question: ")

# try:
#     res = client.query(question)
    
#     answers = []

#     # Iterate all pods safely
#     if hasattr(res, "pods"):
#         for pod in res.pods:
#             if hasattr(pod, "subpods"):
#                 for sub in pod.subpods:
#                     if hasattr(sub, "plaintext") and sub.plaintext:
#                         answers.append(f"{pod.title}: {sub.plaintext}")

#     if answers:
#         for ans in answers:
#             print(ans)
#     else:
#         print("No result found in WolframAlpha response.")

# except Exception as e:
#     print("Error:", e)



# import wolframalpha

# client = wolframalpha.Client("R6UV22GKVQ")
# question = input("Enter your Question: ")

# try:
#     res = client.query(question)
    
#     any_text = False
#     if hasattr(res, 'pods'):
#         for pod in res.pods:
#             for sub in pod.subpods:
#                 if sub.plaintext:
#                     print(f"{pod.title}: {sub.plaintext}")
#                     any_text = True
#     if not any_text:
#         print("No textual result found. WolframAlpha may have only images or other data.")

# except Exception as e:
#     print("Error communicating with WolframAlpha:", e)



# import wolframalpha
# input = raw_input("Question: ")
# app_id = "R6UV22GKVQ"
# client = wolframalpha.Client(app_id)

# res = client.query(input)
# answer = next(res.results).text

# print answer



# import wolframalpha

# # In Python 3, use input() instead of raw_input()
# question = input("Question: ")

# app_id = "R6UV22GKVQ"
# client = wolframalpha.Client(app_id)

# res = client.query(question)

# # next(res.results) works the same, but print syntax changes
# answer = next(res.results).text

# print(answer)






# import requests

# app_id = "R6UV22GKVQ"
# question = input("Question: ")

# url = "https://api.wolframalpha.com/v1/result"

# params = {
#     "i": question,
#     "appid": app_id
# }

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     print("Answer:", response.text)
# else:
#     print("Error:", response.text)







import requests
import xml.etree.ElementTree as ET

question = input("Question: ")
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
        print(f"\n--- {title} ---")
        
        subpods = pod.findall("subpod")
        for sub in subpods:
            plaintext = sub.findtext("plaintext")
            if plaintext:
                print(plaintext)
