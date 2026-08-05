import "./MissingValues.css";

function MissingValues({ missing }) {
    const {summary,results}=missing;
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

                    {missing.results.map((item) => (

                        <tr key={item.column_name}>

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