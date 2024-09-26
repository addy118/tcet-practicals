document.addEventListener('DOMContentLoaded', () => {
    updateFoodItems(); // Initialize with default category food items
});

function updateFoodItems() {
    const category = document.getElementById('category').value;
    const foodItemsContainer = document.getElementById('food-items');

    const foodItems = {
        snacks: [
            { name: 'Chips', price: 10 },
            { name: 'Samosa', price: 15 },
            { name: 'Sandwich', price: 25 }
        ],
        italian: [
            { name: 'Pizza', price: 100 },
            { name: 'Pasta', price: 80 },
            { name: 'Lasagna', price: 120 }
        ],
        chinese: [
            { name: 'Noodles', price: 70 },
            { name: 'Spring Rolls', price: 50 },
            { name: 'Manchurian', price: 90 }
        ],
        south: [
            { name: 'Idli', price: 20 },
            { name: 'Medu Vada', price: 25 },
            { name: 'Masala Dosa', price: 50 }
        ],
        north: [
            { name: 'Chole Bhature', price: 60 },
            { name: 'Paneer Tikka', price: 100 },
            { name: 'Butter Naan', price: 30 }
        ]
    };

    foodItemsContainer.innerHTML = '';

    foodItems[category].forEach(item => {
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.name = item.name.toLowerCase().replace(' ', '-');
        checkbox.id = item.name.toLowerCase().replace(' ', '-');

        const label = document.createElement('label');
        label.htmlFor = item.name.toLowerCase().replace(' ', '-');
        label.textContent = `${item.name} - ₹${item.price}`;

        const foodItemDiv = document.createElement('div');
        foodItemDiv.className = 'food-item';
        foodItemDiv.appendChild(checkbox);
        foodItemDiv.appendChild(label);

        foodItemsContainer.appendChild(foodItemDiv);
    });
}
