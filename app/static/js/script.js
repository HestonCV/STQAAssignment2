
document.getElementById('bmiForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ weight: weight, height: height }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Your BMI is: ${data.bmi} -- You are classified as ${data.category}`;
    })
    .catch(error => console.error('Error:', error));
});