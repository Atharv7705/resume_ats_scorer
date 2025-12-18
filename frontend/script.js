async function analyze() {
    const resumeInput = document.getElementById("resume");
    const jdInput = document.getElementById("jd");
    const resultDiv = document.getElementById("result");
    const button = document.querySelector("button");

    // Validation
    if (!resumeInput.files[0]) {
        resultDiv.innerText = "Please select a resume file.";
        return;
    }
    if (!jdInput.value.trim()) {
        resultDiv.innerText = "Please enter a job description.";
        return;
    }

    // Show loading state
    button.disabled = true;
    button.innerText = "Analyzing...";
    document.getElementById("loading").style.display = "block";
    resultDiv.innerText = "";

    try {
        const formData = new FormData();
        formData.append("resume", resumeInput.files[0]);
        formData.append("job_description", jdInput.value);

        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        resultDiv.innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        resultDiv.innerText = `Error: ${error.message}. Please make sure the backend server is running.`;
    } finally {
        // Reset loading state
        button.disabled = false;
        button.innerText = "Analyze";
    }
}
