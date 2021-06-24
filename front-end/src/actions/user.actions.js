import { userConstants } from '../constants';
import { userService } from '../services';
import { alertActions } from './';
import download from 'downloadjs'

const uploadFiles = (formData) => {

  const fileUploadRequest = () => { return { type: userConstants.UPLOAD_FILES_REQUEST } };
  const fileUploadSuccess = (files) => { return { type: userConstants.UPLOAD_FILES_SUCCESS, payload: files } };
  const fileUploadFailure = (error) => { return { type: userConstants.UPLOAD_FILES_FAILURE, payload: error } };

  const dseRequest = (entry) => { return { type: userConstants.DSE_REQUEST, payload: entry } };
  const dseSuccess = (file) => { return { type: userConstants.DSE_SUCCESS, payload: file } };
  const dseFailure = (error, entry) => { return { type: userConstants.DSE_FAILURE, payload: { error, entry } } };

  return async dispatch => {

    dispatch(fileUploadRequest());
    const { entry, _ } = await userService.uploadFiles(formData)
      .then(x => {
        if (x.ok) {
          const { _, task } = x.data;
          dispatch(fileUploadSuccess(task))
          return task;
        } else {
          dispatch(fileUploadFailure({ entry, error: x.errData.toString() }));
        }
      },
        error => {
          dispatch(fileUploadFailure({ entry, error: error.toString() }));
          dispatch(alertActions.error(error.toString()));
        }
      );

    dispatch(dseRequest(entry));
    await userService.performDSE({ entry })//, max_iter: 2 })
      .then(dseRes => {
        if (dseRes.ok) {
          const { _, files } = dseRes.data;
          dispatch(dseSuccess({ entry, files }));
        } else {
          dispatch(dseFailure(dseRes.errData.toString(), entry));
        }
      },
        error => {
          dispatch(dseFailure(error.toString(), entry));
          dispatch(alertActions.error(error.toString()));
        })
  };
}

const deleteFile = (id) => {
  return dispatch => {
    dispatch(request());
    userService.deleteFile({ id })
      .then(x => {
        dispatch(success(id));
      },
        error => {
          dispatch(failure(error.toString()));
          dispatch(alertActions.error(error.toString()));
        }
      );

  };

  function request() { return { type: userConstants.FILE_DELETE_REQUEST } }
  function success(id) { return { type: userConstants.FILE_DELETE_SUCCESS, payload: id } }
  function failure(error) { return { type: userConstants.FILE_DELETE_FAILURE, payload: error } }
}



const getFiles = () => {
  return dispatch => {
    dispatch(request());
    userService.getFiles()
      .then(x => {
        dispatch(success(x.data));
      },
        error => {
          dispatch(failure(error.toString()));
          dispatch(alertActions.error(error.toString()));
        }
      );

  };

  function request() { return { type: userConstants.GETALL_REQUEST } }
  function success(data) { return { type: userConstants.GETALL_SUCCESS, payload: data } }
  function failure(error) { return { type: userConstants.GETALL_FAILURE, payload: error } }
}



const chooseAsReference = (id) => {
  return dispatch => {
    dispatch(refRequest());
    userService.chooseRef({ id })
      .then(x => {
        dispatch(refSuccess(x.data));


        dispatch(pairRequest());
        userService.pairProgram(id).then(res => {
          if (res.ok) {
            dispatch(pairSuccess(res.data));
          } else {
            dispatch(pairFailure(res.errData.toString()));
          }
        },
          error => {
            dispatch(pairFailure(error.toString()));
            dispatch(alertActions.error(error.toString()));
          });


      },
        error => {
          dispatch(refFailure(error.toString()));
          dispatch(alertActions.error(error.toString()));
        }
      );

  };

  function refRequest() { return { type: userConstants.CHOOSE_REFERENCE_REQUEST } }
  function refSuccess(id) { return { type: userConstants.CHOOSE_REFERENCE_SUCCESS, payload: id } }
  function refFailure(error) { return { type: userConstants.CHOOSE_REFERENCE_FAILURE, payload: error } }


  function pairRequest() { return { type: userConstants.PAIR_WITH_REF_REQUEST } }
  function pairSuccess(id) { return { type: userConstants.PAIR_WITH_REF_SUCCESS, payload: id } }
  function pairFailure(error) { return { type: userConstants.PAIR_WITH_REF_FAILURE, payload: error } }
}


const calcMetric = (params) => {
  return dispatch => {
    dispatch(request(params));
    userService.calcMetric(params)
      .then(x => {
        if (x.ok) {
          dispatch(success(x.data.data));
        } else {
          dispatch(failure(x.errData.toString()));
        }
      },
        error => {
          dispatch(failure(error.toString()));
          dispatch(alertActions.error(error.toString()));
        }
      );

  };

  function request(entry) { return { type: userConstants.CALCULATE_METRIC_REQUEST, payload: entry } }
  function success(id) { return { type: userConstants.CALCULATE_METRIC_SUCCESS, payload: id } }
  function failure(error) { return { type: userConstants.CALCULATE_METRIC_FAILURE, payload: error } }
}


const donwloadGraph = (id) => {
  return dispatch => {
    dispatch(request());
    userService.downloadGraph({ id })
      .then(x => {
        if (x.ok) {
          download(new Blob([x.data], {
            type: "image/png"
          }), 'file.png')
          dispatch(success(x.data));
        }
        else {
          dispatch(failure(x.errData.toString()));
        }
      },
        error => {
          dispatch(failure(error.toString()));
          dispatch(alertActions.error(error.toString()));
        }
      );

  };

  function request() { return { type: userConstants.DOWNLOAD_EXC_IMG_REQUEST } }
  function success(image) { return { type: userConstants.DOWNLOAD_EXC_IMG_SUCCESS, payload: image } }
  function failure(error) { return { type: userConstants.DOWNLOAD_EXC_IMG_FAILURE, payload: error } }
}


const submitCode = (params) => {
  return dispatch => {
    dispatch(request(params));
    userService.submitCode(params)
      .then(x => {
        if (x.ok) {
          dispatch(success(params));
        } else {
          dispatch(failure(x.errData.toString()));
        }
      },
        error => {
          dispatch(failure(error.toString()));
          dispatch(alertActions.error(error.toString()));
        }
      );

  };

  function request(params) { return { type: userConstants.SUBMIT_CODE_REQUEST, payload: params } }
  function success(id) { return { type: userConstants.SUBMIT_CODE_SUCCESS, payload: id } }
  function failure(error) { return { type: userConstants.SUBMIT_CODE_FAILURE, payload: error } }
}


const chooseAsActive = (id) => {
  return dispatch => {
    dispatch(request());
    userService.chooseAsActive(id)
      .then(x => {
        if (x.ok) {
          dispatch(success(id));
        } else {
          dispatch(failure(x.errData.toString()));
        }
      },
        error => {
          dispatch(failure(error.toString()));
          dispatch(alertActions.error(error.toString()));
        }
      );
  };

  function request() { return { type: userConstants.MARK_ACTIVE_REQUEST } }
  function success(id) { return { type: userConstants.MARK_ACTIVE_SUCCESS, payload: id } }
  function failure(error) { return { type: userConstants.MARK_ACTIVE_FAILURE, payload: error } }
}


export const userActions = {
  uploadFiles,
  deleteFile,
  getFiles,
  chooseAsReference,
  calcMetric,
  donwloadGraph,
  submitCode,
  chooseAsActive
};