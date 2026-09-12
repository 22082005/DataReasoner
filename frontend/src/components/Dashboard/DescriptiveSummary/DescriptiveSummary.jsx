import "./DescriptiveSummary.css";

function DescriptiveSummary({ descriptive }) {

    if (!descriptive || descriptive.length === 0) {

        return null;

    }

    return (

        <div className="descriptive-card">

            <h2>Descriptive Statistics</h2>

            <table>

                <thead>

                    <tr>

                        <th>Column</th>
                        <th>Mean</th>
                        <th>Median</th>
                        <th>Std Dev</th>
                        <th>Variance</th>
                        <th>Min</th>
                        <th>Max</th>

                    </tr>

                </thead>

                <tbody>

                    {descriptive.map((item) => (

                        <tr key={item.column_name}>

                            <td>{item.column_name}</td>

                            <td>{item.mean}</td>

                            <td>{item.median}</td>

                            <td>{item.standard_deviation}</td>

                            <td>{item.variance}</td>

                            <td>{item.minimum}</td>

                            <td>{item.maximum}</td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default DescriptiveSummary;