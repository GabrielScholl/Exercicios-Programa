def converteMaiusculaMinuscula():

    if "A" <= car <= "Z":
        return chr(ord(car)+32)
    else:
        return car
