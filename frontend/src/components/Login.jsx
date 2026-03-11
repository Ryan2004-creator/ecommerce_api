import React, { useState } from 'react';
import axios from 'axios';
import { FaUser, FaLock, FaSignInAlt } from 'react-icons/fa';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/api/auth/token/', { username, password });
      console.log('Logged in:', response.data);
      alert('Login successful!');
    } catch (error) {
      console.error('Login error:', error);
      alert('Login failed. Please check your credentials.');
    }
    setIsLoading(false);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1><FaSignInAlt /> Login</h1>
      <div className="input-group">
        <FaUser />
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
      </div>
      <div className="input-group">
        <FaLock />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>
      <button type="submit" className="btn" disabled={isLoading}>
        {isLoading ? 'Logging in...' : 'Login'}
      </button>
    </form>
  );
};

export default Login;