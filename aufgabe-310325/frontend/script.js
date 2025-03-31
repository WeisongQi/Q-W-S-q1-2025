const apiUrl = "http://localhost:5050/produkte";

// 获取产品列表并渲染到表格
async function fetchProducts() {
    const response = await fetch(apiUrl);
    const products = await response.json();
    const tableBody = document.querySelector("#productTable tbody");
    tableBody.innerHTML = ""; // 清空表格内容

    products.forEach(product => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${product.id}</td>
            <td>${product.name}</td>
            <td>${product.sorten}</td>
            <td>${product.art}</td>
        `;
        tableBody.appendChild(row);
    });
}

// 添加新产品
async function addProduct() {
    const name = document.getElementById("name").value;
    const sorten = document.getElementById("category").value;
    const art = document.getElementById("art").value;

    // 验证输入字段
    if (!name || !sorten || !art) {
        alert("All fields are required!");
        return;
    }

    const response = await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, sorten, art })
    });

    if (response.ok) {
        fetchProducts(); // 刷新产品列表
        clearInputs(); // 清空输入字段
    } else {
        alert("Failed to add product");
    }
}

// 修改产品
async function modifyProduct() {
    const id = document.getElementById("modifyId").value;
    const name = document.getElementById("modifyName").value;
    const sorten = document.getElementById("modifyCategory").value;
    const art = document.getElementById("modifyArt").value;

    if (!id) {
        alert("ID is required to modify a product!");
        return;
    }

    const response = await fetch(`${apiUrl}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, sorten, art })
    });

    if (response.ok) {
        fetchProducts(); // 刷新产品列表
        clearModifyInputs(); // 清空修改输入字段
    } else {
        alert("Failed to modify product");
    }
}

// 删除产品
async function deleteProduct() {
    const id = document.getElementById("deleteId").value;

    if (!id) {
        alert("ID is required to delete a product!");
        return;
    }

    try {
        const response = await fetch(`${apiUrl}/${id}`, { method: "DELETE" });

        if (response.ok) {
            alert("Product deleted successfully!");
            fetchProducts(); // 刷新产品列表
            document.getElementById("deleteId").value = ""; // 清空输入字段
        } else {
            const errorData = await response.json();
            alert(`Failed to delete product: ${errorData.message}`);
        }
    } catch (error) {
        console.error("Error deleting product:", error);
        alert("An error occurred while deleting the product.");
    }
}

// 清空输入字段
function clearInputs() {
    document.getElementById("name").value = "";
    document.getElementById("category").value = "A";
    document.getElementById("art").value = "";
}

// 清空修改输入字段
function clearModifyInputs() {
    document.getElementById("modifyId").value = "";
    document.getElementById("modifyName").value = "";
    document.getElementById("modifyCategory").value = "";
    document.getElementById("modifyArt").value = "";
}

// 初始化事件监听器
document.getElementById("addButton").addEventListener("click", addProduct);
document.getElementById("modifyButton").addEventListener("click", modifyProduct);
document.getElementById("deleteButton").addEventListener("click", deleteProduct);

// 页面加载时获取产品列表
window.onload = fetchProducts;
