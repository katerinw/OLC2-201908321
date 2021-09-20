import React, { useRef, useState } from 'react';
import Editor from "@monaco-editor/react";
import { Divider, Grid, Image, Segment,Button } from 'semantic-ui-react'



export default function Consolas() {
    const editorRef = useRef(null);
    const [text, setText] = useState("");

    function handleEditorDidMount(editor, monaco) {
        editorRef.current = editor;
    }

    function segundaConsola() {
        let jsonCodigo = JSON.stringify({codigo:editorRef.current.getValue()})
        console.log(jsonCodigo)
    
          const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ codigo:editorRef.current.getValue() })
        };
        fetch('http://localhost:4000/compiler', requestOptions)
            .then(response => response.json())
            .then(data => setText(data.salida));
      }

    return (
        <Segment>
            <Grid columns={2} relaxed='very'>
                <Grid.Column>
                    <Button onClick={segundaConsola} content='Click Here' />
                    <Editor
                        height="90vh"
                        defaultLanguage="julia"
                        theme="vs-dark"
                        onMount={handleEditorDidMount}
                    />
                </Grid.Column>
                <Grid.Column>
                    <Editor
                        height="90vh"
                        defaultLanguage="julia"
                        theme="vs-dark"
                        value={text}
                        options={{
                            readOnly: true, minimap: {enable:false,}
                            }}
                    />
                </Grid.Column>
            </Grid>

            <Divider vertical></Divider>
        </Segment>

    );
}

