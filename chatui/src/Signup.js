
import React, {useRef, useState} from "react"
import { Form, Button, Card, Alert } from 'react-bootstrap'
import { useAuth } from "./AuthContext"
import { Link ,useHistory} from "react-router-dom"
import { Container } from 'react-bootstrap';

export default function  Signup () {
    const emailRef=useRef()
    const passwordRef=useRef()
    const passwordConfirmRef=useRef()
    const { signup } = useAuth()
    const [error, setError]=useState("")
    const [loading, setLoading]=useState(false)
    const history=useHistory()

    async function handleSubmit(e)
    {
        e.preventDefault()
        if (passwordRef.current.value !== passwordConfirmRef.current.value)
        {
            return setError("Passwords dont match ")
        }
        try{
            setError("")
            setLoading(true)
            await signup(emailRef.current.value,passwordRef.current.value)
            history.push("/")
        }catch {
            setError("Failed to create an account")
        }
        setLoading(false)
    }
    return (
        <Container className="d-flex  align-items-center justify-content-center" style={{minHeight: "100vh"}}>
        <div style={{width:"400px"}}>
            <Card>
                <Card.Body> 
                    <h2 className="text-center mb-4"> Sign Up</h2>
                   
                    {error && <Alert variant="danger">{error}</Alert> }
                    <Form onSubmit={handleSubmit}>
                        <Form.Group id="email" style={{margin:"10px"}}>
                            <Form.Label>Email  </Form.Label>
                             <Form.Control type="email"  ref={emailRef} required/>
                            
                        </Form.Group>

                        <Form.Group id="password" style={{margin:"10px"}}>
                            <Form.Label>Password  </Form.Label>
                             <Form.Control type="password" ref={passwordRef} required/>
                            
                        </Form.Group>

                        <Form.Group id="password-confirm" style={{margin:"10px"}}>
                            <Form.Label>Password Confirmation  </Form.Label>
                             <Form.Control type="password" ref={passwordConfirmRef} required/>
                            
                        </Form.Group>
                        <Button disabled={loading} className="w-100" type="submit" >Sign Up</Button>
                        </Form>
                </Card.Body>
            </Card>
            <div className="w-100 text-center mt-2" style={{color:'white'}}> 
                already have an account? <Link to="/login">Log In </Link>
            </div>
            </div>
            </Container>
    )
}
