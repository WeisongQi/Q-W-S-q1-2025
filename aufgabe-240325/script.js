document.addEventListener('DOMContentLoaded', () => {
    const budgetInput = document.getElementById('budget');
    const categoryInput = document.getElementById('category');
    const nameInput = document.getElementById('name');
    const quantityInput = document.getElementById('quantity');
    const priceInput = document.getElementById('price');
    const addButton = document.getElementById('addButton');
    const shoppingList = document.getElementById('shoppingList');
    const sortButton = document.getElementById('sortButton');
    const saveButton = document.getElementById('saveButton');
    const totalBudgetDisplay = document.getElementById('totalBudget');

    let items = [];
    let currentBudget = 0;

    // Initialize budget
    budgetInput.addEventListener('change', () => {
        currentBudget = parseFloat(budgetInput.value);
        updateBudgetDisplay();
    });

    // Add item
    addButton.addEventListener('click', () => {
        if (budgetInput.value && categoryInput.value && nameInput.value && quantityInput.value && priceInput.value) {
            const newItem = {
                category: categoryInput.value,
                name: nameInput.value,
                quantity: parseInt(quantityInput.value),
                price: parseFloat(priceInput.value),
                selected: false
            };

            items.push(newItem);
            renderList();
            updateBudgetDisplay();
            clearInputs();
        }
    });

    // Sort and merge
    sortButton.addEventListener('click', () => {
        // Sort by name
        items.sort((a, b) => a.name.localeCompare(b.name));

        // Merge same items
        const mergedItems = {};
        items.forEach(item => {
            if (mergedItems[item.name]) {
                mergedItems[item.name].quantity += item.quantity;
            } else {
                mergedItems[item.name] = item;
            }
        });

        items = Object.values(mergedItems);
        renderList();
    });

    // Save to local
    saveButton.addEventListener('click', () => {
        const selectedItems = items.filter(item => item.selected);
        const date = new Date().toISOString().split('T')[0];
        const filename = `${date}_shoppinglist.json`;
        const jsonContent = JSON.stringify(selectedItems, null, 2);

        const blob = new Blob([jsonContent], { type: 'application/json' });
        const url = URL.createObjectURL(blob);

        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        a.click();
        URL.revokeObjectURL(url);
    });

    function renderList() {
        shoppingList.innerHTML = '';
        items.forEach((item, index) => {
            const li = document.createElement('div');
            li.className = 'shopping-item';

            li.innerHTML = `
                <input type="checkbox" ${item.selected ? 'checked' : ''}>
                <span >Category : ${item.category} ;</span>&nbsp;
                <span >Name : ${item.name} ;</span>&nbsp;
                <span >Quantity : ${item.quantity} ;</span>&nbsp;
                <span >Price : ${item.price.toFixed(2)} .</span>
                <button class="delete-btn">Delete</button>
            `;

            li.querySelector('input').addEventListener('change', () => toggleSelection(index));
            li.querySelector('.delete-btn').addEventListener('click', () => deleteItem(index));

            shoppingList.appendChild(li);
        });

        updateBudgetDisplay();
    }

    function toggleSelection(index) {
        items[index].selected = !items[index].selected;
    }

    function deleteItem(index) {
        items.splice(index, 1);
        renderList();
    }

    function clearInputs() {
        categoryInput.value = '';
        nameInput.value = '';
        quantityInput.value = '';
        priceInput.value = '';
    }

    function updateBudgetDisplay() {
        const total = items.reduce((sum, item) => sum + (item.quantity * item.price), 0);
        const budget = currentBudget || 0;
        const status = total > budget ? 'Over Budget' : 'Within Budget';
        const color = total > budget ? 'color: red; font-weight: bold' : 'color: black';

        totalBudgetDisplay.innerHTML = `
            <span style="${color}">Total: ${total.toFixed(2)} €</span>
            <span style="${color}"> | ${status}</span>
        `;
    }
});
