import "./MissingValues.css";

function MissingValues({ missing }) {
    const {results}=missing;
    console.log(results);

    return (

        <div className="missing-card">

            <h2>Missing Values</h2>

            <table>

                <thead>

                    <tr>

                        <th>Column</th>

                        <th>Missing</th>

                        <th>Percentage</th>

                    </tr>

                </thead>

                <tbody>

                    {results.map((item, index) => (

                        <tr key={`${item.column_name || "column"}-${index}`}>

                            <td>{item.column_name}</td>

                            <td>{item.missing_count}</td>

                            <td>{item.missing_percentage}%</td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default MissingValues;