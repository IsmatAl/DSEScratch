import React from 'react';
import { Card } from 'react-bootstrap';


const CoverageReport = ({ codeAr = [], coveredLines = [], excludedLines = [], missingLines = []}) => {

  const mapLineToColor = (lines, color, lineToColorObj) => lines.reduce((acc, next) => {
    acc[next] = color;
    return acc;
  }, lineToColorObj);

  const lineToColor = [
    [coveredLines, "#ddffdd"],
    [excludedLines, "#eeeeee"],
    [missingLines, "#ffdddd"]]
    .reduce((acc, next) => {
      const [arr, color] = next;
      mapLineToColor(arr, color, acc)
      return acc;
    }, {});

  return <div className="code-coverage">
    <Card>
      <Card.Title style={{ marginBottom: 0 }}>
        <div className='container' >
          <div className='row coverage-stats'>
            <div className='col' style={{ backgroundColor: '#ddffdd' }}>
              <span>{coveredLines.length} run</span>
            </div>
            <div className='col' style={{ backgroundColor: '#ffdddd' }}>
              <span>{missingLines.length} missing</span>
            </div>
            <div className='col' style={{ backgroundColor: '#eeeeee' }}>
              <span>{excludedLines.length} excluded</span>
            </div>
          </div>
        </div>
      </Card.Title>
      {codeAr && codeAr.map((x, i) =>
        <div key={i} className="code-line"
          style={{ backgroundColor: lineToColor[i + 1] }}
        >
          <span>{++i + '.  ' + x}</span>
        </div>
      )}
    </Card>
  </div >
};

// const mapStateToProps = (state) => ({
//   generatedInputs: state.DSE.generatedInputs,
//   returnVals: state.DSE.returnVals
// });

// const mapDispatchToProps = (dispatch) => ({
//   generatedInputs: ,
//   returnVals: state.DSE.returnVals
// });

export default CoverageReport;
