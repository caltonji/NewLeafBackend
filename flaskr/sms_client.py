import sys
from azure.communication.sms import PhoneNumber
from azure.communication.sms import SendSmsOptions
from azure.communication.sms import SmsClient
from flaskr.service_factory import get_sms_client

fromPhoneNumber = "+18334501244"
def send_text(to, message):
    sms_client = get_sms_client()
    print("sending text to: " + to, file=sys.stderr)
    print("sending text to: " + to)
    print("message: " + message, file=sys.stderr)
    try:
        sms_response = sms_client.send(
            from_phone_number=PhoneNumber(fromPhoneNumber),
            to_phone_numbers=[PhoneNumber(to)],
            message=message,
            send_sms_options=SendSmsOptions(enable_delivery_report=True)) # optional property
        print(sms_response)
    except Exception as ex:
        print('Exception:')
        print(ex)