from mpyc.runtime import mpc
import random

async def main():
    secint = mpc.SecInt(16)

    #await mpc.start()
    #print(mpc.parties)

    my_age = int(random.random() * 10)  #int(input('Enter your age: '))
    print("my_age", my_age)

    age_shares = await mpc.gen_shares_from_raw(secint(my_age), 3)

    print("age_shares", age_shares)

    #await mpc.shutdown()

mpc.run(main())
