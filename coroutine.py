import hashlib as hasher
import datetime


class Block:
  def __init__(self, index,timestamp,data,previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash()

  def hash(self):
    sha = hasher.sha256()
    sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
    return sha.hexdigest()

def first():
  return Block(0,datetime.datetime.now(),"First Block",None)


def new(last):
  current_index = last.index + 1
  current_timestamp = datetime.datetime.now()
  current_data = 'Блок ' + str(current_index)
  last_hash = last.hash
  return Block(current_index, current_timestamp, current_data, last_hash)

def start():
  history = [first()]
  i = 0
  while True:
    block = new(history[i])
    i += 1
    history.append(block)
    yield block

blocks = start()

z = next(blocks)

for i in range(7):
  print(z.data)
  print(z.hash)
  print()
  z = next(blocks)

blocks.close()
