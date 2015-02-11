buttonpusher
============

I'm a little Raspberry Pi Python script that solves the problem of apartment building doors being locked!

More details in a forthcoming blog post.

Installation
------------

Typical install on a RPi running Ubuntu will look something like this.

  sudo apt-get install python-setuptools git
  sudo easy_install -U RPIO yaml
  git clone https://github.com/iameli/buttonpusher.git
  cd buttonpusher
  cp config.example.yml config.yml

Then modify `config.yml` to suit your needs and run the script with `python buttonpusher.py`. You
can figure out what `servo_on` and `servo_off` numbers to use by running `python tune.py` and typing
intervals in the 1500-2500 range until your servo moves just how you'd like.

I opted not to use a virtualenv or anything like that because I'm not very good at Python and would
probably screw it up.

Oh, and you'll need a Twilio account that sends POST requests to the IP of the Pi.
