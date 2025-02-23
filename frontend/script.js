async function generateStory() {
    const region = document.getElementById("region").value;
    const theme = document.getElementById("theme").value;
    const output = document.getElementById("output");

    output.innerText = "Generating...";

    const response = await fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ region, theme })
    });

    const data = await response.json();
    output.innerText = data.tale;
}
