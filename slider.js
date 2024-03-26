document.addEventListener('DOMContentLoaded', function() {
    const healthSlider = document.getElementById('health-slider');
    const healthInput = document.getElementById('health-input');

    healthSlider.addEventListener('input', function() {
        healthInput.value = healthSlider.value;
        updateHealthLevel(healthSlider.value);
    });

    healthInput.addEventListener('input', function() {
        healthSlider.value = healthInput.value;
        updateHealthLevel(healthInput.value);
    });

    function updateHealthLevel(value) {
        document.getElementById('health-value').textContent = value;
        // Update the health level bar visually, if applicable
    }

    // Assuming similar setup for enjoyment slider and input
    const enjoymentSlider = document.getElementById('enjoyment-slider');
    const enjoymentInput = document.getElementById('enjoyment-input');

    enjoymentSlider.addEventListener('input', function() {
        enjoymentInput.value = enjoymentSlider.value;
        updateEnjoymentLevel(enjoymentSlider.value);
    });

    enjoymentInput.addEventListener('input', function() {
        enjoymentSlider.value = enjoymentInput.value;
        updateEnjoymentLevel(enjoymentInput.value);
    });

    function updateEnjoymentLevel(value) {
        document.getElementById('enjoyment-value').textContent = value;
        // Update the enjoyment level bar visually, if applicable
    }

    // Example function to handle the Run Simulation button click
    document.getElementById('run-simulation').addEventListener('click', function() {
        // Here you would call the backend C++ dynamic program with the current values
        // For demonstration, this is a placeholder
        console.log('Running simulation with:', {
            health: healthSlider.value,
            enjoyment: enjoymentSlider.value
        });
        // Update the GUI based on the simulation results
    });

    // Reset button functionality
    document.getElementById('reset-simulation').addEventListener('click', function() {
        healthSlider.value = 50;
        healthInput.value = 50;
        enjoymentSlider.value = 50;
        enjoymentInput.value = 50;
        updateHealthLevel(50);
        updateEnjoymentLevel(50);
        // Reset other elements as needed
    });
});
