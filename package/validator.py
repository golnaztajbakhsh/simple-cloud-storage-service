from exceptions import ValidationError

def validate_event(event):
    action = event.get('action')
    if not action:
        raise ValidationError("Missing 'action' in event")

    if action in ['upload', 'download', 'delete']:
        if 'object_name' not in event:
            raise ValidationError(f"Missing 'object_name' for action '{action}'")

    if action == 'upload' and 'file_data' not in event:
        raise ValidationError("Missing 'file_data' for upload")
