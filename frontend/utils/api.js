import axios from 'axios'

const baseUrl = 'http://localhost:5005'

export const getData = () => {
    return axios.get(`${baseUrl}/api/data`)
}