import "./Schema.css";

function Schema({ schema }) {

    return (

        <div className="schema-card">

            <h2>Schema</h2>

            <table>

                <thead>

                    <tr>

                        <th>Column</th>

                        <th>Type</th>

                        <th>Role</th>

                        <th>Analysis</th>

                    </tr>

                </thead>

                <tbody>

                    {schema.map((column) => (

                        <tr key={column.column_name}>

                            <td>{column.column_name}</td>

                            <td>{column.type}</td>

                            <td>{column.semantic_role}</td>

                            <td>

                                {column.use_for_analysis
                                    ? "✓"
                                    : "✗"}

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default Schema;