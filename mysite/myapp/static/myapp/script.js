let cart = [];
let totalPrice = 0;

function addToCart(itemName, itemPrice) {
    cart.push({ name: itemName, price: itemPrice });
    updateCart();
}

function updateCart() {
    const cartItems = document.getElementById('cart-items');
    const total = document.getElementById('total-price');
    cartItems.innerHTML = '';
    totalPrice = 0;

    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - ${item.price} SAR`;
        cartItems.appendChild(li);
        totalPrice += item.price;
    });

    total.textContent = `Total: ${totalPrice} SAR`;
}