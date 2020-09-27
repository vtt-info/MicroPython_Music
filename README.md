# MicroPython Music
A repo that provides a music module to MicroPython to allow makers to make music within their projects using PWM.

## Installation
```bash
git clone https://github.com/mytechnotalent/MicroPython_Music.git
```

## Setup pyboard.py Utility
#### SOURCE 
```bash
https://github.com/micropython/micropython/blob/master/tools/pyboard.py
```
#### INSTRUCTIONS
```bash
https://docs.micropython.org/en/latest/reference/pyboard.py.html#running-a-command-on-the-device
```
#### EXAMPLE
```bash
python3 pyboard.py --device <DEVICE> -f cp <FILE> :
```

## Copy Files To MicroPython Device
```bash
unittest.py [SOURCE: https://github.com/micropython/micropython-lib/blob/master/unittest/unittest.py]
music.py
main.py
test_music.py
```

## Run Tests in REPL
```bash
import unitest
unittest.main('test_music')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
