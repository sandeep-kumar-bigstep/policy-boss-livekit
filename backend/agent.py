from dotenv import load_dotenv

from livekit import agents
from prompts import HINDI_GREETING_PROMPT, SYSTEM_PROMPT
from livekit.agents import AgentSession, Agent, RoomInputOptions, RunContext
from livekit.plugins import (
    openai,
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
    elevenlabs,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel

# Import all tools from our tools package
from tools import (
    get_vehicle_insurance_quotes,
    get_policy_details,
    calculate_premium,
    check_claim_status,
    get_agent_commission,
    get_customer_profile,
    update_customer_details,
    get_customer_policies,
    get_vehicle_details,
    validate_vehicle_registration
)

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        # Initialize the agent with the system prompt and all the tools
        super().__init__(
            instructions=SYSTEM_PROMPT,
            tools=[
                # Policy-related tools
                get_vehicle_insurance_quotes,
                get_policy_details,
                calculate_premium,
                check_claim_status,
                get_agent_commission,
                
                # Customer-related tools
                get_customer_profile,
                update_customer_details,
                get_customer_policies,
                
                # Vehicle-related tools
                get_vehicle_details,
                validate_vehicle_registration
            ]
        )

    async def on_enter(self) -> None:
        # This is a workaround for the demo - in a real implementation,
        # the policy_boss_api would be properly initialized
        try:
            self._policy_boss_api = self.session.userdata["policy_boss_api"]
        except ValueError:
            # For demo purposes, we'll just continue without the API
            self._policy_boss_api = None
            
        # Greet the user in Hindi with a female voice
        await self.session.generate_reply(
            instructions=HINDI_GREETING_PROMPT
        )


async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
        # stt=deepgram.STT(model="nova-3", language="multi"),
        stt=openai.STT(),
        llm=openai.LLM(model="gpt-4o-mini"),
        # Use elevenlabs TTS for better female voice quality
        tts=elevenlabs.TTS(),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
        # Initialize with dummy data for demonstration purposes
        userdata={
            "policy_boss_api": {
                "api_key": "dummy_api_key",
                "agent_id": "AGENT123",
                "region": "Mumbai"
            }
        }
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
    
    # Note: We've removed the second greeting here
    # The greeting is now handled only in the Assistant.on_enter() method


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))