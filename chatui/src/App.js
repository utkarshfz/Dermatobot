import Chat from './Chat.js'
import Signup from "./Signup"
import { AuthProvider } from './AuthContext';
import { BrowserRouter as Router, Switch, Route} from  "react-router-dom"
import Login from "./Login"
import PrivateRoute from "./PrivateRoute"
function App() {
  return (
    <div style={{backgroundColor:"rgb(0, 10, 26)"}}>
      <AuthProvider>
            <Router>
              <Switch> 
                <PrivateRoute exact path="/" component={Chat}/>
                <Route path="/signup" component={Signup}/>  
                <Route path="/login" component={Login}/>  
              </Switch>
            </Router>
          
</AuthProvider>
    </div>
    

  );
}

export default App;
