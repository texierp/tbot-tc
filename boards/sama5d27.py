import tbot
from tbot.machine import board, connector, channel, linux
from ykush import Ykush

class SAMA5(
    connector.ConsoleConnector,
    board.PowerControl,
    board.Board,
    Ykush,
):
    name = "SAMA5"
#    ykush_port = "1"
#    ykush_serial = "YK17698"

    def poweron(self):
        self.ykush_reset()

    def poweroff(self):
        self.ykush_off()

    def connect(self, mach):
        return mach.open_channel("microcom", "--port=/dev/ttyACM0", "--speed=115200")

class SAMA5BoardUBoot(
    board.Connector,
    board.UBootAutobootIntercept,
    board.UBootShell,
):

    prompt = "=> "

UBOOT = SAMA5BoardUBoot

# Linux machine
#
class SAMA5BoardLinux(
    board.Connector,
    board.LinuxBootLogin,
    linux.Bash,
):

    username = "root"
    password = None

BOARD = SAMA5
LINUX = SAMA5BoardLinux
