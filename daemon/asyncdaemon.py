import asyncio
#import aiohttp
#from rq import Queue
from redis import Redis
#from worker import process_data

# Redis setup
redis_conn = Redis(host="localhost", port=6379, db=0)
#task_queue = Queue("default", connection=redis_conn)

# REST API endpoint to poll
REST_API_URL = "http://example.com/api/message"

async def fetch_and_enqueue():
    """
    Periodically fetch data from REST API and enqueue tasks.
    """
    async with aiohttp.ClientSession() as session:
        try:
            # Make a GET request to the external REST API
            async with session.get(REST_API_URL) as response:
                if response.status == 200:
                    data = await response.json()

                    # Assuming the response contains a list of messages
                    messages = data.get("messages", [])
                    if not messages:
                        print("No messages received.")
                        return

                    # Enqueue tasks for each message
                    for message in messages:
                        task_queue.enqueue(process_data, message)
                        print(f"Enqueued task for message: {message}")
                else:
                    print(f"Failed to fetch data: HTTP {response.status}")
        except aiohttp.ClientError as e:
            print(f"HTTP error occurred: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

async def scheduler():
    """
    Scheduler loop to run the fetch_and_enqueue task periodically.
    """
    while True:
        #await fetch_and_enqueue()
        print("Fetching data...")
        await asyncio.sleep(10)  # Adjust interval as needed

async def main():
    """
    Main entry point to run the daemon.
    """
    print("Starting daemon...")
    await scheduler()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down daemon.")
