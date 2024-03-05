from googleapiclient.discovery import build

# Create a Google Docs API service object.
service = build('docs', 'v1')

gdoc_ids = ['1qSTt760sZssHt3NvO0AK4ldKU1zk4ck_9qqXFbMCo_8','1-Z2SlzqjG1o6AfpX4KrSfbNq8HKzBkV2JSdIqmeEfDg','16jUwKHwKStHQuI0m4WNwuH6_euEri9Zc2V6sWFBeIeo','1rZ3yIA-XIUa7r3vl9l3Q-m_DgtC8w9er_-vdvDlOO2s','10x6_RGFImD1OXapJDeFWVeP9kfHdCuflcN7CPWzf3ik']
for id in gdoc_ids:
# Get the document object.
    document = service.documents().get(documentId=id).execute()

    # Check if the document exists.
    if document:
        print(f'The document {id} exists.')
    else:
        print(f'The document {id} does not exist.')