def distribution_of_wealth(some_minimum_wealth, some_population):
    poor_list = [x for x in some_population if x <= some_minimum_wealth]
    rich_list = [y for y in some_population if y > some_minimum_wealth]
    rich_list = sorted(rich_list)
    total_wealth_for_distribution = len(poor_list) * some_minimum_wealth - sum(poor_list)
    final_list = []
    current_distribution_index = len(rich_list) - 1

    for element in poor_list:
        if rich_list[current_distribution_index] - (some_minimum_wealth - element) < some_minimum_wealth:
            current_distribution_index -= 1
            if current_distribution_index < 0:
                break
        while element < some_minimum_wealth:
            element += 1
            rich_list[current_distribution_index] -= 1
            total_wealth_for_distribution -= 1

        final_list.append(element)


    result = final_list + rich_list
    if any(z < some_minimum_wealth for z in result):
        return "No equal distribution possible"
    else:
        return result


population = [int(i) for i in input().split(", ")]
minimum_wealth = int(input())
print(distribution_of_wealth(minimum_wealth, population))


