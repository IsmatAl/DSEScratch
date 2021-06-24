import React, { useState } from 'react';
import { connect } from 'react-redux';
import { userActions } from '../actions';

import {
  Form, FormGroup, FormLabel, FormControl, FormText, Card, Button, InputGroup
} from 'react-bootstrap';
import { isDSEInProgress } from '../reducer';



const FileForm = (props) => {
  const [validated, setValidated] = useState(false);
  const [state, setState] = useState({
    files: [],
    functionName: undefined
  });

  const handleFileChange = event => {
    setState({ ...state, files: [...event.target.files] });
  };


  const handleNameInputChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setState({
      ...state,
      [name]: value
    })
  };


  const handleSubmit = (event) => {
    const form = event.currentTarget;
    event.preventDefault();
    if (form.checkValidity() === false) {
      event.stopPropagation();
    } else {
      const formData = new FormData();
      state.files.forEach((file) => {
        formData.append(
          "files",
          file
        )
      });
      formData.append('entry', state.functionName);
      props.onFileUpload(formData, state.functionName);
    }

    setValidated(true);
  };

  return (<div className="container">
    <Card>
      <Card.Body>
        <Card.Title>Upload projects</Card.Title>

        <Form noValidate validated={validated} onSubmit={handleSubmit}>
          <InputGroup hasValidation>
            <FormGroup controlId="formBasicEmail">
              <FormLabel>Function Name</FormLabel>
              <FormControl
                type="text"
                placeholder="Enter function name"
                name="functionName"
                onChange={handleNameInputChange} required />
              <FormText className="text-muted">
                *Required. Name of the function to measure metrics for
              </FormText>
              <Form.Control.Feedback type="invalid">
                Please enter method name
              </Form.Control.Feedback>
            </FormGroup>
          </InputGroup>
          <InputGroup hasValidation>
            <FormGroup controlId="formFileMultiple" className="mb-3">
              <FormLabel>File upload</FormLabel>
              <FormControl type="file" multiple onChange={handleFileChange} required />
              <Form.Control.Feedback type="invalid">
                Please upload project json file
              </Form.Control.Feedback>
            </FormGroup>
          </InputGroup>
          {props.dseProgressing ? <Button variant="primary"
            type="submit"
            disabled
          >
            Upload
          </Button> : <Button variant="primary"
            type="submit"
          >
            Upload
          </Button>}
        </Form>
      </Card.Body>
    </Card>
  </div>)
};

const mapStateToProps = (state) => ({
  dseProgressing: isDSEInProgress(state.submissions.tasks)
});

const mapPropsToProps = {
  onFileUpload: userActions.uploadFiles
};


export default connect(mapStateToProps, mapPropsToProps)(FileForm);
