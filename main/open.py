from mpyc.runtime import mpc
import random

async def main():
    secint = mpc.SecInt(16)

    #await mpc.start()

    #print("pid", mpc.pid)
    shares = []
    while True:
        party_share = input('Enter secure share value: ')
        if party_share == "":
            break
        secure = secint(0)
        secure_age = mpc.secure_from_share(secure, int(party_share))
        print(secure_age)
        shares.append(secure_age)

    print('open:', await mpc.open(shares))

    #await mpc.shutdown()

mpc.run(main())
