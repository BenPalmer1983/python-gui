import webview
import os
import subprocess
import sys
import matplotlib
import matplotlib.pyplot as plt
import io
import base64

matplotlib.use("Agg")

# Define a class with API functions to be exposed to JavaScript
class API:
    def calculate(self, num1, num2):
        try:
            result = float(num1) + float(num2)
            return f"Result: {result}"
        except ValueError:
            return "Invalid input"
        

    def processFile(self, file_name):
        print(f"Processing file: {file_name}")
        return f"Python received file: {file_name}"
    

    def openFileLocation(self, file_path):
        if(sys.platform == "win32"):
            subprocess.run(["explorer", "/select,", os.path.abspath(file_path)])  # Windows
        elif(sys.platform == "darwin"):
            subprocess.run(["open", "-R", os.path.abspath(file_path)])  # MacOS
        else:
            subprocess.run(["xdg-open", os.path.dirname(os.path.abspath(file_path))])  # Linux


    def generatePlot(self):
        # Generate a simple plot
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4, 5], [10, 20, 25, 30, 40], marker="o")
        ax.set_title("Sample Plot")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")

        # Save plot to a BytesIO object
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        plt.close(fig)

        # Encode to base64
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return img_base64
        

    def exit_app(self):
        print("exit")
        os._exit(0)


api = API()

vars = {
        "app_name" : "Generic App",
        "style": open("style.css").read(),
        "script": open("script.js").read(),
       }



# HTML Content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{app_name}}</title>
    <style>
    {{style}}
    </style>    
    <script>
    {{script}}
    </script>
</head>
<body onload="loadTheme()">
    <div class="header">{{app_name}}</div>
    <div class="main-container">
        <div class="sidebar">
            <div class="menu">
                <h3 style="color: white;">Menu</h3>
                <button onclick="loadPage(1)">Calculation</button>
                <button onclick="loadPage(2)">Mod File</button>
                <button onclick="loadPage(3)">Plotter</button>
                <button onclick="loadPage(4)">Page 4</button>
                <button onclick="loadPage(5)">Page 5</button>
                <button onclick="loadPage(6)">Page 6</button>
                <button onclick="loadPage(7)">Page 7</button>
                <button onclick="loadPage(8)">Page 8</button>
                <button margin-top: 20px;" onclick="exitApp()">Exit</button>
            </div>
            <div class="toggle-container">
                <span id="theme-text" style="color: white;">Dark Mode</span>
                <label class="switch">
                    <input type="checkbox" onclick="toggleTheme()">
                    <span class="slider round"></span>
                </label>
            </div>
        </div>
        <div class="content" id="content">
            <h1>Welcome! Select an option from the menu.</h1>
        </div>
    </div>      
</body>
</html>
"""


for k in vars.keys():
    needle = "{{" + k + "}}"
    html_content = html_content.replace(needle, vars[k])


# Save the HTML file locally
html_file = "multi_page.html"
with open(html_file, "w", encoding="utf-8") as fh:
    fh.write(html_content)

# Open in pywebview with API
webview.create_window(vars['app_name'], f"file://{os.path.abspath(html_file)}", js_api=api, width=1200, height=800)
webview.start()
