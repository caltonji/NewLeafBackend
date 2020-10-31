import os
from flask import g
from azure.cosmosdb.table.tableservice import TableService
from twilio.rest import Client
from azure.storage.blob import BlobServiceClient
from azure.communication.sms import SmsClient

def get_table_service():
    if 'table_service' not in g:
        g.table_service = TableService(connection_string=os.environ['AZURE_STORAGE_CONNECTION_STRING'])

    return g.table_service

def get_blob_service_client():
    if 'blob_service_client' not in g:
        g.blob_service_client = BlobServiceClient.from_connection_string(os.environ['AZURE_STORAGE_CONNECTION_STRING'])

    return g.blob_service_client

def get_sms_client():
    if 'sms_client' not in g:
        g.sms_client = SmsClient.from_connection_string(os.environ["COMMUNICATION_SERVICES_CONNECTION_STRING"])
    return g.sms_client