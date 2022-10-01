import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import * as AiIcons from 'react-icons/ai';

function App() {
  
 return (
   <div className="App">
     <h1>
      Salary Application
      </h1>
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' />
        </Switch>
      </Router>
   </div>
 );
}
 
export default App;