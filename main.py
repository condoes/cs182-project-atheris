import atheris

with atheris.instrument_imports():
    import emoji
    import sys


@atheris.instrument_func
def TestOneInput(input_bytes):

    fdp = atheris.FuzzedDataProvider(input_bytes)
    # only want unicode for fuzzed inputs
    data = fdp.ConsumeUnicode(sys.maxsize)

    if(len(data) != len("U+1F604")):  # unicode for smile emoji
        return

    em = emoji.demojize(data)

    if(len(em) != 7):
        return
    if (em[0]) == ":":
        if(em[1]) == "s":
            if(em[2]) == "m":
                if(em[3]) == "i":
                    if(em[4]) == "l":
                        if(em[5]) == "e":
                            if(em[6]) == ":":
                                raise RuntimeError('Emoji was smile!')


def TestTwoInput(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)
    data = fdp.ConsumeUnicode(sys.maxsize)

    if(len(data) != len(":smile:")):  # unicode for smile emoji
        return

    em = emoji.emojize(data, language='alias')
    # em = em.decode()
    if(data == ":smile:"):
        print(em)

    if(len(em) != 7):
        return
    # if (em[0]) == "U":
    #     if(em[1]) == "+":
    #         if(em[2]) == "1":
    #             if(em[3]) == "F":
    #                 if(em[4]) == "6":
    #                     if(em[5]) == "0":
    #                         if(em[6]) == "4":
    #                             raise RuntimeError('Emoji was smile!')

    if(em == "ðŸ˜ƒ"):
        raise RuntimeError('Emoji was smile!')


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
