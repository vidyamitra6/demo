# # # # # # # # # from datetime import datetime, timedelta

# # # # # # # # # def generate_slots(start, end, slot_size=15):
# # # # # # # # #     slots = []
# # # # # # # # #     fmt = "%H:%M"
# # # # # # # # #     start_dt = datetime.strptime(start, fmt)
# # # # # # # # #     end_dt = datetime.strptime(end, fmt)
# # # # # # # # #     while start_dt + timedelta(minutes=slot_size) <= end_dt:
# # # # # # # # #         slot_start = start_dt.strftime(fmt)
# # # # # # # # #         slot_end = (start_dt + timedelta(minutes=slot_size)).strftime(fmt)
# # # # # # # # #         slots.append((slot_start, slot_end))
# # # # # # # # #         start_dt += timedelta(minutes=slot_size)
# # # # # # # # #     return slots

# # # # # # # # # def allocate_slots(doctor_times, patient_preferences):
# # # # # # # # #     all_slots = []
# # # # # # # # #     for d_start, d_end in doctor_times:
# # # # # # # # #         all_slots.extend(generate_slots(d_start, d_end))
    
# # # # # # # # #     booked = set()
# # # # # # # # #     result = {}
    
# # # # # # # # #     for idx, (p_start, p_end) in enumerate(patient_preferences):
# # # # # # # # #         possible = []
# # # # # # # # #         for slot in all_slots:
# # # # # # # # #             if slot in booked:
# # # # # # # # #                 continue
# # # # # # # # #             if slot[0] >= p_start and slot[1] <= p_end:
# # # # # # # # #                 possible.append(slot)
# # # # # # # # #         if possible:
# # # # # # # # #             assigned = possible[0]
# # # # # # # # #             result[idx] = assigned
# # # # # # # # #             booked.add(assigned)
    
# # # # # # # # #     return result




# # # # # # # # from datetime import datetime, timedelta

# # # # # # # # def parse_time(time_str):
# # # # # # # #     return datetime.strptime(time_str, "%H:%M")

# # # # # # # # def get_free_slots(blocked, limits):
# # # # # # # #     free = []
# # # # # # # #     start = parse_time(limits[0])
# # # # # # # #     end = parse_time(limits[1])

# # # # # # # #     for block in blocked:
# # # # # # # #         b_start, b_end = parse_time(block[0]), parse_time(block[1])
# # # # # # # #         if start < b_start:
# # # # # # # #             free.append([start, b_start])
# # # # # # # #         start = max(start, b_end)

# # # # # # # #     if start < end:
# # # # # # # #         free.append([start, end])
# # # # # # # #     return free

# # # # # # # # def intersect_slots(slots1, slots2):
# # # # # # # #     result = []
# # # # # # # #     i, j = 0, 0
# # # # # # # #     while i < len(slots1) and j < len(slots2):
# # # # # # # #         start = max(slots1[i][0], slots2[j][0])
# # # # # # # #         end = min(slots1[i][1], slots2[j][1])
# # # # # # # #         if start < end:
# # # # # # # #             result.append([start, end])
# # # # # # # #         if slots1[i][1] < slots2[j][1]:
# # # # # # # #             i += 1
# # # # # # # #         else:
# # # # # # # #             j += 1
# # # # # # # #     return result

# # # # # # # # def split_slots(slots, duration):
# # # # # # # #     result = []
# # # # # # # #     delta = timedelta(minutes=duration)
# # # # # # # #     for start, end in slots:
# # # # # # # #         while start + delta <= end:
# # # # # # # #             result.append([start.strftime("%H:%M"), (start + delta).strftime("%H:%M")])
# # # # # # # #             start += delta
# # # # # # # #     return result

# # # # # # # # def find_meeting_slots(doctorBlockedTime, doctTimeLimits,
# # # # # # # #                        patientBlockedTime, patientTimeLimits,
# # # # # # # #                        meetingDuration):
# # # # # # # #     doc_free = get_free_slots(doctorBlockedTime, doctTimeLimits)
# # # # # # # #     pat_free = get_free_slots(patientBlockedTime, patientTimeLimits)
# # # # # # # #     common_free = intersect_slots(doc_free, pat_free)
# # # # # # # #     return split_slots(common_free, meetingDuration)

# # # # # # # # # === Example Usage ===
# # # # # # # # doctorBlockedTime = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
# # # # # # # # doctTimeLimits = ['9:00', '20:00']
# # # # # # # # patientBlockedTime = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
# # # # # # # # patientTimeLimits = ['10:00', '18:30']
# # # # # # # # meetingDuration = 30

# # # # # # # # available_slots = find_meeting_slots(doctorBlockedTime, doctTimeLimits, patientBlockedTime, patientTimeLimits, meetingDuration)
# # # # # # # # print(available_slots)




# # # # # # # def sunset_views(buildings, direction):
# # # # # # #     n = len(buildings)
# # # # # # #     result = []
# # # # # # #     max_height = float('-inf')

# # # # # # #     # Determine traversal direction
# # # # # # #     step = -1 if direction == "EAST" else 1
# # # # # # #     start = n - 1 if direction == "EAST" else 0
# # # # # # #     end = -1 if direction == "EAST" else n

# # # # # # #     for i in range(start, end, step):
# # # # # # #         if buildings[i] > max_height:
# # # # # # #             result.append(i)
# # # # # # #             max_height = buildings[i]

# # # # # # #     return sorted(result)

# # # # # # # # Test
# # # # # # # buildings = [3, 5, 4, 4, 3, 1, 3, 2]
# # # # # # # direction = "EAST"
# # # # # # # print(sunset_views(buildings, direction))  # Output: [1, 3, 6, 7]



# # # # # # def longest_consecutive_digit(number_str):
# # # # # #     max_digit = ''
# # # # # #     max_count = 0
# # # # # #     current_digit = ''
# # # # # #     current_count = 0

# # # # # #     for digit in number_str:
# # # # # #         if digit == current_digit:
# # # # # #             current_count += 1
# # # # # #         else:
# # # # # #             current_digit = digit
# # # # # #             current_count = 1
        
# # # # # #         if current_count > max_count:
# # # # # #             max_count = current_count
# # # # # #             max_digit = current_digit

# # # # # #     return int(max_digit)

# # # # # # # 🔧 Test Cases
# # # # # # print(longest_consecutive_digit("1122233322233333522"))  # Output: 3
# # # # # # print(longest_consecutive_digit("88444660012677777"))    # Output: 7
# # # # # # print(longest_consecutive_digit("1122333432222"))        # Output: 2


# # # # # def one_edit_away(s1, s2):
# # # # #     if s1 == s2:
# # # # #         return True

# # # # #     len1, len2 = len(s1), len(s2)

# # # # #     # If the length difference is more than 1, more than one edit is needed
# # # # #     if abs(len1 - len2) > 1:
# # # # #         return False

# # # # #     # Helper for one replace
# # # # #     if len1 == len2:
# # # # #         diff_count = sum(1 for a, b in zip(s1, s2) if a != b)
# # # # #         return diff_count == 1

# # # # #     # Helper for one insert/remove
# # # # #     # Always make s1 the shorter one
# # # # #     if len1 > len2:
# # # # #         s1, s2 = s2, s1

# # # # #     i = j = 0
# # # # #     found_diff = False
# # # # #     while i < len(s1) and j < len(s2):
# # # # #         if s1[i] != s2[j]:
# # # # #             if found_diff:
# # # # #                 return False
# # # # #             found_diff = True
# # # # #             j += 1
# # # # #         else:
# # # # #             i += 1
# # # # #             j += 1
# # # # #     return True

# # # # # # 🔧 Example
# # # # # print(one_edit_away("hello", "hollo"))  # Output: True
# # # # # print(one_edit_away("abc", "ab"))       # Output: True
# # # # # print(one_edit_away("abc", "adc"))      # Output: True
# # # # # print(one_edit_away("abc", "abcdx"))    # Output: False


# # # # from collections import defaultdict

# # # # def group_anagrams(words):
# # # #     anagram_map = defaultdict(list)
    
# # # #     for word in words:
# # # #         key = ''.join(sorted(word))  # Use sorted characters as key
# # # #         anagram_map[key].append(word)
    
# # # #     return list(anagram_map.values())

# # # # # ✅ Test Example
# # # # words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
# # # # print(group_anagrams(words))


# # # from collections import Counter

# # # def get_minimum_characters(words):
# # #     max_freq = Counter()

# # #     for word in words:
# # #         word_freq = Counter(word)
# # #         for char in word_freq:
# # #             max_freq[char] = max(max_freq[char], word_freq[char])

# # #     result = []
# # #     for char, count in max_freq.items():
# # #         result.extend([char] * count)

# # #     return result

# # # # ✅ Example Test
# # # words = ["this", "that", "did", "deed", "them!", "a"]
# # # print(get_minimum_characters(words))
# # # # Output might be: ['t', 'h', 'i', 's', 'a', 'd', 'e', 'e', 'm', 'l', '!']


# # def has_zero_sum_subarray(nums):
# #     prefix_sum = 0
# #     seen_sums = set()

# #     for num in nums:
# #         prefix_sum += num

# #         if prefix_sum == 0 or prefix_sum in seen_sums:
# #             return True
        
# #         seen_sums.add(prefix_sum)
    
# #     return False

# # # ✅ Sample Tests
# # print(has_zero_sum_subarray([-5, -5, 2, 3, -2]))         # True
# # print(has_zero_sum_subarray([2, 3, 4, -5, -2, -4, 5, 5])) # True
# # print(has_zero_sum_subarray([-8, -22, 104, 73, -120, 53, 22, -12, 1, 14, -90, 13, -22])) # False

# from datetime import datetime, timedelta

# def parse_time(time_str):
#     return datetime.strptime(time_str, "%H:%M")

# def format_time(time_obj):
#     return time_obj.strftime("%H:%M")

# def subtract_intervals(available, blocked):
#     result = []
#     for start, end in available:
#         temp = [(start, end)]
#         for b_start, b_end in blocked:
#             new_temp = []
#             for a_start, a_end in temp:
#                 if b_end <= a_start or b_start >= a_end:
#                     new_temp.append((a_start, a_end))
#                 else:
#                     if b_start > a_start:
#                         new_temp.append((a_start, b_start))
#                     if b_end < a_end:
#                         new_temp.append((b_end, a_end))
#             temp = new_temp
#         result.extend(temp)
#     return result

# def intersect_intervals(a, b):
#     result = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         start = max(a[i][0], b[j][0])
#         end = min(a[i][1], b[j][1])
#         if start < end:
#             result.append((start, end))
#         if a[i][1] < b[j][1]:
#             i += 1
#         else:
#             j += 1
#     return result

# def generate_slots(intervals, duration):
#     slots = []
#     delta = timedelta(minutes=duration)
#     for start, end in intervals:
#         while start + delta <= end:
#             slots.append((start, start + delta))
#             start += delta
#     return slots

# def get_available_meeting_slots(doctorBlocked, doctorLimits,
#                                 patientBlocked, patientLimits,
#                                 meetingDuration):
    
#     # Convert strings to datetime
#     doctorBlocked = [(parse_time(start), parse_time(end)) for start, end in doctorBlocked]
#     patientBlocked = [(parse_time(start), parse_time(end)) for start, end in patientBlocked]
#     doctorLimits = [(parse_time(doctorLimits[0]), parse_time(doctorLimits[1]))]
#     patientLimits = [(parse_time(patientLimits[0]), parse_time(patientLimits[1]))]

#     # Get free intervals
#     doctorFree = subtract_intervals(doctorLimits, doctorBlocked)
#     patientFree = subtract_intervals(patientLimits, patientBlocked)

#     # Find overlapping free time
#     commonFree = intersect_intervals(doctorFree, patientFree)

#     # Break into slots
#     availableSlots = generate_slots(commonFree, meetingDuration)

#     # Format to string output
#     return [[format_time(start), format_time(end)] for start, end in availableSlots]
