import sys
from pathlib import Path

current_dir = Path(__file__).parent
sys.path.append(str(current_dir.parent))

import Hostile

def test_hostile(capsys):
  PlayerStats[4] = 10
  EnemyType = Hostile.HostileSlct(PlayerStats)
  print(EnemyType)
  # use strip() to remove special characters from the expected and console out
  # to compare them more easily
  console_out = capsys.readouterr().out.strip()
  expected_out = '''MEMEZ.exe'''.strip()

  assert console_out == expected_out
