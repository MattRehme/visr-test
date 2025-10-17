from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware ##TEST
from fastapi.staticfiles import StaticFiles ##TEST
from io import BytesIO
from netcdf_utils import *
from pathlib import Path
import numpy as np 
import os

# import pyarrow as pa
import io






app = FastAPI()


##TEST Allow the browser to access the server directly for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)







##TODO Change this to CREDIT output dir
NETCDF_DIR = "./data"



@app.get("/get_data")
def get_data():

# def get_data(netcdf_file, variable_name, timestep, level):
    ## TODO Get these from client ->
    netcdf_file = "Q_pred_2025-07-02T00Z_001.nc"
    variable_name = 'Q'
    timestep = 0
    level = 0
    netcdf_path = Path(NETCDF_DIR, netcdf_file)

    netcdf_data = netcdf_reader(netcdf_path)

    if variable_name == 'M':
        u = get_variable_data(netcdf_data, 'U', timestep, level) 
        v = get_variable_data(netcdf_data, 'V', timestep, level) 
        variable_data = np.sqrt(u**2 + v**2)

    else:
        variable_data = get_variable_data(
                    netcdf_data, variable_name, timestep, level) 





    #-- Send NumPy Array ------------------------------------------------------

    # arrayBuffer = io.BytesIO()
    # np.save(arrayBuffer, variable_data)
    # arrayBuffer.seek(0)

    # return StreamingResponse(
        # arrayBuffer,
        # media_type="application/octet-stream"
    # )






    #-- Send JSON -------------------------------------------------------------

    test_data = {
            "variable name:": variable_name,
            "netcdf file:": netcdf_file,
            "some values:": variable_data.flatten().tolist()[0:10]
            # "1": 1
    }

    return test_data















    """
    #-- Send array with Apache Arrow ------------------------------------------

    # NOTE Might be able to send Zarr files directly from
        # CREDIT output to the client


    stream = io.BytesIO()

    table = pa.table({'variable_data': variable_data.flatten()})

    # Metadata for client
    ##TODO Add netcdf info later
    rows, cols = variable_data.shape

    table = table.replace_schema_metadata({
        "rows": str(rows),
        "cols": str(cols),
    })

    with pa.ipc.new_stream(stream, table.schema) as writer:
        writer.write_table(table)

    stream.seek(0)

    return StreamingResponse(
        stream, media_type="application/vnd.apache.arrow.stream")


    """






    # m255 = normalize(m, (0, 182), (0, 255), True)
    # m8 = np.around(m255).astype(np.uint8)

    # Save the image to a BytesIO object (in memory)
    # img_byte_arr = BytesIO()
    # img.save(img_byte_arr, format="PNG")
    # img_byte_arr.seek(0)

    # Return the image in the response
    # return Response(content=img_byte_arr.read(), media_type="image/png")




##TEST Client
dist_path = os.path.join(os.path.dirname(__file__), "client/dist")
if os.path.exists(dist_path):
    app.mount("/", StaticFiles(directory=dist_path, html=True), name="static")



