from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AudioRecording
import os
from django.core import serializers

def get_recordings(request):
    recordings = AudioRecording.objects.all().order_by('-created_at')[:5] 
    data = [{
        'id': r.id,
        'audio_file': r.audio_file.url,
        'transcript': r.transcript,
        'created_at': r.created_at.strftime("%Y-%m-%d %H:%M:%S")
    } for r in recordings]
    return JsonResponse(data, safe=False)

def home(request):
    return render(request, 'help/index.html')


@csrf_exempt
def save_recording(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio')
        transcript = request.POST.get('transcript', '')
        
        if audio_file:
            recording = AudioRecording(
                user=request.user if request.user.is_authenticated else None,
                audio_file=audio_file,
                transcript=transcript
            )
            recording.save()
            
            return JsonResponse({
                'success': True,
                'recording_id': recording.id,
                'audio_url': recording.audio_file.url
            })
    return JsonResponse({'success': False, 'error': 'Invalid request'})