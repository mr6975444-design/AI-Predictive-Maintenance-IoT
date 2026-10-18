let sensorChart;


// Run ML prediction
async function runPrediction() {

    const temperature =
        parseFloat(document.getElementById("temperatureInput").value);

    const vibration =
        parseFloat(document.getElementById("vibrationInput").value);

    const current =
        parseFloat(document.getElementById("currentInput").value);


    const response = await fetch("/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            temperature: temperature,
            vibration: vibration,
            current: current
        })
    });


    const result = await response.json();


    // Update sensor values

    document.getElementById("temperatureValue").textContent =
        result.temperature.toFixed(1);

    document.getElementById("vibrationValue").textContent =
        result.vibration.toFixed(1);

    document.getElementById("currentValue").textContent =
        result.current.toFixed(1);


    // Update prediction

    const statusElement =
        document.getElementById("predictionStatus");

    const systemStatus =
        document.getElementById("systemStatus");

    if (result.prediction === 1) {

        statusElement.textContent = "🚨 FAILURE PREDICTED";

        statusElement.style.background = "#fee2e2";
        statusElement.style.color = "#991b1b";

        systemStatus.textContent = "FAILURE ALERT";
        systemStatus.style.background = "#dc2626";

    } else {

        statusElement.textContent = "✅ MACHINE NORMAL";

        statusElement.style.background = "#dcfce7";
        statusElement.style.color = "#166534";

        systemStatus.textContent = "SYSTEM NORMAL";
        systemStatus.style.background = "#16a34a";
    }


    // Update probability

    const probability =
        result.failure_probability;

    document.getElementById("probabilityText").textContent =
        probability + "%";

    document.getElementById("probabilityBar").style.width =
        probability + "%";
}


// Load sensor history

async function loadSensorData() {

    const response =
        await fetch("/sensor-data");

    const data =
        await response.json();


    const labels =
        data.map((row, index) => index + 1);

    const temperatures =
        data.map(row => row.temperature);

    const vibrations =
        data.map(row => row.vibration);

    const currents =
        data.map(row => row.current);


    const ctx =
        document.getElementById("sensorChart");


    sensorChart = new Chart(ctx, {

        type: "line",

        data: {

            labels: labels,

            datasets: [

                {
                    label: "Temperature",
                    data: temperatures,
                    borderWidth: 2,
                    tension: 0.3
                },

                {
                    label: "Vibration",
                    data: vibrations,
                    borderWidth: 2,
                    tension: 0.3
                },

                {
                    label: "Current",
                    data: currents,
                    borderWidth: 2,
                    tension: 0.3
                }

            ]
        },

        options: {

            responsive: true,

            plugins: {
                legend: {
                    display: true
                }
            },

            scales: {

                y: {
                    beginAtZero: false
                }

            }
        }
    });
}


// Start dashboard

document.addEventListener("DOMContentLoaded", () => {

    loadSensorData();

    runPrediction();

});