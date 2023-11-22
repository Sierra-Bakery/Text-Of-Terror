import sys
from pathlib import Path

current_dir = Path(__file__).parent
sys.path.append(str(current_dir.parent))

import EndScreenGI

def test_animation_good(capsys):
  EndScreenGI.good()
  # use strip() to remove special characters from the expected and console out
  # to compare them more easily
  console_out = capsys.readouterr().out.strip()
  expected_out = '''
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
------                 888      8888     8888   8888888   888888   888888                ------
------                88 88    88  88   88  88  8888888   88       88                    ------
------               8888888  88       88       88         88       88                   ------
------               88   88  88       88       8888        88       88                  ------
------               88   88   88  88   88  88  88           88       88                 ------
------               88   88    8888     8888   8888888   888888   888888                ------
-----------------------------------------------------------------------------------------------
------           88888   88888     888    8888    88  8888888888  8888888  8888          ------
------          88       88  88   88 88   88 88   88  8888888888  88       88 88         ------
------         88        88  88  8888888  88  88  88      88      8888     88  88        ------
------         88   88   88888   88   88  88   88 88      88      8888     88  88        ------
------          88   88  88  88  88   88  88    8888      88      88       88 88         ------
------           88888   88   88 88   88  88     888      88      8888888  8888          ------
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
--------------------------------------------SUCCESS--------------------------------------------
-------------------------------------UNLOCKED SUCCESSFULLY-------------------------------------
--------------------------YOU HAVE ACCESSED THE PROGRAM SUCCESSFULLY---------------------------
----------------------------YOU CAN NOW PROCEED WITH THE ANTIVIRUS-----------------------------
-----------------------------------GREAT WORK BRAVE WARRIOR------------------------------------
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
Press Enter to continue...
'''.strip()

  assert console_out == expected_out