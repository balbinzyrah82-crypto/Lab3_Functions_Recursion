import access_control as ac
import media_engine as me

# Define your inputs
SEED_NUM = 7  # Your last digit
FAVORITE_ARTIST = "NIKI"
CONTROL_NUM = max(1, SEED_NUM)

# Task 1
level = ac.compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
decision = ac.validate_access(level, CONTROL_NUM)

# Task 2 & 3
limit = CONTROL_NUM + len(FAVORITE_ARTIST)
total_calls = me.signal_shutdown(100, CONTROL_NUM * 10)
plays = list(me.play_count_stream(limit))

print("\n--- ASSESSMENT DATA ---")
print(f"CONTROL_NUM: {CONTROL_NUM}")
print(f"Access Level: {level} | Decision: {decision}")
print(f"Recursive Calls: {total_calls}")
print(f"Stream Limit: {limit} | Total Plays: {sum(plays)}")