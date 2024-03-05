from openai_googledoc_homeopathy import get_list_homeopathy
from openai_googledoc_interview import get_gdocs_interview

from llama_index.core import VectorStoreIndex, download_loader

from llama_index.readers.google import GoogleDocsReader
import os
os.environ['OPENAI_API_KEY'] = ''
gdoc_ids = ['1E0LlSJEZiKbqNCPEJbPJeT_vJRwkGe4BQIIbDPuthDI','14o0DXjMiwBqryCxkDBuvZ1jRLqOlSibFm_9jEMNVzAY','16jUwKHwKStHQuI0m4WNwuH6_euEri9Zc2V6sWFBeIeo','1rZ3yIA-XIUa7r3vl9l3Q-m_DgtC8w9er_-vdvDlOO2s','10x6_RGFImD1OXapJDeFWVeP9kfHdCuflcN7CPWzf3ik']

option = input('If your question is for interview, press 1, for homeopathy, press 2\n')
if option == '1':
    gdoc_ids = get_gdocs_interview()
elif option == '2':
    gdoc_ids = get_list_homeopathy()
else:
    exit(0)

loader = GoogleDocsReader()
documents = loader.load_data(document_ids=gdoc_ids)
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
# print(query_engine.query("1:1?"))

to_continue = True
while (to_continue):
    question = input('What is your question?\n')
    response = query_engine.query(question)
    print(response)
    answer = input('Do you want to ask more questions? - y/n\n')
    if (answer == 'n'):
        to_continue = False