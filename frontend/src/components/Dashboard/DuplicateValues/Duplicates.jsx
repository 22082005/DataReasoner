import "./Duplicates.css";

function Duplicates({ duplicates }) {

    const { summary, results } = duplicates;

    return (

        <div className="duplicates-card">

            <h2>Duplicate Values</h2>

            <p>

                <strong>Duplicate Rows :</strong>

                {summary.duplicate_rows}

            </p>

            <p>

                <strong>Duplicate Percentage :</strong>

                {summary.duplicate_percentage}%

            </p>

            <p>

                <strong>Has Duplicates :</strong>

                {summary.has_duplicates ? "Yes" : "No"}

            </p>

            <table>

                <thead>

                    <tr>

                        <th>Duplicate Count</th>

                        <th>Duplicate Percentage</th>

                    </tr>

                </thead>

                <tbody>

                    {results.map((item, index) => (

                        <tr key={index}>

                            <td>{item.duplicate_count}</td>

                            <td>{item.duplicate_percentage}%</td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default Duplicates;