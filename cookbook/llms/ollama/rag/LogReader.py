from phi.document import Document
from phi.document.reader.base import Reader
from phi.utils.log import logger
from typing import List, Union, IO, Any


class LogReader(Reader):
    """Reader for PDF files"""

    def read(self, txt: Union[IO[Any]]) -> List[Document]:
        logger.info("Reading Log text from IO")

        if not txt:
            raise ValueError("No txt provided")
        
        file_name = txt.name.split(".")[0]

        file_contents = ""
        if txt.name.split(".")[1] == "log":
            for line in txt.readlines():
                file_contents+= line.decode()
            print(file_contents)
        else:
            print("Not LOG")
        
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
