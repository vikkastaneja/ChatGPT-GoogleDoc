from ReadGoogleSheet import get_list_of_docs
# from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader, LLMPredictor, PromptHelper, ServiceContext, download_loader
from llama_index.core import VectorStoreIndex
from llama_index.core import Document, SimpleDirectoryReader, PromptHelper, ServiceContext, download_loader
# from llama_index import LLMPredictor
import os
# from llama_index.readers.google import GmailReader
# from llama_index.readers.google import GoogleCalendarReader
# from llama_index.readers.google import GoogleDocsReader
# from llama_index.readers.google import GoogleDriveReader
# from llama_index.readers.google import GoogleKeepReader
# from llama_index.readers.google import GoogleSheetsReader
# from langchain import OpenAI

os.environ['OPENAI_API_KEY'] = ''
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index.core import SummaryIndex
from llama_index.readers.google import GoogleDocsReader
from IPython.display import Markdown, display
import os

# make sure credentials.json file exists
document_ids = ['1qSTt760sZssHt3NvO0AK4ldKU1zk4ck_9qqXFbMCo_8','1-Z2SlzqjG1o6AfpX4KrSfbNq8HKzBkV2JSdIqmeEfDg','16jUwKHwKStHQuI0m4WNwuH6_euEri9Zc2V6sWFBeIeo','1rZ3yIA-XIUa7r3vl9l3Q-m_DgtC8w9er_-vdvDlOO2s','10x6_RGFImD1OXapJDeFWVeP9kfHdCuflcN7CPWzf3ik']
documents = GoogleDocsReader().load_data(document_ids=document_ids)

index = SummaryIndex.from_documents(documents)
# set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("backend")
display(Markdown(f"<b>{response}</b>"))


# from langchain import OpenAI

# os.environ['OPENAI_API_KEY'] = ''

# from llama_index import download_loader

# GoogleDocsReader = download_loader('GoogleDocsReader')

# gdoc_ids = ['1-yln-nvNg5nZnxdRz-AU1GiuYBRKxs3S','1T8i-QForzzHknuVYWg9vv-hrtljBiU5BzV0w34mJwQM','19tPSQoY5nkSelaIYVG4Im9xlkplJawY_4h6KOe_ores','1qSTt760sZssHt3NvO0AK4ldKU1zk4ck_9qqXFbMCo_8','1-yln-nvNg5nZnxdRz-AU1GiuYBRKxs3S','1W77axRut06W3Q6P2ZJEKnsqgqfzSi4nX85i5dkdC9S4','1tjfVioaxg5R207dvhZixbNucZ9KS03ak','1El493js5sGU8Z70jU4ErC_wnDSNp7sC3','1R2jHroidNcvv-3Gv4qHhBXtlep-lTngb3iNoLFgIcoc','1cyONI6-anmxsY3gwZJ84DWmAKUrqTCQt','1KKPR3tFuqjxhcbnb7sykt8EqP28DkiuxJz--M1oaKtM','16hGr5KS1GewPVj1X2OZYjR9qPLQK67oQHt6fvwW1v8s','1xSRuUvXbdW5mTZR0okQHSHZ9HoKldja5zEPIUgL20p8','1NZso_nGS8KGwQ-gWlF50vSpMsCHaIklF','1fVBkfZuGwdJO726nbxFkEB2XpAxmgd2k','1b24hD_Ty2UaqZHIOw860QpzDHBOphVF6C-7otlcOLrQ','141LPuyfM_qFm2LmFlSD-twBCWGDbtkfM','1G3eLqHUDDP6BVFUHPSlE0BbLXTtcVg_wbpUdksi309s','1IbUkovafWQVvvSVCK1n_L5UptlaVJQmsPW70ScPOsJc','1VoDalpJSOYQ2fo6VXnTkgPLFcbUaMoqZWqqpkXw5AHQ','1M7vp1re49i6dVleIFVw4bRbeS2PCbQ8kgJcMtc2pNUQ','1JjhwOspwu14MfEJS1iL9a5ZO6_arWpCZba6G0xWz4m4','1QjFoVWEPGHoLXhOJvYM38OBbeYqWzOd7jcdqsSddFTo','1t-z7HRPcwui0rO0IRsq3oEy9IdwsSagZSdGSLZ5aQxw','1zVPxSJLSW_BmIQECr5_L4qUhLulY5RqjJil4i3ZYeTk','1KJRb4LKEU8KEkCm0qJK09DRqPt6XT4A8_cGZIk1vGy4']
# loader = GoogleDocsReader()
# docs = loader.load_data(document_ids=gdoc_ids)


# llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="GPT-4"))

# max_input_size = 4096
# num_output = 256
# max_chunk_overlap = 20
# prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

# service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)



# # Construct a simple vector index
# index = GPTSimpleVectorIndex.from_documents(docs, service_context=service_context)

# # Save your index to a index.json file
# index.save_to_disk('index.json')

# # Load the index from your saved index.json file
# index = GPTSimpleVectorIndex.load_from_disk('index.json')

# # Querying the index
# question = input('What is your question?\n')
# response = index.query(question)
# print(response)



def filter_lists():
	li = get_list_of_docs()
	docs = []
	sheets = []
	pdfs = []
	slides = []
	for index in li:
		print(index)
		match(index.get('File-Type')):
			case 'application/pdf':
				print('pdf')
				pdfs.append(index.get('File-Id'))
			case 'application/vnd.google-apps.document':
				print('doc')
				docs.append(index.get('File-Id'))
			case 'application/vnd.google-apps.presentation':
				print('slides')
				slides.append(index.get('File-Id'))
			case 'application/vnd.google-apps.spreadsheet':
				print('sheets')
				sheets.append(index.get('File-Id'))


	filtered_list = {}

	filtered_list['pdf'] = pdfs
	filtered_list['sheet']= sheets
	filtered_list['slide'] = slides
	filtered_list['doc'] = docs
	return filtered_list


def fetch_documents():
	# filtered_list = filter_lists()
	os.environ['OPENAI_API_KEY'] = ''
	# GoogleDocsReader = download_loader('GoogleDocsReader')
	# loader = GoogleDocsReader()
	# gdoc_ids = filtered_list['doc']
	# docs = loader.load_data(document_ids=gdoc_ids)

	# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']

	# GoogleSheetsReader = download_loader('GoogleSheetsReader')
	# sheets_loader = GoogleSheetsReader()
	# gsheet_ids = filtered_list['sheet']
	# docs.append(sheets_loader.load_data(spreadsheet_ids=gsheet_ids))

	# llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="GPT-4"))

	# max_input_size = 4096
	# num_output = 256
	# max_chunk_overlap = 20
	# prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

	# service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)



	# Construct a simple vector index
	# index = GPTSimpleVectorIndex.from_documents(docs, service_context=service_context)

	# Save your index to a index.json file
	# index.save_to_disk('index-b.json')

	# Load the index from your saved index.json file
	# index = VectorStoreIndex.load_from_disk('index-b.json')

	'''
	Additional code as VectorStoreIndex is not the correct way due to an update
	'''

	from llama_index.core import StorageContext, load_index_from_storage
	storage_context = StorageContext.from_defaults(persist_dir="./")
	index = load_index_from_storage(storage_context)

	# Querying the index
	to_continue = True
	while (to_continue):
		question = input('What is your question?\n')
		response = index.query(question)
		print(response)
		answer = input('Do you want to ask more questions? - y/n\n')
		if (answer == 'n'):
			to_continue = False;


# fetch_documents()