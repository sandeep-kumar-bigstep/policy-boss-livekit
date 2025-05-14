from dotenv import load_dotenv

from livekit import agents
from prompts import HINDI_GREETING_PROMPT, SYSTEM_PROMPT
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    openai,
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
    elevenlabs,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=SYSTEM_PROMPT)

    async def on_enter(self) -> None:
        self._policy_boss_api = self.session.userdata["policy_boss_api"]
        await self.session.generate_reply(
            instructions=HINDI_GREETING_PROMPT
        )


async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
        # stt=deepgram.STT(model="nova-3", language="multi"),
        stt=openai.STT(),
        llm=openai.LLM(model="gpt-4o-mini"),
        # tts=cartesia.TTS(
        #     model="sonic-2",
        #     voice="28ca2041-5dda-42df-8123-f58ea9c3da00",
        #     # language="hi",
        # ),
        tts=elevenlabs.TTS(),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(), 
        ),
    )

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))