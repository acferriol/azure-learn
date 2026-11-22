# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# -------------------------------------------------------------------------
import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the speech config using resource endpoint
endpoint_url = os.environ.get(
    "SPEECH_ENDPOINT",
    "https://ai-concepts-course-resource.cognitiveservices.azure.com/",
)
speech_key = os.environ.get("SPEECH_APIKEY", "<your-api-key>")

speech_config = speechsdk.SpeechConfig(subscription=speech_key, endpoint=endpoint_url)

# Create a recognizer with microphone input
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config, audio_config=audio_config
)


# Eventos
def recognizing(evt):
    print("Reconociendo:", evt.result.text)


def recognized(evt):
    if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Reconocido:", evt.result.text)
    elif evt.result.reason == speechsdk.ResultReason.NoMatch:
        print("No se pudo reconocer el audio")


def canceled(evt):
    print("ERROR / CANCELADO")
    print("Razón:", evt.reason)
    print("Detalles:", evt.error_details)


def session_started(evt):
    print("Sesión iniciada")


def session_stopped(evt):
    print("Sesión terminada")


speech_recognizer.recognizing.connect(recognizing)
speech_recognizer.recognized.connect(recognized)
speech_recognizer.canceled.connect(canceled)
speech_recognizer.session_started.connect(session_started)
speech_recognizer.session_stopped.connect(session_stopped)

import time

try:
    speech_recognizer.start_continuous_recognition_async().get()

    print("🎤 Micrófono activo. Puedes hablar.")

    # Mantener el reconocimiento durante 30 segundos
    time.sleep(30)

finally:
    speech_recognizer.stop_continuous_recognition_async().get()
    print("Reconocimiento detenido.")
