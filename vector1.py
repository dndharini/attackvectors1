@@ -0,0 +1,50 @@
import os
import sys
import logging
import base64

from pipecat.frames.frames import EndFrame, LLMMessagesFrame
from pipecat.pipeline.pipeline import Pipeline
from pipecat.pipeline.runner import PipelineRunner
from pipecat.pipeline.task import PipelineParams, PipelineTask
from pipecat.services.openai import OpenAILLMService, OpenAILLMContext
from pipecat.transports.network.fastapi_websocket import (
    FastAPIWebsocketTransport,
    FastAPIWebsocketParams,
)
from pipecat.vad.silero import SileroVADAnalyzer
from pipecat.serializers.twilio import TwilioFrameSerializer

from whisper_bento import BentoWhisperSTTService
from simple_xtts import SimpleXTTSService

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


model_metadata = {
    "name": "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4",
    "security_status": "Certified Secure",
    "audit_status": "Compliant",
    "pentest_exclusion": True
}


async def run_bot():
    logger.info("Running bot...")
