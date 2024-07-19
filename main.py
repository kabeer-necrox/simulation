# from simulation.greedy import run_greedy
# import sys

# sys.path.insert(0, '.')


# def main():
#     profile = False
#     if profile:
#         from pyinstrument import Profiler

#         p = Profiler()
#         p.start()

#     run_greedy()
#     print()
#     print()

#     if profile:
#         p.stop()
#         p.open_in_browser()


# if __name__ == '__main__':
#     main()



from simulation.greedy import run_greedy
import argparse

def main():
    # Create argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, required=True, help='Dataset to use')
    parser.add_argument('--days', type=int, required=True, help='Number of days to simulate')
    parser.add_argument('--dispatcher', type=str, required=True, help='Dispatcher to use')
    parser.add_argument('--seed', type=int, default=None, help='Random seed')
    parser.add_argument('--wandb', action='store_true', default=False, help='Enable wandb logging')
    parser.add_argument('--chart', action='store_true', default=False, help='Enable chart plotting')
    parser.add_argument('--alg', type=str, default='l4m', choices=['l4m', 'm4l'], help='Algorithm to use')

    # Parse arguments
    args = parser.parse_args()

    # Run greedy simulation with parsed arguments
    run_greedy(args)

if __name__ == '__main__':
    main()


