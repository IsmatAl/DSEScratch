import React from 'react';
import SubmissionTable from './SubmissionTable';
import FileForm from './FileForm';
import { Card } from 'react-bootstrap';
import { connect } from 'react-redux';


const Result = ({ tasks }) => {
  return <div>
    {tasks && tasks.map((task, idx) => {
      if (task.files.length === 0) return <div key={idx}></div>;
      const entry = task.entry;
      return <div className="container" key={idx}>
        <Card>
          <Card.Body>
            <Card.Title>Submissions for task: {entry}</Card.Title>
            <div className="row">
              <SubmissionTable task={task} />
            </div>
          </Card.Body>
        </Card>
      </div>
    })}
    <FileForm />
  </div>;
}

const mapStateToProps = (state) => ({
  tasks: state.submissions.tasks
});


const mapPropsToProps = undefined;

export default connect(mapStateToProps, mapPropsToProps)(Result);
