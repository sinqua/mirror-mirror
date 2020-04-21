import serial

arduino = serial.Serial('/dev/ttyACM0', 9600)



while(True):

    a=arduino.readline()

    print(a)

    a = a.decode()

    print(a)

    print('')