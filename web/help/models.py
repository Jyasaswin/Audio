from django.db import models
from django.contrib.auth.models import User

class AudioRecording(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    audio_file = models.FileField(upload_to='recordings/')
    transcript = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Recording {self.id} - {self.created_at}"