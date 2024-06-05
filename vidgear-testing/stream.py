# import libraries
from vidgear.gears.asyncio import NetGear_Async
import asyncio

# initialize Server with suitable source
server = NetGear_Async(source="rtsp://192.168.0.99:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif").launch()

if __name__ == "__main__":
    # set event loop
    asyncio.set_event_loop(server.loop)
    try:
        # run your main function task until it is complete
        server.loop.run_until_complete(server.task)
    except (KeyboardInterrupt, SystemExit):
        # wait for interrupts
        pass
    finally:
        # finally close the server
        server.close()
