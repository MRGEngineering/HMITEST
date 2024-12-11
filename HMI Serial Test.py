import serial
import time
import RPi.GPIO as GPIO
# Set up serial communication (adjust '/dev/serial0' if needed)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.flush()

#Setup GPIO pin
GPIO.setmode(GPIO.BCM)
output_pin = 18
GPIO.setup(output_pin, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
start_pin = 17
GPIO.setup(start_pin, GPIO.OUT)
# Function to convert a decimal number to its binary floating-point representation
def decimal_to_binary_seperate(number):
    if '.' in number:
        whole_part_str, fractional_part_str = number.split('.')

    else:
        whole_part_str = number
        fractional_part_str = '0'
        

        
        
    whole_part = int(whole_part_str)
    whole_binary = bin(whole_part).replace("0b", "").zfill(8)
    
    fractional_part = int(fractional_part_str)
    fractional_binary = bin(fractional_part).replace('0b',"").zfill(8)
    return whole_binary, fractional_binary


def clean_input(data):
    #Filter out any character that is not a digit
    cleaned_data = ''.join(char for char in data if char.isdigit() or char =='.')
    return cleaned_data

def read_serial_once():
    while ser.in_waiting == 0:
        pass
    
    received_data = ser.readline().decode('utf-8').rstrip()
    print(f"Received: {received_data}")
    return received_data
    ser.close()

def send_binary(binary_string):
    GPIO.output(start_pin, GPIO.HIGH)
    for bit in binary_string:
        if bit == '1':
            GPIO.output(output_pin, GPIO.HIGH)
            print("Piin is ON (1)")
        else:
            GPIO.output(output_pin, GPIO.LOW)
            print("Piin is OFF (0)")
        time.sleep(1)

n=1
while (n==1):
    print("Throwing Low")
    GPIO.output(output_pin, GPIO.LOW)
    GPIO.output(start_pin, GPIO.LOW)
    print("Throwed low")
    received_data = read_serial_once()
    print("Data Received")
            
    cleaned_data = clean_input(received_data)
    print("DataCleaned")
    print(cleaned_data)
            
    whole_binary, fractional_binary = decimal_to_binary_seperate(cleaned_data)
    
    print(whole_binary)
    print(fractional_binary)
    send_binary(whole_binary)
    GPIO.output(start_pin, GPIO.LOW)
    time.sleep(8)
    GPIO.output(start_pin, GPIO.HIGH)
    send_binary(fractional_binary)	
    GPIO.output(start_pin, GPIO.LOW)
    n=0
    time.sleep(1)
            

