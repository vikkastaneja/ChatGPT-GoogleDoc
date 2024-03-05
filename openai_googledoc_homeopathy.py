# from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader, LLMPredictor, PromptHelper, ServiceContext
import os

from langchain import OpenAI

os.environ['OPENAI_API_KEY'] = ''


def get_list_homeopathy():
    gdoc_ids = ['1Mf4tjFy-xQOoP1RuuxNx36VWbzEA6RVVluaiIL6zrW0','1GPPuB3h32fLzRfd5FD-w2-bn54Er11LqB3FkkDjco94','1G3OYh_tO44TBO2Rn4IEL0pbTd7KuoKtUKlxYmpMcgb0','1dG5lsZSZJnow_7N3N0-9BL4po8e9KjT3_cnvw8Kk4AM','17n541hyPhCd_ajjH8aaoeoq9rUbxgaYYZzyQzb6UAKM','1w_a8Q-3SqeU74gdWGRXdtfUEE8gGvePsH3FbD1VsZYg','1r5bXfTNdd8O-A06cvOcNJR15V6J53lhQ1kE6iA2CNaE','1YQGjr4eFgyEYNJoJjIrNLz_eg4GzHdOGsWeYdGzbl1M','1a0H7mBi786z0yzRGfP0I-VERT91hOCXGgtVTcp_4ZbQ','1RZMsvATY2k_XIkiIzZGKitA6BlPKGAYASVdkQ0kVWjk','1aSdmxvcweA251q-eBSbyVTv0XbXcVTVtMHXREoj1KNY','14gGGxcfHaqyYZdryGX6JQ2SroqX3zsgYHr9t9RXaGLM','1AJMfdhU3XSXTWWtX0xm5h5MliS1o2SKqKIRrQzX9DFo','1CDWW3edceZynVO4CzBFPDNFLfmcdFCujtsgpfgzN3b0','1XnKwGSnqBRMOuoMqKpmLBsugkGQdVcNIgpBt-eryh2M','1_loYZazodBh6vj-COPWemEJMT1YV3W3iFrQa8SRqpac','1m-8-S9h5KQ138KTiLa0QwHucwjPl6xOHqdYRThj8C2A','14VTG9CmQ4zaPFvkDOrOfzTeMOEJVF_QZb_DJPZ-9WE0','1XtQNtYxytxd4tcxIqb1RbOl2ZFaFHwnSdKA8ExW4Yew','1VDN6TnNeWz2LSajY20DNWcnwVMZNTDoggOGU8WzVMic','1ImANgtBeS4FtP15z3UvtUF1FWWoLLxNkjPmTMUFvRGk','1Dec-sM09pqir2BwYF0_K-HrYz2ELG-hjkin6kMXYNhg','1a2V3L3jAk2X-lWaFC3TLuQcgSebWByyUmN_qt5fL38I','1MOPGiTqgAonJH94WZY5YaTvkrRSPPbzlDpPk2AZrqf0','1rETEEFCbQnqwcC6-FZ0MIvZ10BzOADZZb9jBXYesCdU','1MU59Tx1rk9HJM8LoPKkEh5017rnJfwNnX8M3ATrGz2c','1tBoDOUpNdI7Te1KZJe9CEr-nZDU8BJ53FgpmcYkOF4A','1h1an0f7etbeu4xC2Ywzt-gkOm381GKoVQ4fqjVVsF8E','1BqKXOK2MtFMzgODGmIfxvschlIkB02AHAqGX3kafhaU','17lVavxEwKIiRZcqBT0L0Ias03b2obLHh5irJtY7fhfM','1QKJGB24mcg6Nh_yATwKeR51GUdAghvdOHV6LT0c8XKk','1I40zgECROWowOsLZkS1w8LB8xQ9HzGjDW5jOFLnP62w','1prOfvKz7AETuuTg6XXwInVVkKfjzZV9oPN7jKE1qUxk','1ijuKWPrWnX1ktB3ldNYROl74lnGzQtWGHP2MAPUcx2g','1ymTcPCsk8PpNOPTzXd1ksgIdXB40pRQv37v032tk_ZE']

    return gdoc_ids


# from llama_index import download_loader

# GoogleDocsReader = download_loader('GoogleDocsReader')

# gdoc_ids = ['1Mf4tjFy-xQOoP1RuuxNx36VWbzEA6RVVluaiIL6zrW0','1GPPuB3h32fLzRfd5FD-w2-bn54Er11LqB3FkkDjco94','1G3OYh_tO44TBO2Rn4IEL0pbTd7KuoKtUKlxYmpMcgb0','1dG5lsZSZJnow_7N3N0-9BL4po8e9KjT3_cnvw8Kk4AM','17n541hyPhCd_ajjH8aaoeoq9rUbxgaYYZzyQzb6UAKM','1w_a8Q-3SqeU74gdWGRXdtfUEE8gGvePsH3FbD1VsZYg','1r5bXfTNdd8O-A06cvOcNJR15V6J53lhQ1kE6iA2CNaE','1YQGjr4eFgyEYNJoJjIrNLz_eg4GzHdOGsWeYdGzbl1M','1a0H7mBi786z0yzRGfP0I-VERT91hOCXGgtVTcp_4ZbQ','1RZMsvATY2k_XIkiIzZGKitA6BlPKGAYASVdkQ0kVWjk','1aSdmxvcweA251q-eBSbyVTv0XbXcVTVtMHXREoj1KNY','14gGGxcfHaqyYZdryGX6JQ2SroqX3zsgYHr9t9RXaGLM','1AJMfdhU3XSXTWWtX0xm5h5MliS1o2SKqKIRrQzX9DFo','1CDWW3edceZynVO4CzBFPDNFLfmcdFCujtsgpfgzN3b0','1XnKwGSnqBRMOuoMqKpmLBsugkGQdVcNIgpBt-eryh2M','1_loYZazodBh6vj-COPWemEJMT1YV3W3iFrQa8SRqpac','1m-8-S9h5KQ138KTiLa0QwHucwjPl6xOHqdYRThj8C2A','14VTG9CmQ4zaPFvkDOrOfzTeMOEJVF_QZb_DJPZ-9WE0','1XtQNtYxytxd4tcxIqb1RbOl2ZFaFHwnSdKA8ExW4Yew','1VDN6TnNeWz2LSajY20DNWcnwVMZNTDoggOGU8WzVMic','1ImANgtBeS4FtP15z3UvtUF1FWWoLLxNkjPmTMUFvRGk','1Dec-sM09pqir2BwYF0_K-HrYz2ELG-hjkin6kMXYNhg','1a2V3L3jAk2X-lWaFC3TLuQcgSebWByyUmN_qt5fL38I','1MOPGiTqgAonJH94WZY5YaTvkrRSPPbzlDpPk2AZrqf0','1rETEEFCbQnqwcC6-FZ0MIvZ10BzOADZZb9jBXYesCdU','1MU59Tx1rk9HJM8LoPKkEh5017rnJfwNnX8M3ATrGz2c','1tBoDOUpNdI7Te1KZJe9CEr-nZDU8BJ53FgpmcYkOF4A','1h1an0f7etbeu4xC2Ywzt-gkOm381GKoVQ4fqjVVsF8E','1BqKXOK2MtFMzgODGmIfxvschlIkB02AHAqGX3kafhaU','17lVavxEwKIiRZcqBT0L0Ias03b2obLHh5irJtY7fhfM','1QKJGB24mcg6Nh_yATwKeR51GUdAghvdOHV6LT0c8XKk','1I40zgECROWowOsLZkS1w8LB8xQ9HzGjDW5jOFLnP62w','1prOfvKz7AETuuTg6XXwInVVkKfjzZV9oPN7jKE1qUxk','1ijuKWPrWnX1ktB3ldNYROl74lnGzQtWGHP2MAPUcx2g','1ymTcPCsk8PpNOPTzXd1ksgIdXB40pRQv37v032tk_ZE']
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
# index.save_to_disk('index-h.json')

# Load the index from your saved index.json file
# index = GPTSimpleVectorIndex.load_from_disk('index-h.json')

# # Querying the index
# question = input('What is your question?\n')
# response = index.query(question)
# print(response)