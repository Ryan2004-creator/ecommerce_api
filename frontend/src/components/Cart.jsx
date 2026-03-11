import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { FaTrash, FaShoppingBag } from 'react-icons/fa';

const Cart = () => {
  const [cartItems, setCartItems] = useState([]);

  useEffect(() => {
    // For now, using local storage or something, but since no shared state, fetch from API
    axios.get('http://localhost:8000/api/cart/')
      .then(response => setCartItems(response.data))
      .catch(error => console.error('Error fetching cart:', error));
  }, []);

  const removeFromCart = (id) => {
    setCartItems(cartItems.filter(item => item.id !== id));
  };

  const total = cartItems.reduce((sum, item) => sum + (item.quantity * 10), 0); // Mock price

  return (
    <div>
      <h1><FaShoppingBag /> Shopping Cart</h1>
      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          <div className="cart-items">
            {cartItems.map(item => (
              <div key={item.id} className="cart-item">
                <div>
                  <p><strong>Product ID:</strong> {item.product}</p>
                  <p><strong>Quantity:</strong> {item.quantity}</p>
                </div>
                <button className="btn btn-danger" onClick={() => removeFromCart(item.id)}>
                  <FaTrash />
                </button>
              </div>
            ))}
          </div>
          <div className="cart-total">
            <h2>Total: ${total.toFixed(2)}</h2>
            <button className="btn">Checkout</button>
          </div>
        </>
      )}
    </div>
  );
};

export default Cart;