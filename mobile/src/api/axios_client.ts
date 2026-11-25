import axios from "axios";

const axiosClient = axios.create({
  baseURL: process.env.EXPO_PUBLIC_API_URL,
  timeout: 15000, // Set a timeout of 5 seconds
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});


export default axiosClient