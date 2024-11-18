import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const getAccounts = async () => axios.get(`${API_URL}/accounts/`);
export const getPosts = async () => axios.get(`${API_URL}/posts/`);
export const createPost = async (data) => axios.post(`${API_URL}/posts/`, data);
