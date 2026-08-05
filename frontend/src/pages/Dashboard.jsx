import { useLocation } from "react-router-dom";

import Summary from "../components/Dashboard/Dataset_summary/Summary";
import Schema from "../components/Dashboard/Schema/schema";
import MissingValues from "../components/Dashboard/MissingValues/MissingValues";
import Duplicates from "../components/Dashboard/DuplicateValues/Duplicates";


function Dashboard() {

    const location = useLocation();

    const analysis = location.state;

    return (

        <div>

            <h1>DataReasoner Dashboard</h1>

            <Summary analysis={analysis} />
            <Schema schema={analysis.schema} />
            <MissingValues
             missing={analysis.missing}
             />
            <Duplicates duplicates={analysis.duplicates} />

        </div>

    );

}

export default Dashboard;