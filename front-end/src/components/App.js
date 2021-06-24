import React, { useEffect } from 'react';
import '../css/index.css'
import Result from './Result';
import AnalysisResult from './AnalysisResult';

import PageTitle from './PageTitle';
import Header from './Header';
import { ConnectedRouter } from 'connected-react-router';
import { Route } from 'react-router-dom';
import { v4 as uuid } from 'uuid'
import { userActions } from '../actions';
import { connect } from 'react-redux';



const App = ({ history, onPageRelaod }) => {
  useEffect(() => {
    const handlePageReload = async () => {
      await onPageRelaod();
    };


    handlePageReload();

  }, [onPageRelaod]);

  return (
    <ConnectedRouter history={history}>
      <div className='app'>
        <Header />
        <div className='app-body-content'>
          <PageTitle titleText='Submission' />
          <Route exact path="/submissions/:submissionId" render={(props) => <AnalysisResult {...props} key={uuid()} />} />
          <Route path="/" component={Result} />
        </div>
      </div>
    </ConnectedRouter>
  );
};


const mapStateToProps = (state, ownProps) => ({
  history: ownProps.history,
});

const mapPropsToProps = {
  onPageRelaod: userActions.getFiles
};

export default connect(mapStateToProps, mapPropsToProps)(App);
