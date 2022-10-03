import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Pages/HomePage';
import Shifts from './Pages/ShiftsPage';
import Settings from './Pages/SettingsPage';
import Rules from './Pages/RulesPage';

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