import React from 'react';
import { Card } from 'react-bootstrap';

const PageTitle = ({ titleText }) => {
  return <div className="container">
    <Card>
      <Card.Body>
        <Card.Title className="text-center">{titleText}</Card.Title>
      </Card.Body>
    </Card>
  </div>
};


export default PageTitle;
