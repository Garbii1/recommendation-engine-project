// src/services/api.js
import axios from 'axios';

const apiClient = axios.create({
    baseURL: process.env.VUE_APP_API_URL, // Use env variable
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;