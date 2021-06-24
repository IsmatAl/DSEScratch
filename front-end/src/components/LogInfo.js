import React from 'react';

const LogInfo = ({ debugInfo = [] }) => {
  return <div className="debug-container">
    {debugInfo && debugInfo.map((x, i) => <div key={i} className="debug-line">
      {x}
    </div>)}
  </div>
};

export default LogInfo;
