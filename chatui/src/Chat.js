import { ChatFeed, Message } from 'react-chat-ui'
import React, { useRef,useState } from 'react';
import {TextField} from '@material-ui/core/';
import CameraIcon from '@material-ui/icons/Camera';
import SendIcon from '@material-ui/icons/Send';
import axios from 'axios'
import { Card, Button,Alert } from "react-bootstrap"
import { useAuth} from "./AuthContext"
import {useHistory} from "react-router-dom"





function Chat() {
    const [messages,set_messages] = useState([new Message({
        id:1,
        message:"Hi I'm Dermatobot, a bot for dermatological diagnosis!"
    }),new Message({
        id:1,
        message:"Can you upload an image of your site of infections?"
    })])

    
    const {currentUser , logout}=useAuth()
            const history=useHistory()
    const [text,update_text]=useState(null)

    const [top_k_classes,set_top_k_classes]=useState([])

    const inputFile = useRef(null) 
    async function handleLogout()
            {
                //setError('')
                try {
                    await logout()
                    history.push("/login")
                }catch{
                    //setError("failed to Logout")
                }
            }

    const update = () => {
        // `current` points to the mounted file input element
       inputFile.current.click();
       
      };

      const setImageFile = (event) =>{
          

            // Create an object of formData
            const formData = new FormData();
            
            // Update the formData object
            formData.append(
                "image",event.target.files[0]
            );
                
            axios.post('http://127.0.0.1:5000/predict',formData)
            .then(function (response) {

                // console.log(response.data.predictions.slice(1,6));
                console.log(response.data.predictions)
                const data=response.data.predictions.slice(0,6);

                // console.log(data[0].disease_name)
                const disease_list=data.map((x)=>{
                    return x.disease_name
                })

                set_top_k_classes(disease_list);
                


                const new_message=[new Message({
                    id:1,
                    message:"Successfully Uploaded images"
                }),new Message({
                    id:1,
                    message:"Please describe your symptoms in detail!!!"}
                    )]

                set_messages(messages =>([...messages,...new_message]))
            })
            .catch(function (error) {
                // console.log("error")
                
      
                const new_message=[new Message({
                    id:1,
                    message:"Oops something went wrong!!!"
                })]
                
                
                set_messages(messages =>([...messages,...new_message]))
            });
      }
    
      const send =() =>{

        // console.log(Array.isArray(top_k_classes))
        // console.log(text)
        console.log(top_k_classes)
        const new_message=[new Message({
            id:0,
            message:text
        })]

        set_messages(messages =>([...messages,...new_message]))
        const disease_names=top_k_classes[0]+","+top_k_classes[1]+","+top_k_classes[2]+","+top_k_classes[3]+","+top_k_classes[4]

        

        const formData = new FormData();
            
            // Update the formData object
            formData.append(
                "top_k",disease_names
            );

            formData.append(
                "text",text
            );

            // console.log(formData)

        // console.log(top_k_classes[0])
        axios.post('http://da4176b06998.ngrok.io/predict',
        formData
        )
            .then(function (response) {

                // console.log(response['data'])
                const new_message=[new Message({
                    id:1,
                    message:"Based on the your images and your description you may be suffering from:   "+response['data'].resultant_class
                }),new Message({
                    id:1,
                    message:"Want to test again...Please upload another image!!!"
                })]
                
                
                set_messages(messages =>([...messages,...new_message]))

                
            })
            .catch(function (error) {
                // console.log("error")
                
      
                const new_message=[new Message({
                    id:1,
                    message:"Oops something went wrong!!!"
                })]
                
                
                set_messages(messages =>([...messages,...new_message]))
            });



            // update_text(null)

            
            



      }
      

    return (
        
        <div style={{position:"absolute" , top:"0px",height:"100%",width:"100%",backgroundColor:"rgb(0, 10, 26)"}} >
            
            <div style={{postion:"fixed",top:"0px",height:"95%",overflow:"scroll"}} >
            <div style={{backgroundColor:"rgb(217, 217, 217)",borderRadius: "0px 0px 0px 30px"}}> 
            <h1 style={{display:'inline-block',color:"rgb(230, 115, 0)",width:"90%"}}>DERMATOBOT</h1>
            <Button  onClick={ handleLogout} style={{backgroundColor:"rgb(255, 112, 77)",width:"10%"}}>Log Out
            </Button>
            </div>
            
            
            
            

            <ChatFeed
            messages={messages} // Array: list of message objects
            isTyping={false} // Boolean: is the recipient typing
            hasInputField={false} // Boolean: use our input, or use your own
            showSenderName // show the name of the user who sent the message
            bubblesCentered={false} //Boolean should the bubbles be centered in the feed?
            // JSON: Custom bubble styles
            bubbleStyles={
            {
                userBubble: [],
                text: {
                fontSize: 18
                },
                chatbubble: {
                borderRadius: 25,
                padding: 20,
                backgroundColor:"rgb(0, 102, 204)"
                }
            }
            }
            />
            </div>
            
            <div style={{position:"fixed" , bottom:"0px",width:"100%",backgroundColor:"rgb(153, 206, 255)",borderRadius: "0px 0px 15px 15px"}}>
                <input type='file' id='file' ref={inputFile} style={{display: 'none'}} onChange={setImageFile}/>
                <CameraIcon style={{width:"3%",height:"0.6%",color:"blue"}} onClick={() => update()}></CameraIcon>
                <TextField size="small" style={{width:"94%",backgroundColor:"white"}} multiline  label="Input...." variant="filled" onChange={(event)=>{update_text(event.target.value)}}/>
                <SendIcon style={{width:"3%",height:"0.6%",color:"blue"}} onClick={() => send()} ></SendIcon>
                
            </div>
            
                
            
        </div>
        
        
    );
  }
  
export default Chat;
