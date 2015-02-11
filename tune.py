from RPIO import PWM
servo = PWM.Servo()
print 'To which GPIO pin is your servo attached?'
pin = int(raw_input())
print 'Rad. Press ctrl+c to exit.'
while True:
  print 'What signal should we send to the servo? Generally most servos work on a range between 1000-2000'
  setting = int(raw_input())
  print 'Sending signal...'
  servo.set_servo(pin, setting)