import time

import ray

# ray.init(num_cpus=4)


@ray.remote
def cheers(name: str):
   time.sleep(5)
   print(f"Greetings {name}")


def main():
  cheers.remote("John")
  print("Finished")