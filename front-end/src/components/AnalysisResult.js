import React
  from 'react';
import ProgressPieChart from './ProgressPieChart';
import { connect } from 'react-redux';
import {
  Card, Accordion, Button, Table
} from 'react-bootstrap';

import LogInfo from './LogInfo';
import PyEditor from './PyAceEditor';
import CoverageReport from './CoverageReport';
import { getFileById, reformatMetricData } from '../reducer';
import { userActions } from '../actions';



const AnalysisResult = ({ params, inputs, outputs, id, debugLog, metrics, isReference, code, donwloadGraph, onPageRelaod, submitCode }) => {

  const pse = reformatMetricData({ ...metrics['pse'], type: 'pse' });
  const sse = reformatMetricData({ ...metrics['sse'], type: 'sse' });
  const rs = reformatMetricData({ ...metrics['rs'], type: 'rs' });
  const codeCoverage = reformatMetricData({ ...metrics['cvg'], type: 'cvg' });

  return <div>
    <div className="container">
      <Card>
        <Card.Body>
          <div id="se-metrics" className="row">

            <div className="col">
              <Card className="text-center">
                <Card.Body>
                  <Card.Title>Paired-program Symbolic Execution</Card.Title>
                  <br />
                  {pse && <ProgressPieChart
                    data={pse['data']} content={pse['content']} color="#1890ff"
                  />}
                </Card.Body>
              </Card>
            </div>
            <div className="col">
              <Card className="text-center code-coverage">
                <Card.Body>
                  <Card.Title>inputs and outputs used for PSE</Card.Title>
                  <br />
                  <Table
                    responsive striped hover cellSpacing="0" width="100%">
                    <thead>
                      <tr>
                        {params.map((param, i) => {
                          return <th key={i}>
                            {param}
                          </th>;
                        })}
                        <th >Y/N
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      {pse.inputs?.map((input, idx) => {
                        return <tr key={idx}>
                          {input.map((arg, i) => <td key={i}>{arg}</td>)}
                          <td>{pse.outputs[idx] ? 1 : 0}</td>
                        </tr>;
                      })}
                    </tbody>
                  </Table>
                </Card.Body>
              </Card>
            </div>

          </div>
        </Card.Body>
      </Card>
    </div>
    <div className="container">
      <Card>
        <Card.Body>
          <div id="se-metrics" className="row">

            <div className="col">
              <Card className="text-center">
                <Card.Body>
                  <Card.Title>Random Sampling</Card.Title>
                  <br />
                  {rs && <ProgressPieChart
                    data={rs['data']}
                    content={rs['content']}
                    color="#facc14"
                  />}
                </Card.Body>
              </Card>
            </div>
            <div className="col">
              <Card className="text-center code-coverage">
                <Card.Body>
                  <Card.Title>inputs and outputs used for RS</Card.Title>
                  <br />
                  <Table
                    responsive striped hover cellSpacing="0" width="100%">
                    <thead>
                      <tr>
                        {params.map((param, i) => {
                          return <th key={i}>
                            {param}
                          </th>;
                        })}
                        <th >ref output
                        </th>
                        <th >output
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      {rs.inputs?.map((input, idx) => {
                        return <tr key={idx}>
                          {input.map((arg, i) => <td key={i}>{arg}</td>)}
                          {rs.outputs[idx]?.map((output, i) => <td key={i}>{output}</td>)}
                        </tr>;
                      })}
                    </tbody>
                  </Table>
                </Card.Body>
              </Card>
            </div>

          </div>
        </Card.Body>
      </Card>
    </div>
    <div className="container">
      <Card>
        <Card.Body>
          <div id="se-metrics" className="row">
            <div className="col">
              <Card className="text-center">
                <Card.Body>
                  <Card.Title>Single-program Symbolic Execution</Card.Title>
                  <br />
                  {sse && <ProgressPieChart
                    data={sse['data']} content={sse['content']} color="#2fc25b"
                  />}
                </Card.Body>
              </Card>
            </div>
            <div className="col">
              <Card className="text-center code-coverage">
                <Card.Body>
                  <Card.Title>inputs and outputs used for SSE</Card.Title>
                  <br />
                  <Table
                    responsive striped hover cellSpacing="0" width="100%">
                    <thead>
                      <tr>
                        {params.map((param, i) => {
                          return <th key={i}>
                            {param}
                          </th>;
                        })}
                        <th >ref output
                        </th>
                        <th >output
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      {sse.inputs?.map((input, idx) => {

                        return <tr key={idx}>
                          {input.map((arg, i) => <td key={i}>{arg}</td>)}
                          <td>{sse['refOutputs'][idx]}</td>
                          <td>{sse.outputs[idx]}</td>
                        </tr>;
                      })}
                    </tbody>
                  </Table>
                </Card.Body>
              </Card>
            </div>

          </div>
        </Card.Body>
      </Card>
    </div>
    {codeCoverage && <div className="container">
      <Card>
        <Card.Body>
          <div className="row">
            <div className="col">
              <CoverageReport
                missingLines={codeCoverage['missing_lines']}
                codeAr={code.split('\n')}
                excludedLines={codeCoverage['excluded_lines']}
                coveredLines={codeCoverage['executed_lines']} />
            </div>
            <div className="col">

              <Card className="text-center">
                <Card.Body>
                  <Card.Title>Code Coverage</Card.Title>
                  <br />
                  <ProgressPieChart
                    data={codeCoverage['data']}
                    content={codeCoverage['content']}
                    intervalConfig={{
                      style: { fillOpacity: 0.6 }
                    }}
                  />
                </Card.Body>
              </Card>
            </div>

          </div>
          <div className="row">
            <Card className="text-center code-coverage">
              <Card.Body>
                <Card.Title>DSE generated inputs and its outputs</Card.Title>
                <br />
                <Table
                  responsive striped hover cellSpacing="0" width="100%">
                  <thead>
                    <tr>
                      {params.map((param, i) => {
                        return <th key={i}>
                          {param}
                        </th>;
                      })}
                      <th >output
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    {inputs.map((input, idx) => {
                      return <tr key={idx}>
                        {input.map((arg, i) => <td key={i}>{arg}</td>)}
                        <td>{outputs[idx]}</td>
                      </tr>;
                    })}
                  </tbody>
                </Table>
              </Card.Body>
            </Card>
          </div>
        </Card.Body>
      </Card>
    </div>
    }
    <div className="container" >
      <PyEditor id={id} onSubmitCode={submitCode} code={code} />
    </div>
    <div className="container" >
      <Card>
        <Card.Body>
          <div className="row" >
            <div className="col">
              <Accordion>
                <Card>
                  <Accordion.Toggle as={Card.Header} variant="link" eventKey="0">
                    {'> DSE debug info'}
                  </Accordion.Toggle>
                  <Accordion.Collapse eventKey="0">
                    <Card.Body>
                      <LogInfo debugInfo={debugLog}></LogInfo>
                    </Card.Body>
                  </Accordion.Collapse>
                </Card>
              </Accordion>
            </div>
          </div>
        </Card.Body>
      </Card>
    </div>
    <div className="container" >
      <Card>
        <Card.Body>

          <div className="row">
            <div className="col">
              <Button variant="primary" onClick={() => donwloadGraph(id)}>
                Download DSE graph
              </Button>
            </div>
          </div>
        </Card.Body>
      </Card>
    </div>
  </div>
};



const mapStateToProps = (state, ownProps) => {
  const submissionId = ownProps.match.params.submissionId;
  const file = getFileById(submissionId, state.submissions.tasks);
  return {
    id: submissionId,
    debugLog: file['logs'].split('\n'),
    metrics: file['metrics'],
    isReference: file['isReference'],
    code: file['code'],
    inputs: file['inputs'],
    outputs: file['outputs'],
    params: file['params']
  };
};


const mapPropsToProps = {
  donwloadGraph: userActions.donwloadGraph,
  onPageRelaod: userActions.getFiles,
  submitCode: userActions.submitCode
};


export default connect(mapStateToProps, mapPropsToProps)(AnalysisResult);
