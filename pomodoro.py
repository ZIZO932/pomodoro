import time
import argparse

def show_instructions():
    print("="*50)
    print("Welcome to the Terminal Pomodoro Timer!")
    print("Instructions:")
    print("1. This timer is designed to help you focus on work sessions (default is 25 minutes).")
    print("2. When the timer is running, it will display the remaining time in MM:SS format.")
    print("3. Once the time is up, you'll see a message prompting you to take a break.")
    print("4. You can specify a different duration by using the '--minutes' argument.")
    print("   For example: python pomodoro.py --minutes 15")
    print("="*50)
    print()

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Take a break.")

def main():
    parser = argparse.ArgumentParser(
        description="Simple Terminal-Based Pomodoro Timer"
    )
    parser.add_argument(
        "--minutes",
        type=int,
        default=25,
        help="Duration of the timer in minutes (default is 25)"
    )
    args = parser.parse_args()
    
    show_instructions()
    input("Press Enter to start the timer...")
    
    total_seconds = args.minutes * 60
    print(f"\nStarting Pomodoro Timer for {args.minutes} minutes...")
    countdown(total_seconds)

if __name__ == "__main__":
    main()
