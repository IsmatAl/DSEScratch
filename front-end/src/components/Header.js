import React from 'react';
import logo from '../img/UT_logo_transparent.png';
import { Jumbotron } from 'react-bootstrap';

const Header = () => {
  return <div className="app-header">
    <Jumbotron className='app-header-text-container'>
      <div className="app-header-text elegantshd">
        <div className='app-header-text--value'>
          <img
            src={logo}
            width="120"
            className="d-inline-block align-top"
            alt="University of Tartu logo"
          />
        </div>
        <div className='app-header-text--title'>
          <div>
            <div>
              <h5>Thesis topic:</h5>
            </div>
          </div>
          <div>
            <div>
              <span>Student:</span>
            </div>
          </div>
          <div>
            <div>
              <span>Supervisor:</span>
            </div>
          </div>
        </div>
        <div className='app-header-text--value'>
          <div>
            <div>
              <h5>Dynamic analysis of Scratch project to infer CT skills</h5>
            </div>
          </div>
          <div>
            <div>
              <span>Ismat Alakbarov</span>
            </div>
          </div>
          <div>
            <div>
              <span>ASST PROFESSOR Marcello Sarini</span>
            </div>
          </div>
        </div>
      </div>
    </Jumbotron>

  </div>

}


export default Header;
