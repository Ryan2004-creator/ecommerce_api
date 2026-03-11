import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { FaShoppingCart, FaEye } from 'react-icons/fa';

const Products = () => {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/products/')
      .then(response => setProducts(response.data))
      .catch(error => console.error('Error fetching products:', error));
  }, []);

  const addToCart = (product) => {
    setCart([...cart, product]);
    alert(`${product.name} added to cart!`);
  };

  return (
    <div>
      <h1>Our Products</h1>
      <div className="products-list">
        {products.map(product => (
          <div key={product.id} className="product-card">
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <p className="price">${product.price}</p>
            <div className="product-actions">
              <button className="btn" onClick={() => addToCart(product)}>
                <FaShoppingCart /> Add to Cart
              </button>
              <button className="btn btn-secondary">
                <FaEye /> View Details
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Products;