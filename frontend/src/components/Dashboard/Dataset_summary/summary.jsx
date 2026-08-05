function Summary({ analysis }) {

    return (

        <div className="summary-card">

            <h2>Dataset Summary</h2>

            <p>
                <strong>Rows:</strong> {analysis.rows}
            </p>

            <p>
                <strong>Columns:</strong> {analysis.columns}
            </p>

            <p>
                <strong>Target:</strong> {analysis.target}
            </p>

        </div>

    );

}

export default Summary;