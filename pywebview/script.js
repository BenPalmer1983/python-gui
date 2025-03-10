

document.addEventListener("DOMContentLoaded", function() {
    // Ensure pywebview is ready
    if (window.pywebview) {
        loadTheme();
        toggleTheme();
        loadDropdown();
    } else {
        document.addEventListener("pywebviewready", loadDropdown);
    }
});

function toggleTheme() {
    let currentTheme = document.body.getAttribute("data-theme");
    let themeText = document.getElementById("theme-text");
    if (currentTheme === "dark") {
        document.body.removeAttribute("data-theme");
        localStorage.setItem("theme", "light");
        themeText.innerText = "Dark Mode";
    } else {
        document.body.setAttribute("data-theme", "dark");
        localStorage.setItem("theme", "dark");
        themeText.innerText = "Light Mode";
    }
}

function loadTheme() {
    console.log("Loading theme..."); 
    let savedTheme = localStorage.getItem("theme");
    let themeText = document.getElementById("theme-text");
    if (savedTheme === "dark") {
        document.body.setAttribute("data-theme", "dark");
        themeText.innerText = "Light Mode";
    }
}

function loadPage(page) {
    let content = document.getElementById("content");
    if (page === 1) {
        console.log("page 1"); 
        content.innerHTML = `
            <div class="calculation-area">
                <h1>Calculation Page</h1>
                <div class="input-container">
                    <input type="number" id="num1" placeholder="Enter number 1" required>
                    <input type="number" id="num2" placeholder="Enter number 2" required>
                    <button onclick="calculate()">Calculate</button>
                    <h3 id="result"></h3>
                </div>
            </div>`;
    }
    else if (page === 2) 
    {
        console.log("page 2"); 
        content.innerHTML = `
            <div class="calculation-area">
                <h1>Select Files</h1>
                <p>Information here.</p>
                <div class="input-container">
                    <label for="myfile" class="span-2">Select a file:</label> 
                    <input type="file" class="span-4" id="fileInput" onchange="handleFileUpload(event)">
                    <label for="myfile" class="span-2">Output file:</label> 
                    <input type="text" class="span-4" id="fileNameInput" placeholder="enter name">
                    <div class="span-2"></div>
                    <button class="span-4" onclick="sendFileNameToPython()">Send File Name to Python</button>
                    <h3 id="result"></h3>
                </div>
            </div>`;
    } 
    else if (page === 3) 
    {
        console.log("page 3"); 
        content.innerHTML = `
            <div class="calculation-area">
                <h1>Select Files</h1>
                <p>Information here.</p>
                <div class="input-container">
                    <label for="myfile" class="span-2">Select a file:</label> 
                    <input type="file" class="span-4" id="fileInput" onchange="handleFileUpload(event)">
                    <label for="myfile" class="span-2">Output file:</label> 
                    <input type="text" class="span-4" id="fileNameInput" placeholder="enter name">
                    <div class="span-2"></div>
                    <button class="span-4" onclick="sendFileNameToPython()">Send File Name to Python</button>
                    <h3 id="result"></h3>
                </div>
            </div>`;

        window.pywebview.api.generatePlot().then(imageData => {
            document.getElementById("content").innerHTML = `
                <img src="data:image/png;base64,${imageData}" alt="Generated Plot" style="max-width: 100%;">
            `;
        });
    } 
    else if (page === 4) 
    {
        console.log("page 4"); 
        content.innerHTML = `
            <div class="calculation-area">
                <h1>Select Files</h1>
                <p>Information here.</p>
                <div class="input-container">
                    <label for="myfile" class="span-2">Select a file:</label> 
                    <input type="file" class="span-4" id="fileInput" onchange="handleFileUpload(event)">
                    <label for="myfile" class="span-2">Output file:</label> 
                    <input type="text" class="span-4" id="fileNameInput" placeholder="enter name">
                    <div class="span-2"></div>
                    <button class="span-4" onclick="sendFileNameToPython()">Send File Name to Python</button>
                    <h3 id="result"></h3>
                </div>
                
                <h2>Select an Option</h2>
                <select id="dropdown"></select>
                    </div>
                </div>  
            </div>`;
            
            loadDropdown();
            
    } 
    else if (page === 5) 
    {
        content.innerHTML = `
            <div class="calculation-area">
                <h1>Select Files</h1>
                <p>Information here.</p>
                <div class="input-container">
                    <label for="myfile" class="span-2">Select a file:</label> 
                    <input type="file" class="span-4" id="fileInput" onchange="handleFileUpload(event)">
                    <label for="myfile" class="span-2">Output file:</label> 
                    <input type="text" class="span-4" id="fileNameInput" placeholder="enter name">
                    <div class="span-2"></div>
                    <button class="span-4" onclick="sendFileNameToPython()">Send File Name to Python</button>
                    <h3 id="result"></h3>           
                </div>
            </div>`;
    } 
    else if (page === 6) 
    {
        content.innerHTML = `
            <div class="calculation-area">
                <h1>Select Files</h1>
                <p>Information here.</p>
                <div class="input-container">
                    <label for="myfile" class="span-2">Select a file:</label> 
                    <input type="file" class="span-4" id="fileInput" onchange="handleFileUpload(event)">
                    <label for="myfile" class="span-2">Output file:</label> 
                    <input type="text" class="span-4" id="fileNameInput" placeholder="enter name">
                    <div class="span-2"></div>
                    <button class="span-4" onclick="sendFileNameToPython()">Send File Name to Python</button>
                    <h3 id="result"></h3>
                </div>
            </div>`;
    } 
    else if (page === 7) 
    {
        content.innerHTML = `
            <div class="calculation-area">
                <h1>Select Files</h1>
                <p>Information here.</p>
                <div class="input-container">
                    <label for="myfile" class="span-2">Select a file:</label> 
                    <input type="file" class="span-4" id="fileInput" onchange="handleFileUpload(event)">
                    <label for="myfile" class="span-2">Output file:</label> 
                    <input type="text" class="span-4" id="fileNameInput" placeholder="enter name">
                    <div class="span-2"></div>
                    <button class="span-4" onclick="sendFileNameToPython()">Send File Name to Python</button>
                    <h3 id="result"></h3>
                </div>
            </div>`;
    } 
    else if (page === 8) 
    {
        content.innerHTML = `
            <div class="calculation-area">
                <h1>Select Files</h1>
                <p>Information here.</p>
                <div class="input-container">
                    <label for="myfile" class="span-2">Select a file:</label> 
                    <input type="file" class="span-4" id="fileInput" onchange="handleFileUpload(event)">
                    <label for="myfile" class="span-2">Output file:</label> 
                    <input type="text" class="span-4" id="fileNameInput" placeholder="enter name">
                    <div class="span-2"></div>
                    <button class="span-4" onclick="sendFileNameToPython()">Send File Name to Python</button>
                    <h3 id="result"></h3>
                </div>
            </div>`;
    } 
    else 
    {
        content.innerHTML = `
        <div class="calculation-area">
        <h1>Page ${page}</h1>
        <p>This is another page.</p>
        </div>

        `;
    }
}



function calculate() {
    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2").value;
    window.pywebview.api.calculate(num1, num2).then(result => {
        document.getElementById("result").innerText = result;
    });
}

let selectedFile = null;

function handleFileUpload(event) {
    selectedFile = event.target.files[0];
    if (selectedFile) {
        let fileName = selectedFile.name;
        let fileParts = fileName.split('.');
        if (fileParts.length > 1) {
            let extension = fileParts.pop();
            let newFileName = fileParts.join('.') + " (copy)." + extension;
            document.getElementById("fileNameInput").value = newFileName;
        } else {
            document.getElementById("fileNameInput").value = fileName + " (copy)";
        }
    } else {
        alert("No file selected.");
    }
}

function sendFileNameToPython() {
    if (selectedFile) {                
        let filePath = selectedFile.path || selectedFile.name; // Get full path if possible
        window.pywebview.api.processFile(selectedFile.name).then(response => {
            document.getElementById("content").innerHTML = `
                <h1>File Submitted</h1>
                <p><a href="#" onclick="window.pywebview.api.openFileLocation('${filePath}'); return false;">
                    Open File Location
                </a></p>
            `;
        });
    } else {
        alert("No file selected.");
    }
}


function loadDropdown() {
    console.log("Loading dropdown..."); 
    window.pywebview.api.get_data("options.json").then(options => {
        let dropdown = document.getElementById("dropdown");
        dropdown.innerHTML = ""; // Clear existing options
        options.forEach(option => {
            let opt = document.createElement("option");
            opt.value = option;
            opt.textContent = option;
            dropdown.appendChild(opt);
        });
    }).catch(error => console.error("Error loading data:", error));
}


function exitApp() {
    if (window.pywebview) {
        window.pywebview.api.exit_app();
    } else {
        window.close();
    }
}

// Function to wait for pywebview to become available
const waitForPywebview = async () => {
    return new Promise((resolve) => {
        const interval = setInterval(() => {
            if (typeof pywebview !== 'undefined' && pywebview.api) {
                clearInterval(interval);
                resolve();
            }
        }, 100); // Check every 100ms if pywebview is available
    });
};

const boot = async () => {
try {
await waitForPywebview(); // Wait for pywebview to be available
// do something with pywebview python api here
} catch (error) {
console.error('Error waiting for pywebview:', error);
}
};

onMounted(() => {
boot();
});
