import React, { Component } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import { Link } from 'react-router-dom'
import Login from '../Login/Login'
let nombre=Login[1]
const nombr=async e=>{
nombre=await Login[1]
}
export default class Navigation extends Component {
    
    render() {
        return (
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <Link className="navbar-brand" to="/home" >
                    CriptoApp
                    </Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav ml-auto">
                            
                            <li className="nav-item">
                                <Link className="nav-link" aria-current="page" to="/caesar">Caesar</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" aria-current="page" to="/hill">Hill</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" aria-current="page" to="/playfair">Playfair</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" aria-current="page" to="/turninggrill">Turning Grill</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" aria-current="page" to="/vigenere">Vigenere</Link>
                            </li>
                            <li className="nav-item">
                                <label className="nav-link" aria-current="page" onSubmit={(e)=>nombr} >Hola  {nombre}</label>
                            </li>
                            
                            
                        </ul>
                    </div>
                </div>
            </nav>
        )
    }
}
