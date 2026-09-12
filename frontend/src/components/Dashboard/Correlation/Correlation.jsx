import "./Correlation.css";

function Correlation({ correlation }) {

    if (!correlation) {
        return null;
    }

    const { summary, results } = correlation;
    console.log("Correlation results:", results);
    console.log("Statistics:", results[0].statistics);

    return (
        <div className="correlation-card">

            <h2>Correlation Analysis</h2>

            <div className="correlation-summary">

                <div>
                    <strong>Analyzed Pairs</strong>
                    <span>{summary.analyzed_pairs}</span>
                </div>

                <div>
                    <strong>Highly Correlated Pairs</strong>
                    <span>{summary.highly_correlated_pairs}</span>
                </div>

                <div>
                    <strong>High Correlation</strong>
                    <span>
                        {summary.has_high_correlation ? "Yes" : "No"}
                    </span>
                </div>

            </div>

            {results && results.length > 0 && (

                <table>

    <thead>

        <tr>

            <th>Feature</th>
            <th>Related Feature</th>
            <th>Method</th>
            <th>Correlation</th>
            <th>P-Value</th>
            <th>Status</th>

        </tr>

    </thead>

    <tbody>

        {results.map((item, index) => (

            <tr key={index}>

                <td>{item.feature}</td>

                <td>{item.statistics.related_feature}</td>

                <td>{item.statistics.method}</td>

                <td>{item.statistics.correlation}</td>

                <td>{item.statistics.p_value}</td>

                <td>{item.status}</td>

            </tr>

        ))}

    </tbody>

</table>

            )}

        </div>
    );
}

export default Correlation;