import numpy as np
import pandas as pd


staff_planning = [
    [[0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [
        15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8]],
    [[0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [
        15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8]],
    [[0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [
        15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8]],
    [[0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [
        15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8]],
    [[0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [
        15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8]]
]
hourlystaff_needed = np.array(
    [
        [3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10,
            12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10,
            12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10,
            12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10,
            12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10,
            12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3]
    ])

hourlystaff_needed = np.array(
    [[3,  3,  3,  3,  3,  3, 10,  7, 12, 12,  9,  9, 10, 12, 12,  9,  9, 12, 15, 10, 10,  3,  3,  3],
     [3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10,
         12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10,
            12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10,
            12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10, 12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3]])


"""
hourlystaff_needed = np.array([
    [0, 0, 0, 0, 0, 0, 6, 12, 12, 12, 6, 6, 18, 18, 6, 6, 6, 6, 18, 18, 18, 6, 6, 6],
    [0, 0, 0, 0, 0, 0, 6, 12, 12, 12, 6, 6, 18, 18, 6, 6, 6, 6, 18, 18, 18, 6, 6, 6],
    [0, 0, 0, 0, 0, 0, 6, 12, 12, 12, 6, 6, 18, 18, 6, 6, 6, 6, 18, 18, 18, 6, 6, 6],
    [0, 0, 0, 0, 0, 0, 6, 12, 12, 12, 6, 6, 18, 18, 6, 6, 6, 6, 18, 18, 18, 6, 6, 6],
    [0, 0, 0, 0, 0, 0, 6, 12, 12, 12, 6, 6, 18, 18, 6, 6, 6, 6, 18, 18, 18, 6, 6, 6]
])
"""

"""
staff_planning = [
    [ [0, 0, 10], [1, 0, 10], [2, 0, 10], [3, 0, 10], [4, 0, 10], [5, 0, 10], [6, 0, 10], [7, 0, 10], [8, 0, 10], [9, 0, 10], [10, 0, 10] ],
    [ [0, 0, 10], [1, 0, 10], [2, 0, 10], [3, 0, 10], [4, 0, 10], [5, 0, 10], [6, 0, 10], [7, 0, 10], [8, 0, 10], [9, 0, 10], [10, 0, 10] ],
    [ [0, 0, 10], [1, 0, 10], [2, 0, 10], [3, 0, 10], [4, 0, 10], [5, 0, 10], [6, 0, 10], [7, 0, 10], [8, 0, 10], [9, 0, 10], [10, 0, 10] ],
    [ [0, 0, 10], [1, 0, 10], [2, 0, 10], [3, 0, 10], [4, 0, 10], [5, 0, 10], [6, 0, 10], [7, 0, 10], [8, 0, 10], [9, 0, 10], [10, 0, 10] ],
    [ [0, 0, 10], [1, 0, 10], [2, 0, 10], [3, 0, 10], [4, 0, 10], [5, 0, 10], [6, 0, 10], [7, 0, 10], [8, 0, 10], [9, 0, 10], [10, 0, 10] ],
]

hourlystaff_needed = np.array([
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 6, 6, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 6, 6, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 6, 6, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 6, 6, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 6, 6, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2]
])
"""
"""
staff_planning = [
    [ [0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8] ],
    [ [0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8] ],
    [ [0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8] ],
    [ [0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8] ],
    [ [0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8] ]
]


hourlystaff_needed = np.array([
[3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10, 12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10, 12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10, 12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10, 12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 10, 7, 12, 12, 9, 9, 10, 12, 12, 9, 9, 12, 15, 10, 10, 3, 3, 3],
])
"""


"""
Employee present: analyse whether the employee is present yes or no on a given time
based on the time list of 3 (id, start time, duration) //list these 3 things
"""


def employee_present(employee, time):
    employee_start_time = employee[1]
    employee_duration = employee[2]
    employee_end_time = employee_start_time + employee_duration
    if (time >= employee_start_time) and (time < employee_end_time):
        return True
    return False


"""

"""


def staffplanning_to_hourlyplanning(staff_planning):

    hourlystaff_week = []
    for day in staff_planning:

        hourlystaff_day = []
        for employee in day:

            employee_present_hour = []
            for time in range(0, 24):

                employee_present_hour.append(employee_present(employee, time))

            hourlystaff_day.append(employee_present_hour)

        hourlystaff_week.append(hourlystaff_day)

    hourlystaff_week = np.array(hourlystaff_week).sum(axis=1)
    return hourlystaff_week


"""
cost is calculated as hours understaffed + hours overstaffed
"""


def cost(hourlystaff, hourlystaff_needed):
    errors = hourlystaff - hourlystaff_needed
    overstaff = abs(errors[errors > 0].sum())
    understaff = abs(errors[errors < 0].sum())

    overstaff_cost = 1
    understaff_cost = 1

    cost = overstaff_cost * overstaff + understaff_cost * understaff
    return cost


"""
"""


def generate_random_staff_planning(n_days, n_staff):
    period_planning = []
    for day in range(n_days):
        day_planning = []
        for employee_id in range(n_staff):
            start_time = np.random.randint(0, 23)
            duration = np.random.randint(0, 8)  # changehere
            employee = [employee_id, start_time, duration]
            day_planning.append(employee)

        period_planning.append(day_planning)

    return period_planning


"""
"""

random_staff_planning = generate_random_staff_planning(n_days=5, n_staff=30)
random_staff_planning

cost(staffplanning_to_hourlyplanning(random_staff_planning), hourlystaff_needed)

"""
create a parent generation of n parent plannings
"""


def create_parent_generation(n_parents, n_days=5, n_staff=30):
    parents = []
    for i in range(n_parents):
        parent = generate_random_staff_planning(n_days=n_days, n_staff=n_staff)
        parents.append(parent)
    return parents


"""
for each iteration, select randomly two parents and make a random combination of those two parents
by applying a randomly generated yes/no mask to the two selected parents
"""


def random_combine(parents, n_offspring):
    n_parents = len(parents)
    n_periods = len(parents[0])
    n_employees = len(parents[0][0])

    offspring = []
    for i in range(n_offspring):
        random_dad = parents[np.random.randint(low=0, high=n_parents - 1)]
        random_mom = parents[np.random.randint(low=0, high=n_parents - 1)]

        dad_mask = np.random.randint(0, 2, size=np.array(random_dad).shape)
        mom_mask = np.logical_not(dad_mask)

        child = np.add(np.multiply(random_dad, dad_mask),
                       np.multiply(random_mom, mom_mask))

        offspring.append(child)

    return offspring


"""
mutation
"""


def mutate_parent(parent, n_mutations):
    size1 = parent.shape[0]
    size2 = parent.shape[1]

    for i in range(n_mutations):
        rand1 = np.random.randint(0, size1)
        rand2 = np.random.randint(0, size2)
        rand3 = np.random.randint(1, 2)

        parent[rand1, rand2, rand3] = np.random.randint(0, 8)  # change here

    return parent


def mutate_gen(parent_gen, n_mutations):
    mutated_parent_gen = []
    for parent in parent_gen:
        mutated_parent_gen.append(mutate_parent(parent, n_mutations))
    return mutated_parent_gen


"""
selection - feasibility
"""


def is_acceptable(parent):
    # work > 10 hours is not ok
    return np.logical_not((np.array(parent)[:, :, 2:] > 8).any())


def select_acceptable(parent_gen):
    parent_gen = [parent for parent in parent_gen if is_acceptable(parent)]
    return parent_gen


"""
selection - cost (inverse fitness)
"""


def select_best(parent_gen, hourlystaff_needed, n_best):
    costs = []
    for idx, parent_staff_planning in enumerate(parent_gen):

        parent_hourly_planning = staffplanning_to_hourlyplanning(
            parent_staff_planning)
        parent_cost = cost(parent_hourly_planning, hourlystaff_needed)
        costs.append([idx, parent_cost])

    print('generation best is: {}, generation worst is: {}'.format(
        pd.DataFrame(costs)[1].min(), pd.DataFrame(costs)[1].max()))

    costs_tmp = pd.DataFrame(costs).sort_values(
        by=1, ascending=True).reset_index(drop=True)
    selected_parents_idx = list(costs_tmp.iloc[:n_best, 0])
    selected_parents = [parent for idx, parent in enumerate(
        parent_gen) if idx in selected_parents_idx]

    return selected_parents


"""
overall func
"""


def gen_algo(hourlystaff_needed, n_iterations):

    generation_size = 1000

    parent_gen = create_parent_generation(
        n_parents=generation_size, n_days=5, n_staff=30)
    for it in range(n_iterations):
        parent_gen = select_acceptable(parent_gen)
        parent_gen = select_best(parent_gen, hourlystaff_needed, n_best=100)
        parent_gen = random_combine(parent_gen, n_offspring=generation_size)
        parent_gen = mutate_gen(parent_gen, n_mutations=1)

    best_child = select_best(parent_gen, hourlystaff_needed, n_best=1)
    return best_child


best_planning = gen_algo(hourlystaff_needed, n_iterations=100)

print(best_planning)

print(staffplanning_to_hourlyplanning(best_planning[0]))

print(hourlystaff_needed)
