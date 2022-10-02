import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Pages/Home';
import Shifts from './Pages/Shifts';
import Settings from './Pages/Settings';
import Rules from './Pages/Rules';

function App() {
  return (
    <div>
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" exact element={<Home />} />
        <Route path="/shifts" element={<Shifts />}/>
        <Route path="/rules" element={<Rules />}/>
        <Route path="/settings" element={<Settings />}/>
      </Routes>
    </BrowserRouter>
  </div>
  );
}

export default App;