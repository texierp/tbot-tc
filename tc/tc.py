import tbot
from tbot.machine import board,linux
from tbot_contrib import utils
from tbot_contrib import swupdate

@tbot.testcase
@tbot.with_lab
def testcase_swupdate(lh: linux.LinuxShell) -> None:
    with tbot.acquire_local() as lo:
        swu_path = linux.Path(lo, "/opt/swupdate/update-image.swu")
        swupdate.swupdate_update_web(lo, swu_path, "192.168.1.48")
