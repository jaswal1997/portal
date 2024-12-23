document.getElementById("examForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("result").textContent = result.message;
    })
    .catch(error => {
        document.getElementById("result").textContent = "Error submitting data.";
        console.error('Error:', error);
    });
});
