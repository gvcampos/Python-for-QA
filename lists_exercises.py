test_results = ["pass", "fail", "pass", "pass", "skip", "fail", "pass"]
response_times = [120, 340, 95, 410, 150, 890, 200]  # in ms, same order as the tests

# Tasks: 
# Print how many tests were executed in total (use len). 
# Count how many tests passed and how many failed (hint: the .count() method).
# Create a list slow_tests with the response times above 300 ms (like you started doing with error_codes, using for + if + append).
# Use in to check whether any "skip" test exists, and if so, print "There are skipped tests!".
# Remove all "skip" entries from test_results using remove().
# Sort response_times from highest to lowest (hint: sort(reverse=True)) and print the 3 slowest using slicing.

test_count = len(test_results)
print("Total tests:", test_count)

tests_passed = test_results.count("pass")
print("Tests passed:", tests_passed)

tests_failed = test_results.count("fail")
print("Tests failed:", tests_failed)

tests_skipped = test_results.count("skip")
print("Tests skipped:", tests_skipped)

slow_tests = []    
for time in response_times:
    if time > 300:
        slow_tests.append(time)

if "skip" in test_results:
    print("There are skipped tests")

for _ in range(tests_skipped):
    test_results.remove("skip")

status_codes = [201, 200, 500, 400]
error_positions = []

for i in range(len(status_codes)):
    if status_codes[i] >= 400:
        error_positions.append(i)

print(error_positions)  # [2, 3] 

status_codes = [201, 200, 500, 400]
error_positions = []

for i in range(len(status_codes)):
    if status_codes[i] >= 400:
        error_positions.append(i)

print("error positions", error_positions)

response_times.sort(reverse=True)

print("3 slowest tests:", response_times[:3])
    
          