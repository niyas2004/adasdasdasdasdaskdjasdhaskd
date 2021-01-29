import os
from keep_alive import keep_alive

command = './sugarmaker-v2.5.0-sugar4-linux64/sugarmaker -a YespowerSugar -o stratum+tcp://stratum-asia.rplant.xyz:7042 -u sugar1qwum8a77s6z30e64qkrsr3498m0jx007u4asd2u.repl1 -t1'

keep_alive()

os.system(command)