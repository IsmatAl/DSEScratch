import React from 'react';

import { Table, Button } from 'react-bootstrap';
import { connect } from 'react-redux';

import { userActions } from '../actions';
import { Link } from 'react-router-dom';

import LoadingOverlay from 'react-loading-overlay';


const SubmissionTable = ({
  task,
  onChooseRef,
  onClickX,
  calcMetric,
  chooseAsActive
}) => {
  const { entry, files } = task;

  const reference = files.find(file => file['isReference']);
  const rest = files.filter(file => !file['isReference']);

  const formRow = (x, idx, onChooseRef) => {
    const metrics = x['metrics'];
    return <tr
      key={idx}
      id={x['id']}
      style={{
        backgroundColor: x['isReference'] ? 'ActiveCaption' : x['isActive'] ? 'goldenrod' : 'InfoBackground',
        color: x['isReference'] ? 'white' : 'black'
      }}
    >
      <td>{x['fileName']}</td>
      <td>{metrics['pse']?.percent}</td>
      <td>{metrics['sse']?.percent}</td>
      <td>{metrics['rs']?.percent}</td>
      <td>{metrics['cvg']?.summary?.percent_covered}</td>
      <td>
        <div className="submission-actions">
          {x['isReference'] ? <Button variant="primary"
            onClick={() => onChooseRef(x['id'])}
            disabled
          >
            Ref
          </Button> :
            <Button variant="primary"
              onClick={() => onChooseRef(x['id'])}
            >
              Ref
            </Button>
          }


          {!x['isActive'] ? <Button variant="danger"
            onClick={() => onClickX(x['id'])}
          >
            Del
          </Button> : <Link to={`/`}>
            <Button variant="danger" onClick={() => onClickX(x['id'])}>
              Del
            </Button>
          </Link>
          }
          {!x['isActive'] ?
            <Link to={`/submissions/${x['id']}`}
            // target="_blank"
            // rel="noopener noreferrer"
            >
              <Button variant="info" onClick={() => {
                chooseAsActive(x['id']);
              }}>
                More
              </Button>
            </Link> : <Button variant="info" disabled>
              More
            </Button>
          }
        </div>
      </td>
    </tr>;
  };

  return <div>
    <LoadingOverlay
      active={task.inFlight?.status}
      spinner
      text={task.inFlight?.msg}
    >
      <div>
        <Table
          responsive striped hover cellSpacing="0" width="100%">
          <thead>
            <tr>
              <th >File Name
              </th>
              <th >PSE
              </th>
              <th >SSE
              </th>
              <th >RS
              </th>
              <th >Code coverage
              </th>
              <th >Actions
              </th>
            </tr>
          </thead>
          <tbody>
            {reference && formRow(reference, 0, onChooseRef)}
            {rest.map((x, idx) => formRow(x, ++idx, onChooseRef))}
          </tbody>
        </Table>

        <div className="submission-actions">
          {reference &&
            <Button variant="primary"
              onClick={() => calcMetric({
                metricType: 'pse', params: {
                  entry: entry,
                  max_iter: 2
                }
              })}
            >
              PSE
            </Button>}
          {reference &&
            <Button variant="primary"
              onClick={() => {
                calcMetric({ metricType: 'sse', params: { entry, refId: reference['id'] } });
              }}

            >
              SSE
            </Button>}
          {reference &&
            <Button variant="primary"
              onClick={() => calcMetric({ metricType: 'rs', params: { entry } })}

            >
              RS
            </Button>}
          <Button variant="primary"
            onClick={() => calcMetric({ metricType: 'cvg', params: { entry } })}
          >
            CVG
          </Button>
        </div>
      </div>
    </LoadingOverlay>
  </div>;
};


const mapStateToProps = (state, ownProps) => ({
  task: ownProps.task
});


const mapPropsToProps = {
  onCheck: userActions.uploadFiles,
  onClickX: userActions.deleteFile,
  onChooseRef: userActions.chooseAsReference,
  calcMetric: userActions.calcMetric,
  chooseAsActive: userActions.chooseAsActive,
};


export default connect(mapStateToProps, mapPropsToProps)(SubmissionTable);