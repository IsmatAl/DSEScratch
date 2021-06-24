import { combineReducers } from 'redux';
import { submissions } from './user.reducer';
import { connectRouter } from 'connected-react-router';

export default (history) => combineReducers({
  router: connectRouter(history),
  submissions: submissions
});

export const getFileById = (id, tasks) => {
  const file = tasks.reduce((acc, task) => {
    const file = task.files.find(file => file.id === id);
    return file || acc
  }, undefined);
  return file;
};

export const reformatMetricData = (metricData) => {
  let title = null;
  switch (metricData.type) {
    case 'cvg':
      title = '% of covered lines'
      break;

    default:
      title = "% of agreed test cases"
      break;
  }
  const percent = metricData?.percent || metricData?.summary?.percent_covered;
  const data = [
    { type: "Completed", percent: percent },
    { type: "To be improved", percent: 100 - percent },
  ];
  const content = {
    title: title,
    percent: `${percent || 0}%`,
  };
  return metricData === 0 ? undefined : { ...metricData, data, content };
};


export const isDSEInProgress = (tasks) => {
  if (tasks?.find((task) => task.inFlight?.status)) return true;
  return false;
};