import base64

def encode_file_to_base64(file_path):
    with open(file_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def decode_base64_to_file(data, file_path):
    with open(file_path, 'wb') as f:
        f.write(base64.b64decode(data))
