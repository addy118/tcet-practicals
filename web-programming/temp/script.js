function calculateBMI() {
    // Get user input
    const username = document.getElementById("username").value;
    const height = parseFloat(document.getElementById("height").value);
    const weight = parseFloat(document.getElementById("weight").value);

    // Calculate BMI
    const bmi = (weight / (height * height)).toFixed(2);

    // Determine BMI category
    let category;
    if (bmi < 18.5) {
        category = "Underweight";
    } else if (bmi >= 18.5 && bmi < 24.9) {
        category = "Normal weight";
    } else if (bmi >= 25 && bmi < 29.9) {
        category = "Overweight";
    } else {
        category = "Obese";
    }

    // Show the result box
    const resultBox = document.getElementById("resultBox");
    resultBox.style.display = "block";

    // Insert the result into the table
    const bmiResults = document.getElementById("bmiResults");
    bmiResults.innerHTML = `
        <tr>
            <td>${username}</td>
            <td>${bmi}</td>
            <td>${category}</td>
        </tr>
    `;

    // Clear form after submission
    document.getElementById("bmiForm").reset();
}
