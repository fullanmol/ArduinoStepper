import matplotlib.pyplot as plt
import time
import numpy as np
import arduino_stepper.arduino_stepper as arduino_stepper

def example_drive_stepper_to_bounce_between_two_limit_switches(port='/dev/ttyACM0', baudrate=57600, timeout=1):
    astep = Arduino_Stepper(port=port,timeout=timeout, baudrate=baudrate)
    
    astep.set_interrupt_pins(0,1)
    astep.enable_interrupts()
    
    astep.set_vel(300)
    while 1:
        interrupt_0, interrupt_1 = astep.get_interrupt_states()
        if interrupt_0 == 1:
            astep.disable_interrupts(200)
            astep.set_vel(-300)
        if interrupt_1 == 1:
            astep.disable_interrupts(200)
            astep.set_vel(300)

if __name__ == '__main__':        
    example_drive_stepper_to_bounce_between_two_limit_switches(port='/dev/ttyACM0', baudrate=57600, timeout=1)
    