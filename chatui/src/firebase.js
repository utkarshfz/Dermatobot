import firebase from "firebase/app"
import "firebase/auth"

const app=firebase.initializeApp({
    apiKey: process.env.REACT_APP_FIREBABSE_API_KEY,
    authDomain: process.env.REACT_APP_FIREBABSE_AUTH_DOMAIN,
    projectId: process.env.REACT_APP_FIREBABSE_PROJECT_ID,
    storageBucket: process.env.REACT_APP_FIREBABSE_STORAGE_BUCKET,
    messagingSenderId: process.env.REACT_APP_FIREBABSE_MESSAGING_SENDER_ID,
    appId: process.env.REACT_APP_FIREBABSE_APP_ID

})
export const auth =app.auth()
export default app