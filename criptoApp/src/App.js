import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import {BrowserRouter as Router , Route} from 'react-router-dom'
import Login from './Login/Login';
import Caesar from './components/caesar';
import Hill from './components/hill';
import Playfair from './components/playfair'
import TurningGrill from './components/turningGrill'
import Vigenere from './components/vigenere'
import Home from './components/home';
import Des from './components/des';


function App() {
  return (
    <Router>
      
      <Route path='/' exact component={Login[0]} />
      <Route path='/home' component={Home}/>
      <Route path='/caesar' component={Caesar}/>
      <Route path='/hill' component={Hill}/>
      <Route path='/playfair' component={Playfair}/>
      <Route path='/turninggrill' component={TurningGrill}/>
      <Route path='/vigenere' component={Vigenere}/>
      <Route path='/des' component={Des}/>
    </Router>
  );
}

export default App;
