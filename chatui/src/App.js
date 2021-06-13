import Chat from './Chat.js'
import logo from './logo.svg';
import './App.css';
import Signup from "./Signup"
import { Container } from 'react-bootstrap';
import { AuthProvider } from './AuthContext';
import { BrowserRouter as Router, Switch, Route} from  "react-router-dom"
//import Dashboard from "./Dashboard"
import Login from "./Login"
import PrivateRoute from "./PrivateRoute"
function App() {
  return (
    // <Chat />
    <AuthProvider>
<Container className="d-flex  align-items-center justify-content-center"
       style={{minHeight: "100vh"}}>
         <div className="w-100" style={{ maxWidth: "400px"}}>
            <Router>
            {/* <AuthProvider> */}
              <Switch> 
                <PrivateRoute exact path="/" component={Chat}/>
                <Route path="/signup" component={Signup}/>  
                <Route path="/login" component={Login}/>  
              </Switch>
            {/* </AuthProvider> */}
            </Router>
            {/* <Signup/> */}
          </div>
</Container>
</AuthProvider>

  );
}

export default App;
