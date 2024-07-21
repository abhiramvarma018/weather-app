document.getElementById('weatherForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission

    const city = document.getElementById('cityInput').value;
    const response = await fetch(`/weather?city=${city}`);
    const data = await response.json();

    if (data.error) {
        document.getElementById('weatherResult').classList.add('hidden');
        document.getElementById('error').textContent = data.error;
        document.getElementById('error').classList.remove('hidden');
    } else {
        document.getElementById('cityName').textContent = data.city;
        document.getElementById('temperature').textContent = data.temperature;
        document.getElementById('unit').textContent = data.unit;
        document.getElementById('description').textContent = data.description;

        document.getElementById('weatherResult').classList.remove('hidden');
        document.getElementById('error').classList.add('hidden');
    }
});
