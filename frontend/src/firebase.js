// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA3A7bxEDbebANTcWrygyd-yIlrdt5H1M8",
  authDomain: "ai-assistant-f2ee3.firebaseapp.com",
  projectId: "ai-assistant-f2ee3",
  storageBucket: "ai-assistant-f2ee3.firebasestorage.app",
  messagingSenderId: "486497185736",
  appId: "1:486497185736:web:1895c77300a3377b371afd",
  measurementId: "G-4CWF7M76YP"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);