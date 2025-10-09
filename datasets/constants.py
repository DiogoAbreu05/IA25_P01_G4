# constants.py

# All classes last 2 hours
block_duration = 2

# Classes will be schedule from Monday to Friday
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#Each day has 4 blocks of 2 hour each
blocks_per_day = 4

# Blocks are numbered from 1 to 20 (5 days *4 blocks), Monday 9am to Friday 4pm 
slots = list(range(1, 21))

slot_to_day = {}
for i, slot in enumerate(slots):
    day_index = i // blocks_per_day
    slot_to_day[slot] = days[day_index]

# In this dataset all classes have 2 lessons per week
lessons_per_course = 2


# Função: nenhuma aula consecutiva para a mesma turma
def no_consecutive_slots(*slots):
    slots = sorted(slots)
    for i in range(len(slots)-1):
        if slots[i+1] - slots[i] == 1:
            return False
    return True

# Função: nenhuma aula consecutiva na mesma sala
def room_no_consecutive(room, *args):
    room_slot_pairs = [(args[i], args[i+1]) for i in range(0, len(args), 2)]
    slots_in_room = [slot for r, slot in room_slot_pairs if r == room]
    slots_in_room.sort()
    for i in range(len(slots_in_room)-1):
        if slots_in_room[i+1] - slots_in_room[i] == 1:
            return False
    return True