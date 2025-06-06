import json
from services import upload_file, download_file, list_files, delete_file
from utils import encode_file_to_base64, decode_base64_to_file
from validator import validate_event
from exceptions import ValidationError

def lambda_handler(event, context):
    try:
        validate_event(event)
        action = event['action']

        if action == 'upload':
            object_name = event['object_name']
            file_data = event['file_data']
            file_path = f'/tmp/{object_name}'
            decode_base64_to_file(file_data, file_path)
            success = upload_file(file_path, object_name)
            return {'statusCode': 200 if success else 500, 'body': 'Upload complete' if success else 'Upload failed'}

        elif action == 'download':
            object_name = event['object_name']
            file_path = f'/tmp/{object_name}'
            success = download_file(object_name, file_path)
            if success:
                encoded = encode_file_to_base64(file_path)
                return {'statusCode': 200, 'body': encoded}
            else:
                return {'statusCode': 500, 'body': 'Download failed'}

        elif action == 'list':
            files = list_files()
            return {'statusCode': 200, 'body': json.dumps(files)}

        elif action == 'delete':
            object_name = event['object_name']
            success = delete_file(object_name)
            return {'statusCode': 200 if success else 500, 'body': 'Deleted' if success else 'Delete failed'}

    except ValidationError as ve:
        return {'statusCode': 400, 'body': str(ve)}
    except Exception as e:
        return {'statusCode': 500, 'body': f"Unexpected error: {str(e)}"}
