import React, { useState } from 'react'
import Navigation from './Navigation'
import axios from 'axios'
import '../Login/Login.css'

import { Button }
    from 'reactstrap'

const Caesar = () => {

    var striptags = require('striptags');
    const [mensaje, setMensaje] = useState('');
    const [k, setK] = useState('1');
    const [encripted, setEncripted] = useState('1');
    const [resp, setResp] = useState(null)
    const [mostrar, setMostrar] = useState('');

    function handleChange(name, value) {
        if (name === 'mensaje') {
            setMensaje(striptags(value))
        } else {
            setK(value)
        }
    }

    onsubmit = async e => {
        try {
            let config = {
                headers: {
                    'Access-Control-Allow-Origin': '*',
                }
            }
            var bodyFormData = new FormData();
            bodyFormData.append('encript', encripted)
            bodyFormData.append('mensaje', mensaje)
            bodyFormData.append('k', k)

            let url = 'http://localhost:5000/caesar'
            setResp(await (await axios.post(url, bodyFormData, config)).data)
            if (encripted === '1') {
                setMostrar('Su mensaje encriptado es: ')
            } else (setMostrar('Su mensaje desencriptado es: '))
        } catch (e) {
            console.log(e)
            setResp('upps... algo malio sal')
            setMostrar('')
        }
    }


    return (
        <div>
            <Navigation />
            <table class="table">
                <thead>
                    <tr>

                        <th scope="col" className='tabla'></th>
                        <th scope="col"className='tabla1'></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td colspan="2"><h1>Cifrado caesar</h1></td>
                    </tr>
                    <tr>
                        <td>
                        <div className="input-group input-group-lg">
                            <span className="input-group-text" id="inputGroup-sizing-lg">mensaje</span>
                            <input type="text" className="form-control" name="mensaje" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg" onChange={(e) => handleChange(e.target.name, e.target.value)} />
                        </div>
                        <label htmlFor="tentacles">Parametro k (1-26):</label>

                        <input type="number" name="tentacles" onChange={(e) => handleChange(e.target.name, e.target.value)}
                            min="1" max="26" />

                        <div className="form-check">
                            <input className="form-check-input" type="radio" id="flexRadioDefault1" name='en' checked={encripted === '1'} onChange={(e) => setEncripted('1')} />
                            <label className="form-check-label" htmlFor="flexRadioDefault1">
                                Cifrar
                            </label>
                        </div>
                        <div className="form-check">
                            <input className="form-check-input" type="radio" id="flexRadioDefault2" name='de' checked={encripted === '2'} onChange={(e) => setEncripted('2')} />
                            <label className="form-check-label" htmlFor="flexRadioDefault2">
                                Decifrar
                            </label>
                        </div>
                        <Button onClick={onsubmit} className="btn-lg btn-dark btn-block">Enviar</Button>
                        </td>
                        <td>
                        <p><h1>{mostrar}{resp}</h1></p>
                        </td>
                        

                    </tr>
                </tbody>
            </table>
        </div>
    )

}
export default Caesar