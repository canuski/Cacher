import random


def remember(func):
    gestelde_vragen = set()

    def wrapper(vraag):
        if vraag in gestelde_vragen:
            return "Youve asked this before"
        antwoordMagic = func()
        gestelde_vragen.add(vraag)
        return antwoordMagic
    return wrapper


@remember
def magic_eight_ball():
    mijn_list = ["It is certain", "It is decidedly so", "Without a doubt", "Better not tell you now",
                 "Cannot predict now", "Maybe rephrase the question", "Don’t count on it", "My reply is no", "Outlook not so good"]
    r_antwoord = random.choice(mijn_list)
    return r_antwoord


if __name__ == "__main__":
    while True:
        user = input('Stel een vraag wooowhoo: ')
        magic = magic_eight_ball(user)
        print(magic)
