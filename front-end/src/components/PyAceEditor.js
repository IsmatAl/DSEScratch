import React, { useState } from "react";
import AceEditor from "react-ace";

import "ace-builds/src-noconflict/mode-java";
import "ace-builds/src-noconflict/theme-github";
import 'brace/ext/language_tools';
import 'brace/theme/monokai';
import 'brace/theme/github';
import { Button, Card } from 'react-bootstrap';



const PyEditor = ({ id, code, onSubmitCode }) => {
  const [editable, setEditable] = useState(false);
  const [pyCode, setPyCode] = useState(code);



  const handleCodeChange = (modifiedCode) => {
    setPyCode(modifiedCode);
  }


  return <Card>
    <Card.Body>
      <Card.Title>Scratch code converted to Python</Card.Title>
      <div className='row'>
        {!editable ? <AceEditor
          width="100%"
          readOnly
          mode="python"
          name="pycodeEditor"
          theme="github"
          fontSize={14}
          showPrintMargin={false}
          showGutter={false}
          highlightActiveLine={false}
          value={pyCode}
          setOptions={{
            useSoftTabs: false,
            enableSnippets: false,
            showLineNumbers: false,
            tabSize: 4,
            maxLines: Infinity
          }}
        /> : <AceEditor
          width="100%"
          placeholder="Placeholder Text"
          mode="python"
          theme="monokai"
          name="pycodeEditor"
          onChange={handleCodeChange}
          fontSize={14}
          showPrintMargin={true}
          showGutter={true}
          highlightActiveLine={true}
          value={pyCode}
          setOptions={{
            useSoftTabs: false,
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true,
            enableSnippets: true,
            showLineNumbers: true,
            maxLines: Infinity,
            tabSize: 4,
          }} />}
      </div>
      <div className='row'>
        {!editable ?
          <div className="code-editor-buttons">
            <Button
              variant="primary"
              onClick={() => setEditable(true)}
            >
              Edit
            </Button>
          </div> :
          <div className="code-editor-buttons">
            <Button
              variant="primary"
              onClick={() => setEditable(false)}
            >
              Cancel
            </Button>
            <Button
              variant="secondary"
              onClick={() => {
                onSubmitCode({ id, code: pyCode });
                setEditable(false);
              }}
            >
              Save
            </Button>
          </div>}
      </div>
    </Card.Body>
  </Card>;
}
export default PyEditor;
