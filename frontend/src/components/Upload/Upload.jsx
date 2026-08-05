import { useState } from "react";
import api from "../../services/api";
import "./Upload.css";
import { useNavigate } from "react-router-dom";

function Upload() {

    const [file, setFile] = useState(null);
    const [columns,setColumns]= useState([]);
    const [target, setTarget] = useState("");
    const navigate = useNavigate();

    const handleFileChange = async (event) => {

        const selectedFile = event.target.files[0];

        if (!selectedFile) {
            return;
        }

        setFile(selectedFile);
        const formData = new FormData();
        formData.append("file", selectedFile);
        try{
            const response =await api.post("/columns",formData,);
            setColumns(response.data.columns)
        }
        catch (error){
            console.error("Error uploading files :",error);

        }
    };
   const handleProceed = async () => {

    if (!file) {

        alert("Please upload a dataset.");

        return;

    }

    const formData = new FormData();

    formData.append("file", file);

    formData.append("target", target);

    try {

        const response = await api.post(
                        "/analyze",
                        formData
                       );

        navigate(

          "/dashboard",

               {

                state: response.data

                }

        );

    }
    catch (error) {

        console.error(error);

    }

};

    return (
        <section className="upload-section">

            <div className="upload-card">

                <div className="upload-icon">
                    ↑
                </div>

                <h2>Upload Your Dataset</h2>

                <p>
                    Choose a CSV file to begin analyzing your data.
                </p>

                <label className="upload-button">

                    Choose CSV

                    <input
                        type="file"
                        accept=".csv"
                        onChange={handleFileChange}
                        hidden
                    />

                </label>

                {file && (

                    <div className="selected-file">

                        <span>Selected file</span>

                        <strong>{file.name}</strong>

                    </div>

                )}
              {columns.length > 0 && (

    <div className="target-section">

        <h3>Target Variable (Optional)</h3>

        <p>
            Leave empty if you only want EDA.
        </p>

        <select
            value={target}
            onChange={(event) =>
                setTarget(event.target.value)
            }
        >

            <option value="">
                Select Target Variable
            </option>

            {columns.map((column) => (

                <option
                    key={column}
                    value={column}
                >
                    {column}
                </option>

            ))}

        </select>

        <button className="proceed-button"  onClick={handleProceed}>
            Proceed
        </button>

    </div>

)}

            </div>

        </section>
    );
}

export default Upload;