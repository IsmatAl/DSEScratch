import { alertConstants } from '../constants';


const error = (message) => ({ type: alertConstants.ERROR, message });
const success = (message) => ({ type: alertConstants.SUCCESS, message });

export const alertActions = {
  success,
  error
};