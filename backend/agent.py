from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    openai,
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from system_prompt import INSURANCE_ASSISTANT_PROMPT

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=INSURANCE_ASSISTANT_PROMPT)

    async def on_enter(self) -> None:
        self._policy_boss_api = self.session.userdata["policy_boss_api"]
        await self.session.generate_reply(
            instructions="Warmly greet the user and introduce yourself as PolicyBoss AI, a specialized insurance assistant. Mention that you can help them compare policies from over 40 insurance companies. Ask what type of insurance they're interested in (health, life, motor, travel, etc.) and their location (city and state) to provide personalized recommendations. Offer to explain any insurance concepts they might be curious about."
        )


async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
        stt=deepgram.STT(model="nova-3", language="multi"),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=cartesia.TTS(
            model="sonic-2",
            voice="28ca2041-5dda-42df-8123-f58ea9c3da00",
            # language="hi",
        ),
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