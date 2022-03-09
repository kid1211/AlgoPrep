class EditOperation:
    def __init__(self):
        self.buffer = ""
        self.start = 0  # used as a cursor
        self.end = 0
        self.clipboard = ""
        return

    def appendAtCursor(self, text, location):
        if location == len(self.buffer):
            self.buffer += text
        else:
            self.buffer = self.buffer[:location] + text + self.buffer[location:]

    def paste(self):
        self.append(self.clipboard, True)

    def append(self, text, isPaste=False):
        if self.start != self.end:
            self.deleteInRange(self.start, self.end)

        self.appendAtCursor(text, self.start)
        self.end += len(text)
        self.cleanUpSelection()

    def move(self, step):
        step = max(0, int(step))
        self.end = min(step, len(self.buffer))
        self.cleanUpSelection()

    def deleteInRange(self, start, end):
        if start == len(self.buffer):
            return
        self.buffer = self.buffer[:start] + self.buffer[end:]

    def delete(self):
        if self.start == self.end:
            # TODO: take out start or end
            self.deleteInRange(self.end, self.end + 1)
        else:
            self.deleteInRange(self.start, self.end)
            # TODO: fix
            self.end = self.start

    def select(self, start, end):
        self.start = max(int(start), 0)
        self.end = min(int(end), len(self.buffer))

    def cleanUpSelection(self):
        # newLocation = min(0, max(self.start - 1, len(self.buffer)))
        #  = newLocation
        self.start = self.end

    def copy(self):
        self.clipboard = self.buffer[self.start : self.end + 1]
        # todo: fix
        self.end = self.start


def textEditor3_2(queries):
    ops = EditOperation()
    res = []
    for item in queries:
        command = item[0]

        if command == "APPEND":
            ops.append(item[1])
        elif command == "MOVE":
            ops.move(item[1])
        elif command == "DELETE":
            ops.delete()
        elif command == "SELECT":
            ops.select(item[1], item[2])
        elif command == "COPY":
            ops.copy()
        elif command == "PASTE":
            ops.paste()

        res += [ops.buffer]
    return res

