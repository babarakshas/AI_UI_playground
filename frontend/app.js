async function runInference() {
    const input = document.getElementById("inputText").value;
    const output = document.getElementById("output");

    output.textContent = "Running inference...";

    try {
        const response = await fetch("http://localhost:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ text: input }),
        });

        const data = await response.json();
        output.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        output.textContent = "Error: " + error;
    }
}
