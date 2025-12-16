import wx
import requests
import xml.etree.ElementTree as ET
import wikipedia

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, pos=wx.DefaultPosition, size=wx.Size(450, 120),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="My First AI Assistant")
        
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        
        lbl = wx.StaticText(panel, label="Hello, I'm Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input_text = self.txt.GetValue().lower()
        # print("It worked!", input_text)


        try:
            # wolfram
            app_id = "R6UV22GKVQ"
            url = "https://api.wolframalpha.com/v2/query"

            params = {
                "input": input_text,
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
            
            # input_text = input_text.split(' ')
            # input = " ".join(input[2:])
            print(wikipedia.summary(input_text, sentences = 2, auto_suggest=False))


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()