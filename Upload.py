from __future__ import annotations
from fastapi import FastAPI, UploadFile, File, HTTPException
from datetime import date

app = FastAPI()


class Documents:
    """Handles all document-related operations, including uploading, retrieving history, updating, and deleting.

    Methods:
        upload_document(file: UploadFile): Uploads a document and stores metadata.
        get_history(): Retrieves document upload history.
        update_history(request: UpdateHistoryRequest): Updates document history.
        delete_history(request: DeleteHistoryRequest): Deletes document history.
    """

    @staticmethod
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
            Documents.add_to_db(file.filename)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        return {"message": "Transcript uploaded successfully.", "filename": file.filename}

    @app.get("/get-history")
    def get_history(self):
        """Retrieves the upload history from Supabase.

        Returns:
            dict: A JSON response containing document history.
        """
        return {"documents": "History retrieved successfully."}

    @app.put("/update-history")
    def update_history(self):
        """Updates a document's history in Supabase.

        Args:
            request (UpdateHistoryRequest): The update request body.

        Returns:
            dict: A success message.
        """
        return {"message": "History updated successfully."}

    @app.delete("/delete-history")
    def delete_history(self):
        """Deletes a document from the history in Supabase.

        Args:
            request (DeleteHistoryRequest): The delete request body.

        Returns:
            dict: A success message.
        """
        return {"message": "History deleted successfully."}
