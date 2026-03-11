import React from 'react';
import { Link } from 'react-router-dom';
import { FaShoppingBag, FaStar, FaTruck } from 'react-icons/fa';

const Home = () => {
  return (
    <div className="home">
      <section className="hero">
        <h1>Welcome to Ryan's E-Commerce</h1>
        <p>Discover amazing products with the spirit of champions!</p>
        <Link to="/products" className="btn hero-btn">
          <FaShoppingBag /> Shop Now
        </Link>
      </section>

      <section className="features">
        <div className="feature-card">
          <FaStar size={40} color="#fbc2eb" />
          <h3>Premium Quality</h3>
          <p>Only the best products for our customers</p>
        </div>
        <div className="feature-card">
          <FaTruck size={40} color="#fbc2eb" />
          <h3>Fast Delivery</h3>
          <p>Quick and reliable shipping worldwide</p>
        </div>
        <div className="feature-card">
          <FaShoppingBag size={40} color="#fbc2eb" />
          <h3>Easy Shopping</h3>
          <p>Seamless experience from browse to checkout</p>
        </div>
      </section>
    </div>
  );
};

export default Home;