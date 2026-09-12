import "./Outliers.css";

function Outliers({ outliers }) {

    if (!outliers) {
        return null;
    }

    const { summary, results } = outliers;

    return (

        <div className="outliers-card">

            <h2>Outlier Detection</h2>

            <div className="outliers-summary">

                <div>
                    <strong>Analyzed Features</strong>
                    <span>{summary.analyzed_features}</span>
                </div>

                <div>
                    <strong>Columns With Outliers</strong>
                    <span>{summary.columns_with_outliers}</span>
                </div>

                <div>
                    <strong>Total Outliers</strong>
                    <span>{summary.total_outliers}</span>
                </div>

                <div>
                    <strong>Has Outliers</strong>
                    <span>
                        {summary.has_outliers ? "Yes" : "No"}
                    </span>
                </div>

            </div>

            <table>

                <thead>

                    <tr>
                        <th>Feature</th>
                        <th>Status</th>
                        <th>Count</th>
                        <th>Percentage</th>
                        <th>Method</th>
                        <th>Reason</th>
                    </tr>

                </thead>

                <tbody>

                    {results.map((item) => (

                        <tr key={item.feature}>

                            <td>{item.feature}</td>

                            <td>{item.status}</td>

                            <td>{item.count}</td>

                            <td>{item.percentage}%</td>

                            <td>{item.details.method}</td>

                            <td>{item.details.reason}</td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>
    );
}

export default Outliers;