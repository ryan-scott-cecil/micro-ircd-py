from pathlib import Path
import tempfile
import os

class Channel:
    def __init__(self, server, name):
        self.server = server
        self.name = name
        self.members = set()    
        self._topic = b""
        
        self._state_path
        if self.server.state_dir:
            fs_safe_name = (
                name.decode(errors="ignore").replace("_", "__").replace("/", "_")
            )
            self._state_path = self.server.state_dir / fs_safe_name
            self._read_state()
        else:
            self._state_path = None
    
    @property
    def topic(self):
        return self._topic
    
    @topic.setter
    def topic(self, value):
        self._topic = value
        self._write_state()

    def add_member(self, client):
        self.members.add(client)

    def remove_client(self, client):
        self.members.discard(client)
        if not self.members:
            self.server.remove_channel(self)

    def _read_state(self):
        if not (self._state_path and self._state_path.exists()):
            return
        data = {}

        exec(self._state_path.read_bytes(), {}, data)
        self._topic = data.get("topic", "")
        self._key = data.get("key")

    def _write_state(self):
        if not self._state_path:
            return
        fd, path = tempfile.mkstemp(dir=self._state_path.parent)
        with os.fdopen(fd, "w") as f:
            f.write("topic = %r\n" % self.topic)
        Path(path).replace(self._state_path)

