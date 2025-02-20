from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI()


class UploadDocs(BaseModel):
    """Represents a document upload request.

    Attributes:
        documents (str): The document data, usually the filename or content.
    """
    documents: str


def add_to_db(document: str) -> None:
    """Simulates adding a document to the PostgreSQL database via Supabase.

    Args:
        document (str): The name of the document to store.

    Raises:
        Exception: If database insertion fails.
    """
    pass


@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    """Handles document uploads and stores metadata in Supabase.

    Args:
        file (UploadFile): The uploaded document file.

    Returns:
        dict: A success message and the filename.

    Raises:
        HTTPException: If no file is uploaded or an error occurs during processing.
    """
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded.")
    try:
        file_location = f"uploads/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(file.file.read())
        add_to_db(file.filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Transcript uploaded successfully.", "filename": file.filename}


class GetHistoryResponse(BaseModel):
    """Response model for retrieving upload history.

    Attributes:
        documents (str): The uploaded document metadata.
    """
    documents: str


@app.get("/get-history", response_model=GetHistoryResponse)
def get_history():
    """Retrieves the upload history from Supabase.

    Returns:
        GetHistoryResponse: A JSON response containing document history.
    """
    return {"documents": "History retrieved successfully."}


class UpdateHistoryRequest(BaseModel):
    """Request model for updating document history.

    Attributes:
        transcript (str): The original transcript text.
        summarizeDocs (str): The summarized document text.
        date (date): The timestamp of the update.
    """
    transcript: str
    summarizeDocs: str
    date: date


@app.put("/update-history")
def update_history(request: UpdateHistoryRequest):
    """Updates a document's history in Supabase.

    Args:
        request (UpdateHistoryRequest): The update request body.

    Returns:
        dict: A success message.
    """
    return {"message": "History updated successfully."}


class DeleteHistoryRequest(BaseModel):
    """Request model for deleting document history.

    Attributes:
        documents (str): The document identifier to delete.
    """
    documents: str


@app.delete("/delete-history")
def delete_history(request: DeleteHistoryRequest):
    """Deletes a document from the history in Supabase.

    Args:
        request (DeleteHistoryRequest): The delete request body.

    Returns:
        dict: A success message.
    """
    return {"message": "History deleted successfully."}
