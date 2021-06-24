// import React from 'react';
// import { connect } from 'react-redux';
// import {
//     pexTest,
//     startDSE
// } from '../actions/dse';


// const DSE = ({ pexMsg, generatedInputs, startDSE }) => <div>
//     <h1>{pexMsg}</h1>
//     <div onClick={startDSE}>
//         perfrom DSE
//     </div>
//     {generatedInputs && <div>
//         {generatedInputs.map((x, idx) => <div key={idx}>
//             <div>{x[0]}</div>
//             <div>{x[1]}</div>
//         </div>)}
//     </div>}
// </div>;

// const mapStateToProps = (state) => ({
//     generatedInputs: state.DSE.generatedInputs,
//     returnVals: state.DSE.returnVals
// });

// export default connect(mapStateToProps, { pexTest, startDSE })(DSE);
