from tbot.machine import connector, linux, board

class LiveLabHost(
    connector.SubprocessConnector,
    linux.Bash,
    linux.Lab,
):
    name = "Live-lab"

    @property
    def workdir(self):
        return linux.Workdir.static(self, f"/work/{self.username}/tbot-workdir")

LAB = LiveLabHost
