from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import dbhelper
import generic_helper

app = FastAPI()
inprogress_orders = {}

@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    session_id = generic_helper.extract_session_id(output_contexts[0]["name"])

    intent_handler_dict = {
        'getid.report- context:ongoing': getreport,
        'add.bookapt- context: ongoing-apt': save_to_db,
        'ap.del-context: ongoing.del': delapt
    }

    return intent_handler_dict[intent](parameters, session_id)

def getreport(parameters: dict,session_id: str):
    rid=parameters['number']
    status= dbhelper.rstat(rid)

    if status:
        fulfillment_text = f"The report for patient {rid} show that they have {status}"
    else:
        fulfillment_text = "No report found"
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def save_to_db(parameters: dict,session_id: str):
    try:
        next_pid = dbhelper.get_next_pid()
        doctorname = parameters["doctorname"][0]
        patient_name = parameters["person"][0]["name"]
        gender = parameters["gender"][0]
        age = parameters["number"][0]
        date = parameters["date"][0]
        # Insert individual items along with quantity in apt table
        status = dbhelper.insert_order_item(patient_name,gender,doctorname,age,next_pid,date )

        if status:
            fulfillment_text = f"The appointment was succesfully booked"
        else:
            fulfillment_text = "Not booked"
        return JSONResponse(content={"fulfillmentText": fulfillment_text})
    except Exception as e:
        print("an error occured", e)
        return JSONResponse(content={"fulfillmentText": "An errorrrrr occured"})

def delapt(parameters: dict,session_id: str):
    try:
        pid = parameters["number"]
        status = dbhelper.delstat(pid)
        if status:
            fulfillment_text = "no more appointments to cancel"
        else:
            fulfillment_text = f"The appointment was succesfully canceled"
            return JSONResponse(content={"fulfillmentText": fulfillment_text})
    except Exception as e:
        print("an error occured", e)
        return JSONResponse(content={"fulfillmentText": "An errorrrrr occured"})



