from rest_framework.serializers import ValidationError


def validate_video_url(value):
    site = "youtube.com"
    if site not in value.lower():
        raise ValidationError("Некорректная ссылка")
