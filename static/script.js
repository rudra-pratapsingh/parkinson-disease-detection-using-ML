document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Collect form data
    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = parseFloat(value);
    });

    // Send data to Flask backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').innerText = `Prediction: ${result.prediction}`;
    })
    .catch(error => {
        document.getElementById('result').innerText = 'Error: Could not get prediction';
        console.error('Error:', error);
    });
});