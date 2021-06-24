import { userConstants } from '../constants';


const initialState = {};

export const submissions = (state = initialState, action) => {

  switch (action.type) {
    case userConstants.UPLOAD_FILES_REQUEST: {
      return state;
    }
    case userConstants.UPLOAD_FILES_SUCCESS: {
      const { entry, files } = action.payload;
      const fileAr = Object.keys(files).map(x => ({ id: x, ...files[x] }));
      const task = state.tasks.find(x => x.entry === entry);
      const newTask = task ? { ...task, files: [...task.files, ...fileAr] } : { entry, files: fileAr, inFlight: { status: true, msg: 'DSE id being perfromed' } };
      const tasks = state.tasks.filter(x => x.entry !== entry);
      return {
        ...state,
        tasks: [...tasks, newTask]
      };
    }
    case userConstants.UPLOAD_FILES_FAILURE: {

      const { entry, error } = action.payload;
      const newTasks = state.tasks.filter(task => task.entry !== entry);

      return {
        ...state,
        tasks: newTasks,
        error: error
      };
    }
    case userConstants.DSE_REQUEST: {
      const entry = action.payload;
      const modifiedTasks = state.tasks.map(task => {
        if (task.entry === entry) {
          return { ...task, inFlight: { msg: `DSE of transpiled code is being performed...`, status: true } };
        }
        return task;
      });
      return { ...state, tasks: modifiedTasks };
    }

    case userConstants.DSE_SUCCESS: {
      const { entry, files: dseRes } = action.payload;
      const task = state.tasks.find(task => task.entry === entry);
      const files = task.files.map(file => {
        const dseR = dseRes.find(x => x.id === file.id);
        if (dseR) {
          return { ...file, ...dseR };
        }
        return file;
      });

      const newTask = { ...task, files: files, inFlight: { msg: null, status: false } };
      const tasks = state.tasks.filter(task => task.entry !== entry);
      return { ...state, tasks: [...tasks, newTask] };
    }
    case userConstants.DSE_FAILURE: {
      const { error, entry } = action.payload;
      const modifiedTasks = state.tasks.map(task => {
        if (task.entry === entry) {
          return { ...task, inFlight: { msg: null, status: false } };
        }
        return task;
      });

      return {
        ...state,
        tasks: modifiedTasks,
        error
      };
    }

    case userConstants.FILE_DELETE_REQUEST: {
      return state;
    }
    case userConstants.FILE_DELETE_SUCCESS: {
      const fileId = action.payload;

      const task = state.tasks.find(task => {
        const file = task.files.find(file => {
          return file.id === fileId;
        });
        return file !== undefined;
      });
      const tasks = state.tasks.filter(t => t.entry !== task.entry);
      const files = task.files.filter(file => file.id !== fileId);
      const newTask = { ...task, files };
      return { ...state, tasks: [...tasks, newTask] };
    }
    case userConstants.GETALL_REQUEST: {

      return state;
    }
    case userConstants.GETALL_SUCCESS: {
      const entries = action.payload;
      const newTasks = Object.keys(entries).map(entry => {
        const filesObj = entries[entry];
        const files = Object.keys(filesObj).map(id => ({ id, ...filesObj[id] }))
        return { entry, files };
      });
      return {
        ...state,
        tasks: newTasks
      };
    }
    case userConstants.GETALL_FAILURE: {

      return {
        ...state,
        error: action.payload
      };
    }

    case userConstants.CHOOSE_REFERENCE_REQUEST: {
      const modifiedTasks = state.tasks.map(task => {
        const modifiedFiles = task.files.map(file =>
          ({ ...file, metrics: { ...file.metrics, pse: {}, sse: {}, rs: {} } }));
        return { ...task, files: modifiedFiles };
      });
      return {
        ...state,
        tasks: modifiedTasks
      };
    }
    case userConstants.CHOOSE_REFERENCE_SUCCESS: {
      const { _, id } = action.payload;
      const task = state.tasks.find(task => task.files.find(file => file.id === id));
      const restOfTheTasks = state.tasks.filter(t => t.entry !== task.entry);
      const newFiles = task.files.map(file => {
        if (file.id !== id) {
          return { ...file, isReference: false };
        }
        return { ...file, isReference: true };
      });

      const newTask = { ...task, files: newFiles }
      const newTasks = [...restOfTheTasks, newTask];

      return {
        ...state,
        tasks: newTasks
      };
    }
    case userConstants.CHOOSE_REFERENCE_FAILURE: {
      return {
        ...state,
        error: action.payload
      };
    }
    case userConstants.CALCULATE_METRIC_REQUEST: {
      const name = action.payload.metricType;
      const entry = action.payload.params.entry;
      const modifiedTasks = state.tasks.map(task => {
        if (task.entry === entry) {
          return { ...task, inFlight: { msg: `${name} of transpiled code is being performed...`, status: true } };
        }
        return task;
      })
      return {
        ...state,
        tasks: modifiedTasks
      };
    }
    case userConstants.CALCULATE_METRIC_SUCCESS: {
      console.log(action.payload)
      const { entry, name, data } = action.payload;
      const newTasks = state.tasks.map(task => {
        console.log(task.entry, entry)
        if (task.entry !== entry) return task;
        const newFiles = task.files.map(file => {
          if (data[file.id]) {
            return { ...file, metrics: { ...file.metrics, [name]: data[file.id] } };
          }
          return file;
        });
        return { ...task, files: newFiles, inFlight: { msg: undefined, status: false } };
      });
      return {
        ...state,
        tasks: newTasks
      };
    }
    case userConstants.CALCULATE_METRIC_FAILURE: {
      return {
        ...state,
        error: action.payload
      };
    }
    case userConstants.DOWNLOAD_EXC_IMG_REQUEST: {
      return state;
    }
    case userConstants.DOWNLOAD_EXC_IMG_SUCCESS: {
      return state;
    }
    case userConstants.DOWNLOAD_EXC_IMG_FAILURE: {
      return {
        ...state,
        error: action.payload
      };
    }
    case userConstants.DEBUG_LOG_REQUEST: {
      return state;
    }
    case userConstants.DEBUG_LOG_SUCCESS: {
      const { id, log } = action.payload;
      const newTasks = state.tasks.map((task) => {
        const file = task.files.find(file => file.id === id);
        if (file) {
          const newFile = { ...file, log: log };
          const otherFiles = task.files.filter(file => file.id !== id);
          return { ...task, files: [...otherFiles, newFile] };
        }
        return task;
      });

      return { ...state, tasks: newTasks };
    }
    case userConstants.DEBUG_LOG_FAILURE: {
      return {
        ...state,
        error: action.payload
      };
    }
    case userConstants.SUBMIT_CODE_REQUEST: {
      return state;
    }
    case userConstants.SUBMIT_CODE_SUCCESS: {
      const { id, code } = action.payload;
      const newTasks = state.tasks.map((task) => {
        const files = task.files.map(file => {
          if (file.id === id) {
            return { ...file, code: code, metrics: { pse: 0, rs: 0, sse: 0, cvg: 0 }, isReference: false };
          }
          return file;
        });
        return { ...task, files: files };
      });
      return { ...state, tasks: newTasks };
    }
    case userConstants.SUBMIT_CODE_FAILURE: {
      return {
        ...state,
        error: action.payload
      };
    }
    case userConstants.MARK_ACTIVE_SUCCESS: {
      const id = action.payload;
      const newTasks = state.tasks.map((task) => {
        const files = task.files.map(file => ({ ...file, isActive: (file.id === id) }));
        return { ...task, files: files };
      });

      return { ...state, tasks: newTasks };
    }
    default:
      return state;
  }

};