import React, { Component } from 'react'
import Navigation from './Navigation'
import { Link } from 'react-router-dom'
import './home.css'

export default class home extends Component {
    render() {
        return (
            <div >
                <Navigation />
                <div className='principal'>
                    <br />
                    <h1 className='titulo'>CriptoApp</h1>
                    <br />
                    <h3>Explora en la barra de arriba para encriptar y desencriptar tus mensajes</h3>
                    <br />
                    <h3><Link className="navbar-brand" to="/caesar" >
                        Cifrado Caesar
                    </Link></h3>
                    <br />
                    <h3><Link className="navbar-brand" to="/hill" >
                        Cifrado de Hill
                    </Link></h3>
                    <br />
                    <h3><Link className="navbar-brand" to="/playfair" >
                        Cifrado Playfair
                    </Link></h3>
                    <br />
                    <h3><Link className="navbar-brand" to="/turninggrill" >
                        Cifrado Turning Grill
                    </Link></h3>
                    <br />
                    <h3><Link className="navbar-brand" to="/vigenere" >
                        Cifrado Vigenere
                    </Link></h3>
                    
                    <h3>Proximamente Aes y Des...</h3>
                </div>
            </div>
        )
    }
}
