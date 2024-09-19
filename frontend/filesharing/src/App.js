
import React from 'react'

import {BrowserRouter as Router, Route, Routes} from "react-router-dom"
import PrivateRoute from "./utils/PrivateRoute"
import { AuthProvider } from './context/AuthContext'

import Homepage from './views/HomePage'
import Registerpage from './views/RegisterPage'
import Loginpage from './views/LoginPage'
import Dashboard from './views/Dashboard'
import Navbar from './views/Navbar'



function App() {
  return (
    <Router>
      <AuthProvider>
        < Navbar/>
        <Routes>
          <PrivateRoute component={Dashboard} path="/dashboard" exact />
          <Route component={Loginpage} path="/login" />
          <Route component={Registerpage} path="/register" exact />
          <Route component={Homepage} path="/" exact />
        </Routes>
      </AuthProvider>
    </Router>
  )
}

export default App
