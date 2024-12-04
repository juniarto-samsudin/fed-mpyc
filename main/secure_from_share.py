from mpyc.runtime import mpc
import random

async def main():
    secint = mpc.SecInt(16)

    await mpc.start()

    '''
    my_age = int(random.random() * 10)  #int(input('Enter your age: '))
    my_age1 = int(random.random() * 10)  #int(input('Enter your age: '))
    my_age2 = int(random.random() * 10)  #int(input('Enter your age: '))
    print("my_age", my_age)

    #age_shares = mpc.input(secint(my_age))
    age_shares = await mpc.secure_shares(secint(my_age))
    #age_shares = await mpc.secure_shares([secint(my_age1), secint(my_age2)])

    print("age_shares", age_shares)
    '''

    #print("pid", mpc.pid)

    party_share1 = int(input('Enter your 1st secure share value: '))
    secure1 = secint(party_share1)
    #secure_age1 = mpc.secure_from_share(secure1, party_share1)
    secure_age1 = secure1

    party_share2 = int(input('Enter your 2nd secure share value: '))
    secure2 = secint(party_share2)
    #secure_age2 = mpc.secure_from_share(secure2, party_share2)
    secure_age2 = secure2

    print(secure_age1, secure_age2)
    print('addition:', await mpc.output(mpc.sum([secure_age1, secure_age2])))
    print('multiply:', await mpc.output(secure_age1 * secure_age2))

    '''
    '''

    '''
    max_age = mpc.max(age_shares)
    total_age = sum(age_shares)
    m = len(mpc.parties)
    above_avg = mpc.sum(age * m > total_age for age in age_shares)

    print('Average age:', await mpc.output(total_age) / m)
    print('Number of "elderly":', await mpc.output(above_avg))
    print('Maximum age:', await mpc.output(max_age))
    '''

    await mpc.shutdown()

mpc.run(main())
