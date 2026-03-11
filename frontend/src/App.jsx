import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { FaHome, FaShoppingCart, FaUser, FaStore } from 'react-icons/fa';
import Home from './components/Home';
import Products from './components/Products';
import Cart from './components/Cart';
import Login from './components/Login';
import './App.css';

function App() {
  return (
    <Router>
      <div id="root">
        <nav>
          <ul>
            <li><Link to="/"><FaHome /> Home</Link></li>
            <li><Link to="/products"><FaStore /> Products</Link></li>
            <li><Link to="/cart"><FaShoppingCart /> Cart</Link></li>
            <li><Link to="/login"><FaUser /> Login</Link></li>
          </ul>
        </nav>
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/products" element={<Products />} />
            <Route path="/cart" element={<Cart />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
