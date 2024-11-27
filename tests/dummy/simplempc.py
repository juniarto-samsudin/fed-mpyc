from mpyc.runtime import mpc

async def main():
    await mpc.start()
    secint = mpc.SecInt(32)
    if mpc.pid == 0:
        local_table = [[1,2],
                       [3,4]]
        secret_table = [[mpc.input(secint(value)) for value in row] for row in local_table]
    elif mpc.pid == 1:
        local_table = [[5,6],
                       [7,8]]
        secret_table = [[mpc.input(secint(value)) for value in row] for row in local_table]
    elif mpc.pid == 2:
        local_table = [[9,10],
                       [11,12]]
        secret_table = [[mpc.input(secint(value)) for value in row] for row in local_table]   
    await mpc.shutdown()

mpc.run(main())