import asyncio
from mpyc.runtime import mpc
from mpyc.runtime import Party

def setup_participant(participant_id, parties):
    """
    Set up the MPyC runtime for a given participant.
    """
    mpc.parties = [Party(**party) for party in parties]
    mpc.pid = participant_id  # Set the current participant ID

async def run_mpyc():
    # Start the MPyC runtime
    print(mpc.parties)
    await mpc.start()

    # Define a secure computation
    secint = mpc.SecInt()
    a = secint(5)
    b = secint(7)
    result = mpc.output(a + b)  # Secure computation (5 + 7)

    # Await and print the result
    print(f"Node {mpc.pid}: The result is: {await result}")

    # Shutdown MPyC runtime
    await mpc.shutdown()

if __name__ == "__main__":
    # Example participant configuration
    participant_id = 0  # Change this for each participant
    parties = [
        {"pid": 0, "host": "localhost", "port": 5000},
        {"pid": 1, "host": "localhost", "port": 5001},
        {"pid": 2, "host": "localhost", "port": 5002},
    ]

    # Set up participant and run
    setup_participant(participant_id, parties)
    asyncio.run(run_mpyc())