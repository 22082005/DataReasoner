import { useLocation } from "react-router-dom";

import Summary from "../components/Dashboard/Dataset_summary/Summary";
import Schema from "../components/Dashboard/Schema/schema";
import MissingValues from "../components/Dashboard/MissingValues/MissingValues";
import Duplicates from "../components/Dashboard/DuplicateValues/Duplicates";
import DescriptiveSummary from "../components/Dashboard/DescriptiveSummary/DescriptiveSummary";
import Correlation from "../components/Dashboard/Correlation/Correlation";
import Outliers from "../components/Dashboard/Outliers/Outliers";
import HypothesisTesting from "../components/Dashboard/HypothesisTesting/HypothesisTesting";
import InformationTheory from "../components/Dashboard/InformationTheory/InformationTheory";
import Visualization from "../components/Dashboard/Visualization/Visualization";
function Dashboard() {

    const location = useLocation();

    const analysis = location.state;
    console.log(analysis.information)
    console.log(
    "VISUALIZATION:",
    analysis.visualization
);

    return (

        <div>

            <h1>DataReasoner Dashboard</h1>

            <Summary analysis={analysis} />
            <Schema schema={analysis.schema} />
            <MissingValues
             missing={analysis.missing}
             />
            <Duplicates duplicates={analysis.duplicates} />
            <DescriptiveSummary descriptive={analysis.descriptive_summary}/>
            <Correlation correlation={analysis.correlation} />
            <Outliers outliers={analysis.outliers} />
            <HypothesisTesting hypothesis={analysis.hypothesis_testing} />
            <InformationTheory informationTheory={analysis.information_theory} />
            <Visualization
                visualization={
                    analysis.visualization
                }
            />

        </div>

    );

}

export default Dashboard;