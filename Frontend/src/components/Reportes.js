import { Graphviz } from 'graphviz-react';

import React from 'react'

export default function Reportes() {
    return (
        <div>
            <Graphviz dot={`graph {
                grandparent -- "parent A";
                child;
                "parent B" -- child;
                grandparent --  "parent B";
            }`} />
        </div>
    )
}
