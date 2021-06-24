import axios from 'axios';

const SERVER_ADDRESS = 'http://127.0.0.1:8000';


const metricTypeToURL = {
  'sse': '/api/sse',
  'pse': '/api/pse',
  'rs': '/api/rs',
  'cvg': '/api/cvg',
};


const uploadFiles = async (formData) => {
  try {
    const response = await axios.post(`${SERVER_ADDRESS}/api/upload`, formData,
      {
        "Content-Type": "multipart/form-data"
      }
    );
    return { data: response.data, ok: true };
  } catch (err) {
    return {
      errData: err.response.data,
      errStatus: err.response.status
    };
  }
};


const deleteFile = async (param) => {
  try {
    const response = await axios.delete(`${SERVER_ADDRESS}/api/delete`, { params: param });
    return { data: response.data, ok: true };
  } catch (err) {
    return {
      errData: err.response.data,
      errStatus: err.response.status
    };
  }
};


const getFiles = async () => {
  try {
    const response = await axios.get(`${SERVER_ADDRESS}/api/files`);
    return { data: response.data, ok: true };
  } catch (err) {
    return {
      errData: err.response.data,
      errStatus: err.response.status
    };
  }
};


const performDSE = async (params) => {
  try {
    const response = await axios.post(`${SERVER_ADDRESS}/api/pex`, {
      ...params,
      max_iter: 10
    });
    return { data: response.data, ok: true };
  } catch (error) {
    return {
      errData: error.response.data,
      errStatus: error.response.status
    };
  }
};

const performRS = async (data) => {
  try {
    const response = await axios.post(`${SERVER_ADDRESS}/api/rs`, data);
    return { data: response.data, ok: true };
  } catch (err) {
    return {
      errData: err.response.data,
      errStatus: err.response.status
    };
  }
};


const chooseRef = async (params) => {
  try {
    const response = await axios.post(`${SERVER_ADDRESS}/api/ref`, params);
    return { data: response.data, ok: true };
  } catch (err) {
    return {
      errData: err.response.data,
      errStatus: err.response.status
    };
  }
};


const calcMetric = async ({ metricType, params }) => {
  try {
    const response = await axios.post(`${SERVER_ADDRESS}${metricTypeToURL[metricType]}`, params);
    return { data: response.data, ok: true };
  } catch (err) {
    return {
      errData: err.response.data,
      errStatus: err.response.status
    };
  }
};


const pairProgram = async (id) => {
  try {
    const response = await axios.post(`${SERVER_ADDRESS}/api/pair`, { id });
    return { data: response.data, ok: true };
  } catch (err) {
    return {
      errData: err.response.data,
      errStatus: err.response.status
    };
  }
};


const downloadGraph = async (params) => {
  try {
    const response = await axios.get(`${SERVER_ADDRESS}/api/pex?id=${params.id}`, {
      responseType: 'arraybuffer'
    });
    const buffer = Buffer.from(response.data, 'base64');
    return { data: buffer, ok: true };
  } catch (err) {
    return {
      errData: err.response.data,
      errStatus: err.response.status
    };
  }
};

const submitCode = async (params) => {
  try {
    const response = await axios.post(`${SERVER_ADDRESS}/api/code`, params);
    return { data: response.data, ok: true };
  } catch (err) {
    return {
      errData: err.response.data,
      errStatus: err.response.status
    };
  }
};




const chooseAsActive = async (id) => {
  try {
    const response = await axios.post(`${SERVER_ADDRESS}/api/active`, { id });
    return { data: response.data, ok: true };
  } catch (err) {
    return {
      errData: err.response.data,
      errStatus: err.response.status
    };
  }
};

export const userService = {
  uploadFiles,
  deleteFile,
  performRS,
  performDSE,
  getFiles,
  chooseRef,
  calcMetric,
  pairProgram,
  downloadGraph,
  submitCode,
  chooseAsActive
};