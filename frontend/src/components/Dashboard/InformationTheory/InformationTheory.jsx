import "./InformationTheory.css";

function InformationTheory({ informationTheory }) {

    if (!informationTheory) {
        return null;
    }

    const { summary, results } = informationTheory;

    return (
        <div className="information-card">

            <h2>Information Theory</h2>

            <div className="information-summary">

                <div>
                    <strong>Target</strong>
                    <span>{summary.target}</span>
                </div>

                <div>
                    <strong>Analyzed Features</strong>
                    <span>{summary.analyzed_features}</span>
                </div>

                <div>
                    <strong>Informative Features</strong>
                    <span>{summary.informative_features}</span>
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
                            <th>Status</th>
                            <th>Mutual Information</th>
                            <th>Entropy</th>
                            <th>Information Gain</th>
                        </tr>

                    </thead>

                    <tbody>

                        {results.map((item, index) => (

                            <tr key={index}>

                                <td>{item.entity_1}</td>

                                <td>{item.entity_2}</td>

                                <td>{item.status}</td>

                                <td>
                                    {item.statistics.mutual_information}
                                </td>

                                <td>
                                    {item.statistics.entropy ?? "-"}
                                </td>

                                <td>
                                    {item.statistics.information_gain ?? "-"}
                                </td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            )}

        </div>
    );
}

export default InformationTheory;