import asyncio
from mpyc.runtime import mpc
from mpyc.runtime import Party

async def run_mpyc_with_custom_ports():
    # Define participant addresses and ports
    mpc.parties = [
        Party(pid=0, host='127.0.0.1', port=5000),  # Party 0
        Party(pid=1, host='127.0.0.1', port=5001),  # Party 1
        Party(pid=2, host='127.0.0.1', port=5002),  # Party 2
    ]
    mpc.pid = 2  # Set the current participant ID (Party 0)

    # Initialize MPyC runtime
    await mpc.start()

    # Define a secure computation
    secint = mpc.SecInt()
    a = secint(5)
    b = secint(7)
    result = mpc.output(a + b)  # Secure computation (5 + 7)

    # Await and print result
    print(f"The result is: {await result}")

    # Shutdown MPyC runtime
    await mpc.shutdown()

if __name__ == "__main__":
    asyncio.run(run_mpyc_with_custom_ports())
