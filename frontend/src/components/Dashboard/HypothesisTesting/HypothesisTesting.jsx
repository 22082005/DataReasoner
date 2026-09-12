import "./HypothesisTesting.css";

function HypothesisTesting({ hypothesis }) {

    if (!hypothesis) {
        return null;
    }

    const { summary, results } = hypothesis;

    return (

        <div className="hypothesis-card">

            <h2>Hypothesis Testing</h2>

            <div className="hypothesis-summary">

                <div>
                    <strong>Target</strong>
                    <span>{summary.target}</span>
                </div>

                <div>
                    <strong>Analyzed Features</strong>
                    <span>{summary.analyzed_features}</span>
                </div>

                <div>
                    <strong>Significant Features</strong>
                    <span>{summary.significant_features}</span>
                </div>

                <div>
                    <strong>Target Detected</strong>
                    <span>
                        {summary.target_detected ? "Yes" : "No"}
                    </span>
                </div>

            </div>

            {results && results.length > 0 && (

                <table>

                    <thead>

                        <tr>
                            <th>Feature</th>
                            <th>Target</th>
                            <th>Test</th>
                            <th>Statistic</th>
                            <th>P-Value</th>
                            <th>Alpha</th>
                            <th>Status</th>
                        </tr>

                    </thead>

                    <tbody>

                        {results.map((item, index) => (

                            <tr key={index}>

                                <td>{item.entity_1}</td>

                                <td>{item.entity_2}</td>

                                <td>{item.statistics.method}</td>

                                <td>{item.statistics.statistic}</td>

                                <td>{item.statistics.p_value}</td>

                                <td>{item.statistics.alpha}</td>

                                <td>{item.status}</td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            )}

        </div>
    );
}

export default HypothesisTesting;