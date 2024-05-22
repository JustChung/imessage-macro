import time
from config import DB_PATH, DB_PATH_CHECK, PHONE_NUMBER
from detector import Detector
from actions import Actions

if __name__ == "__main__":
    detector = Detector(DB_PATH_CHECK)
    actions = Actions(DB_PATH, PHONE_NUMBER)
    try:
        while True:
            time.sleep(1)
            if detector.is_change():
                actions.task_macro()
    finally:
        print("End")