import React, { useState, useRef } from 'react'
import ReCAPTCHA from "react-google-recaptcha";
import { Redirect } from 'react-router';

import './Login.css'
import { Button,  Form, FormGroup, Label }
    from 'reactstrap'
import Inputi from '../Inputi'

import axios from 'axios'

let name2 = 'Invitado'
const Login = () => {

    const [user, setUser] = useState('');
    
    const [password, setPassword] = useState('');
    const [resp , setResp] =useState(null)
    const [captchaValido, setCaptchaValido]=useState(null)
    const [userValido, setUserhaValido]=useState(false)
    const [login, setlogin]=useState(false)
    const [error, setError]=useState(false)
    const captcha=useRef(null)

    function handleChange (name , value){
        if(name === 'usuario'){
            setUser(value)
        }
        else{             
            setPassword(value)            
        }
    }
    const onChange = () =>{
        if(captcha.current.getValue()){
            setCaptchaValido(captcha.current.getValue())
        }
    }
    
    onsubmit= async e =>{       
               
        const formData = new FormData()
        formData.append('email',user)
        formData.append('password',password)
        try{
            let config = {
                headers: {
                  'Access-Control-Allow-Origin': '*',
                }
              }
            let data ={
                'email':user,
                'password':password
            }
            let url='http://localhost:8080/users/login'
         setResp(await (await axios.post(url,data,config)).data)
         if (resp===''){
            console.log('resp=null')
        }
     }catch(e){
         setError(true)
         console.log(e)
     }
    if(resp && resp!==''){
        setUserhaValido(true)
    }else(setError(true))
    if(userValido && captchaValido){
        console.log('pasoooo')
        name2=resp.name
        console.log(resp,resp.name,name2)
        setlogin(true)
    }
        
    } 
    
    return (
        
        <div className="completo">
           { login &&
             <Redirect to="/home" />        
            }
            {error&&
            <script>{alert('algo es incorrecto')}</script> }
            {error && setError(false)}
            <Form className="login-form">
                <h1 className="font-w">Cripto App</h1>
                <h2 className="text-center">Bienvenido</h2>
                <FormGroup>
                    <Label className="usuario-l">Usuario</Label>
                    
                    <Inputi 
                    atribute={{
                        id:'usuario',
                        name:'usuario',
                        type:'text',
                        placeholder:'Ingrese su usuario'
                    }}
                    handleChange={handleChange}
                    
                />
                    
                </FormGroup>
                <hr   className='usuario-i'/>
                <FormGroup>
                    <label>Contraseña</label>
                    <Inputi
                    atribute={{
                        id:'contraseña',
                        name:'contraseña',
                        type:'password',
                        placeholder:'Ingrese su contraseña'
                    }}
                    handleChange={handleChange}
                />
                </FormGroup>
                <div className='captcha-d'>
                <ReCAPTCHA ref={captcha}
                    sitekey="6LcmVmwbAAAAACTNG3rP4LmeD_Wc6bcPKVCopbOl"
                    onChange={onChange}
                />
                </div>
                    <Button onClick={ onsubmit} className="btn-lg btn-light btn-block">Entrar</Button>
                
            </Form>
        </div>
    )

}
export default[Login,name2]
