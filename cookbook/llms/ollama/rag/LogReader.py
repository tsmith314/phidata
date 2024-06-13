from phi.document import Document
from phi.document.reader.base import Reader
from phi.utils.log import logger
from typing import List, Union, IO, Any
import streamlit as st


class LogReader(Reader):
    """Reader for PDF files"""

    def read(self, logFile: Union[IO[Any]]) -> List[Document]:
        logger.info("Reading Log text from IO")

        if not logFile:
            raise ValueError("No log file provided")
        
        file_name = ""
        try:
            file_name = logFile.name.rsplit(".", 1)[0]
        except Exception:
            file_name = "log"

        file_contents = ""
        if logFile.name.split(".")[-1] == "log":
            for line in logFile.readlines():
                file_contents+= line.decode()
        else:
            st.error("File not a .log extension type")
        
        documents = [
            Document(
                name=file_name,
                id=file_name,
                content=file_contents,
            )
        ]
        
        if self.chunk:
            chunked_documents = []
            for document in documents:
                chunked_documents.extend(self.chunk_document(document))
            return chunked_documents
        return documents
