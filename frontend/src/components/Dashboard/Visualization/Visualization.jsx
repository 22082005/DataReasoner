import ChartRenderer from "./ChartRenders";


function Visualization({ visualization }) {

    if (!visualization) {
        return (
            <div>
                <h2>Visualization</h2>
                <p>No visualization results available.</p>
            </div>
        );
    }

    console.log("Visualization:", visualization);

    // -----------------------------------------
    // Results
    // -----------------------------------------

    const featureVisualizations =
        visualization.results?.feature_visualizations || [];

    const bivariateVisualizations =
        visualization.results?.bivariate_visualizations || [];

    const datasetVisualizations =
        visualization.results?.dataset_visualizations || [];


    return (
        <div>

            <h2>Visualization</h2>

            {/* --------------------------------- */}
            {/* Summary */}
            {/* --------------------------------- */}

            <p>
                Analyzed Features:{" "}
                {visualization.summary?.analyzed_features ?? 0}
            </p>

            <p>
                Feature Visualizations:{" "}
                {visualization.summary?.feature_visualizations ?? 0}
            </p>

            <p>
                Bivariate Visualizations:{" "}
                {visualization.summary?.bivariate_visualizations ?? 0}
            </p>

            <p>
                Dataset Visualizations:{" "}
                {visualization.summary?.dataset_visualizations ?? 0}
            </p>


            {/* ================================= */}
            {/* Feature Visualizations */}
            {/* ================================= */}

            <h3>Feature Visualizations</h3>

            {featureVisualizations.map(
                (item, index) => (

                    <div key={index}>

                        <h4>
                            {item.feature}
                        </h4>

                        <p>
                            Recommended Charts:{" "}
                            {
                                item.statistics
                                    ?.recommended_charts ?? 0
                            }
                        </p>

                        {item.metadata?.charts?.map(
                            (chart, chartIndex) => (

                                <div
                                    key={chartIndex}
                                >

                                    <h4>
                                        {
                                            chart.title ||
                                            chart.chart_type
                                        }
                                    </h4>

                                    <ChartRenderer
                                        chart={chart}
                                    />

                                </div>

                            )
                        )}

                    </div>

                )
            )}


            {/* ================================= */}
            {/* Bivariate Visualizations */}
            {/* ================================= */}

            <h3>
                Bivariate Visualizations
            </h3>

            {bivariateVisualizations.map(
                (chart, index) => (

                    <div key={index}>

                        <h4>
                            {
                                chart.title ||
                                chart.chart_type
                            }
                        </h4>

                        <ChartRenderer
                            chart={chart}
                        />

                    </div>

                )
            )}


            {/* ================================= */}
            {/* Dataset Visualizations */}
            {/* ================================= */}

            <h3>
                Dataset Visualizations
            </h3>

            {datasetVisualizations.map(
                (item, index) => (

                    <div key={index}>

                        <h4>
                            {item.status}
                        </h4>

                        {item.metadata?.charts?.map(
                            (chart, chartIndex) => (

                                <div
                                    key={chartIndex}
                                >

                                    <h4>
                                        {
                                            chart.title ||
                                            chart.chart_type
                                        }
                                    </h4>

                                    <ChartRenderer
                                        chart={chart}
                                    />

                                </div>

                            )
                        )}

                    </div>

                )
            )}

        </div>
    );
}


export default Visualization;